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

    def receive(self):
        try:
            queue = self.resource.get_queue_by_name(QueueName=self.QueueName)
            for message in queue.receive_messages():
                data = message.body
                data = json.loads(data)
                message.delete()
        except Exception:
            return []
        return data


if __name__ == "__main__":
    q = SQSQueue(queueName=AWS_SQS_QUEUE_NAME)
    data = q.receive()
    print(data)