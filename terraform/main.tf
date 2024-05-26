# terraform/main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

module "eks" {
  source          = "terraform-aws-modules/eks/aws"
  cluster_name    = "devops-beatmaster-eks"
  cluster_version = "1.28"
  subnets         = ["subnet-1", "subnet-2"]
  vpc_id          = aws_vpc.main.id
}

resource "aws_s3_bucket" "frontend" {
  bucket = "devops-beatmaster-frontend"
  acl    = "public-read"
}
