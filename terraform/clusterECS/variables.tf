variable "template_name_prefix" {
  type        = string
  description = "a"
}
variable "template_image_id" {
  type        = string
  description = "a"
}
variable "template_instance_type" {
  type        = string
  description = "a"
}
variable "asg_name" {
  type        = string
  description = "a"
}
variable "asg_desired_capacity" {
  type        = number
  description = "a"
}
variable "asg_max_size" {
  type        = number
  description = "a"
}
variable "asg_min_size" {
  type        = number
  description = "a"
}
variable "asg_vpc_zone_identifier" {
  type        = list(string)
  description = "a"
}
variable "lauch_version" {
  type        = string
  description = "a"
}
variable "ecs_cluster_name" {
  type        = string
  description = "a"
}
variable "ecs_capacity_name" {
  type        = string
  description = "a"
}
variable "asg_iam_instance_profile" {
  type        = string
  description = "a"
}
variable "service_name" {
  type        = string
  description = "a"
}
variable "task_family" {
  type        = string
  description = "a"
}
variable "task_cpu" {
  type        = number
  description = "a"
}
variable "task_memory" {
  type        = number
  description = "a"
}
variable "task_compatibilities" {
  type        = list(string)
  description = "a"
}
variable "task_network" {
  type        = string
  description = "a"
}