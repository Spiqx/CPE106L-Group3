
#CPE106L-B3 - GROUP 3
#LABORATORY 2 (POST-LAB PROBLEM)

#2. Filename: LR2_2.py
#Write a program that allows the user to navigate the lines of text in a file. The program
#should prompt the user for a filename and input the lines of text into a list. The program
#then enters a loop in which it prints the number of lines in the file and prompts the user
#for a line number. Actual line numbers range from 1 to the number of lines in the file. If
#the input is 0, the program quits. Otherwise, the program prints the line associated with
#that number.

inputfile = input("Enter the input file name in the space provided: ")

file = open(inputfile, 'r')
linecount = 0

for line in file:
    linecount = linecount + 1

print("The file has",linecount,"lines.")
while True:
    linenum = 0
    num = int(input("Enter a line number or enter 0 to exit the program: "))
    if num >=1 and num <= linecount:
        file = open(inputfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(num,":",lines)
    elif num == 0:
        break
    else:
        if num!= linecount:
            print("ERROR: line number must be less than",linecount)
