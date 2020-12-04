##Sentiment Decider Solutions

#TASK #1:
#STEP 1
def totalReviewSentiment(positiveWordsFile, negativeWordsFile, reviewsFile):
    
    #Create the dictionaries to store the positive and negative words
    #open the positive words file
    #go through all the positive words--> come up with a list of all of the positive words
    #where each item in the list is one of the positive words
    posFileHandler = open(positiveWordsFile,"r")
    posContent = posFileHandler.read() #remember this returns a string of all the content in the file
    posWordsList = posContent.splitlines() #splitlines returns a list where each item is a line in the file
    
    
    #open the negative words file
    #go through all the negative words
    negFileHandler = open(negativeWordsFile,"r")
    negContent = negFileHandler.read() #remember this returns a string of all the content in the file
    negWordsList = negContent.splitlines() #splitlines returns a list where each item is a line in the file
    
    
    #create an empty dictionary like we would do with an empty list
    posWordsDict = {}
    negWordsDict = {}
    
    
    #put those words into a positive word dictionary
    for word in posWordsList:
        posWordsDict[word] = 0
    #put those words into a negative word dictionary
    for word in negWordsList:
        negWordsDict[word] = 0
    
    
    ####################################################################################
    
    
    # Open and read the review file
    #Get all of the words from this file into a list
    reviewsFileHandler = open(reviewsFile,"r")
    reviewString = reviewsFileHandler.read()
    reviewWordList = reviewString.split()
    
    
    # Parse all of the words in the file
        #for every single word we encounter
        #we want to check if that word exists in the positive or negative dictionary
        #if it exists in the positive dictionary, then update that specific
        #word's "count"
        #if it exists in the negative dictionary, then update that specific word's "count"
    for word in reviewWordList:
        if word in posWordsDict:
            posWordsDict[word] += 1
        if word in negWordsDict:
            negWordsDict[word] += 1
    
    
    ####################################################################################
    
    
    # Count how many positive and negative words you've encountered
    
    #variables to store the total positive and total negative number of words we've encountered
    totalPosWords = 0
    totalNegWords = 0
    
    # Loop through the positive dictionary
    for key in posWordsDict:
        numTimesThisWordUsed = posWordsDict[key]
        # Count how many total words were used
        totalPosWords += numTimesThisWordUsed
    print("total times a positive word was used in all of our reviews: " + str(totalPosWords))
        
    # Loop through the negative dictionary
    for key in negWordsDict:
        numTimesThisWordUsed = negWordsDict[key]
        # Count how many total words were used
        totalNegWords += numTimesThisWordUsed
    print("total times a negative word was used in all of our reviews: " + str(totalNegWords))
    
    
    # Return a string that lets us know if the majority of the reviews were positive or negative. 
    if totalPosWords > totalNegWords:
        # If there are more positive reviews, return "The Reviews are Mostly Positive". 
        return "The Reviews are Mostly Positive"
    #If there are more negative reviews, return "The Reviews are Mostly Negative".
    else:
        return "The Reviews are Mostly Negative"
    

#After functional decomposition:

totalReviewSentiment("positivewords.txt","negativewords.txt","reviews.txt")

totalReviewSentiment("positivewords.txt","negativewords.txt","reviews.txt")

def getEmptyPosDictionary(posWords):
    #2. Create the dictionaries with their default values
    posWordsDict = {}
    for word in posWords:
        if word not in posWordsDict:
            posWordsDict[word] = 0
    return posWordsDict

def getEmptyNegDictionary(negWords):
    negWordsDict = {}
    for word in negWords:
        if word not in negWordsDict:
            negWordsDict[word] = 0
            
    return negWordsDict

def countWords(reviewsFile,posWordsDict,negWordsDict):
    #3. Open the reviews + keep track of the pos/neg word counts in each dictionary
    reviewsFileHandler = open(reviewsFile, "r")
    allReviews = reviewsFileHandler.read()
    allWords = allReviews.split()
    for word in allWords:
        if word in posWordsDict:
            posWordsDict[word] += 1
        elif word in negWordsDict:
            negWordsDict[word] += 1
    return[posWordsDict,negWordsDict]


def getPosNegCount(posWordsDict,negWordsDict):
    #4. Calculate the final pos/neg word counts and return
    totalPosWords = 0
    totalNegWords = 0
    for posWord in posWordsDict:
        numTimesPosWordUsed = posWordsDict[posWord]
        if numTimesPosWordUsed > 0:
            totalPosWords += numTimesPosWordUsed
    for negWord in negWordsDict:
        numTimesNegWordUsed = negWordsDict[negWord]
        if numTimesNegWordUsed > 0:
            totalNegWords += numTimesNegWordUsed
    return[totalPosWords,totalNegWords]

# You can also take this a step further and put each function in its own cell!
#Just make sure that any function that is called is defined *ABOVE* (before) where it is called
def totalReviewSentiment(positiveWordsFile, negativeWordsFile, reviewsFile):
    #1. Open the files and get the words in a list
    posFileHandler = open(positiveWordsFile,"r")
    posContent = posFileHandler.read()
    posWords = posContent.splitlines()
    
    negFileHandler = open(negativeWordsFile,"r")
    negContent = negFileHandler.read()
    negWords = negContent.splitlines()
    
    #2. Create the dictionaries with their default values
    posWordsDict = getEmptyPosDictionary(posWords)
    negWordsDict = getEmptyNegDictionary(negWords)
    
    #3. Open the reviews + keep track of the pos/neg word counts in each dictionary
    [posWordsDict,negWordsDict] = countWords(reviewsFile,posWordsDict,negWordsDict)
    
    #4. Calculate the final pos/neg word counts and return
    [totalPosWords,totalNegWords] = getPosNegCount(posWordsDict,negWordsDict)
    
    print("Total positive words used: " + str(totalPosWords))
    print("Total negative words used: " + str(totalNegWords))
    
    if totalPosWords > totalNegWords:
        return("The Reviews Are Mostly Positive")
    else:
        return("The Reviews Are Mostly Negative")
    

