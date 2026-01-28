# Tests per Azure Function - Visitor Counter

## 🧪 Test Suite Completa

Questa test suite copre tutti gli aspetti della funzione `GetVisitorCount`:

### Test Inclusi:

1. ✅ **test_counter_increment_success** - Verifica che il contatore incrementi correttamente
2. ✅ **test_counter_first_visit** - Testa la creazione del contatore al primo visitatore
3. ✅ **test_options_preflight_request** - Verifica la gestione delle richieste OPTIONS (CORS)
4. ✅ **test_cors_headers_present** - Controlla che i CORS headers siano presenti
5. ✅ **test_post_method_works** - Verifica che il metodo POST funzioni
6. ✅ **test_cosmos_connection_error** - Gestione errori di connessione CosmosDB
7. ✅ **test_upsert_error** - Gestione errori durante l'aggiornamento
8. ✅ **test_missing_environment_variables** - Verifica errore per variabili mancanti
9. ✅ **test_json_response_format** - Valida il formato JSON della risposta

## 📦 Installazione

```bash
cd backend
pip install -r requirements-dev.txt --break-system-packages
```

## 🚀 Esecuzione Test

### Test Completi con Coverage
```bash
pytest tests/ -v --cov=function_app --cov-report=html
```

### Solo Test Veloci
```bash
pytest tests/ -v
```

### Test Specifico
```bash
pytest tests/test_function.py::TestGetVisitorCount::test_counter_increment_success -v
```

### Con Output Dettagliato
```bash
pytest tests/ -vv -s
```

## 📊 Coverage Report

Dopo aver eseguito i test, apri il report HTML:
```bash
open htmlcov/index.html
```

Target: **80%+ coverage** ✅

## 🎯 Obiettivi di Testing

- ✅ **Unit Tests**: Testano ogni funzione in isolamento
- ✅ **Mocking**: Simulano CosmosDB senza connessione reale
- ✅ **Edge Cases**: Coprono scenari di errore
- ✅ **CORS**: Verificano headers di sicurezza
- ✅ **HTTP Methods**: Testano GET, POST, OPTIONS

## 🔄 CI/CD Integration

I test vengono eseguiti automaticamente su ogni push tramite GitHub Actions.
Vedi: `.github/workflows/test.yml`

## 📝 Convenzioni

- File di test: `test_*.py`
- Classi di test: `Test*`
- Metodi di test: `test_*`
- Fixtures in `conftest.py` (se necessario)

## 🐛 Debug

Per vedere i log durante i test:
```bash
pytest tests/ -v -s --log-cli-level=INFO
```

## ✨ Best Practices

1. Ogni test testa UNA cosa specifica
2. Mock delle dipendenze esterne (CosmosDB)
3. Test sia success che failure cases
4. Nomi descrittivi per i test
5. Assert chiari e specifici
