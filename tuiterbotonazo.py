#!python3.3

import sys
import urllib.request

print("Usuario: " + sys.argv[1])
print("Email: " + sys.argv[2])
f = urllib.request.urlopen("http://api.twitter.com/1/users/show.json?screen_name=eljulo")
f.read()
print(list(r.headers.items()))