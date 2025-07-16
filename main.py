import face_recognition
import cv2
import os
import urllib.request

choosing = input("Choose image from: folder (must include images/(wanted image)) or link (must include https:// or http://").strip()

if choosing.startswith("http://") or choosing.startswith("https://"):
    tmp_path = "temp_image.jpg"
    urllib.request.urlretrieve(choosing, tmp_path)
    image_path = tmp_path
elif choosing.lower() == "folder":
    print("\nImagini disponibile în folderul images/: ")
    image_fisier = [f for f in os.listdir("images") if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    for idx, file in enumerate(image_fisier):
        print(f"{idx + 1}. {file}")
    try:
        index = int(input("\nAlege numărul imaginii: ")) - 1
        choosing = f"images/{image_fisier[index]}"
    except (ValueError, IndexError):
        print("Alegere invalidă.")
        exit()
    image_path = choosing

else:
    image_path = choosing

try:
    image = face_recognition.load_image_file(image_path)
except Exception as e:
    print(f"Eroare la incarcare imaginii {e}")
    exit()

face_location = face_recognition.face_locations(image)
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

for (top, right, bottom, left) in face_location:
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (108, 2, 161), 3)

cv2.imwrite("images/img_person_marked.jpg", image_bgr)

if choosing.startswith("http://") or choosing.startswith("https://"):
    os.remove(tmp_path)
