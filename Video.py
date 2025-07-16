import face_recognition
import cv2
import time
import os

video_capture = cv2.VideoCapture(0)

prevtime= time.time()

filelog=open("file_log_of_performance.txt", "a")

while True:
    ret, frame = video_capture.read()

    timp=time.time()
    fps = 1/(timp-prevtime)
    prevtime=timp

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)

    for (top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    if fps >= 30:
        color = (0,255,0)
    elif fps >= 20:
        color=(0,255,255)
    else:
        color =  (0,0,255)
    cv2.putText(frame, f"Frame per second: {fps:.2f}", (10,30), cv2.FONT_ITALIC, 1, color,2 )
    cv2.imshow('Detectare fete', frame)

    timpsetat = time.strftime("%H:%M:%S")
    filelog.write(f"[{timpsetat}] Fps: {fps:.2f}")

    if cv2.waitKey(1) & 0xFF == 27:
        break

filelog.close()
video_capture.release()
cv2.destroyAllWindows()
