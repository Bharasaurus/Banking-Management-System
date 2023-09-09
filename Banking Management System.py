
#======================================================#
                        # BANKING MANAGEMENT SYSTEM #
#======================================================#

import mysql.connector as CON                     #Initiating MySQL and Python Connection                
import matplotlib.pyplot as PLY                        #Schematic Representation                   
import random                                                    #Importing Random Module
from datetime import date                              #Importing Date Time Module
import os                                                              #Importing Exiting Module

Data_base = CON.connect( host='localhost', user='root', passwd='GingerN175')                   #SQL establishment
Cursor = Data_base.cursor()
Cursor = Data_base.cursor(buffered = True)
Cursor.execute("Use test")
print("======================================================")
print("l\t\tBANKING MANAGEMENT SYSTEM\t                         l")
print("======================================================")


class Details:
     
     def __init__(self):                #Login System with Client_ID and Client_Password

          self.ID = Initial_ID
          self.Pass = input("\nEnter Password : ")
          Cursor.execute("Use test")
          Cursor.execute("Select Client_Password from Bank_System where Client_ID="+self.ID)
          for variable in Cursor:
              self.Code =  ''.join(variable)
          if self.Pass == self.Code:
               print("\n")
               Cursor.execute("Select Client_Name from bank_system where CLient_ID = "+str(Initial_ID))
               for variable in Cursor:
                    Name =  ''.join(variable)
               print("\n======================================================")
               print("\t\tWelcome to the Bank", Name, "                     ")
               print("======================================================\n")
          elif self.Pass != self.Code:
               for i in range(0,5):                                                                                                  #Wrong Input
                    print("\nTry Again")
                    self.Pass = input("\nEnter Password : ")
                    if self.Pass == self.Code :
                         break
                         Cursor.execute("Select Client_Name from bank_system where CLient_ID = "+str(Initial_ID))
                         for variable in Cursor:
                              Name =  ''.join(variable)
                         print("\n======================================================")
                         print("\t\tWelcome to the Bank", Name, "                     ")
                         print("======================================================\n")
                    else:
                         continue
                         print("\n======================================================")
                         print("l\t\tThank You and Have a Nice Day !!!!!\t   l")
                         print("======================================================\n")
                         os._exit(0)

          if len(Initial_ID)<8 or len(Initial_ID)>8:

               for i in range(0,100):
                    self.Try = print("\nTry Again")
                    self.Final_ID = input("\nEnter ID (08 Digit Code) : ")
                    self.Pass2 = input("\nEnter Password : ")

                    if len(self.Final_ID) == 8:                                                                                                          
                         break
                    else:
                         self.Final_ID1 = input("\nEnter ID (08 Digit Code) : ")
                         self.Pass3 = input("\nEnter Password : ")
                         continue


Info_Obj = Details                 #Object of Details


class Client_Errors:

     def Space_Error(Input):

          Test = Input
          if Test  == (""):
               for i in range(0,100):                                                                                                  #Wrong Input
                    print("\nTry Again")
                    Initial_Input = input("\nEnter Required Information : ")
                    if Initial_Input != ("") :
                         break
                    else:
                         continue
                    Input = Test
                    break

class Process_SQL:

     def __init__(self, Client_ID, Client_Name, Client_Password):                                                                           #Registering Account 1
          
          Client_Info_Bank_System = ("Insert into Bank_System (Client_ID, Client_Name, Client_Password) values(%s, %s,%s)")
          Client_Values = (Client_ID, Client_Name, Client_Password)
          Cursor.execute(Client_Info_Bank_System, Client_Values)
          Data_base.commit()
          print("\nRegisteration Successfully Completed")

     def Client(Client_ID, Client_FName, Client_MName, Client_Sex, Date,  Temp_Variable,  Temp_Variable2,  Temp_Variable3):

          Client_Info = ("Insert into Client_Info (Client_ID, Client_Father_Name, Client_Mother_Name, Client_Sex, Client_DOB,  Client_Account_Type,  Client_ID_Type,  Client_Occupation) values(%s, %s, %s, %s, %s, %s, %s, %s)")
          Client_Info_Values = (Client_ID, Client_FName, Client_MName, Client_Sex, Date,  Temp_Variable,  Temp_Variable2,  Temp_Variable3)
          Cursor.execute(Client_Info, Client_Info_Values)
          Data_base.commit()

     def Client_II(Client_ID, Client_PermanentAddress, Client_TemporaryAddress, Client_DepositAmount):

          Client_Extra = ("Insert into Client_Extra (Client_ID, Client_Permanent_Address, Client_Temporary_Address, Client_Deposit_Amount) values(%s, %s, %s, %s)")
          Client_Extra_Values = (Client_ID, Client_PermanentAddress, Client_TemporaryAddress, Client_DepositAmount)
          Cursor.execute(Client_Extra, Client_Extra_Values)
          Data_base.commit()
          print("\nRegisteration Successfully Completed")


Registration_Obj = Process_SQL

#==============================================================================================================================#
                                                                                                                   # Logging Into Bank Account #
#==============================================================================================================================#

