import unittest
from unittest import mock

import main


class NotifyStorageClassMatchTest(unittest.TestCase):

    @mock.patch.object(main.pubsub_v1, 'PublisherClient')
    def test_notify_storage_class_match_should_publish_if_archive(
            self, mock_publisher_client):

        fake_storage_object = {'storageClass': 'ARCHIVE'}
        main.notify_storage_class_match(fake_storage_object, mock.MagicMock())

        mock_publisher_client.return_value.publish.assert_called_once()

    @mock.patch.object(main.pubsub_v1, 'PublisherClient')
    def test_notify_storage_class_match_should_not_publish_if_not_archive(
            self, mock_publisher_client):

        fake_storage_object = {'storageClass': 'STANDARD'}
        main.notify_storage_class_match(fake_storage_object, mock.MagicMock())

        mock_publisher_client.return_value.publish.assert_not_called()
