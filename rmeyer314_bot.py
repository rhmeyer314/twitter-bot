import tweepy
import time
import datetime

CONSUMER_KEY = 'UcAsfzR52NTlm3vSc35laBaXq'
CONSUMER_SECRET = 'BMsvAwXDQbxwbpe3J6cg7CR8geoBVbpk0Zs0D0x0nfXRirRP4d'
ACCESS_KEY = '1108119737974882316-3C1Ez8PixH9rWeHeOHafN5ebQPvB4T'
ACCESS_SECRET = 'UoePCLFjUauZg9npaQRYGwtUOlV7wfgDQzi9EcHgQbXMK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# retrieve current date and print it, along with how many days left in the year
# and the total percent complete in the yeat
def update():
	currentDT = datetime.datetime.now()
	month = currentDT.month
	day = currentDT.day
	year = currentDT.year
	day_of_year = (currentDT - datetime.datetime(currentDT.year, 1, 1)).days + 1
	totalLeft = 365 - day_of_year
	percent = str(round(day_of_year / 365.0, 2))
	api.update_status('Today is ' + str(month) + '/' + str(day) + '/' + str(year) + '\n'
		'There are ' + str(totalLeft) + ' days left in the year \n'
		'We are ' + str(percent) + '% complete with ' + str(year) + '\n')

# future update
def favorite():
	status_id = api.home_timeline()

	for statusID in status_id:
		if statusID.user.screen_name == 'BBandom':
			api.create_favorite(statusID.id)

while True:
	print('Updating status')
	update()
	#favorite()
	time.sleep(86400)