class Client_Information:

     def Information():

          Flag_Start = 10000000                                                                                                                               #Registering Account
          Flag_End = 99999999
          ID = str(random.randint(Flag_Start, Flag_End))                                                                             #Clients Data
          Client_ID = ID
          print("\nClient_ID : ",Client_ID)
          Client_Password = input("\nEnter Password (Limit 10 Cipher) : ")
          Client_Errors.Space_Error(Client_Password)
          if len(Client_Password)>10:                                                                              #When Client Input exceeds the count of 10

               for i in range(0,100):
                    print("\nTry Again")
                    Client_Password = input("\nEnter Password Again (Limit 10 Cipher) : ")

                    if len(Client_Password) == 10 or len(Client_Password) < 10  :
                         print("\nGood")                                                                                                                          
                         break
                    else:
                         continue

#==============================================================================================================================#
                                                                                                # Clients Data For Registering An Account In the Bank #
#==============================================================================================================================#


          Client_Name = input("\nEnter Your Full Name : ")
          Client_Errors.Space_Error(Client_Name)
          Registration_Obj(Client_ID, Client_Name, Client_Password)
          #Client's Background Information
          Client_FName = input("\nEnter your Father's Name : ")
          Client_Errors.Space_Error(Client_FName)
          Client_MName = input("\nEnter your Mother's Name : ")
          Client_Errors.Space_Error(Client_MName)
          Client_Sex = input("\nSex : ")
          if Client_Sex not in ["M","F","f","m"]:
               for i in range(0,5):
                    print("\nTry Again")
                    Client_Sex = input("\nSex : ")

                    if Client_Sex in ["M","F","f","m"]:
                         break
                    else:
                         continue

#==============================================================================================================================#
                                                                                                                         # Importing Date Module #
#==============================================================================================================================#
          import DateModule                                                                                             
          Day = DateModule.Case_Day
          Month = DateModule.Case_Month                                                                  
          Year = DateModule.Case_Year
          Date = (Year + "-" + Month + "-" + Day)
#==============================================================================================================================#

          Client_AccountType = input("\nEnter Account Type ( 1 - Current      2 - Fixed Account      3 - Saving Account ) : ")
          Temp_Variable = Client_AccountType.lower()

          if Temp_Variable not in ["current", "fixed account", "saving account"]:
               for i in range(0,100):
                    print("\nTry Again")
                    Client_AccountType = input("\nEnter Account Type ( 1 - Current      2 - Fixed Account      3 - Saving Account ) : ")
                    Temp_Variable = Client_AccountType.lower()
                    if Temp_Variable  in ["current", "fixed account", "saving account"]:
                         break
                    else:
                         continue

          Client_IDType = input("\nEnter ID Type ( 1 - Citizenship      2 - Driving Lisence      3 - Passport ) : ")
          Temp_Variable2 = Client_IDType.lower()

          if Temp_Variable2 not in ["citizenship", "driving lisence", "passport"]:

               for i in range(0,100):
                    print("\nTry Again")
                    Client_IDType = input("\nEnter ID Type ( 1 - Citizenship      2 - Driving Lisence      3 - Passport ) : ")
                    Temp_Variable2 = Client_IDType.lower()
                    if Temp_Variable2  in ["citizenship", "driving lisence", "passport"]:
                         break
                    else:
                         continue

          Client_Occupation = input("\nEnter your Occupation ( 1 - Professionals      2 - Businessman      3 - Farmers      4 - Self Employed      5 -Other ) : ")
          Temp_Variable3 = Client_Occupation.lower()

          if Temp_Variable3 not in ["professionals", "businessman", "farmers", "self employed", "other"]:
               for i in range(0,100):
                    print("\nTry Again")
                    Client_Occupation = input("\nEnter your Occupation ( 1 - Professionals      2 - Businessman      3 - Farmers      4 - Self Employed      5 -Other ) : ")
                    Temp_Variable3 = Client_Occupation.lower()
                    if Temp_Variable3  in ["professionals", "businessman", "farmers", "self employed", "other"]:
                         break
                    else:
                         continue

          Client_PermanentAddress = input("\nEnter your Permanent Address : ")
          Client_Errors.Space_Error(Client_PermanentAddress)
          Client_TemporaryAddress = input("\nEnter your Temporary Address : ")
          Client_Errors.Space_Error(Client_TemporaryAddress)
          while True:
               try:
                  Client_DepositAmount = int(input("\nDeposit Primary Amount : "))
                  int(Client_DepositAmount)
                  break
               except ValueError:
                    print("\nNo valid integer! Please try again ...")
          Client_Errors.Space_Error(Client_DepositAmount)
          Date = date.today()
          DOR = Date.strftime('%y-%b-%d')


          Registration_Obj. Client(str(Client_ID), Client_FName, Client_MName, Client_Sex, Date,  Temp_Variable,  Temp_Variable2,  Temp_Variable3)
          Registration_Obj. Client_II(str(Client_ID), Client_PermanentAddress, Client_TemporaryAddress, Client_DepositAmount)
          Cursor.execute("INSERT INTO Client_Date VALUES ('"+Client_ID+"','"+DOR+"')")
          Data_base.commit()

Flag_Obj = Client_Information

#==============================================================================================================================#
                                                                                                # Clients Data For Registering An Account In the Bank#
#==============================================================================================================================#


