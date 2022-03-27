class HBL():
    def __init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager):
        self.Branch_name=Branch_name
        self.Branch_ID=Branch_ID
        self.Branch_Location=Branch_Location
        self.Branch_Manager=Branch_Manager
    def show_main(self):
        print(f"The branch name is {self.Branch_name} and the branch ID is {self.Branch_ID} and the branch location is {self.Branch_Location} and the manager is {self.Branch_Manager}")

class Branch1_HBL(HBL):
    def __init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager,employee1,employee2,employee3,cust1,cust2,cust3):
        HBL.__init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager)
        self.employee1=employee1
        self.employee2=employee2
        self.employee3=employee3
        self.cust1=cust1
        self.cust2=cust2
        self.cust3=cust3
    def show_Branch1(self):
        print(f"The branch name is {self.Branch_name} and the branch ID is {self.Branch_ID} and the branch location is {self.Branch_Location} and the manager is {self.Branch_Manager} employee1 is {self.employee1} and 2nd employee is {self.employee2} and {self.employee3}")
    def show_Branch1_customer(self):
        print(f"The name of customers are {self.cust1},{self.cust2},{self.cust3}")
class cust_data_Branch1(Branch1_HBL):
    def __init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager,name,bank_account_no,Balance):
        HBL.__init__(self, Branch_name, Branch_ID, Branch_Location, Branch_Manager)
        self.name=name
        self.bank_account_no=bank_account_no
        self.Balance=Balance
    def show_cust_data_branch1(self):
        print(f"{self.Branch_name},{self.Branch_ID},{self.Branch_Location},{self.Branch_Manager},{self.name},{self.bank_account_no},{self.Balance}")
class emp_data_Branch2(Branch1_HBL):
    def __init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager,name,age,salary,status):
        HBL.__init__(self, Branch_name, Branch_ID, Branch_Location, Branch_Manager)
        self.name=name
        self.age=age
        self.salary=salary
        self.status=status
    def show_emp_data_branch1(self):
class Branch2_HBL(HBL):
    def __init__(self,Branch_name,Branch_ID,Branch_Location,Branch_Manager,employee1,employee2,employee3,cust1,cust2,cust3):
        HBL.__init__(self, Branch_name, Branch_ID, Branch_Location, Branch_Manager)
        self.employee1 = employee1
        self.employee2 = employee2
        self.employee3 = employee3
        self.cust1 = cust1
        self.cust2 = cust2
        self.cust3 = cust3

