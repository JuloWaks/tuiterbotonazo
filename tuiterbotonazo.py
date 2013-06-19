#!/usr/bin/env python3

import sys
from twitter import OAuth, Twitter

while len(sys.argv) != 3:
    print("Recuerda que debes escribir python3 tuiterbotonazo.py TuUsuario TuEmail")
    exit()
  #Validation

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
ids = f["ids"]

while f["next_cursor"] != 0:
    f = twitter.followers.ids(screen_name=username, cursor=f['next_cursor'])
    ids.extend(f["ids"])  #If the user have more than 5000 followers
    
print("Hola %s , tenes %s seguidores" % (username, len(ids)))
