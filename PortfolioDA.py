from Portfolio import Portfolio

def processPortfolio():
       portfolioList=[]
       portfoilo_file = open('files/Portfolio.txt', 'r')
       for i in portfoilo_file:
           list1=i.split(',')
           a=Portfolio(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],
                       list1[6],list1[7],float(list1[8]))
           portfolioList.append(a)


       return portfolioList

