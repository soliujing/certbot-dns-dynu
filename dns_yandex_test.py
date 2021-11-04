"""Tests for certbot_dns_yandex.dns_yandex"""

import os
import unittest

import mock
from requests.exceptions import HTTPError

from certbot.plugins import dns_test_common
from certbot.plugins import dns_test_common_lexicon
from certbot.plugins.dns_test_common import DOMAIN

from certbot.tests import util as test_util

AUTH_TOKEN = '123456789ABCDEF0000000000000000000000000000000000000'


class AuthenticatorTest(test_util.TempDirTestCase,
                        dns_test_common_lexicon.BaseLexiconAuthenticatorTest):

    def setUp(self):
        super(AuthenticatorTest, self).setUp()

        from certbot_dns_yandex.dns_yandex import Authenticator

        path = os.path.join(self.tempdir, 'file.ini')
        dns_test_common.write(
            {"yandex_auth_token": AUTH_TOKEN},
            path
        )

        print("File content: ")
        # print(open(path).read())
        with open(path) as f:
            print(f.read())

        self.config = mock.MagicMock(yandex_credentials=path,
                                     yandex_propagation_seconds=0)  # don't wait during tests

        self.auth = Authenticator(self.config, "yandex")

        self.mock_client = mock.MagicMock()
        # _get_yandex_client | pylint: disable=protected-access
        self.auth._get_yandex_client = mock.MagicMock(return_value=self.mock_client)



class yandexLexiconClientTest(unittest.TestCase,
                                dns_test_common_lexicon.BaseLexiconClientTest):
    DOMAIN_NOT_FOUND = HTTPError('422 Client Error: Unprocessable Entity for url: {0}.'.format(DOMAIN))
    LOGIN_ERROR = HTTPError('401 Client Error: Unauthorized')

    def setUp(self):
        from certbot_dns_yandex.dns_yandex import _yandexLexiconClient

        self.client = _yandexLexiconClient(auth_token=AUTH_TOKEN, ttl=0)

        self.provider_mock = mock.MagicMock()
        self.client.provider = self.provider_mock


if __name__ == "__main__":
    unittest.main()  # pragma: no cover