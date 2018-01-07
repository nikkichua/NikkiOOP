class Transaction():
    def __init__(self, cardNo, index, tDate, tTime, desc, amount):
        self.__cardNo = cardNo
        self.__index = index #index is the count(running numbers)
        self.__tDate = tDate
        self.__tTime = tTime
        self.__desc = desc
        self.__amount = amount



    def get_index(self):
        return self.__index
    def get_tDate(self):
        return self.__tDate
    def get_tTime(self):
        return self.__tTime
    def get_desc(self):
        return self.__desc
    def get_amount(self):
        return self.__amount
    def get_cardNo(self):
        return self.__cardNo


    def set_index(self,index):
        self.__index = index
    def set_tDate(self, tDate):
        self.__tDate = tDate
    def set_tTime(self, tTime):
        self.__lastname = tTime
    def set_desc(self, desc):
        self.__desc = desc
    def set_amount(self, amount):
        self.__amount = amount
    def set_cardNo(self, cardNo):
        self.__amount = cardNo


# class Transaction():
#   def __init__(self, index,tDate, tTime, desc,type,cardNum, amount):
#       self.__index = index #index is the count(running numbers)
#       self.__tDate = tDate
#       self.__tTime = tTime
#       self.__desc = desc
#       self.__type = type
#       self.__cardNum = cardNum
#       self.__amount = amount
#
#
#   def get_index(self):
#       return self.__index
#   def get_tDate(self):
#       return self.__tDate
#   def get_tTime(self):
#       return self.__tTime
#   def get_desc(self):
#       return self.__desc
#   def get_type(self):
#       return self.__type
#   def get_cardNum(self):
#       return self.get_cardNum
#   def get_amount(self):
#       return self.__amount
#
#
#
#   def set_index(self,index):
#       self.__index = index
#   def set_tDate(self, tDate):
#       self.__tDate = tDate
#   def set_tTime(self, tTime):
#       self.__lastname = tTime
#   def set_desc(self, desc):
#       self.__desc = desc
#   def set_type(self,type):
#       self.__type=type
#   def set_cardNum(self,cardNum):
#       self.__cardNum=cardNum
#   def set_amount(self, amount):
#       self.__amount = amount