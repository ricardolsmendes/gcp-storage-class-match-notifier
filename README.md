# gcp-storage-class-change-notifier

Google Cloud Function that publishes messages to Pub/Sub when a GCS object's
metadata is changed and the storage class meets a given criterion 
(e.g., == `ARCHIVE`).

[![license](https://img.shields.io/github/license/ricardolsmendes/gcp-storage-class-change-notifier.svg)](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/blob/main/LICENSE)
[![issues](https://img.shields.io/github/issues/ricardolsmendes/gcp-storage-class-change-notifier.svg)](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/issues)
[![continuous integration](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/actions/workflows/continuous-integration.yaml/badge.svg)](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/actions/workflows/continuous-integration.yaml)

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/blob/main/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/issues).

Before opening an issue, search the tracker for possible duplicates. If you
find a duplicate, please add a comment saying that you encountered the problem
as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/gcp-storage-class-change-notifier/blob/main/.github/CONTRIBUTING.md)
before making a pull request.
