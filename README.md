# gcp-storage-class-match-notifier

Google Cloud Function that publishes messages to Pub/Sub when the metadata of a
GCS object changes and the object's storage class matches the given criteria — 
e.g., == `ARCHIVE`.

It has been used to notify other systems when GCS objects storage class changes
due to lifecycle rules being applied. Please notice that other metadata changes
will also trigger the function and publish messages to Pub/Sub if the storage
class matches the criteria.

[![license](https://img.shields.io/github/license/ricardolsmendes/gcp-storage-class-match-notifier.svg)](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/blob/main/LICENSE)
[![issues](https://img.shields.io/github/issues/ricardolsmendes/gcp-storage-class-match-notifier.svg)](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/issues)
[![continuous integration](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/actions/workflows/continuous-integration.yaml)

## Deployment instructions

```sh
export PUBSUB_PROJECT_ID=<YOUR-PROJECT-ID>
export PUBSUB_TOPIC_ID=<YOUR-PUBSUB-TOPIC-ID>
export STORAGE_CLASS_MATCH_NOTIF_SA=<PUBSUB-PUBLISHER-SERVICE-ACCOUNT-EMAIL>
export TRIGGER_BUCKET=<YOUR-BUCKET-NAME>

gcloud functions deploy notify-storage-class-match \
  --entry-point notify_storage_class_match \
  --runtime python39 \
  --service-account $STORAGE_CLASS_MATCH_NOTIF_SA \
  --set-env-vars PUBSUB_PROJECT_ID=$PUBSUB_PROJECT_ID,PUBSUB_TOPIC_ID=$PUBSUB_TOPIC_ID \
  --trigger-event google.storage.object.metadataUpdate \
  --trigger-resource $TRIGGER_BUCKET
```

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/blob/main/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/issues).

Before opening an issue, search the tracker for possible duplicates. If you
find a duplicate, please add a comment saying that you encountered the problem
as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/gcp-storage-class-match-notifier/blob/main/.github/CONTRIBUTING.md)
before making a pull request.
