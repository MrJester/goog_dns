from distutils.core import setup
from googdns.googdns import __author__, __author_email__, __version__


setup(
    name='googdns',
    version=str(__version__),
    description='Python program to update Google Dynamic DNS. Useful for '
                'cronjob or some other automated mechanism.',
    author=str(__author__),
    author_email=str(__author_email__),
    license='LICENSE.txt',
    url='https://github.com/MrJester/goog_dns',
    download_url='https://github.com/MrJester/goog_dns/archive/' +
                 str(__version__) + '.tar.gz',
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


