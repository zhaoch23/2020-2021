#This is a program that cuts images
#Exists because pygame is garbage

from PIL import Image
import sys
import os
def fill_image(image):
    width, height = image.size
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
    if width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2),0))
    return new_image

def cut_image(image, w, h):
    width, height = image.size
    item_width = int(width / w)
    item_height = int(height/ h)
    box_list = []
    # (left, upper, right, lower)
    for i in range(0,h):
        for j in range(0, w):
            #print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
            box = (j*item_width,i*item_height,(j+1)*item_width,(i+1)*item_height)
            box_list.append(box)
 
    image_list = [image.crop(box) for box in box_list]
    return image_list

def save_images(image_list):
    index = 1
    for image in image_list:
        image.save("barrages/diamond"+ str(index) + '.png')
        index += 1
 
if __name__ == '__main__':
    work_path = os.path.abspath(os.path.dirname(__file__))
    os.chdir(work_path)
    file_path = "barrages/diamond.png"
    image = Image.open(file_path)
    # image.show()
    #image = fill_image(image)
    image_list = cut_image(image, 16, 1)
    save_images(image_list)