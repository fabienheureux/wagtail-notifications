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
As we can't predict the future, and whether django-notifications will really remain suitable for Wagtail's notifications, I prefer to make user import from wagtail_notifications directly as this package would maybe someday implement its own notifications center models, signals etc.

Local development
-----------------

In the python environment of your choice, navigate to /examples
- Run pip install -r requirements.txt
- Run ./manage.py migrate
- Run server ./manage.py runserver



License
-------
Distributed under the MIT License. See LICENSE for more information.

Contact / Maintaners
--------------------
Fabien Le Frapper
- @fabienheureux_
- email_
.. _fabienheureux: https://github.com/fabienheureux
.. _email: mailto:contact@fabienlefrapper.me
