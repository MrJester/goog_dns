from distutils.core import setup

from goog_dns import *


setup(
    name='goog_dns',
    version=googdns.__version__,
    description='Python program to update Google Dynamic DNS. Useful for '
                'cronjob or some other automated mechanism.',
    author=goog_dns.__author__,
    author_email=goog_dns.__author_email__,
    license='gpl-3.0.txt',
    url='https://github.com/MrJester/',
    download_url='https://github.com/MrJester/python-dumbpig/tarball/0.0.1',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.7.9",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Networking",
        "Topic :: System :: System Administration",
        "Topic :: Utilities"
    ],
    )


