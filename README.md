# Stori Pedro Flores Test

This project is the Pedro Flores test for trying to enter at Stori Company. The project consist in read a CSV file (included in this repo) make calculation by monthly (debit and credit), and then send an email to this address: <pepitonx@gmail.com>.

- stori - Code for the application's Lambda function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

## Pre-requisites for local development
* Install Python 3.11.
* Install pip.
* Install pytest globally.
* Install AWS CLI.
* Install SAM CLI.
* Install Docker.
* Make login into your AWS account, in my case I logged in with my personal account. I made this through visual code.

## Use the SAM CLI to build and test locally

If your are on a UNIX system you can use the make command for installation and execution proccess.

```bash
make build
make invoke
```
Or you can invoke it manually.

```bash
sam build --use-container
sam local invoke StoriFunction
```

The SAM CLI installs dependencies defined in `stori/requirements.txt`, creates a deployment package, and saves it in the `.aws-sam/build` folder.

In my case I was using VisualCode for developing this project, so I enter my AWS credentials in Visual Code, and for run the code I used the play button to execute the lambda.

## Testing in production
I manually deploy the lambda to the AWS account, for testing you have to acces to this [url](https://iqhbl755mxjscqsuvbakvcfavi0dfwxh.lambda-url.us-east-1.on.aws/). You can request me to resend the email to your email address.


## Troubleshooting
* If your are not getting a result you should check if you are logged in correctly into your AWS account, it could be on visual code or in the terminal.
* The lambda is not sending the email: first you have to add the email that you want to send to the SES service, then you have to verify the email, after that you can use it.

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
