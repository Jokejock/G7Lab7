"""
File: student.py
Resources to manage a student's name and test scores.
"""

import numpy as np  # For mean, median, and std
import random       # For randomizing scores
from statistics import mode  # For mode calculation

class Student:
    """Represents a student with scores."""

    def __init__(self, name, number):
        """Initialize student with a name and a given number of scores set to 0."""
        self.name = name
        self.scores = [0] * number  # Creates a list of zeroes

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Resets the ith score (1-based index)."""
        if 1 <= i <= len(self.scores):
            self.scores[i - 1] = score
        else:
            raise IndexError("Score index out of range.")

    def getScore(self, i):
        """Returns the ith score (1-based index)."""
        if 1 <= i <= len(self.scores):
            return self.scores[i - 1]
        else:
            raise IndexError("Score index out of range.")

    def getAverageScore(self):
        """Returns the average score, handling empty lists."""
        return sum(self.scores) / len(self.scores) if self.scores else 0.0

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores) if self.scores else 0.0

    def randomizeScores(self, size, lower, upper):
        """Generates a list of random scores in a given range."""
        self.scores = [random.randint(lower, upper) for _ in range(size)]

    def getMean(self):
        """Returns the mean of scores."""
        return np.mean(self.scores) if self.scores else 0.0

    def getMedian(self):
        """Returns the median of scores."""
        return np.median(self.scores) if self.scores else 0.0

    def getMode(self):
        """Returns the mode of scores, handling cases where no mode exists."""
        try:
            return mode(self.scores)
        except:
            return "No unique mode"

    def getStd(self):
        """Returns the standard deviation of scores."""
        return np.std(self.scores, ddof=1) if len(self.scores) > 1 else 0.0

    def addScore(self, score):
        """Adds a new score to the list."""
        self.scores.append(score)

    def deleteScore(self, i):
        """Deletes the ith score (1-based index)."""
        if 1 <= i <= len(self.scores):
            del self.scores[i - 1]
        else:
            raise IndexError("Score index out of range.")

    def __str__(self):
        """Returns the string representation of the student."""
        result = f"Student: {self.name}\nPosition Score\n"
        for i, score in enumerate(self.scores, start=1):
            result += f"{i:4d}      {score:3d}\n"
        return result

# Simple test
def main():
    student = Student("Ken", 10)
    student.randomizeScores(10, 75, 100)
    print(student)
    print("Mean:", student.getMean())
    print("Median:", student.getMedian())
    print("Mode:", student.getMode())
    print("Standard Deviation:", student.getStd())

if __name__ == "__main__":
    main()
