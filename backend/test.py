import os
import re

image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]
print(image_files[0])
