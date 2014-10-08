#! /usr/bin/env python

#open the JSON file from mind42 and output it

import json
import datetime
import os
import csv

os.chdir("/home/rw13742/Documents/ecouter/p3G_ecouter/data_extractor/")

mm_file=open('1412609393.json')

mm=json.load(mm_file)

#prints root_text i.e. mind map title
#root_text = mm["root"]["attributes"]
#print root_text.values()[0]

#more sophisticated recursion
def print_children2(node,parent):
    #Cycle through each child
    for this_one in node:
       	#see if has children
        #if it does then recurse, else print out this data
        if len(this_one["children"]) > 0:
            #append the current parent to the parents variable, this will give the full path. 
	    parents = parent+'/'+this_one["attributes"]["text"]
	    print_children2(this_one["children"],parents)
	ID = this_one["id"]
	parent = parent
	text = this_one["attributes"]["text"]
	note = this_one["attributes"]["note"]
	links = this_one["attributes"]["links"]
	image = this_one["attributes"]["image"]
	last_editor = this_one["attributes"]["lastEditor"]
	last_edit = datetime.datetime.fromtimestamp(this_one["attributes"]["lastEdit"]/1000).strftime('%Y-%m-%d %H:%M:%S')
	# # print "lastEdit   = "+str(this_one["attributes"]["lastEdit"])
        #This is in milliseconds, so divide by 1000
	
	with open("ouput.csv", "ab") as csvfile:
    	    output_file = csv.writer(csvfile)
	    output_file.writerow([ID, parent, text.encode('utf-8'), note, links, image, last_editor, last_edit]) #add to this list of columns
	
with open("ouput.csv", "ab") as csvfile:
    output_file = csv.writer(csvfile)
    output_file.writerow(["ID", "parent", "text", "note", "links", "image", "last_editor", "last_edit"]) 
  
root_text = mm["root"]["attributes"]
parent = root_text.values()[0]
print_children2(mm["root"]["children"],parent)

        


##################################################
# things to fix
#################################################
# html links are in a dictionary, need to extract
# string manipulation in text column to remove <br>
#summary stats including no of unique contributors
#top five branches that have the most children.
