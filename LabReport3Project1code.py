class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __equal__(self,student): 
        return self.name==student.name
    def __less__(self,student): 
        return self.name<student.name
    def __greater__(self,student):
        return self.name>=student.name
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    print("Student 1 - ")
    student1 = Student("Charlz", 5)
    for i in range(1, 6):
        student1.setScore(i, 92) 
    print(student1)

    print('Student 2 - ')
    student2=Student('Mark',5)
    for i in range(1, 6):
        student2.setScore(i, 88) 
    print(student2)

    print("\nMethods: ")
    print("\nEqual Method") 
    print(student1.__equal__(student2))

    print("\nGreater Than or Equal To Method")
    print(student1.__greater__(student2))

    print("\nLess Than Method")
    print(student1.__less__(student2))
    
    

if __name__ == "__main__":
    main()
