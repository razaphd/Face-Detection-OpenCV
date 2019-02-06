import boto3
from pprint import pprint
import helper_img

client = boto3.client('rekognition')

imgfilename = 'Images/syed-pic4.png'

imgbytes = helper_img.get_image_from_filename(imgfilename)

result = client.detect_faces(Image={'Bytes': imgbytes},
							 Attributes=['ALL'])

pprint(result)

