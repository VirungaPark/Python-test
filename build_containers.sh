#!/bin/bash
PUSH_TO_ECR=false

$PUSH_TO_ECR && AWS_ACCOUNT_ID=$( aws sts get-caller-identity --query "Account" --output text )
$PUSH_TO_ECR && ( aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com ;)

for APP in app auth web; do
    cd $APP
    docker build . -t ${APP}:latest -f ./${APP}.Dockerfile
    $PUSH_TO_ECR && ( docker tag ${APP}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP}:latest ;)
    $PUSH_TO_ECR && ( docker push ${APP}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${APP}:latest ;)
    cd -
done