terraform {
  required_version = ">= 1.5.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "tekforge" {
  location      = var.region
  repository_id = var.artifact_registry_repository
  description   = "Docker repository for TekForge"
  format        = "DOCKER"
}

resource "google_cloud_run_v2_service" "tekforge" {
  name     = var.service_name
  location = var.region

  template {
    max_instance_request_concurrency = 80
    timeout                          = "300s"

    containers {
      image = var.container_image

      ports {
        container_port = 8080
      }

      env {
        name  = "ENVIRONMENT"
        value = "production"
      }

      env {
        name  = "APP_VERSION"
        value = var.app_version
      }

      env {
        name  = "SITE_URL"
        value = var.site_url
      }

      env {
        name  = "SITE_DOMAIN"
        value = var.site_domain
      }

      env {
        name  = "GITHUB_USERNAME"
        value = var.github_username
      }

      resources {
        limits = {
          cpu    = "1"
          memory = "512Mi"
        }
      }
    }

    scaling {
      min_instance_count = 0
      max_instance_count = 1
    }
  }

  ingress = "INGRESS_TRAFFIC_ALL"
}

resource "google_cloud_run_service_iam_member" "public_invoker" {
  location = google_cloud_run_v2_service.tekforge.location
  service  = google_cloud_run_v2_service.tekforge.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
