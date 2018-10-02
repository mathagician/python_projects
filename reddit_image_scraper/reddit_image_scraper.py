import praw
import requests
import getpass
import datetime
import sys

# you need to get your client key and client secret after registering for the reddit API
client_key = ''
client_secret = ''
# reddit credentials. getpass() allows password entry on the command line in unix-style: no visibility
username = ''
password = getpass.getpass()
useragent = ''
op_dir = ''

# initialising the API connection
reddit = praw.Reddit(client_id = client_key,
					 client_secret = client_secret, 
					 username = username,
					 password = password,
					 user_agent = useragent)



# default to 1 post search per sub
num_posts = 1
if len(sys.argv) < 2:
	print('# posts not entered. Defaulting to 1 post per sub')

else:
	try:
		num_posts = int(sys.argv[1])
		if num_posts < 0:
			print('-ve entered. Defaulting to 1 post per sub')
			num_posts = 1
	except ValueError:
		print('Enter integer. Defaulting to 1 post per sub.')


# list of subreddits to scrape
subs = ['me_irl', 'ProgrammerHumor']


try:
	for sub in subs:
		ctr = 0
		print('\nDOWNLOADING FROM r/', sub)
		posts = reddit.subreddit(sub).new(limit=num_posts)
		for post in posts:
			# these are posts that stay at the top of the subreddit, eg. rules of the sub, etc.
			if post.stickied:
				continue
			# if the post contains an image - jpg, it will be present at the end of the url
			if post.url.split('.')[-1] == 'jpg':
				ctr += 1
				print(ctr, ' ', post.url)
				r = requests.get(post.url)
				# if we get a succesful response after sending a get request to this URL,
				if r.status_code == 200:
					# come up with a random name to store the image on disk
					randstr = datetime.datetime.now().strftime('%Y%m%d%H%M%s')
					# and store it in the configured output directory.
					with open(op_dir + randstr + post.url.split('/')[-1], 'wb') as f:
						f.write(r.content)
except Exception as e:
	print('Invalid creds - ', e)


print('Done')


sys.exit(0)
