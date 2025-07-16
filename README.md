# FaceRecognition
A simple project for face recognition.

# IMPORTANT: PROGRAM WORKS ON PYTHON 3.10

# Project Goals

- To learn more about libraries in Python
- To detect human faces through video or images
- To use the knowledge gathered through the years in a project
- Allow image input from local files or direct online links

## Installations

- Create a folder for the project and move the files inside
- In CMD write to activate virtual environment: python -m venv venv (For windows)
- Write to install all libraries needed: pip install -r requirements.txt

### How to run
Main.py - Program to analyze and find the faces of the given image through a URL link or folder
- By using Pycharm or Visual Studio Code, run the Main.py program
- The user will be asked to choose between accessing the folder 'images' images or an online image
- By writing in the console 'folder', the user will be given 4 images to choose from, and can type the number corresponding to the file
- To analyze an online image, write the link to the image containing at the start 'http://' or 'https://"
- In the project folder will appear a new image file named 'img_person_marked' which shows the faces found by the program.

Video.py - Program to access the user's webcam and mark the found face in the camera
- By using Pycharm or Visual Studio Code, run the Video.py program
- The program will access the user's webcam, showing the faces found in a rectangle/square
- In the top-left corner, FPS (frames per second) is displayed and color-coded: green - 30 or higher, yellow - 20 or higher, red - lower than 20.
- To exit the program, press the 'ESC' button on your keyboard
- On pressing the 'ESC' button, the user will receive a new .txt file in their project folder a file named 'file_log_of_performance' which contains their log of their session frames per second

#### Author
Iaroslav Romanov 
Github: dream-of-no-idea
