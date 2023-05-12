now we will going to crate the image form the this docker file: docker build -t my-flask-app .
docker images     # to check the images is created
then run docker container from that image.
docker run -p 5000:5000 my-flask-app      # run on port 5000 in container and in localmachine as well -d is use to deattach
now deploying the docker image to the ECR in amazon 
link how we use boto3 to deploy image to ECR with SDK using python https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

then create ecr.py to create repo in aws ecr
after create the repo then take the credential from repo "view push" command button
in terminal run aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 
push the image to ECR

after deploying the image then create EKS cluster 
after creating the cluster create node on the cluster 

then deploy pods using kubernetes deployment - search kubernetes deployment https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
and also deploy services - https://kubernetes.io/docs/concepts/services-networking/service/

aws eks update-kubeconfig --name cloud_native_cluster   # this how we load the config




