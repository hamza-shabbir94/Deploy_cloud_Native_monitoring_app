import boto3

ecr_client = boto3.client('ecr')

repo_name = "my_cloud_native_repository"
response = ecr_client.create_repository(repositoryName=repo_name)

repo_uri = response['repository']['repositoryUri']
print(repo_uri)

# after create the repo then take the credential from repo "view push" command button
# in terminal run aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 