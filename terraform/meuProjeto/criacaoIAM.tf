resource "aws_iam_user" "user_daniel_testes" {
  name          = var.iam_name
  path          = var.iam_path
  force_destroy = var.iam_force_destroy
  tags          = var.iam_tags
}
resource "aws_iam_access_key" "key_daniel_testes" {
  user = var.iam_name
  depends_on = [
    aws_iam_user.user_daniel_testes
  ]
}
resource "aws_iam_instance_profile" "iam_profile" {
  name = var.iam_profile_name
  role = var.iam_role_name
}
resource "aws_iam_role" "iam_role" {
  name               = var.iam_role_name
  path               = var.iam_path
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}