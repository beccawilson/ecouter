#Contributers
Dr Becca Wilson & Dr Olly Butters <br /> 
[Data 2 Knowledge Research Group](http:www.bristol.ac.uk/d2k "Data 2 Knowledge website"), University of Bristol

# ECOUTER
These scripts are for use during an [ECOUTER](http://www.bristol.ac.uk/ecouter "ECOUTER website") and include:
  * reshaping the .m42 file (JSON) and flattening it to extract a table of mindmap metadata
  * generalised back up script utilising the Mind42 API.
  
# Things to fix in the reshape script
  * generalise the script - currently it requires hard coding file path and the file you want to flatten
  * html links are in a dictionary, need to reshape as a string 
  * extract some summary stats including no of unique contributors, top five branches that have the most children.
