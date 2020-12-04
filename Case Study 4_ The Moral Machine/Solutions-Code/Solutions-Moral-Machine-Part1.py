#Moral Machine Part 1 Solutions

#First you need to teach them this:
#we can use the keyword "import" to import
#libraries into our notebook
#a library holds a bunch of information for us
#including functions that we can call that have 
#already been written!
#we've used built-in functions before like len() or print()
#but libraries are different, they aren't built into
#python or Jupyter, so we have to import them
import csv

#we open the csv in the same way
fileHandle = open("example.csv", "r")
#but now we use this special function to open a csv file
#syntax:
#csv.reader(fileHandleName)
csvReaderObject = csv.reader(fileHandle)
#now, instead of calling .readline() to skip
#the header like we did last week,
#instead we are going to use the next() function

#syntax:
#next(csvReaderObject)
thisIsTheHeaderOfTheCSVFile = next(csvReaderObject)
print(thisIsTheHeaderOfTheCSVFile)
#Now we can loop through the actual data in this file
for row in csvReaderObject:
    print(row)
    #see how nicely it puts everything into a list for us?
    #last week we had to use the .split() function
    #remember that you can access different columns in the data too
    column1 = row[0]
    column2 = row[1]
    print("this is a row in the for loop from the csvReaderObject: [" + column1 + " , " + column2 + "]")
#don't forget to close your csv
fileObject.close()

#option using csv reader
myFileHandle = open("trolley-problem.csv","r")
csvReaderObject = csv.reader(myFileHandle)
header = next(csvReaderObject)
print(header)
for row in csvReaderObject:
    print(row)
myFileHandle.close()

#option using what we learned last week .read() .splitlines() and .split()
myFileHandle = open("trolley-problem.csv","r")
#remember that this returns a sting
content = myFileHandle.read()
#rememer that this returns a list
lines = content.splitlines()
#this is the header
print(lines[0])
for line in lines:
    ls = line.split(",")
    print(ls)
myFileHandle.close()

#option using what we learned last week .readline() and .split()
myFileHandle = open("trolley-problem.csv","r")
header = myFileHandle.readline()
print(header)
for line in myFileHandle:
    print(line.split())
myFileHandle.close()

def parseAndClean(fileName):
    #your code here
    #return listOfLists
    #hint: It will be easier if you start with an empty listOfLists and use the .append() function!
    myFileHandle = open("trolley-problem.csv","r")
    csvReaderObject = csv.reader(myFileHandle)
    header = next(csvReaderObject)
    listOfLists = []
    for row in csvReaderObject:
        cleanedData = [int(row[0]), int(row[1]), row[2], row[3], row[4]]
        listOfLists.append(cleanedData)
    myFileHandle.close()
    return listOfLists

parseAndClean("trolley-problem.csv")

#this is an example of some criteria someone could have chosen,
#the students will all come up with their own personal criteria
def whoDoesTheCarSave(pedestrian,driver):
    saved = ""
    if pedestrian[0] < driver[0] and driver[0] < 60 and pedestrian[0] > 18:
        saved = "Pedestrian"
    elif pedestrian[0] < 18:
        saved = "Pedestrian"
    elif driver[0] > 60:
        saved = "Driver"
    elif driver[1] == "Female":
        saved = "Driver"
    elif pedestrian[2] is not "USA":
        saved = "Pedestrian"
    elif driver[2] is not "USA":
        saved = "Driver"
    elif pedestrian[3] == "Pedestrian" or driver[3] == "Pedestrian":
        saved = "Driver"
    elif pedestrian[3] == "Driver" or driver[3] == "Driver":
        saved = "Pedestrian"
    return saved

#test your function with the following code to make sure it produces the outcome you expect!
ped = [25,"Female","USA","Pedestrian"]
driv = [75, "Male","USA","Pedestrian"]
whoDoesTheCarSave(ped,driv)