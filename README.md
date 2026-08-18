# Smart Attendance System

A Python-based **face recognition attendance system** using Tkinter and OpenCV.

## Features

* Create student profiles
* Capture 30 face images per student
* Face detection using Haar Cascade
* Face recognition using LBPH
* Automatic attendance CSV generation

## Technologies

* Python
* Tkinter
* OpenCV
* NumPy
* Pillow
* CSV

## Installation

```bash
pip install opencv-contrib-python numpy pillow
```

## Run

```bash
python main.py
```

## Usage

1. Click **Create Student Profile** and enter student details.
2. Capture 30 face images.
3. Click **Take Attendance**.
4. The webcam recognizes registered students.
5. Press **Q** to stop.
6. Attendance is saved in the `attendance` folder.

## Project Structure

```text
Smart-Attendance-System/
├── main.py
├── students.csv
├── dataset/
└── attendance/
```

> Make sure your webcam is connected and accessible.

## Note

This project is intended for **educational purposes** and stores face images locally.
