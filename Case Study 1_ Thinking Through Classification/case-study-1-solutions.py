#Solutions for Case Study 1: Thinking Through Classification

def recommitCrimeOrNot(age, occupation, previousCrimes, familyCrimes):
    if age%3 == 0:
        print("This person will re-commit a crime")
    elif occupation == "unemployed":
        print("This person will re-commit a crime")
    elif previousCrimes > 1:
        print("This person will re-commit a crime")
    elif familyCrimes > 3:
        print("This person will re-commit a crime")
    else:
        print("This person will not re-commit a crime")

#test the code
recommitCrimeOrNot(30, "employed",0,2)
#expected answer: This person will re-commit a crime
recommitCrimeOrNot(31, "employed",0,2)
#expected answer: This person will not re-commit a crime
recommitCrimeOrNot(31, "unemployed",0,0)
#expected answer: This person will re-commit a crime
recommitCrimeOrNot(31, "employed",2,0)
#expected answer: This person will re-commit a crime
recommitCrimeOrNot(31, "employed",0,4)
#expected answer: This person will re-commit a crime
recommitCrimeOrNot(31, "employed",1,3)
#expected answer: This person will not re-commit a crime
recommitCrimeOrNot(63, "employed",1,3)
#expected answer: This person will re-commit a crime

def numberOfFakeNews(listOfHeadlines):
    fakeNews = 0
    for headline in listOfHeadlines:
        if "Fake" in headline:
            fakeNews += 1
        elif "Shocking" in headline:
            fakeNews += 1
        elif "Revealed" in headline:
            fakeNews += 1
        elif "Unprecedented" in headline:
            fakeNews += 1
    return fakeNews

#test the code
listOfHeadlines = ["You Won't Believe These 10 Secrets About The President!",
                   "Coronavirus Update From The CDC",
                   "A Shocking Announcement From The Kardashians Has Us Screaming!",
                   "Facebook Fighting Fake News",
                   "New Footage From The SpaceX Launch",
                   "New COVID-19 Vaccine Revealed"]
print(numberOfFakeNews(listOfHeadlines))
#expected answer: 3

listOfHeadlines = ["Fake News Headline", "Real News", "Unprecedented Debate From Candidates"]
numberOfFakeNews(listOfHeadlines)
#expected answer: 2

listOfHeadlines = ["Shocking Unbelievable Information", "Fake Shocking Unprecendented News Revealed", "COVID-19 Data"]
numberOfFakeNews(listOfHeadlines)
#expected answer: 2

listOfHeadlines = ["Real News", "CDC Information"]
numberOfFakeNews(listOfHeadlines)
#expected answer: 0

