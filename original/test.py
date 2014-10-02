#! /usr/bin/env python

#open the JSON file from mind42 and output it

import json
import datetime

mm_file=open('dinner.json')

mm=json.load(mm_file)

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
        print "Leaf, Parents, ID, lastEditor" 
        print this_one["attributes"]["text"]","parent,this_one["id"],this_one["attributes"]["lastEditor"]


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
