from PIL import Image
import os


def generate_splash(target_file_name, target_x, target_y, fg_img_path, bg_color="#000000", padding=0, percent_padding = False):
    dir_name = 'splash'
    imgFg = Image.open(fg_img_path)

    img_width = imgFg.width
    img_height = imgFg.height

    if target_x / target_y > img_width / img_height:
        if percent_padding:
            padding = target_y * padding / 100
        multiplier = (target_y - 2 * padding) / img_height
        offset_x = (target_x - img_width * multiplier) / 2
        offset_y = padding
    else:
        if percent_padding:
            padding = target_x * padding / 100
        multiplier = (target_x - 2 * padding) / img_width
        offset_x = padding
        offset_y = (target_y - img_height * multiplier) / 2

    imgBg = Image.new('RGB', (target_x, target_y), bg_color)

    imgFg = imgFg.resize((int(img_width * multiplier), int(img_height * multiplier)), Image.ANTIALIAS)
    imgBg.paste(imgFg, (int(offset_x), int(offset_y)), imgFg)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    imgBg.save('%s/%s' % (dir_name,target_file_name), "png")
