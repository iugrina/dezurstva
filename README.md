# Jednostavna aplikacija za praćenje dežurstava

Aplikacija je pisana u jeziku Python te koristi Django framework.
Više o potrebnim bibliotekama može se naći u dokumentu
`./requirements.txt`.

Aplikacija koristi LDAP za autentifikaciju.

Za čuvanje podataka koristi se SQLITE baza.

Aplikacija se može pokrenuti (na `localhost` računalu, portu 3033) sa 
```bash
python manage.py runfcgi method=threaded host=127.0.0.1 port=3033
```

Ovako pokrenuta aplikacija koristi FastCGI pa se recimo Apache2 server može
podesiti tako što u direktorij `/etc/apache2/conf.d/` dodamo datoteku
`fcgidez` sa sadržajem
```bash
$ cat fcgidez
FastCGIExternalServer /tmp/dez.fcgi -host 127.0.0.1:3033
```

te prilagodimo apache2 conf tako što dodamo:
```
Alias /static /PATH_TO/lib/python2.7/site-packages/django/contrib/admin/static
RewriteEngine On
RewriteRule ^/(static.*)$ /$1 [QSA,L,PT]
RewriteCond %{REQUEST_FILENAME} !-f
RewriteRule ^/(.*)$ /tmp/dez.fcgi/$1 [QSA,L]
```

Za uredno izvršavanje aplikacije potrebno je prilagoditi i
`./dezurstva/settings.py.sample` te `./dezurstva/urls.py.sample`.
