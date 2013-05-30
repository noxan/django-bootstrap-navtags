# django-bootstrapnavtags

Navigation templatetags for django with twitter bootstrap.

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-bootstrap-navtags

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/noxan/django-bootstrap-navtags#egg=django-bootstrapnavtags

Add `bootstrapnavtags` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'bootstrapnavtags',
        ...
    )

Enable the `django.core.context_processors.request` by adding it to your settings.

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

Default settings value of django for context processors can be found at: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors

## How to use

First make sure to load the templatetag via `{% load bootstrapnavtags %}` in your template.

Then insert navigation entries into your template as it pleases you:

    <ul class="nav">
        {% navitem 'Home' 'home' %}
        {% navitem 'Profile' 'users:profile' %}
    </ul>
