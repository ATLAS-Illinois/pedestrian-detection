import os
import re

# image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]
# print(image_files[0])
files = [os.path.join("./video/frames/", f) for f in os.listdir("./video/frames/")]
# print(files)

def extract_number(f):
    s = re.findall("(\d+).png", f)
    # print(int(s[0]))
    return (int(s[0]) if s else -1, f)

start_number = int(max(files, key=extract_number)[15:-4]) + 1
print(start_number)