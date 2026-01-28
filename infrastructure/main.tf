# Resource Group
resource "azurerm_resource_group" "resume" {
  name     = var.resource_group_name
  location = var.location
  tags     = var.tags
}

# Storage Account per Static Website
resource "azurerm_storage_account" "resume" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.resume.name
  location                 = azurerm_resource_group.resume.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  
  static_website {
    index_document     = "index.html"
    error_404_document = "index.html"
  }
  
  tags = var.tags
}

# Cosmos DB Account
resource "azurerm_cosmosdb_account" "resume" {
  name                = var.cosmosdb_account_name
  location            = azurerm_resource_group.resume.location
  resource_group_name = azurerm_resource_group.resume.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"
  
  capabilities {
    name = "EnableServerless"
  }
  
  consistency_policy {
    consistency_level = "Session"
  }
  
  geo_location {
    location          = azurerm_resource_group.resume.location
    failover_priority = 0
  }
  
  tags = var.tags
}

# Cosmos DB Database
resource "azurerm_cosmosdb_sql_database" "resume" {
  name                = "ResumeDB"
  resource_group_name = azurerm_cosmosdb_account.resume.resource_group_name
  account_name        = azurerm_cosmosdb_account.resume.name
}

# Cosmos DB Container
resource "azurerm_cosmosdb_sql_container" "visitor_counter" {
  name                = "VisitorCounter"
  resource_group_name = azurerm_cosmosdb_account.resume.resource_group_name
  account_name        = azurerm_cosmosdb_account.resume.name
  database_name       = azurerm_cosmosdb_sql_database.resume.name
  partition_key_paths = ["/id"]
}

# App Service Plan (Consumption)
resource "azurerm_service_plan" "function" {
  name                = "ASP-resumerg-b3d3"  # Nome esistente
  resource_group_name = azurerm_resource_group.resume.name
  location            = var.location_function  # Function in westeurope
  os_type             = "Linux"
  sku_name            = "Y1"
  
  tags = var.tags
}

# Application Insights
resource "azurerm_application_insights" "function" {
  name                = "${var.function_app_name}"
  location            = var.location_function  # Function in westeurope
  resource_group_name = azurerm_resource_group.resume.name
  application_type    = "web"
  workspace_id        = "/subscriptions/85a1d18b-76e8-4d1c-94e4-e5ce805c53d3/resourceGroups/DefaultResourceGroup-WEU/providers/Microsoft.OperationalInsights/workspaces/DefaultWorkspace-85a1d18b-76e8-4d1c-94e4-e5ce805c53d3-WEU"
  
  tags = var.tags
}

# Function App
resource "azurerm_linux_function_app" "resume" {
  name                       = var.function_app_name
  resource_group_name        = azurerm_resource_group.resume.name
  location                   = var.location_function  # Function in westeurope
  storage_account_name       = azurerm_storage_account.resume.name  # USA LO STORAGE ESISTENTE
  storage_account_access_key = azurerm_storage_account.resume.primary_access_key
  service_plan_id            = azurerm_service_plan.function.id
  https_only                 = true  # MANTIENE HTTPS OBBLIGATORIO
  
  site_config {
    application_stack {
      python_version = "3.10"  # MANTIENE PYTHON 3.10
    }
    
    cors {
      allowed_origins = [
        "https://lucapcv.z6.web.core.windows.net"
      ]
    }
  }
  
  app_settings = {
    "FUNCTIONS_WORKER_RUNTIME"       = "python"
    "APPINSIGHTS_INSTRUMENTATIONKEY" = azurerm_application_insights.function.instrumentation_key
    "COSMOS_ENDPOINT"                = azurerm_cosmosdb_account.resume.endpoint
    "COSMOS_KEY"                     = azurerm_cosmosdb_account.resume.primary_key
  }
  
  tags = var.tags
}
