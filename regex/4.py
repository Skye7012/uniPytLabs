import re
tweet = 'Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'

def clean_tweet(tweet):  
	tweet = re.sub('http\S+\s*', '', tweet) # удалит URL  
	tweet = re.sub('[\b@+]\w+', '', tweet) # удалит URL  
	tweet = re.sub('[\b#+]\w+', '', tweet) # удалит URL  
	tweet = re.sub('RT||cc:', '', tweet) # удалит URL  
	tweet = re.sub('[\s][:]', '', tweet) # удалит URL  
	return tweet

print(clean_tweet(tweet))  
