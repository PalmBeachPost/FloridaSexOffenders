#!/python27/python
import requests

# For multiple values for the same key, requests wants key-value tuples.

payload = [
    ("county", "Palm Beach"),
    ("county", "Saint Lucie"),
    ("county", "Martin"),
    ("county", "Broward"),
    ("email", "mstucka@pbpost.com"),
    ("l_blnValid", "true"),
    ("mode", "manual"),
    ("submit1", "Download")
    ]

urlin = "http://offender.fdle.state.fl.us/offender/publicDataFile.do"
myget = requests.get(urlin)
cookies = myget.cookies

# Now we know what the site is looking for. Let's respond appropriately.
urlout = urlin + ";jsessionid=" + cookies['JSESSIONID']
myput = requests.post(urlout, data=payload, cookies=cookies)
with open('sexoffenders.csv', 'wb') as handle:
    handle.write(myput.content)
