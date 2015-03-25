import sys
from settings import instgram_access_token

import requests
import requests_cache
import json

# API呼び出しの結果をsqliteにキャッシュする
requests_cache.install_cache('cache_instagram', allowable_methods=('GET', 'POST'))

URL_ROOT = "https://api.instagram.com/v1/"


class InstagramAPI():

    def __init__(self, access_token):
        self.access_token = access_token

    def user_recent_media(self, user_id):
        url = URL_ROOT + "users/{0}/media/recent/?access_token={1}".format(instgram_user_id, self.access_token)

        # headers = {'Accept': 'application/json', 'content-type': 'application/json'}

        r = requests.get(url)

        return r.json()


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if len(argvs) != 2:
        print('Usage: # python %s INSTAGRAM_USER_ID' % argvs[0])
        quit()

    instgram_user_id = argvs[1]

    api = InstagramAPI(access_token=instgram_access_token)
    response_json = api.user_recent_media(user_id=instgram_user_id)

    print(response_json)
