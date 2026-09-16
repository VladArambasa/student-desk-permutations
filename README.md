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

```
```
