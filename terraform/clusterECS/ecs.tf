resource "aws_ecs_cluster" "ecs_cluster" {
  name = var.ecs_cluster_name
}
resource "aws_ecs_cluster_capacity_providers" "ecs_capacity_provider" {
  cluster_name       = aws_ecs_cluster.ecs_cluster.name
  capacity_providers = [aws_ecs_capacity_provider.capacity_provider.name]

  default_capacity_provider_strategy {
    base              = 1
    weight            = 100
    capacity_provider = aws_ecs_capacity_provider.capacity_provider.name
  }
}
resource "aws_ecs_capacity_provider" "capacity_provider" {
  name = var.ecs_capacity_name

  auto_scaling_group_provider {
    auto_scaling_group_arn = aws_autoscaling_group.asg_group.arn
  }
}