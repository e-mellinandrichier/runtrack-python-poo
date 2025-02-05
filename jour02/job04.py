class Student:
    def __init__(self):
        self.__name = ""
        self.__surname = ""
        self.__number = 0
        self.__credits = 0
        self.__level = self. __student_eval()

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_number(self):
        return self.__number

    def get_credits(self):
        return self.__credits

    def set_name(self, new_name):
        self.__name = new_name

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def set_number(self, new_number):
        self.__number = new_number

    def set_credits(self, new_credits):
        self.__credits = new_credit
        
    def add_credits(self, new_credits):
        if new_credits > 0:
            self.__credits += new_credits
        else : 
            print("Added credits must be superior than 0")

    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom = {self.__name} \nPrénom = {self.__surname} \nid = {self.__number} \nNiveau = {self.__level}")
        
    
stud1 = Student()

stud1.set_name("John")
stud1.set_surname("Doe")
stud1.set_number(145)
stud1.add_credits(10)
stud1.add_credits(10)
stud1.add_credits(10)

# print(f"Le nombre de crédits de {stud1.get_name()} {stud1.get_surname()} est de {stud1.get_credits()}")
stud1.student_info()



    

