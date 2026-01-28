output "resource_group_name" {
  description = "Nome del resource group"
  value       = azurerm_resource_group.resume.name
}

output "static_website_url" {
  description = "URL del sito web statico"
  value       = azurerm_storage_account.resume.primary_web_endpoint
}

output "function_app_name" {
  description = "Nome della Function App"
  value       = azurerm_linux_function_app.resume.name
}

output "function_app_url" {
  description = "URL della Function App"
  value       = azurerm_linux_function_app.resume.default_hostname
}

output "cosmosdb_endpoint" {
  description = "Endpoint di Cosmos DB"
  value       = azurerm_cosmosdb_account.resume.endpoint
  sensitive   = true
}

output "cosmosdb_primary_key" {
  description = "Chiave primaria di Cosmos DB"
  value       = azurerm_cosmosdb_account.resume.primary_key
  sensitive   = true
}

output "storage_account_name" {
  description = "Nome dello storage account"
  value       = azurerm_storage_account.resume.name
}
