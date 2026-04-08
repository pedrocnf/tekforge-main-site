output "service_name" {
  value = google_cloud_run_v2_service.tekforge.name
}

output "service_uri" {
  value = google_cloud_run_v2_service.tekforge.uri
}

output "artifact_registry_repository" {
  value = google_artifact_registry_repository.tekforge.id
}
