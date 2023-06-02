import os
class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality,username='doctor', password='123', patients=[], appoinments=[]):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients=patients
        self.__appoinments=appoinments
        self.__username=username
        self.__password=password
        
        
    
    def full_name(self) :
        #ToDo1 done!
        return self.__first_name+" "+self.__surname

    def get_first_name(self) :
        #ToDo2 done!
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3 done!
        self.__first_name=new_first_name

    def get_surname(self) :
        #ToDo4 done!
        return self.__surname

    def set_surname(self, new_surname):
        #ToDo5 done!
        self.__surname=new_surname

    def get_speciality(self) :
        #ToDo6 done!
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7 done!
        self.__speciality=new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def add_appoinments(self, appointment):
        self.__appoinments.append(appointment)

    def set_password(self, password):
        pass

    def set_username(self, u_name):
        pass

    def update_details(self, old, new):
        file=open("doctor_file.txt","r")
        data=file.read()
        data_temp=data.replace(old, new)
        file.close()
        temp=open("temp_file.txt","w")
        temp.write(data_temp)
        temp.close()
        os.remove("doctor_file.txt")
        os.rename("temp_file.txt","doctor_file.txt")
        # with open("doctor_file.txt",'r') as file:
        #     line=file.readline()
        #     while line!="":
        #         data=line.split(";")
        #         patient_str=data[5][13:-1].split(",")
        #         appoinment_str=data[6][17:-2].split(",")
        #         # doctors.append(Doctor(data[2], data[3],data[0],data[1],data[4],patient_str,appoinment_str))
        #         if 
        #         line=file.readline()


    def delete_doctor(self, name):
        with open("doctor_file.txt",'r') as file:
            lines=file.readlines()
            for each_line in lines:
                if name in each_line:
                    lines.pop(lines.index(each_line))
        with open("doctor_file.txt",'w') as file:
            for each_line in lines:
                file.write(each_line)

    def __str__(self) :
        return f"{self.full_name():^30}|{self.__speciality:^15}|{', '.join(self.__patients):^30}|{', '.join(self.__appoinments):^30}"