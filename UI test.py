from pygamemig import *
import os

window = Window(944, 944)
bodyIdx = 0
hairIdx = 0

bodyPath = "img/bodies/"
hairPath = "img/hair/"

#pic = Object("img/faces/" + os.listdir("img/faces")[img_idx], Vector2(200, 200))
#pic.transform.setPos(Vector2(window.width / 2, window.height / 2))

bodyPic = Object(bodyPath + os.listdir(bodyPath)[0], Vector2(800, 800))
bodyPic.transform.setPos((Vector2(window.width / 2, window.height / 2)))

hairPic = Object(hairPath + os.listdir(hairPath)[0], Vector2(800, 800))
hairPic.transform.setPos(Vector2(window.width / 2, window.height / 2))

frame = Object("img/marco.png", Vector2(944, 944))
frame.transform.setPos(Vector2(window.width / 2, window.height / 2))

while window.running:
    if Input.GetKey(K_LEFT) and not left:
        bodyIdx -= 1
    if Input.GetKey(K_RIGHT) and not right:
        bodyIdx += 1

    if Input.GetKey(K_a) and not a:
        hairIdx -= 1
    if Input.GetKey(K_d) and not d:
        hairIdx += 1

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

    bodyPic.SetImg(bodyPath + os.listdir(bodyPath)[bodyIdx])
    hairPic.SetImg(hairPath + os.listdir(hairPath)[hairIdx])
    window.Update()


