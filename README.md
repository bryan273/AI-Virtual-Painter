# AI Virtual Painter
 Paint directly to the monitor through motion without touching the screen

## Description:
 In this pandemic situation, sometimes we cannot be separated from the online meeting. In several online meetings, we sometimes find it challenging to describe what we want to convey when we do not have something to display. Therefore, we designed software that utilizes computer vision field so users can write or draw directly without touching their screen.

We use an existing model that can detect hands and fingers from a model named mediapipe. Through this model, we create a program that can draw and write something on a real-time webcam without touching the screen. The program has features to select colors and delete images. These features utilize the position of our fingers and hands to change it.

## Features

* Draw: We need to lift our index finger and move it to draw the object we want. 
* Select and hold: If we want to select another color or eraser and stop the drawing activity, we must lift both our index and middle fingers. (selection available : pink, blue, green, eraser)
* Erase: To erase, we select the eraser object and delete it the same way as when drawing. 
* Clear all: To clear all of the images, we simply lift our four fingers except the thumb.


<img src="https://user-images.githubusercontent.com/88226713/173982541-7109de3d-0306-4472-993a-be4d1c6fc0af.png" width="500">

## Dependencies

Numpy | OpenCV | Mediapipe
--- | --- | ---

Install the required packages by executing the following command.

`$ pip install -r requirements.txt`

## Files
* main.py : main program to execute real-time webcam virtual painter
* handtrackingmodule.py : detect and draw hand landmarks 
* Header : a folder contains the header of painter components


Source: https://www.computervision.zone/courses/ai-virtual-painter/
