variable "env" {
  default = "prod"
}
variable "aws_region" {
  type = string
}
variable "sqs_queue_name" {
  type = string
}
variable "sqs_queue_url" {
  type = string
}
