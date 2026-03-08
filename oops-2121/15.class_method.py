class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
        
e= Employee()
e.a = 45
e.show()  
'''
self = WO OBJECT JIS MAI METHOD CHAL RHA HAI
cls = WO CLASS JISKA WO OBJECT HAI JIMAI  WO METHOD CHAL RHA HAI, to get class attribute not instance ....
'''
      
      
# class Employee:
#     a=1
#     def show(self):  
#         print(f"the class attribute of a is {self.a}")
# e= Employee()
# e.a = 45
# e.show()      