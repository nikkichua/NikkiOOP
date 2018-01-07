class Portfolio():
   def __init__(self,name,nric,gender,address,postal,houseNum,phoneNum,email,salary):
       self.__name=name
       self.__nric=nric
       self.__gender=gender
       self.__address=address
       self.__postal=postal
       self.__houseNum=houseNum
       self.__phoneNum=phoneNum
       self.__email=email
       self.__salary=salary


   def get_name(self):
       return self.__name

   def get_nric(self):
       return self.__nric

   def get_gender(self):
       return self.__gender

   def get_address(self):
       return self.__address

   def get_postal(self):
       return self.__postal

   def get_houseNum(self):
       return self.__houseNum

   def get_phoneNum(self):
       return self.__phoneNum

   def get_email(self):
       return self.__email

   def get_salary(self):
       return self.__salary

   def set_name(self,name):
       self.__name=name

   def set_nric(self,nric):
       self.__nric=nric

   def set_gender(self,gender):
       self.__gender=gender

   def set_address(self,address):
       self.__address=address

   def set_postal(self,postal):
       self.__postal=postal

   def set_houseNum(self,houseNum):
       self.__houseNum=houseNum

   def set_phoneNum(self,phoneNum):
       self.__phoneNum=phoneNum

   def set_email(self,email):
       self.__email=email

   def set_salary(self,salary):
       self.__salary=salary
