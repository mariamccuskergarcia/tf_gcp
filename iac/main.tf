module "mmg_function_gcp" {
  source         = "git::https://dev.azure.com/kubrick-training/ce06/_git/tf-gcp-function-module"
  gcp_project_id = var.gcp_project_id
  gcp_region = var.gcp_region
  python_source = var.python_source
  python_runtime = var.python_runtime
  function_name = var.function_name
  entry_point = var.entry_point
}
