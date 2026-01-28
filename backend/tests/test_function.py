import pytest
import json
import os
from unittest.mock import Mock, patch, MagicMock
import azure.functions as func
from azure.cosmos import exceptions

# Import del modulo function_app
import function_app


class TestGetVisitorCount:
    """Test suite per la funzione get_visitor_count_logic"""
    
    @pytest.fixture
    def mock_cosmos_env(self, monkeypatch):
        """Setup delle variabili d'ambiente per i test"""
        monkeypatch.setenv("COSMOS_ENDPOINT", "https://test.documents.azure.com:443/")
        monkeypatch.setenv("COSMOS_KEY", "test_key_12345")
    
    @pytest.fixture
    def mock_http_request(self):
        """Crea una mock HTTP request"""
        req = Mock(spec=func.HttpRequest)
        req.method = "GET"
        req.url = "http://localhost/api/GetVisitorCount"
        req.params = {}
        req.headers = {}
        return req
    
    @patch('function_app.CosmosClient')
    def test_counter_increment_success(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Il contatore incrementa correttamente"""
        # Setup mock CosmosDB
        mock_container = MagicMock()
        mock_container.read_item.return_value = {
            'id': 'visitor-count',
            'count': 42
        }
        mock_container.upsert_item.return_value = {
            'id': 'visitor-count',
            'count': 43
        }
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Chiama la business logic direttamente
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica
        assert response.status_code == 200
        body = json.loads(response.get_body())
        assert body['count'] == 43
        
        # Verifica che upsert sia stato chiamato con il valore corretto
        mock_container.upsert_item.assert_called_once()
        upserted_item = mock_container.upsert_item.call_args[0][0]
        assert upserted_item['count'] == 43
        assert upserted_item['id'] == 'visitor-count'
    
    @patch('function_app.CosmosClient')
    def test_counter_first_visit(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Primo visitatore - crea il contatore da zero"""
        # Setup mock CosmosDB - simula che l'item non esista
        mock_container = MagicMock()
        mock_container.read_item.side_effect = exceptions.CosmosResourceNotFoundError(
            message="Item not found"
        )
        mock_container.upsert_item.return_value = {
            'id': 'visitor-count',
            'count': 1
        }
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui la function
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica
        assert response.status_code == 200
        body = json.loads(response.get_body())
        assert body['count'] == 1
        
        # Verifica che sia stato creato un nuovo item
        mock_container.upsert_item.assert_called_once()
        upserted_item = mock_container.upsert_item.call_args[0][0]
        assert upserted_item['count'] == 1
    
    def test_options_preflight_request(self, mock_cosmos_env):
        """Test: Gestione della preflight request OPTIONS"""
        req = Mock(spec=func.HttpRequest)
        req.method = "OPTIONS"
        req.url = "http://localhost/api/GetVisitorCount"
        req.params = {}
        req.headers = {}
        
        response = function_app.get_visitor_count_logic(req)
        
        # Verifica
        assert response.status_code == 200
        assert response.headers['Access-Control-Allow-Origin'] == '*'
        assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, OPTIONS'
        assert response.headers['Access-Control-Allow-Headers'] == 'Content-Type'
    
    @patch('function_app.CosmosClient')
    def test_cors_headers_present(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Verifica che i CORS headers siano presenti"""
        # Setup mock
        mock_container = MagicMock()
        mock_container.read_item.return_value = {'id': 'visitor-count', 'count': 10}
        mock_container.upsert_item.return_value = {'id': 'visitor-count', 'count': 11}
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica CORS headers
        assert response.headers['Access-Control-Allow-Origin'] == '*'
        assert response.headers['Access-Control-Allow-Methods'] == 'GET, POST, OPTIONS'
        assert response.headers['Access-Control-Allow-Headers'] == 'Content-Type'
        assert response.headers['Content-Type'] == 'application/json'
    
    @patch('function_app.CosmosClient')
    def test_post_method_works(self, mock_cosmos_client, mock_cosmos_env):
        """Test: Il metodo POST funziona"""
        req = Mock(spec=func.HttpRequest)
        req.method = "POST"
        req.url = "http://localhost/api/GetVisitorCount"
        req.params = {}
        req.headers = {}
        
        # Setup mock
        mock_container = MagicMock()
        mock_container.read_item.return_value = {'id': 'visitor-count', 'count': 5}
        mock_container.upsert_item.return_value = {'id': 'visitor-count', 'count': 6}
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui
        response = function_app.get_visitor_count_logic(req)
        
        # Verifica
        assert response.status_code == 200
        body = json.loads(response.get_body())
        assert body['count'] == 6
    
    @patch('function_app.CosmosClient')
    def test_cosmos_connection_error(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Gestione errore di connessione a CosmosDB"""
        # Simula un errore di connessione
        mock_cosmos_client.side_effect = Exception("Connection failed")
        
        # Esegui
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica
        assert response.status_code == 500
        body = json.loads(response.get_body())
        assert 'error' in body
        assert 'Connection failed' in body['error']
        
        # Verifica che i CORS headers siano presenti anche in caso di errore
        assert response.headers['Access-Control-Allow-Origin'] == '*'
    
    @patch('function_app.CosmosClient')
    def test_upsert_error(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Gestione errore durante l'upsert"""
        # Setup mock
        mock_container = MagicMock()
        mock_container.read_item.return_value = {'id': 'visitor-count', 'count': 10}
        mock_container.upsert_item.side_effect = Exception("Upsert failed")
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica
        assert response.status_code == 500
        body = json.loads(response.get_body())
        assert 'error' in body
    
    def test_missing_environment_variables(self, mock_http_request):
        """Test: Errore se mancano le variabili d'ambiente"""
        # Salva le variabili originali
        original_endpoint = os.environ.get('COSMOS_ENDPOINT')
        original_key = os.environ.get('COSMOS_KEY')
        
        try:
            # Rimuovi le variabili d'ambiente
            if 'COSMOS_ENDPOINT' in os.environ:
                del os.environ['COSMOS_ENDPOINT']
            if 'COSMOS_KEY' in os.environ:
                del os.environ['COSMOS_KEY']
            
            # Esegui
            response = function_app.get_visitor_count_logic(mock_http_request)
            
            # Verifica
            assert response.status_code == 500
            body = json.loads(response.get_body())
            assert 'error' in body
            assert 'Missing environment variable' in body['error']
        finally:
            # Ripristina le variabili originali
            if original_endpoint:
                os.environ['COSMOS_ENDPOINT'] = original_endpoint
            if original_key:
                os.environ['COSMOS_KEY'] = original_key
    
    @patch('function_app.CosmosClient')
    def test_json_response_format(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Verifica che la risposta sia in formato JSON valido"""
        # Setup mock
        mock_container = MagicMock()
        mock_container.read_item.return_value = {'id': 'visitor-count', 'count': 99}
        mock_container.upsert_item.return_value = {'id': 'visitor-count', 'count': 100}
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica che sia JSON valido
        body = json.loads(response.get_body())
        assert isinstance(body, dict)
        assert 'count' in body
        assert isinstance(body['count'], int)
        assert body['count'] == 100
    
    @patch('function_app.CosmosClient')
    def test_counter_increments_by_one(self, mock_cosmos_client, mock_cosmos_env, mock_http_request):
        """Test: Verifica che il contatore incrementi esattamente di 1"""
        # Setup mock
        mock_container = MagicMock()
        mock_container.read_item.return_value = {'id': 'visitor-count', 'count': 999}
        mock_container.upsert_item.return_value = {'id': 'visitor-count', 'count': 1000}
        
        mock_database = MagicMock()
        mock_database.get_container_client.return_value = mock_container
        
        mock_client_instance = MagicMock()
        mock_client_instance.get_database_client.return_value = mock_database
        mock_cosmos_client.return_value = mock_client_instance
        
        # Esegui
        response = function_app.get_visitor_count_logic(mock_http_request)
        
        # Verifica
        body = json.loads(response.get_body())
        assert body['count'] == 1000
        
        # Verifica che l'incremento sia esattamente +1
        upserted_item = mock_container.upsert_item.call_args[0][0]
        assert upserted_item['count'] == 1000


if __name__ == "__main__":
    # Esegui i test
    pytest.main([__file__, "-v", "--cov=function_app", "--cov-report=html"])
