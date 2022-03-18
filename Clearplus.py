import requests
import requests.exceptions
import re
from pandas import DataFrame
import pandas as pd 

filename = {{variable}}
df = pd.read_excel(filename)
stuff = []
stuff = list(df['Forum'])
stuff = list(dict.fromkeys(stuff)) 
new_urls= [http]

emails = []

for url in new_urls:

	# get url's content
	#print("Processing %s" % url)
	try:
		response = requests.get(url, timeout=20)
	except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidSchema, requests.exceptions.ReadTimeout
	):
		# ignore pages with errors
		continue

	# extract all email addresses and add them into the resulting set
	new_emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b.", response.text, re.I)
	emails.append(new_emails)
 
email_df = pd.DataFrame(emails)
combine = email_df[0].append(email_df[1]).reset_index(drop=True)
#combine2 = email_df.stack().reset_index()

combine.to_excel('{Excel File}')



