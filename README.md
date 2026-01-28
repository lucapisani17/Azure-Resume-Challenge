# 🚀 Azure Cloud Resume Challenge

[![Deploy Azure Cloud Resume](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/deploy.yml/badge.svg)](https://github.com/lucapisani17/Azure-Resume-Challenge/actions/workflows/deploy.yml)

Un curriculum digitale moderno e interattivo costruito con tecnologie cloud-native Azure, completando l'**Azure Cloud Resume Challenge**.

## 🌐 Demo Live

**[Visualizza il CV →](https://lucapcv.z6.web.core.windows.net)**

## 📋 Panoramica del Progetto

Questo progetto dimostra competenze pratiche in:
- ☁️ **Cloud Computing** (Azure)
- 🐍 **Backend Development** (Python, Azure Functions)
- 🎨 **Frontend Development** (HTML/CSS/JavaScript)
- 🗄️ **Database** (Azure Cosmos DB)
- 🔄 **CI/CD** (GitHub Actions)
- 🏗️ **Infrastructure as Code** (Terraform/Bicep - in arrivo)

## 🏗️ Architettura
```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Azure Storage (Static Website)                       │  │
│  │  - HTML/CSS/JavaScript                                │  │
│  │  - HTTPS automatico                                   │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP Request
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Azure Functions                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  GetVisitorCount (Python 3.11)                        │  │
│  │  - CORS enabled                                       │  │
│  │  - Serverless compute                                 │  │
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
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                         ▲
                         │
┌────────────────────────┴────────────────────────────────────┐
│                   GitHub Actions CI/CD                       │
│  - Automated deployment on push                             │
│  - Frontend → Azure Storage                                 │
│  - Backend → Azure Functions                                │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Stack Tecnologico

### Frontend
- **HTML5** - Struttura semantica
- **CSS3** - Styling moderno con animazioni
- **JavaScript (Vanilla)** - Fetch API per chiamate backend

### Backend
- **Python 3.11** - Linguaggio di programmazione
- **Azure Functions** - Serverless compute
- **Azure Cosmos DB** - Database NoSQL

### DevOps
- **GitHub Actions** - CI/CD pipeline
- **Azure CLI** - Deployment automation
- **Git** - Version control

### Infrastructure (In Arrivo)
- **Terraform/Bicep** - Infrastructure as Code

## 📁 Struttura del Progetto
```
Azure-Resume-Challenge/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
├── frontend/
│   └── index.html              # CV HTML con CSS/JS inline
├── backend/
│   ├── function_app.py         # Azure Function
│   ├── requirements.txt        # Dipendenze Python
│   ├── host.json              # Configurazione Function
│   └── .funcignore            # File da ignorare nel deploy
├── tests/
│   └── test_function.py       # Unit tests (TODO)
├── infrastructure/
│   └── main.tf                # Terraform config (TODO)
├── .gitignore
└── README.md
```

## 🚀 Setup Locale

### Prerequisiti
- Python 3.11+
- Azure CLI
- Azure Functions Core Tools
- Node.js (opzionale, per testing frontend)

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
    "COSMOS_ENDPOINT": "your-cosmos-endpoint",
    "COSMOS_KEY": "your-cosmos-key"
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
```

## 🔄 Deployment

### Automatico (GitHub Actions)
Ogni push sul branch `main` triggera automaticamente il deployment:
1. Frontend → Azure Storage Static Website
2. Backend → Azure Functions

### Manuale

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
func azure functionapp publish resume-rg-counter
```

## 🧪 Testing
```bash
# Backend tests
cd tests
pytest test_function.py

# Frontend tests (TODO)
npm test
```

## 📊 Funzionalità

### ✅ Implementate
- [x] CV HTML responsive con design moderno
- [x] Contatore visite con Azure Functions
- [x] Database Cosmos DB per persistenza
- [x] Deploy automatico con GitHub Actions
- [x] HTTPS abilitato
- [x] CORS configurato
- [x] Versione bilingue (IT/EN)

### 🔄 In Sviluppo
- [ ] Infrastructure as Code (Terraform)
- [ ] Unit Tests completi
- [ ] Custom Domain + CDN
- [ ] Monitoring e Alerts
- [ ] Blog post documentazione

## 🎓 Azure Cloud Resume Challenge

Questo progetto completa l'[Azure Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/azure/), che include:

1. ✅ Certificazione (AZ-900 - opzionale)
2. ✅ HTML Resume
3. ✅ CSS Styling
4. ✅ Static Website (Azure Storage)
5. ✅ HTTPS
6. ⏳ Custom Domain (opzionale)
7. ✅ Visitor Counter (JavaScript)
8. ✅ Database (Cosmos DB)
9. ✅ API (Azure Functions)
10. ✅ Python Code
11. ⏳ Tests
12. ⏳ Infrastructure as Code
13. ✅ Source Control (GitHub)
14. ✅ CI/CD (GitHub Actions)
15. ⏳ Blog Post

## 📝 Licenza

Questo progetto è open source e disponibile sotto la [MIT License](LICENSE).

## 👤 Autore

**Luca Pisani**
- GitHub: [@lucapisani17](https://github.com/lucapisani17)
- Email: luca.pisani99@outlook.com
- LinkedIn: [Luca Pisani](https://linkedin.com/in/luca-pisani)

## 🙏 Riconoscimenti

- [Azure Cloud Resume Challenge](https://cloudresumechallenge.dev/)
- [Forrest Brazeal](https://forrestbrazeal.com/) - Creatore della challenge

---

⭐️ Se questo progetto ti è stato utile, lascia una stella!x

