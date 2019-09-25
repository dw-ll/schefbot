import json
from json import dumps
import datetime
from yahoo_oauth import OAuth2
import pandas as pand


class API():
    def __init__(self, consumer_key, consumer_secret, access_key):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self.access_key = access_key
        self.authorization = None

    def _login(self):
        global oauth
        oauth = OAuth2(None, None, from_file=('./auth/oauth.json'))
        if not oauth.token_is_valid():
            oauth.refresh_access_token()
class Refetch():
    def FetchTransactions(self):
        load_file=open('./transactions/old_trans.json')
        old_news = json.load(load_file)
        load_file.close()

        load_file=open('./transactions/new_trans.json')
        new_news=json.load(load_file)
        load_file.close()

        with open('./transactions/old_trans.json', 'w') as outfile:
            json.dump(new_news,outfile)

        load_file=open('./transactions/old_trans.json')
        old_news=json.load(load_file)
        load_file.close()

        API._login()
        url = "https://football.fantasysports.yahoo.com/f1/192970/transactions"
        response=oauth.session.get(url,params={'format':'json'})
        resp = response.json()
        with open('./transactions/new_trans.json','w') as outfile:
            json.dump(resp,outfile)
        load_file = open('./transactions/new_trans.json')
        new_news=json.load(load_file)
        load_file.close()

        old_trans = old_news['fantasy_content']['league'][1]['transactions']['count']        old_trans = old_news['fantasy_content']['league'][1]['transactions']['count']
        new_trans = new_news['fantasy_content']['league'][1]['transactions']['count']
        most_recent_news = (new_trans-old_trans)

        transactions = new_news['fantasy_content']['league'][1]['transactions']['count']

       