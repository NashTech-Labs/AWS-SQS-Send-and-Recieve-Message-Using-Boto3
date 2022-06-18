import boto3
import os
import json

AWS_SQS_QUEUE_NAME = "<your_queue_name>"

class SQSQueue(object):

    def __init__(self, queueName=None):
        self.resource = boto3.resource('sqs', region_name='ap-south-1',
                                       aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
                                       aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))
        self.queue = self.resource.get_queue_by_name(QueueName=AWS_SQS_QUEUE_NAME)
        self.QueueName = queueName

    def send(self, Message={}):
        data = json.dumps(Message)
        response = self.queue.send_message(MessageBody=data)
        return response

if __name__ == "__main__":
    q = SQSQueue(queueName=AWS_SQS_QUEUE_NAME)
    Message = {"<your_message>"}
    response = q.send(Message=Message)
    print(response)
   