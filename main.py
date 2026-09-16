import random
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk


# PATHS
BASE_DIR = Path(__file__).resolve().parent
CLASSES_DIR = BASE_DIR / "classes"
DESKS_FILE = BASE_DIR / "desks.txt"


# APPLICATION
class ClassroomRandomiser:
    def __init__(self, root):
        self.root = root
        self.root.title("Classroom Randomiser")
        self.root.geometry("1100x750")
        self.root.minsize(900, 600)

        self.current_class = None
        self.current_group = None

        self.desk_layout = []
        self.desk_positions = []
        self.students = []
        self.assignment = {}

        self.build_gui()
        self.load_classes()

    # GUI
    def build_gui(self):
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)

        # TOP CONTROLS
        controls = ttk.LabelFrame(
            main,
            text="Class selection",
            padding=10
        )
        controls.pack(fill="x", pady=(0, 10))

        ttk.Label(
            controls,
            text="Class:"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.class_combo = ttk.Combobox(
            controls,
            state="readonly",
            width=10
        )
        self.class_combo.grid(row=0, column=1, padx=5, pady=5)
        self.class_combo.bind(
            "<<ComboboxSelected>>",
            self.class_selected
        )

        ttk.Label(
            controls,
            text="Group:"
        ).grid(row=0, column=2, padx=5, pady=5)

        self.group_combo = ttk.Combobox(
            controls,
            state="readonly",
            width=10
        )
        self.group_combo.grid(row=0, column=3, padx=5, pady=5)
        self.group_combo.bind(
            "<<ComboboxSelected>>",
            self.group_selected
        )

        ttk.Button(
            controls,
            text="Randomise",
            command=self.randomise
        ).grid(row=0, column=4, padx=15, pady=5)

        ttk.Button(
            controls,
            text="Reload",
            command=self.reload
        ).grid(row=0, column=5, padx=5, pady=5)

        ttk.Button(
            controls,
            text="Edit desks.txt",
            command=self.edit_desks
        ).grid(row=0, column=6, padx=5, pady=5)

        # INFORMATION
        self.info_label = ttk.Label(
            main,
            text="Select a class and group.",
            anchor="center"
        )
        self.info_label.pack(fill="x", pady=(0, 10))

        # CLASSROOM
        classroom_frame = ttk.LabelFrame(
            main,
            text="Classroom",
            padding=15
        )
        classroom_frame.pack(
            fill="both",
            expand=True
        )

        self.canvas = tk.Canvas(
            classroom_frame,
            background="white",
            highlightthickness=1
        )
        self.canvas.pack(
            fill="both",
            expand=True
        )

        # BOTTOM
        bottom = ttk.Frame(main)
        bottom.pack(fill="x", pady=(10, 0))

        self.status_label = ttk.Label(
            bottom,
            text="Ready."
        )
        self.status_label.pack(side="left")

    # LOAD CLASSES
    def load_classes(self):
        CLASSES_DIR.mkdir(exist_ok=True)

        classes = [
            directory.name
            for directory in CLASSES_DIR.iterdir()
            if directory.is_dir()
        ]

        def class_sort(value):
            try:
                return int(value)
            except ValueError:
                return 999

        classes.sort(key=class_sort)

        self.class_combo["values"] = classes

        if classes:
            self.class_combo.current(0)
            self.class_selected()

    # CLASS SELECTED
    def class_selected(self, event=None):
        selected = self.class_combo.get()

        if not selected:
            return

        self.current_class = selected

        class_dir = CLASSES_DIR / selected

        groups = [
            directory.name
            for directory in class_dir.iterdir()
            if directory.is_dir()
        ]

        groups.sort()

        self.group_combo["values"] = groups

        if groups:
            self.group_combo.current(0)
            self.group_selected()
        else:
            self.current_group = None
            self.clear_classroom()

    # GROUP SELECTED
    def group_selected(self, event=None):
        selected = self.group_combo.get()

        if not selected:
            return

        self.current_group = selected

        self.load_students()
        self.load_desks()

        self.draw_classroom()

    # LOAD STUDENTS
    def load_students(self):
        if not self.current_class or not self.current_group:
            return

        group_dir = (
            CLASSES_DIR
            / self.current_class
            / self.current_group
        )

        students_file = None

        possible_names = [
            "Students",
            "Students.txt",
            "students",
            "students.txt",
        ]

        for name in possible_names:
            candidate = group_dir / name

            if candidate.is_file():
                students_file = candidate
                break

        if students_file is None:
            self.students = []

            self.info_label.config(
                text=(
                    f"Class {self.current_class}{self.current_group}: "
                    "Students file not found."
                )
            )

            return

        with students_file.open(
            "r",
            encoding="utf-8"
        ) as file:
            self.students = [
                line.strip()
                for line in file
                if line.strip()
            ]

        self.info_label.config(
            text=(
                f"Class {self.current_class}{self.current_group} — "
                f"{len(self.students)} students"
            )
        )

    # LOAD DESKS
    def load_desks(self):
        if not DESKS_FILE.is_file():
            messagebox.showerror(
                "Missing desks.txt",
                f"Could not find:\n{DESKS_FILE}"
            )
            self.desk_layout = []
            return

        with DESKS_FILE.open(
            "r",
            encoding="utf-8"
        ) as file:
            lines = [
                line.rstrip("\n")
                for line in file
            ]

        # REMOVE EMPTY LINES AT THE END
        while lines and not lines[-1].strip():
            lines.pop()

        self.desk_layout = [
            list(line)
            for line in lines
        ]

        self.desk_positions = []

        for row, line in enumerate(self.desk_layout):
            for column, character in enumerate(line):
                if character == "#":
                    self.desk_positions.append(
                        (row, column)
                    )

    # RANDOMISE
    def randomise(self):
        if not self.students:
            messagebox.showwarning(
                "No students",
                "No students were loaded."
            )
            return

        if not self.desk_positions:
            messagebox.showwarning(
                "No desks",
                "No '#' desks were found in desks.txt."
            )
            return

        if len(self.students) > len(self.desk_positions):
            messagebox.showerror(
                "Not enough desks",
                (
                    f"There are {len(self.students)} students "
                    f"but only {len(self.desk_positions)} desks."
                )
            )
            return

        shuffled_students = self.students.copy()
        random.shuffle(shuffled_students)

        self.assignment = {}

        for position, student in zip(
            self.desk_positions,
            shuffled_students
        ):
            self.assignment[position] = student

        self.draw_classroom()

        self.status_label.config(
            text=(
                f"Randomised {len(self.assignment)} students."
            )
        )

    # DRAW CLASSROOM
    def draw_classroom(self):
        self.canvas.delete("all")

        if not self.desk_layout:
            return

        rows = len(self.desk_layout)

        columns = max(
            len(row)
            for row in self.desk_layout
        )

        if rows == 0 or columns == 0:
            return

        canvas_width = max(
            self.canvas.winfo_width(),
            500
        )

        canvas_height = max(
            self.canvas.winfo_height(),
            400
        )

        cell_width = canvas_width / columns
        cell_height = canvas_height / rows

        # KEEP CELLS REASONABLY SQUARE
        cell_size = min(
            cell_width,
            cell_height
        )

        total_width = columns * cell_size
        total_height = rows * cell_size

        offset_x = (
            canvas_width - total_width
        ) / 2

        offset_y = (
            canvas_height - total_height
        ) / 2

        for row, line in enumerate(self.desk_layout):
            for column, character in enumerate(line):

                x1 = (
                    offset_x
                    + column * cell_size
                    + 5
                )

                y1 = (
                    offset_y
                    + row * cell_size
                    + 5
                )

                x2 = (
                    offset_x
                    + (column + 1) * cell_size
                    - 5
                )

                y2 = (
                    offset_y
                    + (row + 1) * cell_size
                    - 5
                )

                if character == "#":
                    self.draw_desk(
                        x1,
                        y1,
                        x2,
                        y2,
                        self.assignment.get(
                            (row, column),
                            ""
                        )
                    )

                elif character == "@":
                    self.draw_teacher_desk(
                        x1,
                        y1,
                        x2,
                        y2
                    )

        self.canvas.update_idletasks()

    # STUDENT DESK
    def draw_desk(
        self,
        x1,
        y1,
        x2,
        y2,
        student
    ):
        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            outline="black",
            width=2
        )

        if student:
            self.canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text=student,
                width=(x2 - x1) - 10,
                font=("Arial", 11, "bold"),
                justify="center"
            )
        else:
            self.canvas.create_text(
                (x1 + x2) / 2,
                (y1 + y2) / 2,
                text="EMPTY",
                fill="gray",
                font=("Arial", 9)
            )

    # TEACHER DESK
    def draw_teacher_desk(
        self,
        x1,
        y1,
        x2,
        y2
    ):
        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            outline="black",
            width=2
        )

        self.canvas.create_text(
            (x1 + x2) / 2,
            (y1 + y2) / 2,
            text="TEACHER",
            font=("Arial", 10, "bold")
        )

    # CLEAR
    def clear_classroom(self):
        self.canvas.delete("all")
        self.assignment = {}
        self.desk_positions = []
        self.desk_layout = []

        self.info_label.config(
            text="No group selected."
        )

    # RELOAD
    def reload(self):
        self.assignment = {}
        self.load_classes()

        self.status_label.config(
            text="Reloaded."
        )

    # OPEN DESKS FILE
    def edit_desks(self):
        if not DESKS_FILE.exists():
            DESKS_FILE.touch()

        try:
            import os

            if os.name == "nt":
                os.startfile(DESKS_FILE)

            elif os.name == "posix":
                import subprocess

                subprocess.Popen(
                    ["xdg-open", str(DESKS_FILE)]
                )

        except Exception as error:
            messagebox.showerror(
                "Could not open file",
                str(error)
            )


# START
if __name__ == "__main__":
    root = tk.Tk()

    app = ClassroomRandomiser(root)

    root.mainloop()