class Bank_Process:

     
     def Display(self):                                                                                                                                               #Displaying of Various Loan Types

          print("\n========================")
          print("l\tLOAN TYPES\t     l")
          print("========================")

          print("\n========================")
          print('l\tPersonal Loan\t     l')
          print('l\tHousing Loan\t     l')
          print('l\tEducation Loan\t     l')
          print("========================\n")

     def Client_Deposition(self):                                                                             #Depositing Information

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Client_Deposit = input("\nDeposited By : ")
          Client_Errors.Space_Error(Client_Deposit)
          while True:
               try:
                  Amount_Deposit = int(input("\nEnter Required Amount to Deposit: "))
                  int(Amount_Deposit)
                  break
               except ValueError:
                    print("\nNo valid integer! Please try again ...")
          Client_Errors.Space_Error(Amount_Deposit)

          if Amount_Deposit > 500000:
               print("\nMaximum Error ")
               os._exit(0)
          else:
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Amount_Deposit)+' WHERE Client_ID =' + str(Initial_ID))
               Data_base.commit()
               print("\nAmount Successfully Deposited Into the Account")

#==============================================================================================================================#

     def Client_Withdraw(self):                                                                               #Withdrawing Information

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Client_Withdraw = input("\nWithdrawn By : ")
          Client_Errors.Space_Error(Client_Withdraw)
          while True:
               try:
                  Amount_Withdraw = int(input("\nEnter Required Amount to Withdraw: "))
                  int(Amount_Withdraw)
                  break
               except ValueError:
                    print("\nNo valid integer! Please try again ...")
          Client_Errors.Space_Error(Amount_Withdraw)
          Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
          for variable in Cursor:
               Withdraw =  ''.join(variable)

          if int(Withdraw) - Amount_Withdraw  < 1000 or int(Withdraw) - Amount_Withdraw == 1000:
               print("\nCannot Withraw Amount, Due to the presence of Minimal Amount \nAmount Present :",Withdraw)
               os._exit(0)
          else:
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(- Amount_Withdraw)+' WHERE Client_ID =' + str(Initial_ID))
               Data_base.commit()
               print("\nAmount Successfully Withdrawn from the Account")

#==============================================================================================================================#

     def Client_Transfer(self):                                                                               #Transfer Details

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Client_Transfer_ID = input("\nEnter the ID (08 Digit Code) of the Person to Transfer : ")
          Client_Errors.Space_Error(Client_Transfer_ID)
          while True:
               try:
                  Amount_Transfer = int(input("\nEnter Amount to Transfer: "))
                  int(Amount_Transfer)
                  break
               except ValueError:
                    print("\nNo valid integer! Please try again ...")
          Client_Errors.Space_Error(Amount_Transfer)

          Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
          for variable in Cursor:
               Decrement =  int(''.join(map(str, variable)))
          Cursor.execute("Select Client_ID from Client_Extra where Client_ID="+Client_Transfer_ID)
          for variableI in Cursor:
               Transfer_Details = ''.join(variableI)

          if int(Decrement) - Amount_Transfer  < 1000 or int(Decrement) - Amount_Transfer == 1000:
               print("\nCannot Transfer Amount, Due to the presence of Minimal Amount \nAmount Present :",Decrement)
               os._exit(0)

          if Client_Transfer_ID == Transfer_Details:
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(- Amount_Transfer)+' WHERE Client_ID =' + str(Initial_ID))
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Amount_Transfer)+' WHERE Client_ID =' + str(Client_Transfer_ID))
               Data_base.commit()
               print("\nAmount Successfully Transformed to the respective Account")

          else:
               for i in range(0,5):
                    print("\nTry Again")
                    Client_Transfer_ID = input("\nEnter the ID (10 Digit Code) of the Person to Transfer : ")
                    Client_Errors.Space_Error(Client_Transfer_ID)
                    if Client_Transfer_ID == Transfer_Details:
                         Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(- Amount_Transfer)+' WHERE Client_ID =' + str(Initial_ID))
                         Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Amount_Transfer)+' WHERE Client_ID =' + str(Client_Transfer_ID))
                         Data_base.commit()
                         print("\nAmount Successfully Transformed to the respective Account")
                         break
                    else:
                         continue
                    break
                    os._exit(0)

