#!/usr/bin/env python3

import sys
from twitter import OAuth, Twitter

with open("tokens.cfg") as fh:
    cfg = dict(x.split() for x in fh)
  # Getting the tokens on the file "tokens.cfg"

twitter = Twitter(auth=OAuth(
    cfg['access_token'], 
    cfg['access_token_secret'],
    cfg['consumer_key'],
    cfg['consumer_secret']))  # Getting the authentication requiered by Twitter

username = sys.argv[1]  # Saving username

print("Usuario: " + sys.argv[1])
print("Email: " + sys.argv[2])

f = twitter.followers.ids(screen_name=username)  # Getting user followers ids

print("Hola %s , tenes %s seguidores" % (username, len(f["ids"])))
