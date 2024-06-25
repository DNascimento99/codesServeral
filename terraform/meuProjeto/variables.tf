variable "envinroment" {
  type        = string
  description = ""
}
##Main
variable "region_name" {
  type        = string
  description = "Nome da região"
}
variable "profile_name" {
  type        = string
  description = "Nome do perfil"
}
##Bucket
variable "bucket_name_1" {
  type        = string
  description = "Nome do bucket"
}
variable "bucket_name_2" {
  type        = string
  description = "Nome do bucket"
}
variable "bucket_tags" {
  type        = map(string)
  description = "Tags para o bucket"
}
##Instância
variable "instance_ami" {
  type        = string
  description = "Imagem utilizada para criação da instância"
}
variable "instance_type" {
  type        = string
  description = "Tipo da instância"
}

variable "instance_tags" {
  type        = map(string)
  description = "Tags para instância"
}
##Usuário IAM
variable "iam_name" {
  type        = string
  description = "Nome do usuário IAM"
}
variable "iam_path" {
  type        = string
  description = "Caminho da pasta do usuário"
}
variable "iam_force_destroy" {
  type        = bool
  description = "Força destruíção de qualquer alteração feita"
}
variable "iam_tags" {
  type        = map(string)
  description = "Tags do usuário IAM"
}
variable "iam_profile_name" {
  type        = string
  description = "Nome do profile do iam"
}
variable "iam_role_name" {
  type        = string
  description = "Nome da role do iam"
}
##Policy
variable "policy_name" {
  type        = string
  description = "Nome da policy"
}