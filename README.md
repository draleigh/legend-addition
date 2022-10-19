# legend-addition
 For producing PDF documents with a map on one page and a legend on the next (back side).

Notes: 
My background is in geospatial data management and cartography. I was recently asked to produce maps 
with the main display on the front side of a sheet of paper but to move the legend to the back side.
This grated against my sense of cartography, and I realized that I couldn't easily produce a 
"second page" for each of the layout tabs within my ArcGIS Pro document. Instead, I produced a "legend" PDF 
in both portrait and landscape forms with the appropriate legend graphic and wrote this script to append
the legend to the "back" of each map according to its orientation (the maps produced prior to running the script
were defined within the script itself).

To anyone reading: I am confident that there is a way to iterate the process to append the correct legend PDFs
to their constituent maps according to the orientation of the input maps. If you have the time and any advice 
on how to improve this script, please let me know! In addition, I'm sure that this script could be tweaked to add a 
postscript or final page (or even initial page) to any PDF document that you may have. 