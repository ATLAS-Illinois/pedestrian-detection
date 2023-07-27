import os
import re
import csv

# image_files = [os.path.join("./data/video/frames/", f) for f in os.listdir("./data/video/frames/")]
# print(image_files[0])
# files = [os.path.join("./video/frames/", f) for f in os.listdir("./video/frames/")]
# print(files)

# def extract_number(f):
#     s = re.findall("(\d+).png", f)
#     # print(int(s[0]))
#     return (int(s[0]) if s else -1, f)

# start_number = int(max(files, key=extract_number)[15:-4]) + 1
# print(start_number)
num_people = 0
last_line_read = 0
def read_csv():
    global last_line_read
    global num_people
    with open('people_time_data.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        total_lines = 0
        # rows = enumerate(csv_reader)
        # last_line_read = len(rows)
        for _ in range(last_line_read):
            next(csv_reader)
        for row in csv_reader:
            total_lines += 1
            if len(row) > 0:
                # Convert the first element to an integer and add it to the sum
                try:
                    num_people += int(row[0])
                except ValueError:
                    print(f"Skipping invalid entry: {row[0]}")
        last_line_read = total_lines
 
# data = pandas.read_csv('people_time_data.csv')
# for row in 
# with open('people_time_data.csv', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter=',')
#     for row in rows:
#         if len(row) > 0 and len(row) < 3:
#             row.insert(0, "counted")
#             csv_writer.writerow(row)

read_csv()
print(num_people) 
print(last_line_read)
# read_csv()
# print(num_people) 
# print(last_line_read)