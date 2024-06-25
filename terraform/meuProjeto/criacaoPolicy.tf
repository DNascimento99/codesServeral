resource "aws_iam_user_policy" "policy_daniel_testes" {
  name = var.policy_name
  user = var.iam_name
  depends_on = [
    aws_iam_user.user_daniel_testes
  ]
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "ec2:Describe*",
        ]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}
data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
    principals {
      type        = "AWS"
      identifiers = [aws_iam_user.user_daniel_testes.arn]
    }
    actions = ["sts:AssumeRole"]
  }
}