import os
from Person import Person
class Doctor(Person):
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, username, password, speciality, patients=[], appoinments=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        super().__init__(first_name, surname, username, password, "doctor")
        self.__speciality = speciality
        self.__patients=patients
        self.appoinments=appoinments
        
        
        

    def get_speciality(self) :
        #ToDo6 done!
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7 done!
        self.__speciality=new_speciality

    def add_patient(self, patient_name):
        self.__patients.append(patient_name)
        read_file=open("doctor_file.txt",'r')
        write_file=open("temp_file.txt",'w')
        line=read_file.readline()
        while(line!=""):
            if self.get_first_name() in line:
                
                data=line.split(";")
                extract=data[5][13:-1]
                data[5]=data[5].replace((extract),f"{extract+','+patient_name}")
                string=";".join(data)
                write_file.write(string)
            else:
                write_file.write(line)
            line=read_file.readline()
        read_file.close()
        write_file.close()
        os.remove("doctor_file.txt")
        os.rename("temp_file.txt","doctor_file.txt")

    def add_appointment(self, date):
        read_file=open("doctor_file.txt",'r')
        write_file=open("temp_file.txt",'w')
        line=read_file.readline()
        while(line!=""):
            if self.get_first_name() in line:
    
                data=line.split(";")
                extract=data[7][13:-1]
                data[7]=data[5].replace((extract),f"{extract+','+date}")
                string=";".join(data)
                write_file.write(string)
            else:
                write_file.write(line)
            line=read_file.readline()
        read_file.close()
        write_file.close()
        os.remove("doctor_file.txt")
        os.rename("temp_file.txt","doctor_file.txt")

                    



    def add_appoinments(self, appointment):
        self.__appoinments.append(appointment)


    def __str__(self) :
        return f"{self.full_name():^30}|{self.__speciality:^15}|{', '.join(self.__patients):^30}|{', '.join(self.appoinments):^30}"