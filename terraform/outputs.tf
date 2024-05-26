# terraform/outputs.tf

output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "eks_cluster_name" {
  description = "The name of the EKS cluster"
  value       = module.eks.cluster_id
}

output "s3_bucket_name" {
  description = "The name of the S3 bucket for frontend"
  value       = aws_s3_bucket.frontend.bucket
}
