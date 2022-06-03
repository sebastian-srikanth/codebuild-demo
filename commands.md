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
<!--  EC2 -->
 aws batch create-compute-environment --compute-environment-name batch-demo --type MANAGED --state ENABLED --compute-resources type=EC2,minvCpus=0,maxvCpus=256,desiredvCpus=0,instanceTypes=optimal,subnets=['subnet-1c106a50','subnet-b5c4d1dd','subnet-2e34b955'],securityGroupIds=['sg-ae0b3dc9'],instanceRole=arn:aws:iam::670117393651:instance-profile/ecsInstanceRole --service-role arn:aws:iam::670117393651:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch

<!-- SPOT -->
 aws batch create-compute-environment --compute-environment spot-batch-demo --type MANAGED --state ENABLED --compute-resources type=SPOT,minvCpus=0,maxvCpus=256,desiredvCpus=0,instanceTypes=optimal,allocationStrategy=SPOT_CAPACITY_OPTIMIZED,subnets=['subnet-1c106a50','subnet-b5c4d1dd','subnet-2e34b955'],securityGroupIds=['sg-ae0b3dc9'],instanceRole=arn:aws:iam::670117393651:instance-profile/ecsInstanceRole --service-role arn:aws:iam::670117393651:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch

aws batch describe-compute-environments

<!-- Create Job queue -->
aws batch create-job-queue --job-queue-name=demo-queue --state=ENABLED --priority=100 --compute-environment-order order=1,computeEnvironment=spot-batch-demo

aws batch update-job-queue --job-queue demo-queue --compute-environment-order order=1,computeEnvironment=spot-batch-demo


aws batch describe-job-queues

aws batch register-job-definition --job-definition-name=demo-definition --type=container --container-properties '{ "image": "670117393651.dkr.ecr.ap-south-1.amazonaws.com/demo-codebuild:latest", "vcpus": 1, "memory": 128, "command": [ "python", "main.py","sebastian"]}'


aws batch deregister-job-definition --job-definition demo-definition



aws batch describe-job-definitions

 aws batch submit-job --job-name test-batch-job --job-queue demo-queue --job-definition demo-definition --container-overrides command=["python","main.py","srikanth"]

 aws codebuild create-project \
    --name codebuild-demo \
    --environment type=LINUX_CONTAINER,image=aws/codebuild/amazonlinux2-x86_64-standard:3.0,computeType=BUILD_GENERAL1_SMALL \
    --source type=GITHUB,location=https://github.com/sebastian-srikanth/codebuild-demo \
    --service-role arn:aws:iam::670117393651:role/demo-codebuild-role \
    --artifacts type=NO_ARTIFACTS


Image
aws/codebuild/amazonlinux2-x86_64-standard:3.0

Environment type
Linux

Service role
arn:aws:iam::670117393651:role/demo-codebuild-role


HEAD_REF
code-build

1. Move the data from DB1 to DB2
2. Get the data type report
3. Get the data reports with Graph
    Some issue with reporting and new dev
4. A dev goes on leave and client wants to run on his own
    Set up a container, install all packages, dependencies, build image and give
5. Lazy to run python main.py so client get fed up 
    As soon as the data comes to DB1 it has to go to DB2
6. Even though I get the wrong data I need to clean and load that data, So that I can fasten the data flow process
7. DB1 contract I lost and its giving poor performance I'm chaning the DB1
    7a. I need to add few more validations
    7b. And accept new source
        Batch process data
        Stream Data
8. I need a website that accepts any database to any database
9. Any cloud to any other cloud
10. Need a visualzations with charmings dashboards
11. Website should be able to run AI/ML algorithms
12. 