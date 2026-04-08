variable "project_id" {
  type = string
}

variable "region" {
  type    = string
  default = "us-central1"
}

variable "service_name" {
  type    = string
  default = "tekforge"
}

variable "artifact_registry_repository" {
  type    = string
  default = "tekforge"
}

variable "container_image" {
  type = string
}

variable "app_version" {
  type    = string
  default = "v12-deploy"
}

variable "site_url" {
  type    = string
  default = "https://tekforge.com.br"
}

variable "site_domain" {
  type    = string
  default = "tekforge.com.br"
}

variable "github_username" {
  type    = string
  default = "pedrocnf"
}
