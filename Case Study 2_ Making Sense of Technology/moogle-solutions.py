#You can use this list later to test your code
#this list represents example profiles of people
#who are applying for this job!
#The scores in each list represent:
# 0.Intro to CS: 100
# 1.Data Structures: 95
# 2.Software Engineering: 80
# 3.Algorithms: 89
# 4.Computer Organization: 91 
# 5.Operative Systems: 75
# 6.Overall GPA: 83
applicant_list = [[93, 89, 63, 88, 60, 73, 80], 
                [100, 63, 57, 96, 58, 71, 78], 
                [81, 91, 99, 78, 57, 87, 86], 
                [81, 73, 100, 57, 91, 60, 66], 
                [86, 89, 64, 81, 69, 93, 92], 
                [78, 63, 88, 95, 59, 98, 90], 
                [55, 74, 68, 55, 69, 94, 80], 
                [64, 77, 75, 92, 77, 72, 83], 
                [95, 58, 92, 62, 77, 64, 59], 
                [94, 78, 84, 83, 68, 63, 76]]
test_applicant = [78, 63, 88, 95, 90, 98, 90]
test_applicant_two = [78, 66, 88, 95, 90, 98, 68]

#defining the function
#defining the function does NOT "run" or "test" your function
def analyzeApplicant1(applicant):
    """
    Given the GPAs of a single applicant, return True if they are qualified
    Qualification: An applicant is qualified if...
        - their Overall College GPA is above 80

    @param applicant: a list of GPAs (integers)
    @return True if the applicant qualifies
    """
    
    #create a variable that represents the overall college gpa for this specific applicant
    overallGPA = applicant[6]
    #check to see if the overall college gpa is above 80
    #if it is, return True
    #if it is not, return False
    if overallGPA > 80:
        return True
    else:
        return False


#in order to "use" or "test" your function
#you must CALL it like so:
#functionName(value(s) you want to pass in)
analyzeApplicant1(test_applicant_two)


# test_applicant_two = [78, 63, 88, 95, 90, 98, 40]
#function definition - this does not do anything by itself
def analyzeApplicant2(applicant):
    """
    Given the GPAs of a single applicant, return True if they are qualified
    Qualification: An applicant is qualified if...
        - they have no grade below a 65

    @param applicant: a list of GPAs (integers)
    @return True if the applicant qualifies
    """
    #loop through all of the gpas of the applicant
    for gpa in applicant:
        #if grade is below 65:
        if (gpa < 65):
            #they are not qualified
            #Return False
            return False
    
    #return true
    #WHENEVER A PYTHON FUNCTION RETURNS ANYTHING
    #IT WILL RETURN THAT VALUE AND IMMEDIATELY EXIT
    #THE FUNCTION, SO NO MORE CODE AFTER THAT RETURN STATEMENT
    #WILL BE RUN.
    return True


test_problematic_applicant = [-1, 95, 99, 94, 96, 98, 95]
print(analyzeApplicant2(test_problematic_applicant))

#testing the function
analyzeApplicant2(test_applicant)

#testing the function
analyzeApplicant2(test_applicant_two)

def analyzeApplicant3(applicant):
    """
    Given the GPAs of a single applicant, return True if they are qualified
    Qualification: An applicant is qualified if...
        - they have at least 4 grades above 85

    @param applicant: a list of GPAs (integers)
    @return True if the applicant qualifies
    """

#Use this cell to test your function!
analyzeApplicant3(test_applicant)

def analyzeApplicant4(applicant):
    """
    Given the GPAs of a single applicant, return True if they are qualified
    Qualification: An applicant is qualified if...
        - the average GPA of their CS courses (all but Overall) is above 85

    @param applicant: a list of GPAs (integers)
    @return True if the applicant qualifies
    """
    #average of a list of numbers is:
    #sum of the numbers / amount of numbers
    #create a sum variable
    
    #loop through all of the gpas (but not the overall)
        #update the sum variable
    
    #create a variable for the amount of gpas
    #calculate the average
    
    #if average is above 85 --> return True
    #else (average is below or equal to 85) --> return False

    # do pseudo code with them and then have them write the code in their groups
def analyzeApplicant4(applicant):
    """
    Given the GPAs of a single applicant, return True if they are qualified
    Qualification: An applicant is qualified if...
        - the average GPA of their CS courses (all but Overall) is above 85

    @param applicant: a list of GPAs (integers)
    @return True if the applicant qualifies
    """
    #create a sum variable
    totalSum = 0
    #loop through all of the gpas but not the overall gpa
    for i in range(0,6):
        #add to totalSum variable
        totalSum += applicant[i]
    #calculate the average variable
    average = totalSum/6
    #if the average is over 85 return true otherwise return false
    if average > 85:
        return True
    else:
        return False


#Use this cell to test your function!
analyzeApplicant4(test_applicant)

#I have written code to help you test out all of your functions!
#This function will create a list of the top applicants and return it!
#It's up to you to choose which of the analyzeApplicant functions will
#be the chosen function that Moogle will implement into its official
#hiring system. Right now, it has defaulted to the function: AnalyzeApplicant1
def getBestApplicants(appList):
    """
    Given applicant data, return the most qualified applications

    @param app_list: a 2D list containing lists of application data
    @return a 2D list of the best applications
    """
    finalists = []

    for applicant in appList:
    # choose which of these functions you would like
    # to make the final decision for you!
    # Right now this function is defaulting to use the:
    # analyzeApplicant1 function
        if analyzeApplicant1(applicant) == True:
            finalists.append(applicant)

    return finalists

#Call your function to get the return value
#Pass in the parameter applicant_list that we created at the beginning
#set this return value equal to a variable called "finalists"
finalists = getBestApplicants(applicant_list)

#I have written this code for you!
#Simply run this cell and if everything was done correctly,
#You'll get the finalists for the job at Moogle!
print('')
print("-------------------------")
print()
print("The finalists are...")
for finalist in finalists:
    print(finalist)
print("Your algorithm kept", round(len(finalists)/len(applicant_list)*100), "percent of applicants")