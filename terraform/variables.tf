variable "sqs_queue_name" { type = string }
variable "sqs_queue_url" { type = string }

### Variables provided per default by the Makefile
variable "account_id" {}
variable "env" {}
variable "plan_name" {}
variable "region" {}
variable "repository" {}
