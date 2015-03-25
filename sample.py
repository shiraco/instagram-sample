from __future__ import print_function

import sys
from instagram.client import InstagramAPI
from settings import instgram_access_token


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if len(argvs) != 2:
        print('Usage: # python %s INSTAGRAM_USER_ID' % argvs[0])
        quit()

    instgram_user_id = argvs[1]

    api = InstagramAPI(access_token=instgram_access_token)
    recent_media, next_ = api.user_recent_media(user_id=instgram_user_id, count=10)

    for media in recent_media:
        print(media.caption.text)
