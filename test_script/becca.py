#! /usr/bin/env python

#open the JSON file from mind42 and output it

import json
import datetime
import os
os.chdir("/home/rw13742/Documents/ecouter/ecouter/test_script")

mm_file=open('test_scripts.json')

mm=json.load(mm_file)

#prints root_text i.e. mind map title
#root_text = mm["root"]["attributes"]
#print root_text.values()[0]

#more sophisticated recursion
def print_children2(node,parent):
    #Cycle through each child
    for this_one in node:
        root_text = mm["root"]["attributes"]
        #see if has children
        #if it does then recurse, else print out this data
        if len(this_one["children"]) > 0:
            #append the current parent to the parents variable, this will give the full path. 
	    if parent == "":
		parent = root_text.values()[0]
	    else:
            	parents = parent+'/'+this_one["attributes"]["text"]
            	print_children2(this_one["children"],parents)
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	#    print "children = "+this_one["children"]
       # print "Leaf       = "+this_one["attributes"]["text"]
       # print "Parents    = "+parent
       # print "ID         = "+this_one["id"]
       # print "lastEditor = "+this_one["attributes"]["lastEditor"]
       # print "lastEdit   = "+str(this_one["attributes"]["lastEdit"])
        #This is in milliseconds, so divide by 1000
       # print "lastEdit   = "+datetime.datetime.fromtimestamp(this_one["attributes"]["lastEdit"]/1000).strftime('%Y-%m-%d %H:%M:%S')
       # print "note       = "+this_one["attributes"]["note"]
        #links is a dict object, so needs some extra care.
        #print "links      = "+this_one["attributes"]["links"]
        

#Actually run the thing
print_children2(mm["root"]["children"],"")
