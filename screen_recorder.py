# I tried to record my pc screen with some window programmes but it includes water marks.So I decided to make my own.
# This is from https://www.geeksforgeeks.org/create-a-screen-recorder-using-python/

import pyautogui
import cv2
import numpy as np

resolution = (1920, 1080)
codec      = cv2.VideoWriter_fourcc(*"XVID")
filename   = "Recording.avi"
fps        = 30.0
out        = cv2.VideoWriter(filename, codec, fps, resolution)



