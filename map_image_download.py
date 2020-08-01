import cv2
import imutils 
import pandas as pd
import os

# Set the map parameters to use in the URL
# https://developers.google.com/maps/documentation/maps-static/start
latitude, longitude = 28.6048761, 77.1982977
map_zoom = 18
image_size = 640 # 640x640
map_scale = 1
map_type = 'satellite'
gmap_api_key = 'INSERT-YOUR-KEY-HERE'

# Create/download image from URL and save it
def save_map_image(url, file_save_path):
    # Get the map image from the URL 
    # Using the url_to_image function from https://github.com/jrosebr1/imutils
    map_image = imutils.url_to_image(url)

    # Write the map image
    cv2.imwrite(file_save_path, map_image)

    # Display the image
    # cv2.imshow("URL to Image", map_image)
    # cv2.waitKey(0)

def batch_save_map_images(csv_path, output_folder):
    coordinates_df = pd.read_csv(csv_path)
    for i,coord_row in coordinates_df.iterrows():
        file_name = coord_row['ID']
        lat_coord = coord_row['Latitude']
        long_coord = coord_row['Longitude']

        url = "https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&zoom={2}&size={3}x{3}&scale={4}&maptype={5}&key={6}".format(
            lat_coord, long_coord, map_zoom, image_size, map_scale, map_type, gmap_api_key
        )
        
        image_full_path = os.path.join(output_folder,"{}.png".format(file_name))
        save_map_image(url, image_full_path)
        
        print('{} created'.format(image_full_path))
    
if __name__ == '__main__':
    # Single map image download ---------------------------------
    # url = "https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&zoom={2}&size={3}x{3}&scale={4}&maptype={5}&key={6}".format(
    #     latitude, longitude, map_zoom, image_size, map_scale, map_type, gmap_api_key
    # )
    
    # save_map_image(url, "map_image.png")
    # -----------------------------------------------------------

    # Batch map images download
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--csv_path", required=True, help="path to the coordinates csv file")
    ap.add_argument("-o", "--output_folder", required=True, help="path to output folder to save map images")

    args = vars(ap.parse_args())
    batch_save_map_images(args["csv_path"], args["output_folder"])
