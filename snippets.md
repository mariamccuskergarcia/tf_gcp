
# terraform fmt
- this will fix the format, not the code

# terraform init
- this begins terraform, need to do each time creating new module

# terraform plan -out plan.tfplan
- this creates a terraform plan

# terraform apply plan.tfplan
- this executes the plan

# terraform apply
- this allows you to apply without doing the whole plan again (type 'yes')

# terraform destroy
- destroys your current terraform init

# terraform plan -var-file=dev.tfvars --out plan.tfplan
- this will add the coded variables to the plan

# terraform-docs markdown .
- this creates a markdown file with all your info specified - can put this in a 'README.md' file