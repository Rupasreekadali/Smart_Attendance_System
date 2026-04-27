import tkinter as tk
from tkinter import messagebox
import cv2
import os
import csv
import numpy as np
from datetime import datetime
from PIL import Image, ImageTk

cam = None

# automatically load haarcascade from opencv installation
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def create_student_profile():

    global cam

    win = tk.Toplevel(root)
    win.title("Create Student Profile")
    win.geometry("420x600")

    tk.Label(win, text="Name").pack()
    name_entry = tk.Entry(win)
    name_entry.pack()

    tk.Label(win, text="Roll Number").pack()
    roll_entry = tk.Entry(win)
    roll_entry.pack()

    tk.Label(win, text="Mobile Number").pack()
    phone_entry = tk.Entry(win)
    phone_entry.pack()

    tk.Label(win, text="Branch").pack()
    branch_entry = tk.Entry(win)
    branch_entry.pack()

    tk.Label(win, text="Section").pack()
    section_entry = tk.Entry(win)
    section_entry.pack(pady=5)

    preview_label = tk.Label(win)
    preview_label.pack(pady=15)

    cam = cv2.VideoCapture(0)

    def update_camera():

        ret, frame = cam.read()

        if ret:

            frame_small = cv2.resize(frame,(300,200))
            frame_rgb = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)

            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            preview_label.imgtk = imgtk
            preview_label.configure(image=imgtk)

        win.after(10, update_camera)

    update_camera()


    def capture_faces():

        name = name_entry.get()
        roll = roll_entry.get()
        phone = phone_entry.get()
        branch = branch_entry.get()
        section = section_entry.get()

        if name == "" or roll == "":
            messagebox.showerror("Error","Name and Roll required")
            return

        folder = f"dataset/{roll}_{name}"
        os.makedirs(folder, exist_ok=True)

        # save student data
        if not os.path.exists("students.csv"):

            with open("students.csv","w",newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Roll","Name","Branch","Section","Phone","ImagePath"])

        with open("students.csv","a",newline="") as f:

            writer = csv.writer(f)
            writer.writerow([roll,name,branch,section,phone,f"{folder}/1.jpg"])

        count = 0

        while count < 30:

            ret, frame = cam.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_detector.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:

                count += 1

                face = frame[y:y+h, x:x+w]

                cv2.imwrite(f"{folder}/{count}.jpg", face)

        messagebox.showinfo("Success","Student saved with 30 images")


    tk.Button(
        win,
        text="Capture Face & Save",
        command=capture_faces,
        width=22,
        height=2,
        bg="#20bf6b",
        fg="white"
    ).pack(pady=20)

    tk.Button(
        win,
        text="Close",
        command=win.destroy
    ).pack()



def take_attendance():

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    faces = []
    labels = []
    names = []

    dataset_path = "dataset"

    if not os.path.exists(dataset_path):
        messagebox.showerror("Error","Dataset not found")
        return

    label_id = 0
    label_map = {}

    for person in os.listdir(dataset_path):

        person_path = os.path.join(dataset_path, person)

        if not os.path.isdir(person_path):
            continue

        label_map[label_id] = person

        for image in os.listdir(person_path):

            img_path = os.path.join(person_path, image)

            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            faces.append(img)
            labels.append(label_id)

        label_id += 1


    if len(faces) == 0:
        messagebox.showerror("Error","No training images found")
        return


    recognizer.train(faces, np.array(labels))

    cam = cv2.VideoCapture(0)

    present_students = set()

    while True:

        ret, frame = cam.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces_detected = face_detector.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces_detected:

            label, confidence = recognizer.predict(gray[y:y+h, x:x+w])

            if confidence < 80:

                name = label_map[label]

                present_students.add(name)

                cv2.putText(frame,name,(x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,(0,255,0),2)

            else:

                cv2.putText(frame,"Unknown",(x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.9,(0,0,255),2)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow("Face Recognition - Press Q to stop", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    os.makedirs("attendance", exist_ok=True)

    date = datetime.now().strftime("%d-%m-%Y")

    filename = f"attendance/Attendance_{date}.csv"

    with open(filename,"w",newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["Student","Status"])

        for student in present_students:
            writer.writerow([student,"Present"])

    messagebox.showinfo("Attendance Saved",f"Saved in {filename}")



root = tk.Tk()
root.title("Smart Attendance System")
root.geometry("400x350")

tk.Button(
    root,
    text="Create Student Profile",
    command=create_student_profile,
    width=25,
    height=2
).pack(pady=40)

tk.Button(
    root,
    text="Take Attendance",
    command=take_attendance,
    width=25,
    height=2
).pack()

root.mainloop()