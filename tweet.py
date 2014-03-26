import twitter
import json
import urllib2
from datetime import datetime
import re
from config import *

# Parser for tranforming Peduto schedule-speak into the lyric timbre of BillPedutoBot!
def writeTweet( event ):
	keywords = {
		# Food 
		"(?i)^(Coffee )?Meeting with ": "I'm meeting with %s",
		"(?i) luncheon$": "I'm eating at a %s luncheon",
		"(?i)^breakfast with ": "I'm having breakfast with %s",
		"(?i)^lunch with ": "I'm having lunch with %s",
		"(?i)^dinner with ": "I'm having dinner with %s",
		# Meetings
		"(?i)^standing meeting: ": "I have a regularly-scheduled meeting with %s",
		"(?i)^(Standing )?Weekly meeting ": "I have my weekly meeting %s",
		"(?i)^(conference call:|conference call) ": "I'll be on a conference call with %s",
		"(?i)^Telephone call: ": "I'm on the phone with %s",
		"(?i) meeting$": "I'm going to a %s meeting",
		# Events
		"(?i)^Attending ": "I'm attending %s",
		"(?i) retreat$": "I'm holing up in a %s retreat",
		"(?i) reception$": "I'm receptioning at a %s reception",
		"(?i)^(Speaking at |Speaking: )": "I'm speaking at %s",
		"(?i)^Visit from ": "I'm hosting a vist from %s",
		"(?i)^Serve as": "I'm serving as %s",
		# Press
		"(?i)^(Telephone )?Interview with ": "I have an interview with %s",
		"(?i)^(On air |Call-in |Call in )": "I'll be on air %s",
		"(?i) taping$": "I'm taping \"%s\"",
		"(?i)^Press conference: ": "I'm holding a press conference on %s",
		"(?i)^Press conference with ": "I'm holding a press conference with %s",
		# Travel
		"(?i)^Return home ": "I'm going home to Pittsburgh%s! See see you soon.",
		"(?i)^(Travel|Drive|Driving) to ": "I'm leaving for %s",
		"(?i)^(Travel|Drive|Driving) from ": "I'm traveling from %s",
		# Misc
		"(?i)^Working in office": "%sI'm working in my office until",
	}
	
	message = ""
	# Loop through keyword dictionary and find matching phrases
	for keyword, template in keywords.iteritems():
		search = re.search(keyword, event["title"])
		if search:
			message = template % (re.sub(keyword, "", event["title"]))
			break
		else:
			# If nothing found, use the default message format.
			message = "I'll be at \"" + event["title"] + "\""
	
	# If length is longer than 100 characters, truncate to fit in tweet
	if (len(message) > 100):
		message = message[:100] + "..."
	
	# Add time element
	start = datetime.strptime(event["start"], "%H:%M:%S").strftime("%I:%M%p").lstrip("0")
	end = datetime.strptime(event["end"], "%H:%M:%S").strftime("%I:%M%p").lstrip("0")
	
	# If formatted message has "until" in it, print the end time, not the beginning.
	if re.search("until$", message):
		message += " " + end + "."
	else:
		message += " at " + start + "."

	# Add link to Where's Bill
	message += " (http://newsinteractive.post-gazette.com/wheresbill/?date=" + event["date"] + "&time=" + event["start"].replace(":","") + ")"
	
	return message
	
# Build Twitter-Python object with BillPedutoBot credentials
api = twitter.Api(consumer_key=creds["consumer_key"],
    consumer_secret=creds["consumer_secret"],
    access_token_key=creds["access_token_key"],
    access_token_secret=creds["access_token_secret"])

# Get latest event from simple Where's Bill API
event = urllib2.urlopen('http://newsinteractive.post-gazette.com/wheresbill/api').read()

# Make sure there actually is an event.
if (event != "false"):
	event = json.loads(event)
	
	# Write and print tweet
	status = api.PostUpdate(writeTweet(event))
	print status.text
else:
	print "No new events."
	
