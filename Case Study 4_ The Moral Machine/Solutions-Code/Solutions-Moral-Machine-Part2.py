#Moral Machine Part 1 Solutions

#an example for what someone's function could look like:
def whoDoesTheCarSave(pedestrian,driver):
    saved = ""
    #my criteria is to check who's fault it was
    #if it was the pedestrian's fault,
    #only save the pedestrian if they are a minor
    #if it was the drivers fault,
    #only save the driver if the pedestrian is over 75
    if pedestrian[3] == "Pedestrian":
        if pedestrian[0] > 18:
            saved = "Driver"
        else:
            saved = "Pedestrian"
    else:
        if pedestrian[0] > 75:
            saved = "Driver"
        else:
            saved = "Pedestrian"
    return saved

    import csv
def messlasMoralMachine(fileName):
    #code here
    #return a list of the people who were saved for each incident
    
    
    #(question to ask: if your input file is 100 rows, how many items should
    #be in your returned list for this function?)
    
    
    myFileHandle = open(fileName,"r")
    csvReaderObject = csv.reader(myFileHandle)
    header = next(csvReaderObject)
    
    saved = []
    
    for row in csvReaderObject:
        cleanedDataPass = [int(row[1]), row[2], row[3], row[4]]
        driver = next(csvReaderObject)
        cleanedDataDriver = [int(driver[1]), driver[2], driver[3], driver[4]]
        currentSave = whoDoesTheCarSave(cleanedDataPass, cleanedDataDriver)
        saved.append(currentSave)
    myFileHandle.close()
    return saved

#you can use this to test your function,
#you can expect your output to look something like this
#but of course it will be specific to your criteria that you chose
messlasMoralMachine("trolley-problem.csv")


def moralMachine(inputFileName, outputFileName):
    #first we need to call our old function to get the list of those who were saved
    saved = messlasMoralMachine(inputFileName)
    #now we can open our output file for writing
    fileOut = open(outputFileName, "w")
    
    #don't forget to write the header:
    fileOut.write("rowNumber,Person,Saved\n")
    
    #we need to loop through all of the rows we expect to write in our csv
    #how can we obtain that?
    totalRows = len(saved) * 2
    #then we will loop through the length of the list of saved people
    for i in range(0,totalRows):
        #we need to write a row to the csv file in this format
        #rowNumber,personSaved
        #let's take a look at how our rows are going to work
        #and how we can access who was saved
        #(show them on the whiteboard)
        safeIndex = i//2
        #now we need to check if we are writing a row for a driver
        #or a row for a pedestrian.. how can we do that?
        #well, we can check to see if the row we are on is even or odd!
        if i %2 == 0:
            person = "Pedestrian"
        else:
            person = "Driver"
        #now we just need to create a string with all of our info for
        #this specific row
        newCSVrow = str(i) + "," + person + "," + saved[safeIndex] + "\n"
        #and write that string to our out file
        fileOut.write(newCSVrow)
    fileOut.close()

#you'll notice that this code
#will produce an extra new line at the end
#of your csv file, don't worry about that for now!

#to test your code, you want to use the following code:
#how can you check to see if your code worked?
#well.. you'll need to check the csv file you've created!
moralMachine("trolley-problem.csv","test-out.csv")