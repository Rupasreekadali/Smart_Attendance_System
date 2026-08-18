# Smart Attendance System

A simple **face-recognition-based student attendance system** built with Python, Tkinter, OpenCV, NumPy, and Pillow.

The application allows you to:

* Create student profiles
* Capture 30 face images for each student
* Store student information in a CSV file
* Train an LBPH face-recognition model
* Recognize students using a webcam
* Automatically record present students in a daily attendance CSV file

## Features

### 1. Create Student Profile

The **Create Student Profile** option collects:

* Student Name
* Roll Number
* Mobile Number
* Branch
* Section

After entering the details, the webcam is used to capture **30 face images** of the student.

Images are stored inside:

```text
dataset/
└── RollNumber_Name/
    ├── 1.jpg
    ├── 2.jpg
    ├── 3.jpg
    ├── ...
    └── 30.jpg
```

### 2. Face Recognition

The system uses:

* OpenCV Haar Cascade for face detection
* LBPH (Local Binary Patterns Histograms) for face recognition

During attendance, the webcam detects faces and compares them with the images stored in the dataset.

Recognized students are marked as **Present**.

### 3. Attendance CSV

Attendance is automatically saved in the `attendance` folder.

Example:

```text
attendance/
└── Attendance_18-08-2026.csv
```

The generated file contains:

```csv
Student,Status
101_John,Present
102_Rahul,Present
```

## Technologies Used

| Technology | Purpose                                       |
| ---------- | --------------------------------------------- |
| Python     | Main programming language                     |
| Tkinter    | Graphical user interface                      |
| OpenCV     | Camera access, face detection and recognition |
| NumPy      | Numerical processing                          |
| Pillow     | Displaying webcam frames in Tkinter           |
| CSV        | Student and attendance data storage           |

## Requirements

Make sure Python is installed on your system.

Install the required packages:

```bash
pip install opencv-contrib-python numpy pillow
```

> **Important:** `opencv-contrib-python` is required because the project uses `cv2.face.LBPHFaceRecognizer_create()`.

Tkinter is normally included with Python on Windows. On some Linux distributions, you may need to install it separately.

## Project Structure

After running the application, the project may look like this:

```text
Smart-Attendance-System/
│
├── main.py
├── students.csv
│
├── dataset/
│   ├── 101_John/
│   │   ├── 1.jpg
│   │   ├── 2.jpg
│   │   └── ...
│   │
│   └── 102_Rahul/
│       ├── 1.jpg
│       ├── 2.jpg
│       └── ...
│
└── attendance/
    └── Attendance_18-08-2026.csv
```

## How to Run

### Step 1 — Clone or download the project

Download the project files to your computer.

### Step 2 — Install dependencies

Open a terminal in the project directory and run:

```bash
pip install opencv-contrib-python numpy pillow
```

### Step 3 — Run the application

```bash
python main.py
```

The application window will open.

## How to Use

### Register a Student

1. Click **Create Student Profile**.
2. Enter the student's name.
3. Enter the roll number.
4. Enter the mobile number.
5. Enter the branch.
6. Enter the section.
7. Make sure the student's face is visible to the camera.
8. Click **Capture Face & Save**.
9. The system captures 30 face images.
10. Student information is saved in `students.csv`.

### Take Attendance

1. Click **Take Attendance**.
2. The system loads all images from the `dataset` folder.
3. The LBPH recognizer is trained using those images.
4. The webcam opens.
5. Students look at the camera.
6. Recognized students are displayed on the screen.
7. Press **Q** to stop attendance.
8. Attendance is saved automatically in the `attendance` folder.

## Important Notes

### Camera

The application uses the default webcam:

```python
cv2.VideoCapture(0)
```

If your computer has multiple cameras, you may need to change `0` to another camera index.

For example:

```python
cv2.VideoCapture(1)
```

### Face Recognition Threshold

The current recognition threshold is:

```python
if confidence < 80:
```

Lower values generally indicate a closer match in OpenCV's LBPH implementation. You may need to experiment with the threshold depending on lighting, camera quality, and dataset quality.

### Lighting and Face Position

For better recognition:

* Use good lighting.
* Keep the face clearly visible.
* Avoid extreme angles.
* Capture images from slightly different angles.
* Avoid covering the face.
* Use a consistent camera position during attendance.

## Data Files

### `students.csv`

Stores registered student information:

```csv
Roll,Name,Branch,Section,Phone,ImagePath
101,John,CSE,A,9876543210,dataset/101_John/1.jpg
```

### Attendance CSV

Stores students recognized during an attendance session:

```csv
Student,Status
101_John,Present
102_Rahul,Present
```

## Limitations

This project is intended as a simple educational/demo attendance system.

Current limitations include:

* No login or authentication system
* No database; CSV files are used for storage
* Attendance only records students recognized during the current session
* Students who are absent are not included in the attendance CSV
* LBPH recognition can be affected by lighting and camera quality
* Student folders are generated using roll number and name
* There is no duplicate-student validation
* The camera must be available and accessible
* The face dataset is stored locally

## Future Improvements

Possible improvements include:

* Add a proper database such as SQLite or MySQL
* Add student deletion/update functionality
* Add an admin login system
* Record both Present and Absent students
* Add date and time to attendance records
* Add automatic attendance reports
* Export reports to Excel
* Improve face recognition accuracy
* Add anti-spoofing/liveness detection
* Add a better camera preview
* Add multiple-camera support
* Prevent duplicate student registration
* Add attendance history and search functionality
* Create a more modern GUI

## Privacy

This project stores biometric face images locally. Use it only with appropriate authorization and consent, and protect the `dataset` directory and student information from unauthorized access.

## License

This project is provided for educational and demonstration purposes. You may modify and extend it according to your project's requirements.
