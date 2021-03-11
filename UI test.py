from pygamemig import *
import os
from PIL import Image

window = Window(944, 944)
bodyIdx = 0
hairIdx = 0

bodyPath = "img/bodies/"
hairPath = "img/hair/"

# pic = Object("img/faces/" + os.listdir("img/faces")[img_idx], Vector2(200, 200))
# pic.transform.setPos(Vector2(window.width / 2, window.height / 2))

bodyPic = Object(bodyPath + os.listdir(bodyPath)[0], Vector2(800, 800))
bodyPic.transform.setPos((Vector2(window.width / 2, window.height / 2)))

hairPic = Object(hairPath + os.listdir(hairPath)[0], Vector2(800, 800))
hairPic.transform.setPos(Vector2(window.width / 2, window.height / 2))

frame = Object("img/marco.png", Vector2(944, 944))
frame.transform.setPos(Vector2(window.width / 2, window.height / 2))


def Export():  # RGBA
    body = Image.open(bodyPath + os.listdir(bodyPath)[bodyIdx])
    hair = Image.open(hairPath + os.listdir(hairPath)[hairIdx])

    result = Image.new("RGBA", (11, 11))
    pixels = result.load()

    for y in range(11):  # IMG[11y + x]
        for x in range(11):
            if hair.getpixel((x, y))[3] == 0:  # place body's pixel
                pixels[x, y] = body.getpixel((x, y))
            else:  # place hair's pixel
                pixels[x, y] = hair.getpixel((x, y))
    result.save("results/test.png")


while window.running:
    if Input.GetKey(K_LEFT) and not left:
        bodyIdx -= 1
    if Input.GetKey(K_RIGHT) and not right:
        bodyIdx += 1

    if Input.GetKey(K_a) and not a:
        hairIdx -= 1
    if Input.GetKey(K_d) and not d:
        hairIdx += 1

    if Input.GetKey(K_SPACE) and not space:
        Export()

    if bodyIdx >= len(os.listdir(bodyPath)):
        bodyIdx = 0
    elif bodyIdx < 0:
        bodyIdx = len(os.listdir(bodyPath)) - 1

    if hairIdx >= len(os.listdir(hairPath)):
        hairIdx = 0
    elif hairIdx < 0:
        hairIdx = len(os.listdir(hairPath)) - 1

    left = Input.GetKey(K_LEFT)
    right = Input.GetKey(K_RIGHT)
    a = Input.GetKey(K_a)
    d = Input.GetKey(K_d)
    space = Input.GetKey(K_SPACE)

    bodyPic.SetImg(bodyPath + os.listdir(bodyPath)[bodyIdx])
    hairPic.SetImg(hairPath + os.listdir(hairPath)[hairIdx])

    window.Update()