#STEP 2
def reviewSentiment(review,posWordsDict,negWordsDict):
    #your code here
    
    posWords = 0
    negWords = 0
    
    #get all the words from the review
    reviewWordsList = review.split()
    
    #loop through the words from the review
    for word in reviewWordsList:
        #1. is the word positive or negative?
        if word in posWordsDict:
            #do something
            posWords += 1
        #2. count how many positive and negative words we are encountering
        if word in negWordsDict:
            #do something
            negWords += 1
        
    #calculate the positive sentiment / negative sentiment of the review
        #hint: you only need to calculate the positive sentiment ratio and check if it is
        #above or below 0.5 to know the answer this
    #3. how do we calculate the positive sentiment ratio?
        positiveSentiment = posWords / (posWords + negWords)
    
    4. return a string that says whether this review is more positive or negative
    print(positiveSentiment)
    if positiveSentiment > 0.5:
        print("This review has a positive sentiment")
    elif positiveSentiment < 0.5:
        print("This review has a negative sentiment")
    else:
        print("This review was entirely neutral")

#Test the function using code that we already wrote:
posFileHandler = open("positivewords.txt","r")
posContent = posFileHandler.read()
posWords = posContent.splitlines()

negFileHandler = open("negativewords.txt","r")
negContent = negFileHandler.read()
negWords = negContent.splitlines()

posWordsDict = getEmptyPosDictionary(posWords)
negWordsDict = getEmptyNegDictionary(negWords)

#our testing code here

#example test cases
review = "I really enjoyed this product!!!"
reviewSentiment(review,posWordsDict,negWordsDict)

review = "I really hated this product!!!"
reviewSentiment(review,posWordsDict,negWordsDict)

review = "I really hated and loved this product but ultimately it was okay!!!"
reviewSentiment(review,posWordsDict,negWordsDict)


#TASK #2:
#example answers:
#these are some examples... there are many more examples the students can come up with!
review = "This product was an a+ accurately depicted amazing disaster"
reviewSentiment(review,posWordsDict,negWordsDict)

review = "I'm baffled at how freaking goofy the film was"
reviewSentiment(review,posWordsDict,negWordsDict)

#TASK #3:

def getReviewSentiment(review,posWordsDict,negWordsDict):
    #your code here
    
    posWords = 0
    negWords = 0
    
    #get all the words from the review
    reviewWordsList = review.split()
    
    #loop through the words from the review
    for word in reviewWordsList:
        #1. is the word positive or negative?
        if word in posWordsDict:
            #do something
            posWords += 1
        #2. count how many positive and negative words we are encountering
        if word in negWordsDict:
            #do something
            negWords += 1
        
    #calculate the positive sentiment / negative sentiment of the review
        #hint: you only need to calculate the positive sentiment ratio and check if it is
        #above or below 0.5 to know the answer this
    #3. how do we calculate the positive sentiment ratio?
    if posWords > 0 and negWords > 0:
        positiveSentiment = posWords / (posWords + negWords)
    else:
        return 0.5
    return positiveSentiment

#FIX THE FOLLOWING FUNCTION:
def sentimentForAllReviews(positiveWordsFile, negativeWordsFile, reviewsFile):
    posFileHandler = open(positiveWordsFile,"r")
    posContent = posFileHandler.read()
    posWords = posContent.splitlines()
    
    negFileHandler = open(negativeWordsFile,"r")
    negContent = negFileHandler.read()
    negWords = negContent.splitlines()
    
    #Create the dictionaries with their default values
    posWordsDict = getEmptyPosDictionary(posWords)
    negWordsDict = getEmptyNegDictionary(negWords)
    
    
    #FIND THE ERRORS BELOW!
    #Hint: There are 3 errors :-)
    
    #1. Change the open mode to "r" instead of "a" - then explain what "a" means
    reviewFileHandler = open(reviewsFile,"r")
    #2. Make sure you get your string of the entire file using the .read() functin
    #before you call the spitlines() function on the contents of the file
    reviewString = reviewFileHandler.read()
    allReviewList = reviewString.splitlines()
    
    sentimentList = []
    
    for review in allReviewList:
        #call the function we wrote!
        sentiment = getReviewSentiment(review,posWordsDict,negWordsDict)
        #Use the .append() function to add an item to a list, not the += operator
        sentimentList.append(sentiment)
        
        
    #END OF ERRORS
        
    #get the average sentiment of all the reviews
    totalSentiment = 0
    for sentiment in sentimentList:
        totalSentiment += sentiment
    averageSentiment = totalSentiment/len(sentimentList)
    
    return averageSentiment
    
#This is the output that we want to see!
averageSentiment = sentimentForAllReviews("positivewords.txt","negativewords.txt","reviews.txt")
print("The average sentiment of all of the reviews is: " + str(averageSentiment))