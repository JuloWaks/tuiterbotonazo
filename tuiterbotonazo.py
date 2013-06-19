#!/usr/bin/env python3

import sys
from twitter import OAuth, Twitter

with open("tokens.cfg") as fh:
    cfg = dict(x.split() for x in fh)
print(cfg)
twitter = Twitter(auth=OAuth(
    cfg['access_token'], 
    cfg['access_token_secret'],
    cfg['consumer_key'],
    cfg['consumer_secret']))
Usuario = sys.argv[1]
print("Usuario: " + sys.argv[1])
print("Email: " + sys.argv[2])
f = twitter.followers.ids(screen_name=sys.argv[1])
print("Hola %s , tenes %s seguidores" % (Usuario, len(f["ids"])))




