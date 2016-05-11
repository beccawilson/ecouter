#!/usr/bin/env python2
## Mind42 API
##
## API seems to want manual user confirmation of
## a third party application getting access.
## This is supposed to be done through a browser.
## It works in same way a website or app might allow a user to use their
## facebook or google account to post a comment for example. This would first
## prompt for fb/google account login, then prompt the user to confirm
## that the third party app can use their account for this purpose

## API wants a user to manually sign in through a browser to
## confirm authorization for the application go gain acocunt access.
## So, first step is to emulate this, get a cookie, and confirm access

#todo
#v1
#log stuff, maybe with a debug flag
#get thumbnail image
#save files the revisionId, then only need to save if it has changed.

#v2
#do an auto diff and highlight what has changed. Can we do this with the native
#API calls?
#Let the admin know when changes happen (email?)

__author__ = "Tom Clark, Olly Butters"
__date__ = 11/5/2016
__version__ = 0.3

import ConfigParser
import httplib
import json
import re
import time


#################################################
#Nothing to edit below here
#################################################
config = ConfigParser.ConfigParser()
config.read("config.ini")
print config.sections()
try:
    uname                  = config.get('mind42_settings','uname')
    pword                  = config.get('mind42_settings','pword')
    client_id              = config.get('mind42_settings','client_id')
    client_secret          = config.get('mind42_settings','client_secret')
    redirect_uri           = config.get('mind42_settings','redirect_uri')
    requested_mindmap_name = config.get('local_settings','requested_mindmap_name')
    file_path_root_dir     = config.get('local_settings','file_path_root_dir')
except:
    print 'Problem with the settings file'
    exit(0)

##########################################################################
#wrap this up as an auth module?

#################################################
#OAuth variables, shouldnt need to change these.
response_type = 'code'
scope = 'read'
state = ''

#################################################
#Sign in and get a cookie
postdata = 'username='+uname+'&password='+pword
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib.HTTPSConnection("mind42.com")
conn.request("POST","/api/signin", postdata, headers)
res = conn.getresponse()
print res.status, res.reason
responseheaders = res.msg
body = res.read()
cookie= responseheaders.get('set-cookie')
#print dict(message)
print cookie
print "end"
print '-'*40

#################################################
#Get the oauth page using the cookie from above
getdata = 'response_type='+response_type+'&client_id='+client_id+'&redirect_uri='+redirect_uri+'&scope='+scope+'&state='+state

print getdata

headers = {"Cookie": cookie}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("GET","/api/oauth2/auth?"+getdata, '', headers)
res = conn.getresponse()
print res.status, res.reason, res.msg
body = res.read()
#print body
print '-'*40

#################################################
## press the 'Agree' button to allow app access
## nedds to POST a transaction_id which is in the web source code
## so find this value
idsearch =  re.search('transaction_id.+?value=\"(.+?)\"', body)
transaction_id = idsearch.group(1)
print 'transaction id from html = '+transaction_id


postdata = 'transaction_id='+transaction_id
#headers = {"Cookie": cookie}
headers = {"Content-type": "application/x-www-form-urlencoded","Cookie": cookie}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("POST","/api/oauth2/auth", postdata , headers)
res = conn.getresponse()
print res.status, res.reason, res.msg
body=res.read()

## response contain the auth code
authcodesearch = re.search('title.+?code=(.+?)\<',body)
authcode = authcodesearch.group(1)

print 'authcode '+authcode

#################################################
## next step is to get token from   /api/oauth2/token
## need the following params
## code
## client_id,
## client_secret
## redirect_uri
## grant_type

grant_type='authorization_code'


postdata = 'code='+authcode+'&client_id='+client_id+'&client_secret='+client_secret+'&redirect_uri='+redirect_uri+'&grant_type='+grant_type
print postdata
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("POST","/api/oauth2/token", postdata , headers)
res = conn.getresponse()
print res.status, res.reason, res.msg
body=res.read()
#print body

jsonresp = json.loads(body)
print
print jsonresp ['access_token']
print jsonresp ['refresh_token']
print jsonresp ['expires_in']
print jsonresp ['token_type']

print'-'*40
#end auth module
#######################################################################################


#################################################
## now have everything needed for auth
## get mindmap list from /api/oauth2/v1/mindmapList
headers = {"Authorization": 'Bearer '+jsonresp['access_token']}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("GET","/api/oauth2/v1/mindmapList", '', headers)
res = conn.getresponse()
print res.status, res.reason, res.msg
body = res.read()
print type(body)
print '-'*40
print body
print'-'*40
mindmapList = json.loads(body)
number_of_mindmaps = len(mindmapList['data'])
for i in range(0, len(mindmapList['data'])):
    print mindmapList['data'][i]['name']
    match_obj = re.match(requested_mindmap_name, mindmapList['data'][i]['name'])
    if match_obj:
        print 'matches!'
        mindmapId = mindmapList['data'][i]['mindmapId']
        break

#################################################
## get particular mindmap from /api/oauth2/v1/mindmapGet
headers = {"Authorization": 'Bearer '+jsonresp['access_token']}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("GET","/api/oauth2/v1/mindmapGet?mindmapId="+mindmapId+"&online=false", '', headers)
res = conn.getresponse()
##print res.status, res.reason, res.msg
body = res.read()
#print body


#revid = body['data']['revisionId']

#################################################
#Save it somewhere
time_string = time.strftime("%Y-%m-%d_%H%M%S",time.localtime())
full_file_path = file_path_root_dir+'/'+time_string
f = open(full_file_path, 'w')
f.write(body)

#################################################
#Grab the png image of the mindmap. The largest of these is still really small
#not convinced this is very useful.
headers = {"Authorization": 'Bearer '+jsonresp['access_token']}
conn = httplib.HTTPSConnection('mind42.com')
conn.request("GET","/api/oauth2/v1/mindmapThumbnail?mindmapId=03ea308a-6e65-4d62-9f3e-f2f1232c6b02&size=gallery", '', headers)
res = conn.getresponse()
print res.status, res.reason, res.msg
body = res.read()
#print body

png_file_path = file_path_root_dir+'/'+time_string+'.png'
fp = open(png_file_path, 'w')
fp.write(body)
