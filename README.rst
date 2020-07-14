=====================
Wagtail Notifications
=====================


.. image:: https://img.shields.io/pypi/v/wagtail_notifications.svg
        :target: https://pypi.python.org/pypi/wagtail_notifications

.. image:: https://img.shields.io/travis/fabienheureux/wagtail_notifications.svg
        :target: https://travis-ci.com/fabienheureux/wagtail_notifications

.. image:: https://readthedocs.org/projects/wagtail-notifications/badge/?version=latest
        :target: https://wagtail-notifications.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




GitHub notifications alike app for Wagtail


* Free software: MIT license
* Documentation: https://wagtail-notifications.readthedocs.io.

Getting started
---------------
- ``pip install wagtail-notifications``
- Add to your ``settings.py``:
.. code-block:: python
  :linenos:
    INSTALLED_APPS = [
            ...,
            'notifications',
            'wagtail_notifications',
            ...
    ]




Usage
--------
This Wagtail's package is mainly a proxy of django-notifications_ package. You can use every

.. _django-notifications: https://github.com/django-notifications/django-notifications


Integrations
------------


Why proxy django-notifications ?
--------------------------------
As we can't predict the future, and whethe django-notifications will really remain suitable for Wagtail's notifications, I prefer to make user import from wagtail_notifications directly as this package would maybe someday implement its own notifications center models, signals etc.



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
