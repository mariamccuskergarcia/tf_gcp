variable "gcp_project_id" {
  description = "GCP project id"
  type        = string
}

variable "gcp_region" {
  description = "GCP deployment region"
  type        = string
}

variable "python_source" {
  type        = string
  description = "Function source code location"
}

variable "python_runtime" {
  type        = string
  description = "Python runtime version"
}

variable "function_name" {
  type        = string
  description = "Cloud function name"
}

variable "entry_point" {
  type        = string
  description = "Cloud function entry point"
}