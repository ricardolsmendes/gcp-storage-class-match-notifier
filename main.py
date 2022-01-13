import json
import os

from google.cloud import pubsub_v1


def notify_storage_class_match(storage_object, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This function publishes a message to Pub/Sub when the object's storage
       class is ARCHIVE. The message body is fulfilled with the
       `storage_object` dictionary content.
    Args:
        storage_object (dict): Contains a description of the object in the
                               Cloud Storage `object` format described here:
                               https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging.
    """
    print(f'Event ID: {context.event_id}')
    print(f'Event type: {context.event_type}')
    print(f'Bucket: {storage_object.get("bucket")}')
    print(f'File: {storage_object.get("name")}')
    print(f'Metageneration: {storage_object.get("metageneration")}')
    print(f'Created: {storage_object.get("timeCreated")}')
    print(f'Updated: {storage_object.get("updated")}')
    print(f'Storage class update time:'
          f' {storage_object.get("timeStorageClassUpdated")}')

    current_storage_class = storage_object.get('storageClass')
    print('Storage class: {}'.format(current_storage_class))

    archive_storage_class = 'ARCHIVE'
    if current_storage_class != archive_storage_class:
        print('Skipping Pub/Sub notification...')
        return

    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(os.getenv('PUBSUB_PROJECT_ID'),
                                      os.getenv('PUBSUB_TOPIC_ID'))

    # Data must be a bytestring.
    data = json.dumps(storage_object)
    data = data.encode("utf-8")

    # When you publish a message, the client returns a future.
    # The .result() method will block until the future is complete.
    # If there is an error, it will raise an exception.
    future = publisher.publish(topic_path, data)
    message_id = future.result()

    print(f'Message {message_id} published to {topic_path}.')
