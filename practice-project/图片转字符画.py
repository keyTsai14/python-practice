from PIL import Image

# 原图片
img = 'practice-project\pic\duolaameng.webp'
width = 300
height = 400
# 字符画
result ='practice-project/output/newPic.txt'

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    # 灰度值公式：Gray=0.2126×R+0.7152×G+0.0722×B
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (255.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(img)
    im = im.resize((width,height),Image.NEAREST)
    txt = ''
    for i in range(height):
        for j in range(width):
            txt += get_char(*im.getpixel((j,i)))
        txt+= '\n'
    print(txt)
    with open(result,'w') as f:
        f.write(txt)        