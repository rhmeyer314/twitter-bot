import tweepy
import time
import datetime

CONSUMER_KEY = 'top secret'
CONSUMER_SECRET = 'top secret'
ACCESS_KEY = 'top secret'
ACCESS_SECRET = 'top secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

i = 0
dayNum = 100 # number set to 100 because this program started running on the 101st day of the year

# retrieve current date and print it, along with how many days left in the year
# and the total percent complete in the yeat
def update(dayNum):
	currentDT = datetime.datetime.now()
	month = currentDT.month
	day = currentDT.day
	year = currentDT.year
	totalLeft = 365 - dayNum
	percent = str(round(dayNum / 365.0, 2))
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
	if dayNum == 366: # indicates a new year has started so reset the current day to 0
		dayNum = 0

	dayNum +=1
	print('Updating status')
	update(dayNum)
	#favorite()
	time.sleep(86400)

