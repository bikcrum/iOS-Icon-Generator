import json
import re
import sys
from generator import generate_splash

device_sizes = json.load(open('splash-screen-sizes.json', 'r'))

if len(sys.argv) < 4:
    print("Insufficient arguments %d. Please provide <foreground_image_path> '<background_color>' <padding>[%%]" % (
        len(sys.argv)))
    exit()

fg_file_path = sys.argv[1]
bg_color = sys.argv[2]

percent_padding = sys.argv[3].endswith('%')
padding = int(sys.argv[3].strip('%'))


def generate_icon(name, size):
    global padding
    file_name = "%s-%dx%d-%s.png" % (
        re.sub('[^0-9a-zA-Z]+', '_', name),
        size['width'],
        size['height'],
        size['type'])

    generate_splash(file_name, size['width'], size['height'], fg_file_path, bg_color, padding, percent_padding)


count = 0


def show_progress(progress, total):
    com_per = int(progress * (100 / total) + 0.5)
    if com_per < 100:
        print("#" * com_per + " " * (100 - com_per) + ":%d%% %d/%d" % (com_per, progress, total), end='\r')
    else:
        print("#" * com_per + " " * (100 - com_per) + ":%d%% %d/%d" % (com_per, progress, total), end='\n\n')


print("\n\nGenerating splash screens")
show_progress(0, len(device_sizes))
for device_size in device_sizes:
    name = device_size['device_name']
    for size in device_size['sizes']:
        generate_icon(name, size)
    count += 1
    show_progress(count, len(device_sizes))
