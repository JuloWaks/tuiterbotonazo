#!/usr/bin/env python3

import sys
from twitter import OAuth, Twitter
from os import path

if len(sys.argv) != 3:   # Validation
    print("Recuerda que debes escribir python3 tuiterbotonazo.py TuUsuario TuEmail")
    exit()


with open("tokens.cfg") as fh:  # Getting the tokens on the file "tokens.cfg"
    cfg = dict(x.split() for x in fh)


twitter = Twitter(auth=OAuth(
    cfg['access_token'],
    cfg['access_token_secret'],
    cfg['consumer_key'],
    cfg['consumer_secret']))  # Getting the authentication requiered by Twitter

username, email = sys.argv[1].lower(), sys.argv[2].lower()  # Saving username and email


print("Usuario: %s" % username)
print("Email: %s" % email)


f = twitter.followers.ids(screen_name=username)
# Getting user followers ids
new_ids = list(str(idd).strip() for idd in f["ids"])


while f["next_cursor"] != 0:
    # If the user have more than 5000 followers
    f = twitter.followers.ids(
        screen_name=username,
        cursor=f['next_cursor'])
    new_ids.extend(list(str(idd).strip() for idd in f["ids"]))

if path.isfile("%s.flwrs" % username):
    # If the user has already use the script
    with open("%s.flwrs" % username) as slist:
        old_ids = list(idd.strip() for idd in slist)

    set_old_ids = set(old_ids)
    set_new_ids = set(new_ids)
    # Converting lists to sets

    lst_unflws = list(set_old_ids.difference(set_new_ids))
    lst_flws = list(set_new_ids.difference(set_old_ids))
    # Getting the differnce of the sets

    print("Te comenzaron a seguir %s personas, y dejaron de seguirte %s personas"
        % (len(lst_flws), len(lst_unflws)))
    # Printing the counts of follows and unfollows
    d_unflws = dict()  # Initalizing dictionaries, not sure very pythonic
    d_flws = dict()
    for idk in lst_unflws:
        r_unflws = twitter.users.show(user_id=idk)
        d_unflws[idk] = r_unflws["screen_name"]
        # Getting the name of the unfollower
    for idd in lst_unflws:
        print("Te dejo de seguir: @%s" % (d_unflws[idk]))
        # Printing the name of the unfollower
    for idk in lst_flws:
        r_flws = twitter.users.show(user_id=idk)
        d_flws[idk] = r_flws["screen_name"]
        # Getting the name of the NEW follower
    for idd in lst_flws:
        print("Te comenzo de seguir: @%s" % (d_flws[idk]))
        # Printing the name of the NEW follower
with open("%s.flwrs" % username, "w") as slist:

    for idd in new_ids:
        # Saving the list of followers for further comparing
        slist.write("%s\n" % idd)

print("Hola %s , tenes %s seguidores" % (username, len(new_ids)))
