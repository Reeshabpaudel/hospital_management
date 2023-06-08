from Person import Person
import os
class Patient(Person):
    """Patient class"""

    def __init__(self, first_name, surname, username, password, age, mobile, postcode, symptoms="", doctor="not set", appointment="not set"):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        super().__init__(first_name, surname, username, password, "patient")
        self.__age=age
        self.__mobile=mobile
        self.__postcode=postcode
        self.symptoms=symptoms


        #ToDo1 done!
        self.__doctor = doctor
        self.appointmet=appointment
       

    
        #ToDo2 done!
        
    def set_symptoms(self, symp):
        self.symptoms=symp

    def get_doctor(self) :
        return self.__doctor
        #ToDo3 done!


    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor
        read_file=open("patient_file.txt",'r')
        write_file=open("temp_file.txt",'w')
        line=read_file.readline()
        while(line!=""):
            if self.get_first_name() in line:
                string=''
                data=line.split(";")
                data[8]=doctor
                string=";".join(data)
                write_file.write(string)
            else:
                write_file.write(line)
            line=read_file.readline()
        read_file.close()
        write_file.close()
        os.remove("patient_file.txt")
        os.rename("temp_file.txt","patient_file.txt")
        

    def print_symptoms(self):
        """prints all the symptoms"""
        print(self.symptoms)
        #ToDo4 done!


    def __str__(self):
        return f'{self.full_name():^30}|{self.__doctor:^30}|{self.__age:^5}|{self.__mobile:^15}|{self.__postcode:^10}'
   
