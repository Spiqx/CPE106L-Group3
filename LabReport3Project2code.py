import random

class Student(object):
  
   def __init__(self, name, number):
       self.name = name
       self.scores = []
       for count in range(number):
           self.scores.append(0)
                  
   def getName(self):
       return self.name
      
   def setScore(self, i, score):
       self.scores[i - 1] = score
      
   def getScore(self, i):
       return self.scores[i - 1]
      
   def getAverage(self):
       return sum(self.scores) / len(self.scores)
      
   def getHighScore(self):
       return max(self.scores)
      
   def compareEqual(self,other):
       compareS=self.name.lower()
       compareO = other.name.lower()
       if compareS==compareO:
           return "True"
       else:
           return "False"
   def compareLess(self,other):
       compareS=self.name.lower()
       compareO = other.name.lower()
       if compareS <= compareO:
           return "True"
       else:
           return "False"     
   def __gt__(self,other):
      compareS=self.name.lower()
      compareO = other.name.lower()
      if compareS >= compareO:
          return "True"
      else:
          return "False"             
   def __str__(self):
       return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))      
      
def main():
	
	studentList = []

	student1 = Student("JL", 5)
	for i in range(1, 6):
		student1.setScore(i, 15)
	studentList.append(student1)

	student2 = Student("Mark", 5)
	for i in range(1, 6):
		student2.setScore(i, 20)
	studentList.append(student2)

	student3 = Student("Juancho", 5)
	for i in range(1, 6):
		student2.setScore(i, 30)
	studentList.append(student3)


	random.shuffle(studentList)

	print("STUDENTS SHUFFLED LIST: ")
	for i in studentList:
		print(i.__str__())

	studentList.sort(key=lambda x: x.scores)

	print("\nSTUDENTS BY SCORE: ")
	for i in studentList:
		print(i.__str__())

	studentList.sort(key=lambda x: x.name)

	print("\nSTUDENTS BY NAME: ")
	for i in studentList:
		print(i.__str__())

if __name__ == "__main__":
		main()
