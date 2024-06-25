region_name       = "us-east-1"
profile_name      = "default"
bucket_name_1     = "bucket-danielnascimento-terrafromwithaws-1"
bucket_name_2     = "bucket-danielnascimento-terrafromwithaws-2"
instance_ami      = "ami-0557a15b87f6559cf"
instance_type     = "t2.micro"
iam_name          = "daniel-testes"
iam_path          = "/system/"
iam_force_destroy = true
iam_profile_name  = "profile-name"
iam_role_name     = "role-name"
policy_name       = "policy-name"
iam_tags = {
  "Create"    = "15-03-22"
  "ManagedBy" = "Terraform"
  "Project"   = "default"
}
instance_tags = {
  "Name"      = "linuxInstance"
  "Create"    = "10-03-2023"
  "ManagedBy" = "Terraform"
  "Project"   = "default"
}
bucket_tags = {
  "Name"       = "My bucket"
  "ManagedBy"  = "Terraform"
  "UpdateDate" = "10-03-2023"
}