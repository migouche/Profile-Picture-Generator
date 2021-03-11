from pygamemig import *
import os

window = Window(800, 600)
img_idx = 0
img_path = str(os.listdir("img/faces")[0])
print(img_path)

pic = Object("img/faces/" + os.listdir("img/faces")[img_idx], Vector2(200, 200))
pic.transform.setPos(Vector2(window.width / 2, window.height / 2))

while window.running:
    if Input.GetKey(K_LEFT) and not left:
        img_idx -= 1
    if Input.GetKey(K_RIGHT) and not right:
        img_idx += 1
    if img_idx >= len(os.listdir("img/faces")):
        img_idx = 0
    elif img_idx < 0:
        img_idx = len(os.listdir("img/faces")) - 1

    left = Input.GetKey(K_LEFT)
    right = Input.GetKey(K_RIGHT)
    pic.SetImg("img/faces/" + os.listdir("img/faces")[img_idx])
    window.Update()


