# Django Simple Account

Simple Django authentication wrapper that extended account details.  The purpose of this app is to allow for a simple drop in that instantly offers login, logout, reset password, etc.

## Install

1. Add "account" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'account',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^account/', include('account.urls')),

3. Run `python manage.py syncdb` to create the APPNAME models.