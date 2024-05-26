from pillow_heif import register_heif_opener, read_heif
from PIL import Image
import os

register_heif_opener()

# Get list of HEIF and HEIC files in directory
directory = 'C:\\Users\\muj\\Pictures\\jummah'
files = [f for f in os.listdir(directory) if f.endswith('.HEIC') or f.endswith('.heif')]

# Create output directory if it does not exist
if not os.path.exists(os.path.join(directory, 'output')):
    os.makedirs(os.path.join(directory, 'output'))

# Convert each file to JPEG
count = 0
for filename in files:
    try:

        heif_file = read_heif(os.path.join(directory, filename))
        image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data)
        image.save(os.path.join(directory, 'output', os.path.splitext(filename)[0] + '.jpg'))
        count += 1
        print(count)
    except Exception as e:
        print(e)

