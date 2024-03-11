create-stack:
	@echo "Creating CloudFormation stack..."
	aws cloudformation create-stack --stack-name QuestionAnswersStack --template-body file://dynamodb-table.yml --capabilities CAPABILITY_IAM

delete-stack:
	@echo "Deleting CloudFormation stack..."
	aws cloudformation delete-stack --stack-name QuestionAnswersStack
