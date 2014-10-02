#! /usr/bin/env python

#open the JSON file from mind42 and output it

import json
import datetime

mm_file=open('dinner.json')

mm=json.load(mm_file)

#print everything
#print(mm)

#print version
#print mm["version"]

#print almost everything
#print mm["root"]

#print id of top
#print mm["id"]

#print id of root
#print mm["root"]["id"]

#print out the top level branches
#for this_one in mm["root"]["children"]:
#    print "#######"
#    print this_one["id"]
#    print this_one["attributes"]["text"]    
##    print this_one
#    print "~~~~~~~"

#recursion!
def print_children(node):
    for this_one in node:
        print "#######"
        print this_one["id"]
        print this_one["attributes"]["text"]
        
        #see if has children
        if len(this_one["children"]) > 0:
            print_children(this_one["children"])

        #    print this_one
        print "~~~~~~~"


#more sophisticated recursion
def print_children2(node,parent):
    #Cycle through each child
    for this_one in node:
        
        #see if has children
        #if it does then recurse, else print out this data
        if len(this_one["children"]) > 0:
            #append the current parent to the parents variable, this will give the full path. 
            parents = parent+' / '+this_one["attributes"]["text"]
            print_children2(this_one["children"],parents)
 

        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "Leaf       = "+this_one["attributes"]["text"]
        print "Parents    = "+parent
        print "ID         = "+this_one["id"]
        print "lastEditor = "+this_one["attributes"]["lastEditor"]
        print "lastEdit   = "+str(this_one["attributes"]["lastEdit"])
        #This is in milliseconds, so divide by 1000
        print "lastEdit   = "+datetime.datetime.fromtimestamp(this_one["attributes"]["lastEdit"]/1000).strftime('%Y-%m-%d %H:%M:%S')
        print "note       = "+this_one["attributes"]["note"]
        #links is a dict object, so needs some extra care.
        #print "links      = "+this_one["attributes"]["links"]
        

#Actually run the thing
print_children2(mm["root"]["children"],"")
