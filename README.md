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
pip intall git+https://github.com/soliujing/certbot-dns-yandex
```

Verify:

```
$ certbot plugins --text

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
* dns-dynu
Description: Obtain certificates using a DNS TXT record (if you are using Dynu
for DNS.)
Interfaces: Authenticator, Plugin
Entry point: dns-dynu = certbot_dns_dynu.dns_dynu:Authenticator

...
...
```

Configuration
-------------

The credentials file e.g. `~/dynu-credentials.ini` should look like this:

```
dns_dynu_auth_token = AbCbASsd!@34
```

Usage
-----


```
certbot ... \
        -a dns-dynu  \
        --dns-dynu-credentials ~/dynu-credentials.ini \
        --dns-dynu-propagation-seconds 1880
        certonly
```

License
--------

Copyright (c) 2021 [Bikramjeet Singh](https://github.com/bikram990)

Credits
--------
[PowerDNS](https://github.com/pan-net-security/certbot-dns-powerdns)

[dns-lexicon](https://github.com/AnalogJ/lexicon)

Helpful links
--------

[DNS Plugin list](https://certbot.eff.org/docs/using.html?highlight=dns#dns-plugins)

[acme.sh](https://github.com/acmesh-official/acme.sh)

[dynu with acme.sh](https://gist.github.com/tavinus/15ea64c50ac5fb7cea918e7786c94a95)

[dynu api](https://www.dynu.com/Support/API)






