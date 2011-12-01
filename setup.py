from distutils.core import setup
setup(
    name = "django-achievements",
    packages = ["achievements", "achievements.migrations", "achievements.templatetags"],
    version = "0.0.7",
    description = "Django application to deal with achievements and rewards unlocked by users",
    author = "Olivier Girardot",
    author_email = "ssaboum@gmail.com",
    url = "https://github.com/ssaboum/django-achievements",
    install_requires = ["importlib>=1.0.2", "django-appconf>=0.4.1"],
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
