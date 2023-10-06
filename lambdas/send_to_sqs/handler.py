import json

from sqsHandler import SqsHandler

queue = SqsHandler("URLDAFILA")


def handler(event, context):
    queue.send(json.dumps(event))