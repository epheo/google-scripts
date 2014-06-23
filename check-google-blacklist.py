#!/usr/bin/python

import string
import random
import requests

def generate_random_terms(size=56, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

def check_status_code():
        randsearch = generate_random_terms()
        google_search = ('https://www.google.com/search?q=%s' % randsearch)
        r = requests.get(google_search)
        return r.status_code

status_code = check_status_code()

if status_code == 200:
        print "Everithing s alright"
elif status_code == 503:
        print "Youston, we have a problem"
else:
        print "Nothing good here"
        print status_code