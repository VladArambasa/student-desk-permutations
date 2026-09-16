````markdown
# Classroom Randomiser

A simple Python/Tkinter application for randomly assigning students to desks in a classroom.

The application reads classes and student lists from a directory structure and uses a text-based classroom layout to determine where desks are located.

## Features

- Python + Tkinter
- No third-party Python dependencies
- Automatically detects classes
- Supports classes 5–12
- Supports groups from A–Z
- One `Students.txt` file per group
- Text-based classroom layout
- Supports student desks, empty spaces and teacher desk
- Random student assignment
- Visual classroom display
- Reload classes without restarting the application

## Requirements

Python 3.10 or newer is recommended.

The application uses only Python's standard library:

- `tkinter`
- `pathlib`
- `random`
- `os`
- `subprocess`

No `pip install` is required.

### Ubuntu / Debian

If Tkinter is not installed:

```bash
sudo apt install python3-tk
````

### Windows

Install Python from the official Python installer.

Make sure that the standard Tkinter component is included.

## Installation

Clone or copy the project:

```text
classroom-randomiser/
```

The directory should contain:

```text
classroom-randomiser/
├── main.py
├── desks.txt
├── README.md
├── LICENSE
└── classes/
```

## Directory Structure

The `classes` directory contains the school classes.

```text
classes/
├── 5/
├── 6/
├── 7/
├── 8/
├── 9/
├── 10/
├── 11/
└── 12/
```

Each class may contain groups from `a` to `z`.

For example:

```text
classes/
└── 6/
    ├── a/
    │   └── Students.txt
    ├── b/
    │   └── Students.txt
    └── f/
        └── Students.txt
```

The application automatically discovers the directories.

You do not need to configure the classes manually in Python.

## Students.txt

Each group contains a `Students.txt` file.

Example:

```text
Popescu Ion
Ionescu Maria
Georgescu Andrei
Dumitrescu Elena
Stan Mihai
Radu Alexandra
```

Each line represents one student.

Blank lines are ignored.

## Classroom Layout

The classroom layout is stored in:

```text
desks.txt
```

The following characters are supported:

```text
#   Student desk
O   Empty space
@   Teacher desk
```

Example:

```text
#####
#####
OOOOO
#####
#####
OO@OO
```

This represents:

```text
DESK DESK DESK DESK DESK
DESK DESK DESK DESK DESK
SPACE SPACE SPACE SPACE SPACE
DESK DESK DESK DESK DESK
DESK DESK DESK DESK DESK
SPACE SPACE TEACHER SPACE SPACE
```

The number of `#` characters determines the maximum number of students that can be seated.

## Running the Application

From the project directory:

```bash
python3 main.py
```

or:

```bash
python main.py
```

depending on the operating system.

## Using the Application

1. Start the application.
2. Select a class.
3. Select a group.
4. The student list is loaded automatically.
5. The classroom layout is loaded from `desks.txt`.
6. Press `Randomise`.
7. Students are randomly assigned to desks.

Pressing `Randomise` again creates a new assignment.

## Important

The application does not permanently modify `Students.txt`.

The original student list therefore remains unchanged.

The random assignment exists in the current application session.

## Number of Students vs Desks

If there are more students than desks, the application will display an error.

For example:

```text
Students: 28
Desks:    25
```

The application will not perform the assignment.

If there are fewer students than desks, the remaining desks are displayed as empty.

## Editing desks.txt

The application includes an `Edit desks.txt` button.

You can also edit the file manually using any text editor.

After changing the layout, press `Reload`.

## Project Structure

```text
classroom-randomiser/
│
├── main.py
├── desks.txt
├── README.md
├── LICENSE
│
└── classes/
    ├── 5/
    ├── 6/
    ├── 7/
    ├── 8/
    ├── 9/
    ├── 10/
    ├── 11/
    └── 12/
```

## License

This project is distributed under the MIT License.

See `LICENSE` for the full license text.


````markdown
## Installation

### 1. Install Python

Python 3.10 or newer is recommended.

Check your Python version:

```bash
python3 --version
````

### 2. Install Tkinter

Tkinter is part of Python's standard library, but on Linux it may need to be installed separately.

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-tk
```

Test that Tkinter is available:

```bash
python3 -m tkinter
```

A small Tkinter window should appear.

### 3. Install the Python dependencies

The project includes a `requirements.txt` file.

Install the dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

This installs:

* ReportLab — used to generate the printable PDF seating charts.

Tkinter is deliberately **not** included in `requirements.txt` because it is not installed through pip on a normal Python installation.

### 4. Run the application

From the directory containing `main.py`:

```bash
python3 main.py
```

On systems where `python` points to Python 3, you can also use:

```bash
python main.py
```

## Usage

### Select a class

When the application starts, it automatically scans the `classes` directory.

Select a class from the **Class** dropdown.

For example:

```text
5
6
7
8
9
10
11
12
```

### Select a group

After selecting a class, the **Group** dropdown is populated automatically with the groups that exist inside that class.

For example:

```text
a
b
f
```

If the directory exists:

```text
classes/6/f/
```

the application will look for:

```text
classes/6/f/Students.txt
```

### Randomise students

Press:

```text
Randomise
```

The application randomly shuffles the students and assigns them to the available `#` desks from `desks.txt`.

The original `Students.txt` file is not modified.

Pressing **Randomise** again creates another random seating arrangement.

### Reload

Press:

```text
Reload
```

to rescan the `classes` directory and reload the available classes and groups.

Use this after adding a new class or group while the application is running.

### Edit desks.txt

The **Edit desks.txt** button opens the classroom layout file in the system's default text editor.

After changing the layout, press **Reload**.

### Export PDF

Press:

```text
Export PDF
```

to create a printable seating chart.

The generated PDF is:

* A4
* Landscape
* Vector-based
* Suitable for printing
* Scaled automatically to fit the classroom layout
* Labeled with the class/group
* Contains the assigned student names
* Contains the teacher's desk

For example:

```text
Class_6F_Seating_2026-09-16.pdf
```

The PDF is generated directly with ReportLab; **LaTeX and TikZ are not required**.

The application exports the currently displayed seating arrangement. If no seating arrangement has been generated yet, the application will ask you to randomise the students first.

### Example workflow

```text
1. Start the application

   python3 main.py

2. Select class

   6

3. Select group

   f

4. Check the classroom layout

5. Press:

   Randomise

6. Check the generated seating arrangement

7. Press:

   Export PDF

8. Choose where to save the PDF
```

## Dependencies

Python standard library:

```text
tkinter
pathlib
random
os
subprocess
```

Third-party Python package:

```text
reportlab
```

Install the third-party package with:

```bash
python3 -m pip install -r requirements.txt
```

Tkinter is installed separately on Ubuntu/Debian with:

```bash
sudo apt install python3-tk
```

```
```

