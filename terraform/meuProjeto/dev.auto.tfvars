envinroment   = "dev"
instance_type = "t1.micro"
iam_tags = {
  "Create"    = "15-03-22"
  "ManagedBy" = "Terraform"
  "Project"   = "dev"
}
instance_tags = {
  "Name"      = "linuxInstance"
  "Create"    = "10-03-2023"
  "ManagedBy" = "Terraform"
  "Project"   = "dev"
}
bucket_tags = {
  "Name"       = "My bucket"
  "ManagedBy"  = "Terraform"
  "UpdateDate" = "10-03-2023"
  "Project"    = "dev"
}