#==============================================================================================================================#

     def Client_Loan(self):                                                                                                             #Client Loan process 

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Obj_Client_Process.Display()
          Loan_Type = input("Enter Loan Type ( 1 - Personal Loan      2 - Housing Loan     3 - Education Loan ) : ")
          Client_Errors.Space_Error(Loan_Type)
          Temp_Variable4 = Loan_Type.lower()
          if Temp_Variable4 not in ["personal loan", "housing loan", "education loan"]:
               for i in range(0,100):
                    print("\nTry Again")
                    Client_AccountType = input("\nEnter Loan Type ( 1 - Personal Loan      2 - Housing Loan      3 - Education Loan ) : ")
                    Client_Errors.Space_Error(Client_AccountType)
                    Temp_Variable4 = Client_AccountType.lower()
                    if Temp_Variable4  in ["personal loan", "housing loan", "education loan"]:
                         break
                    else:
                         continue

          if Temp_Variable4 == "personal loan":
               while True:
                    try:
                         Client_Salary = int(input("\nEnter Your Monthly Salary: "))                                           #Client Salary taken into account for the Registeration of Loan
                         int(Client_Salary)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Client_Salary)
               Collateral = input("\nDocuments of Security/Collateral: ")
               Client_Errors.Space_Error(Collateral)
               while True:
                    try:
                         Loan_Required = int(input("\nEnter Required Amount for Loan: "))                                           
                         int(Loan_Required)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Loan_Required)
               P = Loan_Required
               Calc_1 = (10 * Loan_Required)/100
               if Client_Salary > Calc_1:
                    pass
               else:
                    print("\nSorry, Not Eligible to Take Loan")
                    print("\nThank You and Have a Nice Day !!!!!\n")
                    os._exit(0)
               Rate = 11/100
               Time_Given_Month = 12
               n = Time_Given_Month
               EMI = int(round((P * Rate * (1 + Rate) * n)/((1 + Rate) * n - 1),0))
               Monthly_Payment = int(round(EMI/48,0))
               print("\nLoan EMI: ", Monthly_Payment)
               print("\nTotal Payment: ", EMI+Loan_Required)

               print("\n=====================================")
               print("l\tLoan Successfully Withdrawn              l")
               print("=====================================")

               Graph_input = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
               Client_Errors.Space_Error(Graph_input)
               Graph_Lower = Graph_input.lower()
               if Graph_Lower not in ["y", "n"]:
                    for i in range(0,100):
                         print("\nTry Again")
                         Graph_Type = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
                         Client_Errors.Space_Error(Graph_Type)
                         Graph_Lower = Graph_Type.lower()
                         if Graph_Lower  in ["y", "n"]:
                              break
                         else:
                              continue
               if Graph_Lower == "y":
                    Loan_Information = ("Loan EMI", "Total Payment")
                    Loan_Quantity = [Monthly_Payment * 48, EMI+Loan_Required]
                    Color = ["orange","blue"]
                    PLY.pie(Loan_Quantity, labels = Loan_Information, colors = Color)
                    PLY.show()
               else:
                    pass
               print("\n======================================================")
               print("l\t\tThank You and Have a Nice Day !!!!!\t   l")
               print("======================================================\n")
               Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
               for variable in Cursor:
                    Loan_1 =  int(''.join(map(str, variable)))
               Date = date.today()
               DOR = Date.strftime('%y-%b-%d')
               Cursor.execute("insert into Client_Loan_Info values('"+str(Initial_ID)+"','"+str(EMI+Loan_Required)+"','"+str(DOR)+"')")
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Loan_Required)+' WHERE Client_ID =' + str(Initial_ID))
               Data_base.commit()

#==============================================================================================================================#

          elif Temp_Variable4 == "housing loan":
               while True:
                    try:
                         Client_Salary = int(input("\nEnter Your Monthly Salary: "))                                           #Client Salary taken into account for the Registeration of Loan
                         int(Client_Salary)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Client_Salary)
               Collateral = input("\nDocuments of Security/Collateral: ")
               Client_Errors.Space_Error(Collateral)
               while True:
                    try:
                         Loan_Required = int(input("\nEnter Required Amount for Loan: "))                                           
                         int(Loan_Required)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Loan_Required)
               P = Loan_Required
               Calc_1 = (9 * Loan_Required)/100
               if Client_Salary > Calc_1:
                    print("")
               else:
                    print("\nSorry, Not Eligible to Take Loan")
                    print("\nThank You and Have a Nice Day !!!!!\n")
                    os._exit(0)
               Rate = 10/100
               Time_Given_Month = 12
               n = Time_Given_Month
               EMI = round((P * Rate * (1 + Rate) * n)/((1 + Rate) * n - 1),0)
               Monthly_Payment = round(EMI/48,0)
               print("\nLoan EMI: ", Monthly_Payment)
               print("\nTotal Payment: ", EMI+Loan_Required)
               print("\n=====================================")
               print("l\tLoan Successfully Withdrawn              l")
               print("=====================================")

               Graph_input = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
               Client_Errors.Space_Error(Graph_input)
               Graph_Lower = Graph_input.lower()
               if Graph_Lower not in ["y", "n"]:
                    for i in range(0,100):
                         print("\nTry Again")
                         Graph_Type = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
                         Client_Errors.Space_Error(Graph_Type)
                         Graph_Lower = Graph_Type.lower()
                         if Graph_Lower  in ["y", "n"]:
                              break
                         else:
                              continue
               if Graph_Lower == "y":
                    Loan_Information = ("Loan EMI", "Total Payment")
                    Loan_Quantity = [Monthly_Payment * 48, EMI+Loan_Required]
                    Color = ["yellow","red"]
                    PLY.pie(Loan_Quantity, labels = Loan_Information, colors = Color)
                    PLY.show()
               else:
                    pass
               print("\n======================================================")
               print("l\t\tThank You and Have a Nice Day !!!!!\t   l")
               print("======================================================\n")
               Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
               for variable in Cursor:
                    Loan_1 =  int(''.join(map(str, variable)))
               Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
               Date = date.today()
               DOR = Date.strftime('%y-%b-%d')
               Cursor.execute("insert into Client_Loan_Info values('"+str(Initial_ID)+"','"+str(EMI+Loan_Required)+"','"+str(DOR)+"')")
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Loan_Required)+' WHERE Client_ID =' + str(Initial_ID))
               Data_base.commit()

