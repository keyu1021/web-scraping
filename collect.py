import requests
import os,sys
import os.path as osp
import json


# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('0eSLcjG7idZ7rhk1AwzZVg', '8CWpEIbQ5ixKyB0emwCZ0GTMzu5KsA')

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'SuccessfulSoft7018',
        'password': 'Karina1004!'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)
urls1 = []
url_funny = "https://oauth.reddit.com/r/funny/new/?limit=100"
url_AskReddit = "https://oauth.reddit.com/r/AskReddit/new/?limit=100"
url_gaming = "https://oauth.reddit.com/r/gaming/new/?limit=100"
url_aww = "https://oauth.reddit.com/r/aww/new/?limit=100"
url_pics = "https://oauth.reddit.com/r/pics/new/?limit=100"
url_Music = "https://oauth.reddit.com/r/Music/new/?limit=100"
url_science = "https://oauth.reddit.com/r/science/new/?limit=100"
url_worldnews = "https://oauth.reddit.com/r/worldnews/new/?limit=100"
url_videos = "https://oauth.reddit.com/r/videos/new/?limit=100"
url_todayilearned = "https://oauth.reddit.com/r/todayilearned/new/?limit=100"

urls1.append(url_funny)
urls1.append(url_AskReddit)
urls1.append(url_gaming)
urls1.append(url_aww)
urls1.append(url_pics)
urls1.append(url_Music)
urls1.append(url_science)
urls1.append(url_worldnews)
urls1.append(url_videos)
urls1.append(url_todayilearned)

with open('sample1.json', 'w') as f1:
    for url in urls1:
        content = requests.get(url,  headers=headers).json()
        for i in range(0,100):
            f1.write(json.dumps(content['data']['children'][i]))
            f1.write('\n')
    f1.close()

urls2 = []
urls2.append("https://oauth.reddit.com/r/AskReddit/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/memes/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/politics/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/nfl/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/nba/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/wallstreetbets/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/teenagers/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/PublicFreakout/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/leagueoflegends/new/?limit=100")
urls2.append("https://oauth.reddit.com/r/unpopularopinion/new/?limit=100")

with open('sample2.json', 'w') as f2:
    for url in urls2:
        content = requests.get(url,  headers=headers).json()
        for j in range(0,100):
            f2.write(json.dumps(content['data']['children'][j]))
            f2.write('\n')
    f2.close()
