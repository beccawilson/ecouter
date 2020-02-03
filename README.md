[![DOI](https://zenodo.org/badge/22005/beccawilson/ecouter.svg)](https://zenodo.org/badge/latestdoi/22005/beccawilson/ecouter)

# ECOUTER Project Publications
* Murtagh, M.J et al., The ECOUTER methodology for stakeholder engagement in translational research. BMC Med Ethics 18, 24 (2017). [DOI: 10.1186/s12910-017-0167-z](https://doi.org/10.1186/s12910-017-0167-z)
* Wilson RC et al., Digital Methodology to implement the ECOUTER engagement process (version 2; peer review: 2 approved). F1000Research 2017, 5:1307 [DOI: 10.12688/f1000research.8786.2](https://doi.org/10.12688/f1000research.8786.2)


# Software Contributers
* Dr Becca Wilson, [Data 2 Knowledge Research Group](http:www.bristol.ac.uk/d2k "Data 2 Knowledge website"), University of Bristol
* Dr Olly Butters, [ALSPAC](http://www.bristol.ac.uk/alspac), University of Bristol
* Tom Clark, [MRC IEU](http://www.bristol.ac.uk/integrative-epidemiology/), University of Bristol

# ECOUTER
These scripts are for use during an [ECOUTER](http://www.bristol.ac.uk/ecouter "ECOUTER website") and include:
  * reshaping the .m42 file (JSON) and flattening it to extract a table of mindmap metadata
  * generalised back up script utilising the Mind42 API.
  
# Things to fix in the reshape script
  * generalise the script - currently it requires hard coding file path and the file you want to flatten
  * html links are in a dictionary, need to reshape as a string 
  * extract some summary stats including no of unique contributors, top five branches that have the most children.