#==============================================================================================================================#

          elif Temp_Variable4 == "education loan":
               while True:
                    try:
                         Client_Salary = int(input("\nEnter Your Monthly Salary: "))                                           #Client Salary taken into account for the Registeration of Loan
                         int(Client_Salary)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Client_Salary)
               Collateral = input("\nDocuments of Security/Collateral: ")
               Client_Errors.Space_Error(Collateral)
               while True:
                    try:
                         Loan_Required = int(input("\nEnter Required Amount for Loan: "))                                           
                         int(Loan_Required)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Loan_Required)
               P = Loan_Required
               Calc_1 = (7 * Loan_Required)/100
               if Client_Salary > Calc_1:
                    print("")
               else:
                    print("\nSorry, Not Eligible to Take Loan")
                    print("\nThank You and Have a Nice Day !!!!!\n")
                    os._exit(0)
               Rate = 8/100
               Time_Given_Month = 12
               n = Time_Given_Month
               EMI = round((P * Rate * (1 + Rate) * n)/((1 + Rate) * n - 1),0)
               Monthly_Payment = round(EMI/48,0)
               print("\nLoan EMI: ", Monthly_Payment)
               print("\nTotal Payment: ", EMI+Loan_Required)
               print("\n=====================================")
               print("l\tLoan Successfully Withdrawn              l")
               print("=====================================")

               Graph_input = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
               Client_Errors.Space_Error(Graph_input)
               Graph_Lower = Graph_input.lower()
               if Graph_Lower not in ["y", "n"]:
                    for i in range(0,100):
                         print("\nTry Again")
                         Graph_Type = input("\nDo You Want to See the Graphical Representation of Loan EMI and Total Payment ( Y/N) : ")
                         Client_Errors.Space_Error(Graph_Type)
                         Graph_Lower = Graph_Type.lower()
                         if Graph_Lower  in ["y", "n"]:
                              break
                         else:
                              continue
               if Graph_Lower == "y":
                    Loan_Information = ("Loan EMI", "Total Payment")
                    Loan_Quantity = [Monthly_Payment * 48, EMI+Loan_Required]
                    Color = ["orange","blue"]
                    PLY.pie(Loan_Quantity, labels = Loan_Information, colors = Color)
                    PLY.show()
               else:
                    pass
               print("\n======================================================")
               print("l\t\tThank You and Have a Nice Day !!!!!\t   l")
               print("======================================================\n")
               Cursor.execute("Select Client_Deposit_Amount from Client_Extra where Client_ID="+Initial_ID)
               for variable in Cursor:
                    Loan_1 =  int(''.join(map(str, variable)))
               Date = date.today()
               DOR = Date.strftime('%y-%b-%d')
               Cursor.execute("insert into Client_Loan_Info values('"+str(Initial_ID)+"','"+str(EMI+Loan_Required)+"','"+str(DOR)+"')")
               Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(+ Loan_Required)+' WHERE Client_ID =' + str(Initial_ID))
               Data_base.commit()

     def Client_Loan_Payment(self):

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Cursor.execute("Select DOL from Client_Loan_Info where Client_ID ="+Initial_ID)
          for variable in Cursor:
               DOL = variable                                                                                                     # This the Date at which the Loan was issued
#==============================================================================================================================#
          Date_DOL =  ''.join(DOL)                              
          Month_Dict = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
          Date = Date_DOL [0:2]                                                                                              #Slicing of the Date from the Date the Loan was issued 
          Flag_Month = Date_DOL [3:6]                                                                                   #Slicing of the Month from the Date the Loan was issued
          Month = Month_Dict.get(Flag_Month)                                                                  #Converting the Month into their Respective Numbers
          Year = Date_DOL [7:9]                                                                                                   #Slicing of the Year from the Date the Loan was issued
#==============================================================================================================================#
          Date_1 = date.today()                                                                                     #Present Date
          DOR = Date_1.strftime('%y-%b-%d')            
          Current_Date = DOR[0:2]                                                                                       #Slicing of Present Date
          Cur_Month = DOR[3:6]                                                                                #Slicing of Present Month
          Current_Month = Month_Dict.get(Cur_Month)                                   #Converting the Present Month into their Respective Numbers
          Current_Year = DOR[7:9]                                                                             #Slicing of Precent Year
          Current_Date_Repayment = ( int(Current_Date), Current_Month,  int(Current_Year) )
#==============================================================================================================================#
          Date_of_Loan = ( int(Date), Month, int(Year) )              #Tuple form of the Date (DD, MM, YY)
          Date_of_Return = ( int(Date), Month, int(Year) + 1)         #Tuple form of the Date (DD, MM, YY + 1)
          Date_of_Return_Comparison = ( int(Year) + 1, Month, int(Date) )       #Comparison Tuple form of the Date (YY + 1, MM, )
          Current_Return = ( int(Current_Year), Current_Month, int(Current_Date) )           #Comparison Tuple form of the Date (YY, MM, YY)
