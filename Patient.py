class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode, symptoms=""):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.first_name=first_name
        self.surname=surname
        self.__age=age
        self.__mobile=mobile
        self.__postcode=postcode
        self.symptoms=symptoms

        #ToDo1 done!
        self.__doctor = 'None'
       

    
    def full_name(self) :
        """full name is first_name and surname"""
        return self.first_name +' '+ self.surname
    
        #ToDo2 done!
        
    def set_symptoms(self, symp):
        self.symptoms=symp

    def get_doctor(self) :
        return self.__doctor
        #ToDo3 done!


    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.symptoms)
        #ToDo4 done!


    # def __str__(self):
    #     return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
    def __str__(self):
        return (f"{self.full_name()},{self.__doctor},{self.__age},{self.__mobile},{self.__postcode}")
