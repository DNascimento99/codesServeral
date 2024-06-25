resource "aws_ecs_task_definition" "taskdefinition" {
  family                   = var.task_family
  container_definitions    = "${file("${path.module}/ecs-task.json")}"
  cpu                      = var.task_cpu
  memory                   = var.task_memory
  requires_compatibilities = var.task_compatibilities
  network_mode             = var.task_network
}