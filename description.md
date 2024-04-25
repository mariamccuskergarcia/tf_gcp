# Creating a GCP function using a module

Reference function creation module:
https://dev.azure.com/kubrick-training/ce06/_git/tf-gcp-function-module

- Use the provided module
- Call the module with a source that points directly from AzDo Repo
- No hardcode the names or variables  >> all variables in a tfvars file used to deploy
- Make sure your resources have a clear prefix that identify you
- Extra: if you want you can use a more complex naming convention where your variables are used by locals and the locals build your names in a structured way
- Made as repository in AzDO, have gitignore that is appropriate (ignore those terraform specific files / python venv and other commonly ignored python files)

- When we run terraform apply with the right variables from inside the /iac folder of this repo >> it should create a function in GCP

- We will run this locally from our laptops

### Some tips:
- For this template the variable **python_source** will be `../src` (confirm that this is how you refer to a parent folder)
- When we pass a git source to a module this is the format:
```
source         = "git::https://dev.azure.com/kubrick-training/ce06/_git/tf-gcp-function-module"
```

