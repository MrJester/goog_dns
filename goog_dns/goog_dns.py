#!/usr/bin/env python

"""
goog-dns

goog-dns is a python program to update Google Dynamic DNS. Useful for
cronjob or some other automated mechanism.

Licence : GPL v3 or any later version


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = 'Ryan Hays'
__author_email__ = 'ryan@blackbagsecurity.net'
__version__ = '0.0.2'
__last_modification__ = '2015.01.26'

import sys
import argparse
import urllib2
import json


class GoogleDNS(object):
    # Class initializer
    def __init__(self):
        self._goog_api_url = 'domains.google.com/nic/update'
        self._url = ''
        self._username = ''
        self._password = ''
        self._useragent = 'Goog_DNS Dynamic DNS Updater v%s' % str(__version__)
        self._ext_ip = ''

    # Establish all the getters/setters
    # Only placing a getter for the API URL because you normally wouldn't
    # change this very often.
    @property
    def google_api_url(self):
        return self._goog_api_url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def ext_ip(self):
        return self._ext_ip

    @ext_ip.setter
    def ext_ip(self, ext_ip):
        self._ext_ip = ext_ip

    @property
    def useragent(self):
        return self._useragent

    # Collect external IP Address
    @staticmethod
    def get_ext_ip():
        # Using myexternalip.com to collect and report IP
        try:
            response = urllib2.urlopen('http://myexternalip.com/json')
            data = json.load(response)
            print '[+] External IP: %s' % data['ip']
            return data['ip']
        except urllib2.URLError:
            print '[!] ERROR Could not get external IP'
            sys.exit(1)

    def set_goog_dns(self):
        # Sets the Google Dynamic DNS with the API
        # Verify that the user has passed the needed parameters
        if self._username == '':
            print '[!] ERROR No username specified'
            sys.exit(1)
        if self._password == '':
            print '[!] ERROR No password specified'
        if self._url == '':
            print '[!] ERROR No sub domain specified'
        if self._ext_ip == '':
            print '[!] ERROR No External IP specified'

        # Build out the API URL
        api_url = 'https://%s?hostname=%s&myip=%s' % (self._goog_api_url,
                                                      self._url,
                                                      self._ext_ip)

        user_agent = self._useragent

        # Build the url opener
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, api_url, self._username, self._password)
        auth_handler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(auth_handler)
        opener.addheaders = [('User-agent', user_agent)]
        urllib2.install_opener(opener)
        response = urllib2.urlopen(api_url)

        answer = response.read().split()
        if answer[0] == 'nochg':
            print '[!] Dynamic IP Unchanged %s' % answer[1]
        if answer[0] == 'good':
            print '[+] Dynamic IP Successfully changed to %s' % answer[1]
        if answer[0] == 'nohost':
            print '[!] ERROR Hostname does not exist, or does not have Dynamic ' \
                  'DNS enabled'
        if answer[0] == 'badauth':
            print '[!] ERROR The username/password combo is not valid'
        if answer[0] == 'notfqdn':
            print '[!] ERROR Supplied hostname is not a valid FQDN'
        if answer[0] == 'badagent':
            print '[!] ERROR Bad UserAgent stop using and contact Developer'
        if answer[0] == 'abuse':
            print '[!] ERROR Dynamic DNS access is blocked contact Google ' \
                  'and/or developer'
        if answer[0] == '911':
            print '[!] ERROR on server side wait 5 minutes for next request'


def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--domain",
                        metavar="SUBDOMAIN",
                        help="Enter the sub domain that you would like updated",
                        type=str,
                        dest="sub_domain",
                        default=None)

    parser.add_argument("-u", "--username",
                        metavar="USERNAME",
                        help="Enter the username that Google Domains gave you.",
                        type=str,
                        dest="username",
                        default=None)

    parser.add_argument("-p", "--password",
                        metavar="PASSWORD",
                        help="Enter the username that Google Domains gave you.",
                        type=str,
                        dest="password",
                        default=None)

    values = parser.parse_args()

    if not values.sub_domain or not values.username or not values.password:
        parser.error("[!] ERROR You need to specify all parameters.")
    else:
        return values.sub_domain, values.username, values.password


# Main area of the program
if __name__ == "__main__":
    googdns = GoogleDNS()
    googdns.url, googdns.username, googdns.password = build_parser()

    googdns.ext_ip = GoogleDNS.get_ext_ip()

    googdns.set_goog_dns()