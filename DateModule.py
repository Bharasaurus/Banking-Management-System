
#======================================================#
                        # BANKING MANAGEMENT SYSTEM #
#======================================================#


#DATE MODULE ( DATE OF BIRTH )

import os                                                                                                       #Importing Exiting Module
LD =["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]                          #List of Dates
for Element in range(10,32):
    LD.append(str(Element))
LM = LD[0:13]                                                                                                #List of Months
LY = []
for Years in range(1920,2021):
    LY.append(str(Years))

class DATE_OF_BIRTH:

    def Day(self):
        self.Client_DOB = print("\nClient's Date of Birth (DOB)")
        self.Client_Day = input("\nEnter Day of Birth (Limit 2 Digits) : ")
        if (len(self.Client_Day) > 2 or len(self.Client_Day) < 2) or (self.Client_Day == 00) or (self.Client_Day not in LD):                                                                          #When Client Day exceeds the count of 2
            for i in range(0,100):
                self.Try_Statement = print("\nTry Again")
                self.Client_Day = input("\nEnter Day of Birth Again: ")
                if len(self.Client_Day) == 2 and self.Client_Day in LD:
                    break
                else:
                    continue
        return self.Client_Day

    def Month(self):
        self.Client_Month = input("\nEnter Month of Birth (Limit 2 Digits) : ")
        if (len(self.Client_Month) > 2 or len(self.Client_Month) < 2) or (self.Client_Month == 00) or (self.Client_Month not in LM):                                                                              #When Client Month exceeds the count of 2
            for i in range(0,100):
                self.Try_Statement = print("\nTry Again")
                self.Client_Month = input("\nEnter Month of Birth Again: ")
                if len(self.Client_Month) == 2 and (self.Client_Month) in LM:
                     break
                else:
                    continue
        return self.Client_Month

    def Year(self):
        self.Client_Year = input("\nEnter Year of Year (Limit 4 Digits) : ")
        if (len(self.Client_Year) > 4 or len(self.Client_Year) < 4) or (self.Client_Year == 0000) or (self.Client_Year not in LY):                                                                              #When Client Year exceeds the count of 4
            for i in range(0,100):
                Try_Statement = print("\nTry Again")
                self.Client_Year = input("\nEnter Year of Birth Again: ")
                if len(self.Client_Year) == 4 and (self.Client_Year) in LY and (2020 - int(self.Client_Year)) < 18:                                                                                                                          
                    print("\nAccount Registiration Not Possible, Due to Age Restrictions")
                    print("\n======================================================")
                    print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
                    print("======================================================\n")
                    os._exit(0)
                    break
                elif len(self.Client_Year) == 4 and (self.Client_Year) in LY and (2020 - int(self.Client_Year)) > 18:
                    break
                else:
                    continue
        elif (2020 - int(self.Client_Year)) < 18:                                                                                                                                                           #Age Restrictions
            print("\nAccount Registiration Not Possible, Due to Age Restrictions")
            print("\n======================================================")
            print("l\t\tThank You and Have a Nice Day !!!!!\t         l")
            print("======================================================\n")
            os._exit(0)
        return


DOB_Obj = DATE_OF_BIRTH()                                                                       #Object for Date for Birth
DOB_Obj.Day()
#Calling Day Function
DOB_Obj.Month()
#Calling Month Function
DOB_Obj.Year()
#Calling Year Function
Case_Day = DOB_Obj.Client_Day
Case_Month = DOB_Obj.Client_Month
Case_Year = DOB_Obj.Client_Year

