"""DNS Authenticator for Yandex."""

import logging

import zope.interface
from certbot import interfaces
from certbot import errors

from certbot.plugins import dns_common
from certbot.plugins import dns_common_lexicon

from lexicon.providers import yandex

logger = logging.getLogger(__name__)


@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for Yandex."""

    description = 'Obtain certificates using a DNS TXT record ' + \
                  '(if you are using Yandex for DNS.)'

    ttl = 10

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)
        self.credentials = None

    @classmethod
    def add_parser_arguments(cls, add):
        super(Authenticator, cls).add_parser_arguments(
            add, default_propagation_seconds=180)
        add("credentials", help="Yandex credentials file.")

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using ' + \
               'Yandex API'

    def _setup_credentials(self):
        self._configure_file('credentials',
                             'Absolute path to Yandex credentials file')
        dns_common.validate_file_permissions(self.conf('credentials'))
        self.credentials = self._configure_credentials(
            'credentials',
            'Yandex credentials file',
            {
                'auth-token': 'Yandex PDD KEY',
            }
        )

    def _perform(self, domain, validation_name, validation):
        self._get_yandex_client().add_txt_record(
            domain, validation_name, validation)

    def _cleanup(self, domain, validation_name, validation):
        self._get_yandex_client().del_txt_record(
            domain, validation_name, validation)

    def _get_yandex_client(self):
        return _yandexLexiconClient(
            self.credentials.conf('auth-token'),
            self.ttl
        )


class _yandexLexiconClient(dns_common_lexicon.LexiconClient):
    """
    Encapsulates all communication with the Yandex via Lexicon.
    """

    def __init__(self, auth_token, ttl):
        super(_yandexLexiconClient, self).__init__()

        config = dns_common_lexicon.build_lexicon_config('yandex', {
            'ttl': ttl,
        }, {
            'auth_token': auth_token,
        })

        self.provider = yandex.Provider(config)

    def _handle_http_error(self, e, domain_name):
        if domain_name in str(e) and (
            # 4.0 and 4.1 compatibility
            str(e).startswith('422 Client Error: Unprocessable Entity for url:') or
            # 4.2
            str(e).startswith('404 Client Error: Not Found for url:')
        ):
            return  # Expected errors when zone name guess is wrong
        return super(_yandexLexiconClient, self)._handle_http_error(e, domain_name)

