# FILE NO # 1
# this is a simple code dependant on BING engine to download pictures
# we used this code to download the clustered data( module data ) , also the test data

from bing_image_downloader import downloader # importing function from a library

# the follwoing function takes ( name of object you want to search ,Number of pics you want,
# name of folder to be saved in )

downloader.download("cat png", limit=5,  output_dir='dataset',
                    adult_filter_off=True, force_replace=False, timeout=60)

# the follwoing function takes ( name of object you want to search ,Number of pics you want,
# name of folder to be saved in )

downloader.download("dog png", limit=5,  output_dir='dataset',
                    adult_filter_off=True, force_replace=False, timeout=60)