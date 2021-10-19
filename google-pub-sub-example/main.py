import base64
import logging

def hello_pubsub(event, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
                        event. The `@type` field maps to
                         `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
                        The `data` field maps to the PubsubMessage data
                        in a base64-encoded string. The `attributes` field maps
                        to the PubsubMessage attributes if any is present.
         context (google.cloud.functions.Context): Metadata of triggering event
                        including `event_id` which maps to the PubsubMessage
                        messageId, `timestamp` which maps to the PubsubMessage
                        publishTime, `event_type` which maps to
                        `google.pubsub.topic.publish`, and `resource` which is
                        a dictionary that describes the service API endpoint
                        pubsub.googleapis.com, the triggering topic's name, and
                        the triggering event type
                        `type.googleapis.com/google.pubsub.v1.PubsubMessage`.
    Returns:
        None. The output is written to Cloud Logging.
    """
    import base64

    print("""This Function was triggered by messageId {} published at {} to {}
    """.format(context.event_id, context.timestamp, context.resource["name"]))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    print('Hello {}!'.format(name))


# Triggered from a message on a Cloud Pub/Sub topic.
def subscribe(event, context):
    # Print out the data from Pub/Sub, to prove that it worked
    print(event)
    logging.info(str(event))


import base64
import json
import os

from google.cloud import pubsub


# Instantiates a Pub/Sub client
publisher = pubsub.PublisherClient()
PROJECT_ID = 'leasera-200719'


# Publishes a message to a Cloud Pub/Sub topic.
def publish(request):
    #request_json = request.get_json(silent=True)

    #topic_name = request_json.get("topic")
    #message = request_json.get("message")

    #if not topic_name or not message:
    #    return ('Missing "topic" and/or "message" parameter.', 400)

    print('Publishing message to topic ')

    # References an existing topic
    #topic_path = publisher.topic_path(PROJECT_ID, 'queueDemo')

    #message_json = json.dumps({
    #    'data': {'message': "abc"},
    #})
    #message_bytes = message_json.encode('utf-8')

    # Publishes a message
    try:
        publish_future = publisher.publish('projects/leasera-200719/topics/queueDemo', data=b'New lead comment added.', key="value")
#        publish_future.result()  # Verify the publish succeeded
        return 'Message published.'
    except Exception as e:
        print(e)
        return str(e)