#==============================================================================================================================#
          if Current_Return <= Date_of_Return_Comparison :
               Cursor.execute("Select Loan_Repay_Amount from Client_Loan_Info where Client_ID = "+Initial_ID)
               for variable in Cursor:
                    Loan_Repay_Amount = int(''.join(map(str, variable)))
               while True:
                    try:
                         Amount_to_Repay = int(input("\nEnter Required Amount to Repay : "))                                
                         int(Amount_to_Repay)
                         break
                    except ValueError:
                         print("\nNo valid integer! Please try again ...")
               Client_Errors.Space_Error(Amount_to_Repay)
               if Amount_to_Repay != Loan_Repay_Amount:
                    for i in range(0,100):
                         print("\nTry Again")
                         while True:
                              try:
                                   Amount_to_Repay = int(input("\nEnter Required Amount to Repay : "))                                
                                   int(Amount_to_Repay)
                                   break
                              except ValueError:
                                   print("\nNo valid integer! Please try again ...")
                         Client_Errors.Space_Error(Amount_to_Repay)
                         if Amount_to_Repay == Loan_Repay_Amount:
                              Cursor.execute('UPDATE Client_Loan_Info SET Loan_Repay_Amount = Loan_Repay_Amount + '+str(- Loan_Repay_Amount)+' WHERE Client_ID =' + str(Initial_ID))
                              Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(- Loan_Repay_Amount)+' WHERE Client_ID =' + str(Initial_ID))
                              Data_base.commit()
                              print("\n=====================================")
                              print("l\tLoan Successfully Deposited               l")
                              print("=====================================")
                              break

               else:
                    Cursor.execute('UPDATE Client_Loan_Info SET Loan_Repay_Amount = Loan_Repay_Amount + '+str(- Loan_Repay_Amount)+' WHERE Client_ID =' + str(Initial_ID))
                    Cursor.execute('UPDATE Client_Extra SET Client_Deposit_Amount = Client_Deposit_Amount + '+str(- Loan_Repay_Amount)+' WHERE Client_ID =' + str(Initial_ID))
                    Data_base.commit()
                    print("\n=====================================")
                    print("l\tLoan Successfully Deposited               l")
                    print("=====================================")
                    

          else:
               print("\n======================================================")
               print("l\tGIVEN TIME EXCEEDED AND ACCOUNT CANCELLED\t         l")
               print("======================================================\n")

               Cursor.execute("Delete from Bank_System where Client_ID = "+Initial_ID)
               Data_base.commit()
               Cursor.execute("Delete from Client_Date where Client_ID = "+Initial_ID)
               Data_base.commit()
               Cursor.execute("Delete from Client_Extra where Client_ID = "+Initial_ID)
               Data_base.commit()
               Cursor.execute("Delete from Client_Info where Client_ID = "+Initial_ID)
               Data_base.commit()
               Cursor.execute("Delete from Client_Loan_Info where Client_ID = "+Initial_ID)
               Data_base.commit()
               os._exit(0)
               
               
Obj_Client_Process = Bank_Process()

#==============================================================================================================================#

