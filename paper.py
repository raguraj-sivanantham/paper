import string

#to check if year is a leap year or not
#if year is leap, it will return True else False
def isLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return(True)
            else:
                return(False)
        else:
            return(True)
    else:
        return(False)
#--------------------------------------------------
#Get Year From User
year=int(input("Enter Year : "))
while year != 0:
    #open file
    currentFile=str(year)+".txt"
    fileObj=open(currentFile,"a")
    leapOrNot=isLeap(year)
    #Define Months and Days
    #Date Format  : MM/DD/YYYY
    months=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    if leapOrNot==True:
        days=[31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        days=[31,28,31,30,31,30,31,31,30,31,30,31]

    #Check Months
    for i in range(12):
        temp=input("Enter Missed Dates For Month "+months[i]+" : ")
        tempList=temp.split(",")
        #write in to the file
        for j in range(days[i]):
            if (str(j+1)) not in tempList:
                #print((i+1),"/",(j+1),year,file=fileObj)  
                fileObj.write(str(i+1)+"/"+str(j+1)+"/"+str(year)+"\n") 
        #check other missed dates
        #if no missed dates hit just enter
        current=input("Any missed dates in other months ? ")
        if current !="":
            #loop will work while it gets input as "end"
            currentDate=input("Enter date in DD/MM/YYYY format ")
            while(currentDate != ""):
                currentDate=(currentDate.split("/"))
                tempVar=currentDate[1]+"/"+currentDate[0]+"/"+currentDate[2]
                tempVar=tempVar.translate({ord(c): None for c in string.whitespace})
                fileObj.write(tempVar+"\n")
                currentDate=input("Enter date in DD/MM/YYYY format ")
                currentDate=currentDate.upper()
        print("***************************************")
    print("Year : ",year," Finished")
    print("============================================================")
    fileObj.close()
    year=input("another year? Enter Year : ")
    if year=="":
        year=0
    else:
        year=int(year)
print("Finished !")
