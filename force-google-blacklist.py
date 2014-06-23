#!/usr/bin/python

import string
import random
import requests

def generate_random_terms(size=56, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

while True:
        randsearch = generate_random_terms()
        google_search = ('https://www.google.com/search?q=%s' % randsearch)
        r = requests.get(google_search)
        print r.status_code