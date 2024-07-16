import {
  to = aws_sqs_queue.csv_object_created
  id = "https://sqs.eu-west-3.amazonaws.com/505394176116/csv-object-created"
}

resource "aws_sqs_queue" "csv_object_created" {
  name                      = var.sqs_queue_name
  delay_seconds             = 90
  max_message_size          = 2048
  message_retention_seconds = 86400
  receive_wait_time_seconds = 10

  tags = {
    Environment = var.env
  }
}