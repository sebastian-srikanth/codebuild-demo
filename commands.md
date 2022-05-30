cmd:
aws ecr create-repository --repository-name demo-codebuild --region ap-south-1

response:
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:ap-south-1:670117393651:repository/demo-codebuild",
        "registryId": "670117393651",
        "repositoryName": "demo-codebuild",
        "repositoryUri": "670117393651.dkr.ecr.ap-south-1.amazonaws.com/demo-codebuild",
        "createdAt": 1653876228.0,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}


<!-- Setup Compute environment -->

 aws batch create-compute-environment --compute-environment-name batch-demo --type MANAGED --state ENABLED --compute-resources type=EC2,minvCpus=0,maxvCpus=256,desiredvCpus=0,instanceTypes=optimal,subnets=['subnet-1c106a50','subnet-b5c4d1dd','subnet-2e34b955'],securityGroupIds=['sg-ae0b3dc9'],instanceRole=arn:aws:iam::670117393651:instance-profile/ecsInstanceRole --service-role arn:aws:iam::670117393651:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch

 aws batch create-compute-environment --compute-environment spot-batch-demo --type MANAGED --state ENABLED --compute-resources type=SPOT,minvCpus=0,maxvCpus=256,desiredvCpus=0,instanceTypes=optimal,allocationStrategy=SPOT_CAPACITY_OPTIMIZED,subnets=['subnet-1c106a50','subnet-b5c4d1dd','subnet-2e34b955'],securityGroupIds=['sg-ae0b3dc9'],instanceRole=arn:aws:iam::670117393651:instance-profile/ecsInstanceRole --service-role arn:aws:iam::670117393651:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch

aws batch describe-compute-environments

<!-- Create Job queue -->
aws batch create-job-queue --job-queue-name=demo-queue --state=ENABLED --priority=100 --compute-environment-order order=1,computeEnvironment=batch-demo

aws batch update-job-queue --job-queue demo-queue --compute-environment-order order=1,computeEnvironment=spot-batch-demo


aws batch describe-job-queues

aws batch register-job-definition --job-definition-name=demo-definition --type=container --container-properties '{ "image": "670117393651.dkr.ecr.ap-south-1.amazonaws.com/demo-codebuild:latest", "vcpus": 1, "memory": 128, "command": [ "python", "main.py","sebastian"]}'


aws batch deregister-job-definition --job-definition demo-definition



aws batch describe-job-definitions

 aws batch submit-job --job-name test-batch-job --job-queue demo-queue --job-definition demo-definition --container-overrides command=["python","main.py srikanth"]

