# For gmail notification with Furby

# doesn't work with indeed mail, maybe because it requires 2-stage authentication...
# does work with raw gmail addresses

import sys, feedparser, urllib, os, time, getpass, platform

OS=platform.system()
APLAYER=''
if OS == 'Darwin':
    APLAYER = 'afplay'
elif OS == 'Linux':
    APLAYER = 'aplay'

print OS
print APLAYER

SRCDIR=os.path.dirname(os.path.realpath(__file__))
WAVDIR=SRCDIR+'/../wav/'

shortSleep=5 # for re-hypnotize Furby (sec)

longSleep=10 
# this needs to be less than 60 to keep Furby obedient to the program
# check gmail inbox every 'longSleep' (sec)

PROTO="https://"
SERVER="mail.google.com"
PATH="/mail/feed/atom"
USERNAME=raw_input("Enter username: ")
PASSWORD=getpass.getpass("Enter password: ")

# get ATOM feed from gmail for checking authentication error
feed=feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
if feed['feed'].has_key('summary') and feed['feed']['summary'].find('Error') >= 0:
    print 'Authenticaion failed'
    exit()
else:
    print 'Authentication succeed'

while True:
    newmails = int(feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)["feed"]["fullcount"])
    if newmails > 0:
        print 'talking to your Furby'
        os.system(APLAYER+' '+WAVDIR+'friend.wav')
    # in case Furby speaks, we need to hypnotize after he finishes speaking otherwise hypnotize command will be ignored
    time.sleep(shortSleep)

    # hypnotize here at every loop
    print 'hypnotizing Furby'

    os.system(APLAYER+' '+WAVDIR+'hypnotize.wav')
    print 'start long sleep'
    time.sleep(longSleep)
    print 'end long sleep!'
