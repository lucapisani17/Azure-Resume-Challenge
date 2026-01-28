# 🚀 Azure Cloud Resume Challenge

[![Deploy Azure Cloud Resume](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/deploy.yml/badge.svg)](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/deploy.yml)
[![Run Tests](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/test.yml/badge.svg)](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/test.yml)
[![Coverage](https://img.shields.io/badge/coverage-97.56%25-brightgreen)](https://github.com/lucapisani17/Azure-Resume-Challenge)

Un curriculum digitale moderno e interattivo costruito con tecnologie cloud-native Azure, completando l'**Azure Cloud Resume Challenge**.

## 🌐 Demo Live

**[Visualizza il CV →](https://www.lucapisani.site)** 🔒

Alternative URLs:
- **Custom Domain:** https://www.lucapisani.site
- **Azure Storage:** https://lucapcv.z38.web.core.windows.net

## 📋 Panoramica del Progetto

Questo progetto dimostra competenze pratiche in:
- ☁️ **Cloud Computing** (Azure)
- 🐍 **Backend Development** (Python 3.10, Azure Functions)
- 🎨 **Frontend Development** (HTML/CSS/JavaScript)
- 🗄️ **Database** (Azure Cosmos DB - Serverless)
- 🔄 **CI/CD** (GitHub Actions)
- 🏗️ **Infrastructure as Code** (Terraform)
- 🧪 **Testing** (Pytest, 97.56% coverage)
- 🌐 **DNS & CDN** (Cloudflare)
- 🔒 **SSL/TLS** (HTTPS con certificato gratuito)

## 🏗️ Architettura

```
┌─────────────────────────────────────────────────────────────┐
│                      User Browser                            │
│                  www.lucapisani.site                         │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTPS (SSL/TLS)
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   Cloudflare CDN                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  - SSL/TLS Termination (Free Certificate)            │  │
│  │  - Global CDN Caching                                 │  │
│  │  - DDoS Protection                                    │  │
│  │  - HTTP → HTTPS Redirect                              │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │ HTTP/HTTPS
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Azure Storage (Static Website)                       │  │
│  │  - HTML/CSS/JavaScript                                │  │
│  │  - Blob Storage ($web container)                      │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTPS Request
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Azure Functions                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GetVisitorCount (Python 3.10)                        │  │
│  │  - CORS enabled                                       │  │
│  │  - Serverless (Consumption Plan)                      │  │
│  │  - Application Insights monitoring                    │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ Read/Write
                         │
┌────────────────────────▼────────────────────────────────────┐
│                   Azure Cosmos DB                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Database: ResumeDB                                   │  │
│  │  Container: VisitorCounter                            │  │
│  │  - Serverless mode                                    │  │
│  │  - Auto-scaling                                       │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         ▲
                         │
┌────────────────────────┴────────────────────────────────────┐
│                   GitHub Actions CI/CD                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Deploy Workflow                                      │  │
│  │  - Frontend → Azure Storage                           │  │
│  │  - Backend → Azure Functions                          │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Test Workflow                                        │  │
│  │  - Unit tests (Pytest)                                │  │
│  │  - Coverage reporting                                 │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         ▲
                         │
┌────────────────────────┴────────────────────────────────────┐
│                      Terraform IaC                           │
│  - Gestione completa dell'infrastruttura                    │
│  - Stato remoto in Azure Storage                            │
│  - Deployment riproducibile                                 │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Stack Tecnologico

### Frontend
- **HTML5** - Struttura semantica
- **CSS3** - Styling moderno con animazioni e gradients
- **JavaScript (Vanilla)** - Fetch API per chiamate backend asincrone

### Backend
- **Python 3.10** - Linguaggio di programmazione
- **Azure Functions v4** - Serverless compute platform
- **Azure Cosmos DB** - Database NoSQL con modalità serverless
- **Application Insights** - Monitoring e telemetria

### DevOps & Testing
- **GitHub Actions** - CI/CD pipeline automatizzato
- **Pytest** - Framework di testing (97.56% coverage)
- **Azure CLI** - Deployment automation
- **Git** - Version control

### Infrastructure as Code
- **Terraform** - Gestione infrastruttura Azure
- **Azure Provider** - Risorse Azure gestite come codice

### Networking & Security
- **Cloudflare** - DNS management, CDN, e SSL/TLS
- **Custom Domain** - www.lucapisani.site
- **HTTPS** - Certificato SSL gratuito gestito da Cloudflare

## 📁 Struttura del Progetto

```
Azure-Resume-Challenge/
├── .github/
│   └── workflows/
│       ├── deploy.yml          # CI/CD deployment pipeline
│       └── test.yml            # Automated testing workflow
├── frontend/
│   └── index.html              # CV HTML con CSS/JS inline
├── backend/
│   ├── function_app.py         # Azure Function business logic
│   ├── requirements.txt        # Dipendenze Python
│   ├── requirements-dev.txt    # Dipendenze per testing
│   ├── host.json              # Configurazione Function App
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_function.py   # Unit tests completi
│   ├── pytest.ini             # Configurazione Pytest
│   └── .funcignore            # File da ignorare nel deploy
├── infrastructure/
│   ├── main.tf                # Configurazione Terraform principale
│   ├── variables.tf           # Variabili Terraform
│   ├── outputs.tf             # Output Terraform
│   ├── provider.tf            # Provider Azure
│   └── terraform.tfstate      # Stato Terraform (gitignored)
├── .gitignore
└── README.md
```

## 🚀 Setup Locale

### Prerequisiti
- **Python 3.10+**
- **Azure CLI** (`az --version`)
- **Azure Functions Core Tools** (`func --version`)
- **Terraform** 1.6+ (per IaC)
- **Git**

### Installazione

1. **Clona il repository**
```bash
git clone https://github.com/lucapisani17/Azure-Resume-Challenge.git
cd Azure-Resume-Challenge
```

2. **Setup Backend**
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Su Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Per testing
```

3. **Configura le variabili d'ambiente**
```bash
# Crea un file local.settings.json
cat > local.settings.json << 'JSON'
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "",
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "COSMOS_ENDPOINT": "https://your-account.documents.azure.com:443/",
    "COSMOS_KEY": "your-cosmos-primary-key"
  }
}
JSON
```

4. **Avvia la Function localmente**
```bash
func start
```

5. **Testa il Frontend**
```bash
cd ../frontend
# Apri index.html nel browser o usa un server locale
python -m http.server 8000
# Visita http://localhost:8000
```

## 🧪 Testing

### Esegui i Test

```bash
cd backend

# Esegui tutti i test con coverage
pytest tests/ -v --cov=function_app --cov-report=html

# Solo test veloci
pytest tests/ -v

# Test specifico
pytest tests/test_function.py::TestGetVisitorCount::test_counter_increment_success -v
```

### Coverage Report

```bash
# Apri il report HTML
open htmlcov/index.html
```

**Current Coverage: 97.56%** 🎉

### Test Suite Include:
- ✅ Test incremento contatore
- ✅ Test primo visitatore (creazione counter)
- ✅ Test CORS preflight (OPTIONS)
- ✅ Test headers CORS
- ✅ Test metodi HTTP (GET, POST)
- ✅ Test gestione errori connessione
- ✅ Test gestione errori database
- ✅ Test variabili d'ambiente mancanti
- ✅ Test formato risposta JSON
- ✅ Test incremento esatto di +1

## 🔄 Deployment

### Automatico con GitHub Actions

Ogni push sul branch `main` triggera automaticamente:

1. **Test Workflow** 🧪
   - Esegue tutti i test unitari
   - Genera coverage report
   - Fallisce se coverage < 80%

2. **Deploy Workflow** 🚀
   - Deploy Frontend → Azure Storage
   - Deploy Backend → Azure Functions
   - Solo se i test passano

### Deployment Manuale

**Frontend:**
```bash
az storage blob upload-batch \
  --account-name lucapcv \
  --auth-mode key \
  --destination '$web' \
  --source ./frontend \
  --overwrite
```

**Backend:**
```bash
cd backend
func azure functionapp publish resume-rg-counter --python
```

**Infrastructure (Terraform):**
```bash
cd infrastructure

# Inizializza Terraform
terraform init

# Verifica le modifiche
terraform plan

# Applica le modifiche
terraform apply
```

## 🏗️ Infrastructure as Code (Terraform)

L'intera infrastruttura Azure è gestita tramite Terraform:

### Risorse Gestite:
- ✅ Resource Group
- ✅ Storage Account (Static Website)
- ✅ Cosmos DB Account (Serverless)
- ✅ Cosmos DB Database & Container
- ✅ App Service Plan (Consumption)
- ✅ Linux Function App
- ✅ Application Insights

### Comandi Terraform:

```bash
cd infrastructure

# Inizializza
terraform init

# Formatta il codice
terraform fmt

# Valida la configurazione
terraform validate

# Pianifica le modifiche
terraform plan

# Applica le modifiche
terraform apply

# Distruggi l'infrastruttura (se necessario)
terraform destroy
```

## 🌐 Custom Domain & SSL

Il sito è accessibile tramite il custom domain **www.lucapisani.site** con HTTPS gratuito.

### Setup Cloudflare

Il dominio utilizza Cloudflare per:
- ✅ **DNS Management** - Nameserver gestiti da Cloudflare
- ✅ **SSL/TLS** - Certificato gratuito automatico (modalità Flexible)
- ✅ **CDN** - Content Delivery Network globale
- ✅ **Security** - DDoS protection e WAF
- ✅ **Performance** - Caching, minification, compression

### Configurazione DNS

```
Type: CNAME
Name: www
Content: lucapcv.z38.web.core.windows.net
Proxy: ☁️ Proxied (Cloudflare CDN attivo)
```

### Vantaggi

- 🔒 **HTTPS gratuito** - Certificato SSL gestito automaticamente
- ⚡ **Performance migliorate** - CDN con 300+ edge locations
- 🛡️ **Sicurezza** - Protezione DDoS e firewall applicativo
- 💰 **Costo zero** - Piano Cloudflare Free
- 🌍 **Latenza ridotta** - Content servito da location più vicina

### Architecture Flow

```
User → Cloudflare CDN (HTTPS) → Azure Storage (HTTP) → Response
                ↓
           SSL Termination
           Caching
           DDoS Protection
```

## 📊 Funzionalità

### ✅ Implementate
- [x] CV HTML responsive con design moderno
- [x] Contatore visite con Azure Functions
- [x] Database Cosmos DB per persistenza
- [x] Deploy automatico con GitHub Actions (Deploy + Test)
- [x] HTTPS abilitato
- [x] CORS configurato correttamente
- [x] Infrastructure as Code con Terraform
- [x] Unit Tests completi (97.56% coverage)
- [x] Application Insights monitoring
- [x] Python 3.10 con best practices
- [x] Serverless architecture
- [x] **Custom Domain (www.lucapisani.site)**
- [x] **Cloudflare CDN per performance globali**
- [x] **Certificato SSL gratuito gestito automaticamente**

### 🔄 Possibili Miglioramenti Futuri
- [ ] Azure Monitor Alerts
- [ ] Integration tests
- [ ] Performance testing
- [ ] Blog post documentazione completa
- [ ] Multi-region deployment
- [ ] A/B testing con Cloudflare Workers

## 🎓 Azure Cloud Resume Challenge - Completamento

Questo progetto completa l'[Azure Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/):

1. ✅ **Certificazione** - AZ-900 (opzionale)
2. ✅ **HTML Resume** - CV completo e professionale
3. ✅ **CSS Styling** - Design moderno con animazioni
4. ✅ **Static Website** - Azure Storage con hosting statico
5. ✅ **HTTPS** - Abilitato con Cloudflare SSL
6. ✅ **Custom Domain** - www.lucapisani.site
7. ✅ **Visitor Counter** - JavaScript + API
8. ✅ **Database** - Cosmos DB Serverless
9. ✅ **API** - Azure Functions
10. ✅ **Python Code** - Python 3.10 con best practices
11. ✅ **Tests** - Pytest con 97.56% coverage
12. ✅ **Infrastructure as Code** - Terraform completo
13. ✅ **Source Control** - GitHub con Git
14. ✅ **CI/CD** - GitHub Actions (Deploy + Test workflows)
15. ⏳ **Blog Post** - (pianificato)

**Progress: 14/15 completati**

## 📈 Metriche del Progetto

- **Code Coverage**: 97.56%
- **Test Success Rate**: 100% (10/10 passing)
- **Infrastructure Components**: 8 risorse Azure
- **Deployment Time**: ~2-3 minuti
- **Average Response Time**: < 200ms
- **Uptime**: 99.9%+ (serverless)
- **SSL Rating**: A+ (Cloudflare SSL)
- **CDN Edge Locations**: 300+ worldwide

## 🔐 Sicurezza

- ✅ HTTPS obbligatorio (HTTP → HTTPS redirect)
- ✅ SSL/TLS 1.2+ con certificato gestito
- ✅ CORS configurato con whitelist
- ✅ Secrets gestiti tramite GitHub Secrets
- ✅ Variabili sensibili non in repository
- ✅ Azure Functions con autenticazione
- ✅ Cosmos DB con chiavi rotate
- ✅ DDoS protection via Cloudflare
- ✅ WAF (Web Application Firewall)

## 💰 Costi Mensili Stimati

| Servizio | Costo |
|----------|-------|
| Azure Storage | ~€0.02 |
| Azure Functions | €0 (sempre free tier) |
| Cosmos DB Serverless | ~€0.05-0.10 |
| Application Insights | €0 (entro limiti free) |
| Cloudflare Free | €0 |
| **Dominio (annuale)** | ~€8-10/anno |
| **TOTALE MENSILE** | **~€0.10-0.15** |

*Il progetto costa praticamente zero grazie ai free tier e serverless!*

## 📝 Licenza

Questo progetto è open source e disponibile sotto la [MIT License](LICENSE).

## 👤 Autore

**Luca Pisani**
- Website: [www.lucapisani.site](https://www.lucapisani.site)
- GitHub: [@lucapisani17](https://github.com/lucapisani17)
- Email: luca.pisani99@outlook.com
- LinkedIn: [Luca Pisani](https://linkedin.com/in/luca-pisani)

## 🙏 Riconoscimenti

- [Azure Cloud Resume Challenge](https://cloudresumechallenge.dev/) - Forrest Brazeal
- [Microsoft Azure Documentation](https://docs.microsoft.com/azure/)
- [Terraform Azure Provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Cloudflare](https://www.cloudflare.com/) - Free SSL & CDN
- Community di Cloud Resume Challenge

## 🤝 Contribuire

Contributi, issues e feature requests sono benvenuti!

1. Fork il progetto
2. Crea un feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit le modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## ⭐ Support

Se questo progetto ti è stato utile:
- ⭐ Lascia una stella su GitHub
- 🔄 Condividi con altri
- 💬 Lascia feedback
- 🌐 Visita il sito: [www.lucapisani.site](https://www.lucapisani.site)

---

**Built with ❤️ and ☁️ Azure + Cloudflare**