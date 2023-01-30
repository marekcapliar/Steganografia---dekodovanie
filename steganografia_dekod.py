from PIL import Image

img = Image.open('obrsospr.png')
pixels = img.load()


def png_to_bin(image):
    msg_bin = []
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            pixel = pixels[j, i]
            pix_blu = pixel[2]
            bin_blu = bin(pix_blu)[-1]
            msg_bin.append(bin_blu)
    return msg_bin


def real_bin(image: list):
    binar = png_to_bin(image)
    bin_msg = []
    bin_num = ''
    for i in range(len(binar)//8):
        for j in range(8):
            bin_num += binar[8 * i + j]
        bin_msg.append(bin_num)
        bin_num = ''
    return bin_msg


def message(binary: list):
    msg_list = real_bin(binary)
    msg = ''
    letter = ''
    for i in msg_list:
        if letter != '#':
            ordinal = int(i, 2)
            letter = chr(ordinal)
            msg += letter
        else:
            break
    msg = msg.replace('#', '')
    print(msg)


message(img)
