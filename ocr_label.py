import io
import os
import re

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.abspath('/home/plato/Downloads/receipt2.jpeg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

# Performs text detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations
para = (texts[0].description)
para = re.sub('\n+',' ',para)
print((para))

# print('Texts:')
# print(' "{}" '.format(texts[0].description))
# for text in texts:

#     print(' "{}" '.format(text.description))

#     # vertices = (['({},{})'.format(vertex.x, vertex.y)
#     #             for vertex in text.bounding_poly.vertices])

#     # print('bounds: {}'.format(','.join(vertices)))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))