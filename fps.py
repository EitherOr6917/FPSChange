from moviepy.editor import *
from os import path
import string


# Code from seanh on GitHub
def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename


# Getting the path and making sure it's correct
while True:
    video_input_path = input('Enter input file path: ')
    if path.exists(video_input_path):
        break
    else:
        print('Invalid filepath.')

output_name = format_filename(input('Please enter output filename: '))
video_output_path = path.dirname(video_input_path) + output_name

while True:
    newFPS = input('Enter new video FPS: ')
    if newFPS.isdigit():
        break
    else:
        print('Invalid FPS, make sure you enter a valid integer.')

clip = VideoFileClip(video_input_path)
clip.write_videofile(video_output_path, fps=newFPS)
clip.reader.close()
