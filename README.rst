=======================================================
 django-achievements - Django App for user achievements
=======================================================

:Version: 0.0.1 alpha
:Source: http://github.com/ssaboum/django-achievements/

django-achievements is an application allowing you to handle 
Achievements and link them to users. 
Apart from defining these two objects the projet aims to provide
a framework allowing you to define Achievement classes and callbacks
that will be called by an Engine responsible for checking if a specific 
achievement has been unlocked by a user.
You can access this engine from any part of your application and ask
it to verify if a precise achievement has been unlocked given a context.

Warning, Warning
================

DO NOT USE IN PRODUCTION YET, it is the alpha version
but any feedback would be appreciated and any help welcomed.

Using django-achievements
=========================

To enable ``django-achievements`` for your project you need to add ``achievements`` to
``INSTALLED_APPS``::

    INSTALLED_APPS += ("achievements", )

That's all.
If you want you can also customize the application settings these variables in your  ``settings.py``::

    ACHIEVEMENT_USE_CELERY = True

Documentation
=============

The documentation is generated using Sphinx and available on :
    
    http://readthedocs.org/docs/django-achievements/en/latest/


Installation
=============

This package is now uploaded on PyPi so all you need to do is to install it using :

    pip install django-achievements


License
=======

This software is licensed under the ``New BSD License``. See the ``LICENSE``
file in the top distribution directory for the full license text.

.. # vim: syntax=rst expandtab tabstop=4 shiftwidth=4 shiftround

