resource "aws_launch_configuration" "asg_template" {
  name_prefix          = var.template_name_prefix
  image_id             = var.template_image_id
  instance_type        = var.template_instance_type
  user_data            = "#!/bin/bash\necho ECS_CLUSTER=${aws_ecs_cluster.ecs_cluster.name} >> /etc/ecs/ecs.config"
  iam_instance_profile = var.asg_iam_instance_profile
}

resource "aws_autoscaling_group" "asg_group" {
  name                = var.asg_name
  desired_capacity    = var.asg_desired_capacity
  max_size            = var.asg_max_size
  min_size            = var.asg_min_size
  vpc_zone_identifier = var.asg_vpc_zone_identifier

  launch_configuration = aws_launch_configuration.asg_template.id
}