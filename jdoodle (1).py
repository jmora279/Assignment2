class Assignment2:
    def __init__(self, year):
        self.year = year
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print("Your age is ", age)
    def listAnniversaries(self):
        anniversaries = []
        age = 2023 - self.year
        count = 0
        while age > 0:
            count += 1
            age -= 1
            if count % 10 == 0:
              anniversaries.append(count)  
        return anniversaries
    def modifyYear(self, n):
        yearStr = str(self.year)
        finalStr = ""
        count = 0
        while count < n * 2:
            if count % 2 == 0:
               finalStr += yearStr[0] 
            else:
                finalStr += yearStr(self.year)[1]
        count = 0        
        multiYear = self.year * n
        multiYearStr = str(multiYear)
        resultStr = ""
        while  count < multiYearStr.len:
            if count % 2 != 0:
                resultStr += multiYearStr[count]
        str = str + resultStr
obj1 = Assignment2(1998)
obj1.tellAge(2023)
ret = obj1.listAnniversaries()
print(ret)
ret = obj1.modifyYear(3)
print(ret)