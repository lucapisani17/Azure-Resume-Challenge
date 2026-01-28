variable "resource_group_name" {
  description = "Nome del resource group"
  type        = string
  default     = "resume-rg"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "italynorth"  # Cambiato da westeurope
}

variable "location_function" {
  description = "Azure region per Function App"
  type        = string
  default     = "westeurope"  # Function è in westeurope
}

variable "storage_account_name" {
  description = "Nome dello storage account (deve essere univoco)"
  type        = string
  default     = "lucapcv"
}

variable "function_app_name" {
  description = "Nome della Function App"
  type        = string
  default     = "resume-rg-counter"
}

variable "cosmosdb_account_name" {
  description = "Nome del Cosmos DB account"
  type        = string
  default     = "conta"  # Cambiato da resume-cosmosdb
}

variable "tags" {
  description = "Tags da applicare alle risorse"
  type        = map(string)
  default = {
    Environment = "Production"
    Project     = "Azure-Cloud-Resume-Challenge"
    ManagedBy   = "Terraform"
  }
}
