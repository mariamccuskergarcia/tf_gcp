## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_archive"></a> [archive](#requirement\_archive) | 2.3.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.4.3 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_archive"></a> [archive](#provider\_archive) | 2.3.0 |
| <a name="provider_google"></a> [google](#provider\_google) | n/a |
| <a name="provider_random"></a> [random](#provider\_random) | 3.4.3 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [google_cloud_run_service_iam_member.allow_unauthenticated](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_service_iam_member) | resource |
| [google_cloudfunctions2_function.function](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function) | resource |
| [google_cloudfunctions2_function_iam_member.invoker](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function_iam_member) | resource |
| [google_storage_bucket.bucket](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket) | resource |
| [google_storage_bucket_object.zip](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object) | resource |
| [random_uuid.python_src_hash](https://registry.terraform.io/providers/hashicorp/random/3.4.3/docs/resources/uuid) | resource |
| [archive_file.source](https://registry.terraform.io/providers/hashicorp/archive/2.3.0/docs/data-sources/file) | data source |
| [google_cloud_run_service.run_service](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloud_run_service) | data source |
| [google_project.project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/project) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_entry_point"></a> [entry\_point](#input\_entry\_point) | Cloud function entry point | `string` | n/a | yes |
| <a name="input_function_name"></a> [function\_name](#input\_function\_name) | Cloud function name | `string` | n/a | yes |
| <a name="input_gcp_project_id"></a> [gcp\_project\_id](#input\_gcp\_project\_id) | GCP project id | `string` | n/a | yes |
| <a name="input_gcp_region"></a> [gcp\_region](#input\_gcp\_region) | GCP deployment region | `string` | n/a | yes |
| <a name="input_python_runtime"></a> [python\_runtime](#input\_python\_runtime) | Python runtime version | `string` | n/a | yes |
| <a name="input_python_source"></a> [python\_source](#input\_python\_source) | Function source code location | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_url"></a> [url](#output\_url) | Target Cloud function url |
