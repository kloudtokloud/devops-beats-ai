# terraform/variables.tf

variable "region" {
  description = "The AWS region to deploy to"
  type        = string
  default     = "us-east-1"
}

variable "vpc_cidr" {
  description = "The CIDR block for the VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "subnets" {
  description = "A list of subnet IDs"
  type        = list(string)
  default     = ["subnet-1", "subnet-2"]
}

variable "bucket_name" {
  description = "The name of the S3 bucket for frontend"
  type        = string
  default     = "devops-beatmaster-frontend"
}
