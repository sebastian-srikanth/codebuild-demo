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
