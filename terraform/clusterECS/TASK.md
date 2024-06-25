# Etapas para criar um ECS

## Setup Network

* VPC
* Subnet privada
* Subnet publica
    * Route Table
    * ACL
    * SG
* Internet GW
* Nat GW

## Setup ECS Cluster

* ECS Cluster
* ECS Cluster Capacity Provider
* ECS Capacity Provider ASG
    * ASG Definition
    * ASG 

## Setup ECS Task Definition

* Imagem 
* Mapeamento de portas
* Definição da maquina
    * CPU
    * Memory

## Setup ECS Service

* Definição da task
* Definição do Capacity Provider
* Peso
* Quantidade minima de task
* Passar dependência da criação do Capacity Provider