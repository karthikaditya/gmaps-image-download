import cv2
import imutils 

latitude, longitude = 28.6048761, 77.1982977
map_zoom = 18
image_size = 640 # 640x640
map_scale = 1
map_type = 'satellite'
gmap_api_key = 'INSERT-YOUR-KEY-HERE'

url = "https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&zoom={2}&size={3}x{3}&scale={4}&maptype={5}&key={6}".format(
    latitude, longitude, map_zoom, image_size, map_scale, map_type, gmap_api_key
)

logo = imutils.url_to_image(url)
cv2.imshow("URL to Image", logo)
cv2.imwrite("image.png", logo)
cv2.waitKey(0)