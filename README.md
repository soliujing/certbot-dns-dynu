certbot-dns-yandex

forked from upstream and modified a bit to support yandex dns API :)

============

Yandex DNS Authenticator plugin for [Certbot](https://certbot.eff.org/).

This plugin is built from the ground up and follows the development style and life-cycle
of other `certbot-dns-*` plugins found in the
[Official Certbot Repository](https://github.com/certbot/certbot).

Installation
------------

```
pip install --upgrade certbot
pip install certbot-dns-yandex
```

Verify:

```
$ certbot plugins --text

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
* dns-yandex
Description: Obtain certificates using a DNS TXT record (if you are using Yandex
for DNS.)
Interfaces: Authenticator, Plugin
Entry point: dns-yandex = certbot_dns_yandex.dns_yandex:Authenticator

...
...
```

Configuration
-------------

The credentials file e.g. `~/yandex-credentials.ini` should look like this:

```
dns_yandex_auth_token = 123456789ABCDEF0000000000000000000000000000000000000
```

Usage
-----



```
certbot ... \
        -a dns-yandex  \
        --dns-yandex-credentials ~/yandex-credentials.ini \
        --dns-yandex-propagation-seconds 1880 \
        certonly
```

don't know why propagation on yandex need such long time, 30 mins is a safe value.


Credits
--------
[PowerDNS](https://github.com/pan-net-security/certbot-dns-powerdns)
[certbot-dns-dynu](https://github.com/bikram990/certbot-dns-dynu)
[dns-lexicon](https://github.com/AnalogJ/lexicon)

Helpful links
--------

[DNS Plugin list](https://certbot.eff.org/docs/using.html?highlight=dns#dns-plugins)

[acme.sh](https://github.com/acmesh-official/acme.sh)






