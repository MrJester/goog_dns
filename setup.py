from distutils.core import setup
from googdns import __author__, __author_email__, __version__


setup(
    name='googdns',
    version=__version__,
    description='Python program to update Google Dynamic DNS. Useful for '
                'cronjob or some other automated mechanism.',
    author=__author__,
    author_email=__author_email__,
    license='gpl-3.0.txt',
    url='https://github.com/MrJester/goog_dns',
    download_url='https://github.com/MrJester/goog_dns/archive/0.0.4.tar.gz',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Networking",
        "Topic :: Utilities"
    ],
    )


