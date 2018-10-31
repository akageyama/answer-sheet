#!/usr/local/bin/python
# -*- coding: utf-8 -*-
#
#   by Akira Kageyama
#   on 2018.10.30
#   for my lectures at Kobe Univ.
#
from PIL import Image, ImageDraw, ImageFont
import sys

student_id_list_file = 'student_id_list.txt'

args = sys.argv

height = 2970
width = 2100

nbit = 20  # 1812345T => 812345 (inner 6 digits) => 20 bit
fontpath = "/System/Library/Fonts/AquaKana.ttc"


def func(student_id):
    im = Image.new("RGB", (width, height), '#ffffff')
    draw = ImageDraw.Draw(im)
    s = width // 10
    w = (width - 2*s ) // (2*nbit - 1)

    #                                         nbit-1
    #                                        /
    #  |       | 0 |   | 1 |   | 2 |...   |n-1|   s   |
    #  |   s   | w | w | w | w | w |... w | w |   s   |
    #  |       |   |   |   |   |   |...   |   |       |
    #  +-------+---+---+---+---+---+...---+---+-------+
    #  |       |   |   |   |   |   |...   |   |       |
    #  |       |   |   |   |   |   |...   |   |       |
    #  +-------+---+---+---+---+---+...---+---+-------+


    # student_id = '1823456F'

    student_id_number = int(student_id[1:7]) # 1823456F => 1823456
    number = student_id_number % 1000000 # 1823456 ==> 823456

    bin_str = format(number, '020b') # 20 bit with leading zeros
                                     # 1823456 ==> 11001001000010100000

    for i in range(20):
        bit = bin_str[i]
        # print(bit)
        if bit=='1':
            draw.rectangle((s+2*i*w, 2, s+2*i*w+w, 102), \
                           fill=(  0,   0,   0), outline=(0, 0, 0))
        else:
            draw.rectangle((s+2*i*w, 2, s+2*i*w+w, 102), \
                           fill=(255, 255, 255), outline=(0, 0, 0))

    font = ImageFont.truetype(fontpath, 50)

    draw.text((200,150), u'学籍番号:  ' + student_id, font=font, fill='#000000')
    draw.rectangle((435, 140, 725, 212), outline='#000000')
    draw.text((200,250), u'氏名: ', font=font, fill='#000000')
    draw.line((350,300,900,300), fill='#000000', width=1)
    draw.text((200,350), u'学部・学科: ', font=font, fill='#000000')
    draw.line((500,400,1300,400), fill='#000000', width=1)

    draw.line((100,480,width-100,480), fill='#000000', width=3)

    im.save(student_id + '.jpg', quality=95)


if __name__ == '__main__':
    f = open(student_id_list_file, 'r')
    list = f.readlines()
    for student_id in list:
        func(student_id.rstrip())
    f.close()
