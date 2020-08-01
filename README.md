# gmaps-image

Download images from Google Maps using Python 3 and Maps Static API.

Before using the script, obtain a API key for Google Maps Static API (https://developers.google.com/maps/documentation/maps-static/overview). This key is to be used in the script.
A URL corresponding to the coordinates of location of interest is created. The URL is then used to download the image using imutils and OpenCV packages. 

To download map images in batch mode, use the Coordinates.csv and modify the coordinate values as required.

Refer https://developers.google.com/maps/documentation/maps-static/start to know about the map parameters to use construct the URL.

# Usage
map_image_download.py -c Coordinates.csv -o C:\\Downloads

Where -c is path to the csv file with coordinate values, -o is path to folder where images will be saved

