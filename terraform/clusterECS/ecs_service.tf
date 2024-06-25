resource "aws_ecs_service" "tutum" {
  name            = var.service_name
  cluster         = var.ecs_cluster_name
  task_definition = aws_ecs_task_definition.taskdefinition.arn
  desired_count   = 1
  capacity_provider_strategy {
    capacity_provider = aws_ecs_capacity_provider.capacity_provider.name
    base = 1
    weight = 1
  }
  depends_on = [
    aws_ecs_capacity_provider.capacity_provider
  ]
}