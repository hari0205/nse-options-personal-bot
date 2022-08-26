from email import header
from http import cookies
from urllib import response
from webbrowser import get
import requests 
import pandas 
"""
First let's grab Nifty's data from nse website 
"""

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"


headers = {
   "user-agent" :  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
   "accept-encoding":"gzip, deflate, br",
   "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
}


session = requests.Session()
request = session.get(url, headers=headers)
cookies = dict(request.cookies)
response = session.get(url,headers=headers, cookies=cookies).json()



rawdata= pandas.DataFrame(response)
#print(rawdata)


# =============================================================================
# Now let's try grabbing details like strike price , LTP and expiry dates data
# Expiry date = records->expiryDates[0]
# =============================================================================

# Fetch current weekly expiry date
def getExpiry(rd):
    return(rd['records']['expiryDates'][0]) 


curexp = getExpiry(rawdata)

print(curexp)

