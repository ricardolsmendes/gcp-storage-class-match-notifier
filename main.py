import json
import os

from google.cloud import pubsub_v1


def notify_storage_class_change(event, context):
    """Background Cloud Function to be triggered by Cloud Storage when an
       object's metadata is changed.
       This function publishes a message to Pub/Sub when the object's storage
       class is ARCHIVE.
    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    print(f'Event ID: {context.event_id}')
    print(f'Event type: {context.event_type}')
    print(f'Bucket: {event["bucket"]}')
    print(f'File: {event["name"]}')
    print(f'Metageneration: {event["metageneration"]}')
    print(f'Created: {event["timeCreated"]}')
    print(f'Updated: {event["updated"]}')
    print(f'Storage class update time: {event["timeStorageClassUpdated"]}')

    current_storage_class = event['storageClass']
    print('Storage class: {}'.format(current_storage_class))

    archive_storage_class = 'ARCHIVE'
    if current_storage_class != archive_storage_class:
        print('Skipping Pub/Sub notification...')
        return

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(os.getenv('PUB_SUB_PROJECT_ID'),
                                      os.getenv('PUB_SUB_TOPIC_ID'))

    data = json.dumps(event)
    # Data must be a bytestring.
    data = data.encode("utf-8")

    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data)
    print(future.result())

    print(f'Message published to {topic_path}.')