class Updation:

     def Updating_Client_Info(self):

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()

          print("\n==================================")
          print("l         Choose the Following To Update       l")
          print("==================================")
          print("l                                                                           l")
          print("l 1 - Press 1 to Change Your Password         l")
          print("l                                                                           l")
          print("l 2 - Press 2 to Edit Your Name                        l")
          print("l                                                                           l")
          print("l 3 - Press 3 to Edit Your Father's Name         l")
          print("l                                                                           l")
          print("l 4 - Press 4 to Edit Your Mother's Name       l")
          print("l                                                                           l")
          print("l 5 - Press 5 to Change Your Account Type l")
          print("l                                                                           l")
          print("l 6 - Press 6 to Edit Your Adress                       l")
          print("l                                                                           l")
          print("l E - Press E to Exit                                             l")
          print("l                                                                           l")
          print("==================================")

          Updation_Choice = input("\nEnter the Required Choice: ")
          Temp_Variable_11 = Updation_Choice.lower()
          if Temp_Variable_11 not in ["1", "2", "3", "4", "5", "6", "e"]:
               for i in range(0,100):
                    print("\nTry Again")
                    Input = input("\nEnter Required Input: ")
                    Client_Errors.Space_Error(Input)
                    Temp_Variable_11 = Input.lower()
                    if Temp_Variable_11  in ["1", "2", "3", "4", "5", "6", "e"]:
                         break
                    else:
                         continue

          if Temp_Variable_11 == "1":
          
               Client_Password = input("\nEnter New Password (Limit 10 Cipher) : ")
               Client_Errors.Space_Error(Client_Password)
               if len(Client_Password)>10:                                                                              #When Client Input exceeds the count of 10
                    for i in range(0,100):
                         print("\nTry Again")
                         Client_Password = input("\nEnter New Password Again (Limit 10 Cipher) : ")

                         if len(Client_Password) == 10 or len(Client_Password) < 10  :
                              print("\nGood")                                                                                                                          
                              break
                         else:
                              continue
               Cursor.execute("UPDATE Bank_System SET Client_Password ='"+str(Client_Password)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()

          elif Temp_Variable_11 == "2":

               Client_Name = input("\nEnter Your Full Name : ")
               Client_Errors.Space_Error(Client_Name)
               Cursor.execute("UPDATE Bank_System SET Client_Name ='"+str(Client_Name)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()

          elif Temp_Variable_11 == "3":

               Client_FName = input("\nEnter your Father's Name : ")
               Client_Errors.Space_Error(Client_FName)
               Cursor.execute("UPDATE Client_Info SET Client_Father_Name ='"+str(Client_FName)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()

          elif Temp_Variable_11 == "4":

                Client_MName = input("\nEnter your Mother's Name : ")
                Client_Errors.Space_Error(Client_MName)
                Cursor.execute("UPDATE Client_Info SET Client_Mother_Name ='"+str(Client_MName)+"'WHERE Client_ID ="''+str(Initial_ID))
                print("\n==============================")
                print("l\tUpdated Successfully \t   l")
                print("==============================\n")
                Data_base.commit()

          elif Temp_Variable_11 == "5":

               Client_AccountType = input("\nEnter Account Type ( 1 - Current      2 - Fixed Account      3 - Saving Account ) : ")
               Temp_Variable = Client_AccountType.lower()
               if Temp_Variable not in ["current", "fixed account", "saving account"]:
                    for i in range(0,100):
                         print("\nTry Again")
                         Client_AccountType = input("\nEnter Account Type ( 1 - Current      2 - Fixed Account      3 - Saving Account ) : ")
                         Temp_Variable = Client_AccountType.lower()
                         if Temp_Variable  in ["current", "fixed account", "saving account"]:
                              break
                         else:
                              continue
               Cursor.execute("UPDATE Client_Info SET Client_Account_Type ='"+str(Temp_Variable)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()

          elif Temp_Variable_11 == "6":

               Client_PermanentAddress = input("\nEnter your Permanent Address : ")
               Client_Errors.Space_Error(Client_PermanentAddress)
               Cursor.execute("UPDATE Client_Extra SET Client_Permanent_Address ='"+str(Client_PermanentAddress)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()
               
               Client_TemporaryAddress = input("\nEnter your Temporary Address : ")
               Client_Errors.Space_Error(Client_TemporaryAddress)
               Cursor.execute("UPDATE Client_Extra SET Client_Temporary_Address ='"+str(Client_TemporaryAddress)+"'WHERE Client_ID ="''+str(Initial_ID))
               print("\n==============================")
               print("l\tUpdated Successfully \t   l")
               print("==============================\n")
               Data_base.commit()

          elif Temp_Variable_11 == "e":
               print("\n======================================================")
               print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
               print("======================================================\n")
               os._exit(0)

Obj_Client_Account_Updation = Updation()

#==============================================================================================================================#

class Deletion:

     def Deleting_Client_Account(self):

          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Cursor.execute("Delete from Bank_System where Client_ID = "+Initial_ID)
          Data_base.commit()
          Cursor.execute("Delete from Client_Date where Client_ID = "+Initial_ID)
          Data_base.commit()
          Cursor.execute("Delete from Client_Extra where Client_ID = "+Initial_ID)
          Data_base.commit()
          Cursor.execute("Delete from Client_Info where Client_ID = "+Initial_ID)
          Data_base.commit()
          Cursor.execute("Delete from Client_Loan_Info where Client_ID = "+Initial_ID)
          Data_base.commit()
          print("\n======================================================")
          print("l\t\tSuccessfully Deleted Account\t                         l")
          print("======================================================\n")
          os._exit(0)

Obj_Client_Account_Deletion = Deletion()

#==============================================================================================================================#               

class Client_Choice:                    #Client Chooses from these given options

     def Selection():                                                                                                                                               #Selection according to Clients Desire

         print("\n==============================================")
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 1 for Registering Account\t                       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 2 to Deposit into Account\t                       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 3 to Withdraw from Account\t                       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 4 to Transfer into Another Account\t       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 5 to Register for Loan or to Pay Loan\t       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 6 to Update Personal Info\t                       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter 7 to Cancel Your Account\t                       l')
         print('l\t\t\t\t\t                       l')
         print('l\tEnter E to Exit\t                                                       l')
         print('l\t\t\t\t\t                       l')
         print("==============================================")

#==============================================================================================================================#

     def Client_Review():

         print("\n======================================================")
         print("l\t\tPlease Comment on Your Review Here\t         l")
         print("======================================================\n")
         Client_Review = open("Client_Reviews.txt", "a")
         Review = str(input("\n>>>\t"))
         Client_Errors.Space_Error(Review)
         Client_Review.write(Review)
         Client_Review.close()
         print("\n======================================================")
         print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
         print("======================================================\n")

#==============================================================================================================================#
         

     def Object():

          Client_Input = input("Enter Required Choice : ")
          Temp_Variable_10 = Client_Input.lower()
          Client_Errors.Space_Error(Client_Input)
          if Client_Input == "1":
               Flag_Obj.Information()
               Client_Choice.Client_Review()

          elif Client_Input == "2":
              Obj_Client_Process.Client_Deposition()                                                                                                                             #Object of Details from 'Class  Details'
              Client_Choice.Client_Review()

          elif Client_Input == "3":
              Obj_Client_Process.Client_Withdraw()
              Client_Choice.Client_Review()

          elif Client_Input == "4":
              Obj_Client_Process.Client_Transfer()
              Client_Choice.Client_Review()

          elif Client_Input == "5":

               Loan_Input = input("\nEnter Your Requirement ( 1 - Register to get Loan      2 - Loan Payment ) : ")
               Client_Errors.Space_Error(Loan_Input)
               Temp_Variable5 = Loan_Input.lower()
               if Temp_Variable5 not in ["register to get loan", "loan payment"]:
                    for i in range(0,100):
                         print("\nTry Again")
                         Loan_Input  = input("\nEnter Your Requirement ( 1 - Register to get Loan      2 - Loan Payment ) : ")
                         Client_Errors.Space_Error(Loan_Input)
                         Temp_Variable5 = Loan_Input .lower()
                         if Temp_Variable5  in ["register to get loan", "loan payment"]:
                              break
                         else:
                              continue
               if Temp_Variable5 == "register to get loan" :
                    Obj_Client_Process.Client_Loan()
                    Client_Choice.Client_Review()

               else:
                    Obj_Client_Process.Client_Loan_Payment()
                    Client_Choice.Client_Review()

          elif Client_Input == "6":
               Obj_Client_Account_Updation.Updating_Client_Info()
               Client_Choice.Client_Review()

          elif Client_Input == "7":
              Obj_Client_Account_Deletion.Deleting_Client_Account()
              Client_Choice.Client_Review()

          elif Temp_Variable_10 == "e":
               print("\n======================================================")
               print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
               print("======================================================\n")
               os._exit(0)

          elif Client_Input not in ["1", "2" , "3", "4", "5", "6", "7", "e"]:                                                                                           #Incorrect Input By the Client
               for i in range(0,100):
                    print("\nIncorrect Option, Try Again\n")
                    Client_Choice.Selection()
                    Client_Input = input("\nEnter Required Choice : ")
                    Client_Errors.Space_Error(Client_Input)
                    Temp_Variable_11 = Client_Input.lower()

                    if Client_Input in ["1", "2" , "3", "4", "5", "6", "7", "e"]:
                         if Client_Input == "1":
                              Flag_Obj.Information()
                              Client_Choice.Client_Review()

                         elif Client_Input == "2":
                              Obj_Client_Process.Client_Deposition()                                                                                                                             #Object of Details from 'Class  Details'
                              Client_Choice.Client_Review()                                                                                                                                #Object of Details from 'Class  Details'                                                                                                                       

                         elif Client_Input == "3":
                              Obj_Client_Process.Client_Withdraw()
                              Client_Choice.Client_Review()                                                                                                                                     #EDITING REQUIRED

                         elif Client_Input == "4":
                              Obj_Client_Process.Client_Transfer()
                              Client_Choice.Client_Review()

                         elif Client_Input == "5":

                              Loan_Input = input("\nEnter Your Requirement ( 1 - Register to get Loan      2 - Loan Payment ) : ")
                              Client_Errors.Space_Error(Loan_Input)
                              Temp_Variable5 = Loan_Input.lower()
                              if Temp_Variable5 not in ["register to get loan", "loan payment"]:
                                   for i in range(0,100):
                                        print("\nTry Again")
                                        Loan_Input  = input("\nEnter Your Requirement ( 1 - Register to get Loan      2 - Loan Payment ) : ")
                                        Client_Errors.Space_Error(Loan_Input)
                                        Temp_Variable5 = Loan_Input .lower()
                                        if Temp_Variable5  in ["register to get loan", "loan payment"]:
                                             break
                                        else:
                                             continue
                              if Temp_Variable5 == "register to get loan" :
                                   Obj_Client_Process.Client_Loan()
                                   Client_Choice.Client_Review()

                              else:
                                   Obj_Client_Process.Client_Loan_Payment()
                                   Client_Choice.Client_Review()

                         elif Client_Input == "6":
                              Obj_Client_Account_Updation.Updating_Client_Info()
                              Client_Choice.Client_Review()

                         elif Client_Input == "7":
                              Obj_Client_Account_Deletion.Deleting_Client_Account()
                              Client_Choice.Client_Review()

                         elif Client_Input == "e":
                             print("\n======================================================")
                             print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
                             print("======================================================\n")
                             os._exit(0)
                             break
                    else:
                         continue
                    
Client_Obj = Client_Choice                   #Object of Client_Choice
Client_Obj.Selection()
print("\n")
Client_Obj.Object()

#==============================================================================================================================#
                                                                                                                                  # MENU TABLE #
#==============================================================================================================================#

def Menu_Table():

     print("\n=================================")
     print("l\t  Menu Table\t\t          l")
     print("=================================")
     print("l                                                                         l")
     print("l C - Press C to Access the Bank Again     l")
     print("l                                                                         l")
     print("l O - Press O to View Account                    l")
     print("l                                                                         l")
     print("l E - Press E to Exit                                           l")
     print("l                                                                         l")
     print("=================================")

     Input = input("\nEnter Required Input: ")
     Client_Errors.Space_Error(Input)
     Temp_Variable7 = Input.lower()
     if Temp_Variable7 not in ["c", "e", "o"]:
          for i in range(0,100):
               print("\nTry Again")
               Input = input("\nEnter Required Input: ")
               Client_Errors.Space_Error(Input)
               Temp_Variable7 = Input.lower()
               if Temp_Variable7  in ["c", "e", "o"]:
                    break
               else:
                    continue

     if Temp_Variable7 == "e":
          print("\n======================================================")
          print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
          print("======================================================\n")
          os._exit(0)

     elif Temp_Variable7 == "o":
          global Initial_ID
          Initial_ID = input("\nEnter ID (08 Digit Code) : ")
          Client_Errors.Space_Error(Initial_ID)
          Info_Obj()
          Cursor.execute("Select Bank_System.Client_ID, Client_Name, Client_Deposit_Amount from Bank_System, Client_Extra where Bank_System.Client_ID ="+Initial_ID+" and Bank_System.Client_ID = Client_Extra.Client_ID;")
          print("\n\t================================================")
          print("\tl Client_ID\t       Cleint_Name\t               Client Amount  l")
          print("\t================================================\n")
          for variable in Cursor:
               Code =  '                       '.join(variable)
               print("\t",Code, end = "\n\n")
          print("\t================================================\n")

     else:
          Client_Obj.Selection()
          print("\n")
          Client_Obj.Object()

for Input in range(0,100):
     Menu_Table()
     User_Input = input("\nM - Press M to bring back Menu Table\tOR\tE - Press E to Exit : ")
     Temp_Variable_9 = User_Input.lower()
     if Temp_Variable_9 == "m":
          continue
     else:
         print("\n======================================================")
         print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
         print("======================================================\n")
         os._exit(0)
     
#==============================================================================================================================#  
