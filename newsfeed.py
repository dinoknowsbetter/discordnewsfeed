import newsapi
import time
from discord import Webhook, RequestsWebhookAdapter


webhook = Webhook.partial(WEBHOOD_ID, 'WEBHOOK_TOKEN', adapter=RequestsWebhookAdapter())

while True:
    print('Pushing a notification to discord for latest news: ')
    for i in range(1,11):
        api = newsapi.NewsApiClient(api_key="NEWSAPI_KEY") #get at newsapi.org
        query = api.get_top_headlines(category='technology', language='en', country= 'us')
        name = query["articles"][i]["source"]["name"]
        title = query["articles"][i]["title"]
        description = query["articles"][i]["description"]
        url = query["articles"][i]["url"]
        thumbnail = query["articles"][i]["urlToImage"]
        webhook.send('**' + name + '** - ' + title + ' ' + description + ' ' + url, username='DKB Newsfeed')
       
    print('Sleeping for 6 hours')
    time.sleep(21600)
