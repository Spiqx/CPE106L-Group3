
#CPE106L-B3 - GROUP 3
#LABORATORY 2 (POST-LAB)


#1. Filename: stats.py
#A group of statisticians at a local college has asked you to create a set 
#of functions that compute the median and mode of a set of numbers, as defined in the below sample programs: 
#· mode.py 
#· median.py
#Define these functions in a module named stats.py. 
#Also include a function named mean, which computes the average of a set 
#of numbers. Each function should expect a list of numbers as an argument 
#and return a single number. Each function should return 0 if the list is empty. 
#Include a main function that tests the three statistical functions with a given list

def GetMode(listNum):
    
    if len(listNum) == 0:
        return 0
    else:
        freqNum = {}
        for num in listNum:
            hold = freqNum.get(num, None)
            if hold == None:
                freqNum[num] = 1
            else:
                freqNum[num] = hold + 1
        highestFreq = max(freqNum.values())
        for highFreqNum in freqNum:
            if freqNum[highFreqNum] == highestFreq:
                return highFreqNum

def GetMedian(listNum):
    if len(listNum) == 0:
        return 0
    else:
        listNum.sort()
        midpoint = len(listNum) // 2
        if len(listNum) % 2 == 1: 
            return listNum[midpoint]
        else:
            return (listNum[midpoint] + listNum[midpoint-1]) / 2

def GetMean(listNum):
    if len(listNum) == 0:
        return 0
    else:
        sum = 0
        for i in listNum:
            sum += i
        return sum/len(listNum)

def main():
    print("Enter numbers then input a letter when finished")
    try:
        listNum = []
        while True:
            listNum.append(int(input()))
    except:
        print("The listed number is as follows: ")
        if len(listNum) == 0:
            print("0 or EMPTY")
        else:
            for y in listNum:
                print(y)

    print("\n")
    mode = GetMode(listNum)
    median = GetMedian(listNum)
    mean = GetMean(listNum)
    print("The Mode is: " + str(mode))
    print("The Median is: " + str(median))
    print("The Mean is: " + str(mean))

main()
