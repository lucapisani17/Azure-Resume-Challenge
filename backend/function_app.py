import azure.functions as func
import logging
import json
import os
from azure.cosmos import CosmosClient, exceptions

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def get_visitor_count_logic(req: func.HttpRequest) -> func.HttpResponse:
    """
    Business logic per il visitor counter - separata per il testing
    """
    logging.info('Processing visitor count request')
    
    # Headers CORS
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
    }
    
    # Gestisci preflight request
    if req.method == 'OPTIONS':
        return func.HttpResponse(
            status_code=200,
            headers=headers
        )

    # Configurazione CosmosDB
    try:
        cosmos_endpoint = os.environ["COSMOS_ENDPOINT"]
        cosmos_key = os.environ["COSMOS_KEY"]
    except KeyError as e:
        logging.error(f"Missing environment variable: {str(e)}")
        return func.HttpResponse(
            body=json.dumps({"error": f"Missing environment variable: {str(e)}"}),
            status_code=500,
            headers=headers
        )
    
    database_name = "ResumeDB"
    container_name = "VisitorCounter"
    
    try:
        # Connessione a CosmosDB
        client = CosmosClient(cosmos_endpoint, cosmos_key)
        database = client.get_database_client(database_name)
        container = database.get_container_client(container_name)
        
        # ID del documento contatore
        counter_id = "visitor-count"
        
        # Leggi il contatore attuale
        try:
            counter_item = container.read_item(item=counter_id, partition_key=counter_id)
            current_count = counter_item['count']
        except exceptions.CosmosResourceNotFoundError:
            # Se non esiste, crealo
            current_count = 0
            counter_item = {
                'id': counter_id,
                'count': current_count
            }
        
        # Incrementa il contatore
        new_count = current_count + 1
        counter_item['count'] = new_count
        
        # Salva in CosmosDB
        container.upsert_item(counter_item)
        
        logging.info(f'Visitor count updated to: {new_count}')
        
        # Ritorna la risposta con CORS headers
        return func.HttpResponse(
            body=json.dumps({"count": new_count}),
            status_code=200,
            headers=headers
        )
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse(
            body=json.dumps({"error": str(e)}),
            status_code=500,
            headers=headers
        )

@app.route(route="GetVisitorCount", methods=["GET", "POST", "OPTIONS"])
def GetVisitorCount(req: func.HttpRequest) -> func.HttpResponse:
    """Azure Function endpoint - chiama la business logic"""
    return get_visitor_count_logic(req)
