import os
class Person:
    def __init__(self, first_name, surname, username, password, type):
        self.first_name=first_name
        self.surname=surname
        self.username=username
        self.password=password
        self.type=type
        if(self.type=="doctor"):
            self.file="doctor_file.txt"
        elif(self.type=="patient"):
            self.file="patient_file.txt"

    def full_name(self):
        return self.first_name+' '+self.surname
    
    def get_first_name(self):
        return self.first_name
    
    def set_first_name(self,file_name, new_first_name):
        self.update_personal_details(file_name, self.first_name, new_first_name)
        self.first_name=new_first_name
        
    def get_surname(self):
        return self.surname
    
    def set_surname(self, new_surname):
        self.update_personal_details(self.surname, new_surname)
        self.surname=new_surname

    def get_password(self):
        return self.password
    
    def set_password(self, new_pass):
        self.update_details(self.password, new_pass)
        self.password=new_pass

    def get_username(self, new_uname):
        self.update_details( self.first_name, new_uname)
        self.username=new_uname

    def update_details(self, old, new):
        file_name=self.file
        file=open(self.file,'r')
        data=file.read()
        data_temp=data.replace(old, new)
        file.close()
        temp=open("temp_file.txt",'w')
        temp.write(data_temp)
        temp.close()
        os.remove(self.file)
        os.rename("temp_file.txt",file_name)

    def delete_person(self, name):
        with open(self.file,'r') as file:
            lines=file.readlines()
            for each_line in lines:
                if name in each_line:
                    lines.pop(lines.index(each_line))
        with open(self.file,'w') as file:
            for line in lines:
                file.write(line)
        
        