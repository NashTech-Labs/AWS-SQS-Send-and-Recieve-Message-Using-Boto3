### Amazon SQS
AWS SQS is a fast ,reliable ,fully managed message queue service .It is a webservice that gives you access to message queues that stores messages waiting to be processed.It is a fully manged message queuing service that enables you to decouple and scale microservices, distrubuted systems ,and severless application.

### Install Boto3:

`$ pip install boto3`

### Sending message in AWS SQS Queue:
Your AWS must be configured for this. Replace AWS_SQS_QUEUE_NAME with <your_queue_name> inside the code. Put your message there which you want to send and run the code using following command:

```
$ python3 send_message.py
```

### Recieving message from AWS SQS Queue:
Recieve your message using the following command:

```
$ python3 recieve_message.py
```


