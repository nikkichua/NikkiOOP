from Transaction import Transaction
from datetime import datetime


# def retrieveTransList():
#     transList = []
#     count = 1
#     trans_file = open('files/transactionhistory.txt', 'r')
#     for a in trans_file:
#         list = a.split(',')
#         s = Transaction(count, list[0], list[1], list[2], list[3], list[4], float(list[5]))
#         transList.append(s)
#         count += 1
#     print(list[4])
#     return transList
def retrieveTransList():
    transList = []
    count=1
    trans_file = open('files/transactionhistory.txt', 'r')
    for tlist in trans_file:
        list = tlist.split(',')
        s = Transaction(list[0], count, list[1], list[2], list[3], float(list[4]))

        count+=1
        transList.append(s)
    return transList

# def cardNo():
#     cards = retrieveTransList()
#     cardnumber = Transaction(list[0])
#
#     print(cardnumber)
#     return cardNo()

def calcTotalAmountByMonth(month):
    transList = retrieveTransList()
    totalAmt = 0.0

    for obj in transList:
        dt_obj = datetime.strptime(obj.get_tDate(), '%d/%m/%Y')
        if dt_obj.month == month:
            totalAmt = totalAmt + float(obj.get_amount())


    return totalAmt


def filterTransByMonth(month):
    transList = retrieveTransList()
    filteredList = []
    count=1

    for obj in transList:
        dt_obj = datetime.strptime(obj.get_tDate(), '%d/%m/%Y')
        if dt_obj.month == month:
            obj.set_index(count)
            filteredList.append(obj)
            count+=1

    return filteredList



def filterTransByDateRange(start, end):
    transList = retrieveTransList()
    filteredList = []
    startDt_obj = datetime.strptime(start, '%d/%m/%Y')
    endDt_obj = datetime.strptime(end, '%d/%m/%Y')
    #converting date from string to date
    count=1

    for obj in transList:
        dt_obj = datetime.strptime(obj.get_tDate(), '%d/%m/%Y')
        if dt_obj>=startDt_obj and dt_obj<=endDt_obj: #the range of the dates
            obj.set_index(count)
            filteredList.append(obj)
            #print(obj.get_desc())
            count+=1
    return filteredList


def calcTotalAmountByDate(start,end):
    transList = retrieveTransList()
    totalAmt = 0.0
    startDt_obj = datetime.strptime(start, '%d/%m/%Y')
    endDt_obj = datetime.strptime(end, '%d/%m/%Y')
    #converting date from string to date
    count=1

    for obj in transList:
        dt_obj = datetime.strptime(obj.get_tDate(), '%d/%m/%Y')
        if dt_obj>=startDt_obj and dt_obj<=endDt_obj: #the range of the dates
            obj.set_index(count)
            totalAmt = totalAmt + float(obj.get_amount())
            #print(obj.get_desc())
            count+=1


    return totalAmt

def cardno():
    transList = retrieveTransList()
    for obj in transList:
        card = obj.get_cardNo()

    #print(card)
    return card