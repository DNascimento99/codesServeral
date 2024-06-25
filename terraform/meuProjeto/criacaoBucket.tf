resource "aws_s3_bucket" "criacao_bucket_1" {
  bucket = var.bucket_name_1
  tags   = local.bucket_common_tags
}
resource "aws_s3_bucket" "criacao_bucket_2" {
  bucket = var.bucket_name_2
  tags   = local.bucket_common_tags
}