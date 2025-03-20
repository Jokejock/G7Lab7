"""
File: studentapp.py
The application for editing and analyzing student scores.
"""

from breezypythongui import EasyFrame
from student import Student
import matplotlib.pyplot as plt

class StudentApp(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Student Score Manager")
        self.addLabel("title", "Student Score Manager", row=0, column=0, columnspan=2)

        # Input fields for student name and scores
        self.addLabel("nameLabel", "Student Name:", row=1, column=0)
        self.nameField = self.addTextField("", row=1, column=1)

        self.addLabel("scoreLabel", "Scores (comma-separated):", row=2, column=0)
        self.scoreField = self.addTextField("", row=2, column=1)

        # Buttons for actions
        self.addButton("Add Student", self.addStudent, row=3, column=0)
        self.addButton("Plot Scores", self.plotScores, row=3, column=1)

        self.students = []  # List to hold student objects

    def addStudent(self):
        name = self.nameField.getText().strip()
        scores_text = self.scoreField.getText().strip()

        if not name:
            self.messageBox("Error", "Student name cannot be empty.")
            return
        
        if not scores_text:
            self.messageBox("Error", "Please enter scores.")
            return

        try:
            scores = [int(score.strip()) for score in scores_text.split(",") if score.strip().isdigit()]
            if not scores:
                raise ValueError("No valid scores entered.")
        except ValueError as e:
            self.messageBox("Error", f"Invalid input: {e}")
            return

        student = Student(name, scores)
        self.students.append(student)
        self.nameField.setText("")
        self.scoreField.setText("")
        self.messageBox("Success", f"Added student: {name}")

    def plotScores(self):
        if not self.students:
            self.messageBox("Error", "No students to plot.")
            return
        
        plt.figure(figsize=(8, 5))
        
        max_tests = max(len(student.scores) for student in self.students)
        
        for student in self.students:
            plt.plot(student.scores, marker='o', label=student.name, linestyle='dashed')

        plt.title("Student Scores")
        plt.xlabel("Test Position")
        plt.ylabel("Score")
        plt.xticks(range(max_tests))  # Ensure proper tick positions
        plt.ylim(0, 100)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    app = StudentApp()
    app.mainloop()
