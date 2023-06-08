from Doctor import Doctor
from Patient import Patient
import os

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """
        file=open("admin_file.txt",'r')
        data=file.read().split(';')
        self.__username = data[0]
        self.__password = data[1]
        self.__address =  data[2]
        file.close()

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def for_report(self, a_list):
        string=''
        for index, item in enumerate(a_list):
            string+=(f'{index+1:3}|{item}\n')
        return string

    def admin_details(self):
        print(f"Username:{self.__username}")
        print(f"Password:{self.__password}")
        print(f"Address:{self.__address}")

    # def login(self) :
    #     """
    #     A method that deals with the login
    #     Raises:
    #         Exception: returned when the username and the password ...
    #                 ... don`t match the data registered
    #     Returns:
    #         string: the username
    #     """
    
    #     print("-----Login-----")
    #     #Get the details of the admin
    #     username = input('Enter the username: ')
    #     if(self.__username==username):
    #         password = input('Enter the password: ')
    #         if(self.__password==password):
    #             return True
    #         else:
    #             print ("Incorrect password!")
    #     else:
    #         print("Username not found!")
    #     # check if the username and password match the registered ones
    #     #ToDo1 done1
    #     # if(self.__username==username and self.__password==password):
    #     #     return True
    #     # else:
    #     #     return False

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self, doctors) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """

        doc_fname=input("Enter the first name of the doctor:")
        doc_sname=input("Enter the surname of the doctor:")
        # check if the name is already registered
        name_exists = self.is_exists(doctors, doc_fname, doc_sname)
        while name_exists==True:
            print("Please enter name again!")
            doc_fname=input("First-name: ")
            doc_sname=input("Last-name: ")
            name_exists=self.is_exists(doctors, doc_fname, doc_sname)
        #ToDo2 done!
        
        doc_spec=input("Enter the speciality of the doctor:")
        doc_username=input("Enter username for doctor(actual name not recommended): ")
        while True:
            doc_pass=input("Create a password(try not to include your name): ")
            pass_confirm=input("Confirm password: ")
            if doc_pass==pass_confirm:
                return doc_fname, doc_sname, doc_spec, doc_username, doc_pass
            else:
                print("Sorry, password couldn't be confirmed")

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op=input("Your option?:")

        # register
        if op == '1':
            print("-----Register-----")

            print('Enter the doctor\'s details:')
            #ToDo4

            # get the doctor details
            try:
                doc_fname, doc_sname, doc_spec, doc_uname, doc_pass=self.get_doctor_details(doctors)

                

                #ToDo6
                # add the doctor ...
                # ... to the list of doctors
                doctors.append(Doctor(doc_fname, doc_sname, doc_spec, doc_uname, doc_pass,))           
                with open("doctor_file.txt",'a') as file:
                    file.write(f"\n{doc_uname};{doc_pass};{doc_fname};{doc_sname};{doc_spec};patient_list[];appoinment_list[]")
                    file.close()
                print('Doctor registered.')
                self.view(doctors)
            except TypeError:
                print("Please try again!")

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:
                         # menu
                        print('Choose the field to be updated:')
                        print(' 1 First name')
                        print(' 2 Surname')
                        print(' 3 Speciality')
                        f_op = int(input('Input: ')) # make the user input lowercase
                        if f_op==1:
                            print(doctors[index])
                            new_firstname=input("Enter the new first name: ")
                            doctors[index].update_details(doctors[index].get_first_name(), new_firstname)
                            doctors[index].set_first_name(new_firstname)
                            
                            print("Your first name is updated.")
                            self.view(doctors)
                        elif f_op==2:
                            new_surname=input("Enter the new surname: ")
                            doctors[index].update_details(doctors[index].get_surname(), new_surname)
                            doctors[index].set_surname(new_surname)
                            print("Your surname is updated.")
                            self.view(doctors)
                        elif f_op==3:
                            new_spec=input("Enter the new speciality: ")
                            doctors[index].update_details(doctors[index].get_speciality(), new_spec)
                            doctors[index].set_speciality(new_spec)
                            self.view(doctors)
                        else:
                            print("Field not available")
                    else:
                        print("Doctor not found")
                        # doctor_index is the ID mines one (-1)
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

           

            #ToDo8 done inside try

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
            self.view(doctors)

            index = int(input('Enter the ID of the doctor to be deleted: '))-1
            doctor_index=self.find_index(index, doctors)
            if(doctor_index!=False):
                doctors[index].delete_person(doctors[index].get_first_name())
                doctors.pop(index)
                print("Doctor deleted")
                self.view(doctors)
            #ToDo9
            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def get_patient_detail(self):
        #get the details of patients
        p_fname=input("Enter the first name of patient: ")
        p_sname=input("Enter the surname of the patient: ")
        p_symp=input("Enter the symptoms: ")
        p_age=input("Enter age: ")
        p_phnum=input("Enter phone number: ")
        p_post=input("Enter postcode: ")
        p_uname=input("Create a username so that patient can log-in(recommended username is other than name): ")
        p_pass=input("Create a password (try not to incude patient name): ")
        if p_pass==input("Confirm password: "):
            return p_uname, p_pass, p_fname, p_sname, p_age,p_phnum, p_post, p_symp
        else:
            print("Sorry, password couldn't be confirmed")

    
    
    def patient_management(self, patients, doctors):
        print("-----Patient Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        op=input("Please inter your option: ")
        if op=="1":
            print("-------Register patients------")
            print("Enter the patient's details:")
            try:
                pat_uname,pat_pass,pat_name,pat_surname,pat_age,pat_ph_num,pat_post,pat_symp=self.get_patient_detail()
                patients.append(Patient(pat_name, pat_surname, pat_uname, pat_pass, pat_age, pat_ph_num,pat_post,pat_symp))
    
                with open("patient_file.txt",'a') as file:
                    file.write(f"\n{pat_uname};{pat_pass};{pat_name};{pat_surname};{pat_age};{pat_ph_num};{pat_post};{pat_symp};doctor;appointment")
                print("Patient registered.")
                op_1=input("Do you want to set doctor?(y/n) ")
                if op_1.upper()=="YES" or op_1.upper()=='Y':
                        self.assign_doctor_to_patient(patients, doctors)
            except TypeError:
                print("Try again")
        elif op=="2":
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
            self.view(patients)
        else:
            print("Sorry, operation not identified")

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                
                print('The patient is now assign to the doctor.')
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')

                self.view(patients)

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        self.view(patients)
        try:
            patient_index = int(input('Please enter the patient ID: '))-1
            if patient_index in range(len(patients)):
                name=patients[patient_index].full_name()
                with open("patient_file.txt","r") as file:
                    line=file.readline()
                    while line!="":
                        check_name=line.split(";")[2]+" "+line.split(";")[3]
                        if check_name==name:
                            with open("discharged_patients_file.txt",'a') as write_file:
                                write_file.write(line)
                                print(name.split()[0])
                                patients[patient_index].delete_person(name.split()[0])
                      
                        line=file.readline()
                discharged_patients.append(patients.pop(patient_index))
            else:
                print("id not found")
            self.view(patients)
        except TypeError:
            print("such id cannot be accepted")
        #ToDo12
        

    def view_discharged(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
        #ToDo13
        self.view(discharged_patients)

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = input('Input: ')
        
        if op == "1":
            #ToDo14
            self.admin_details()
            username1=input('Enter the new username: ')
            #validate the username
            username2=input("Enter the new username again: ")
            if(username1==username2):
                print("Username matched.")
                self.upadate_admin_details(self.__username,username1)
                print("--------------------------------------")
                self.admin_details()
                print("----------Username updated---------")
            else:
                print("Username not matched")

        elif op == "2":
            self.admin_details()
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                print("Password matched")
                self.upadate_admin_details(self.__password,password)
                print("--------------------------------------")
                self.admin_details()
                print("------Password updated-----")
            else:
                print("Password not matched")

        elif op == "3":
            #ToDo15
            self.admin_details()
            address=input("Enter the new address: ")
            #validate the address
            if address==input("Enter the new address again: "):
                print("Address matched!")
                self.upadate_admin_details(self.__address,address)
                print("--------------------------------------")
                self.admin_details()
                print("-----Address updated-----")
            else:
                print("Address not matched!")
        else:
            #ToDo16
            print("invalid choice")

    def is_exists(self, doctors,fname, sname):
        for doctor in doctors:
            if fname == doctor.get_first_name() and sname == doctor.get_surname():
                print('Name already exists.')
                #ToDo5 
                return True
            
    def upadate_admin_details(self, old, new):
        file=open("admin_file.txt","r")
        data=file.read()
        data_temp=data.replace(old, new)
        file.close()
        temp=open("temp_file.txt","w")
        temp.write(data_temp)
        temp.close()
        os.remove("admin_file.txt")
        os.rename("temp_file.txt","admin_file.txt")
        self.__init__()
            
    def display_report(self, patients, doctors):
        import tkinter
        self.window=tkinter.Tk()
        self.window.title("Admin Management Report")
        self.window.geometry("800x700")
        self.window.config(background='#eef8ff')
        self.doctor_frame=tkinter.Frame(self.window, bg="#EEF8FF")
        self.patient_frame=tkinter.Frame(self.window, bg="#eef8ff")
        # self.doc_var=tkinter.StringVar()
        # self.pat_var=tkinter.StringVar()

        self.heading=tkinter.Label(self.window, text="Management Report", font=("", 20, "bold"), bg="#EEF8FF", pady=20)
        
        # self.pat_var.set(f"ID |      Full name               |  Speciality   |           Patients           |         Appoinments        \n{self.for_report(doctors)}")
        # self.doc_var.set(f"ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode \n{self.for_report(patients)}")

        self.display_doc_list=tkinter.Label(self.doctor_frame, text="Doctors List",bg="#EEF8FF", font=("",15,"underline"))
        self.display_doc_list.grid(column=5, pady=15)

        tkinter.Label(self.doctor_frame, text="Username", bg="#EEF8FF", font=("",14)).grid(row=1, column=1, padx=10, pady=10)
        tkinter.Label(self.doctor_frame, text="Password", bg="#EEF8FF", font=("",14)).grid(row=1, column=2, padx=10, pady=10)
        tkinter.Label(self.doctor_frame, text="First Name", bg="#EEF8FF", font=("",14)).grid(row=1, column=3, padx=10, pady=10)
        tkinter.Label(self.doctor_frame, text="Last Name", bg="#EEF8FF", font=("",14)).grid(row=1, column=4, padx=10, pady=10)
        tkinter.Label(self.doctor_frame, text="Speciality", bg="#EEF8FF", font=("",14)).grid(row=1, column=5, padx=10, pady=10)   
        tkinter.Label(self.doctor_frame, text="Patients", bg="#EEF8FF", font=("",14)).grid(row=1, column=6, padx=10, pady=10)   
        tkinter.Label(self.doctor_frame, text="Appointment", bg="#EEF8FF", font=("",14)).grid(row=1, column=7, padx=10, pady=10)   

        with open("doctor_file.txt",'r') as file:
            data=file.readlines()
        for i in range (len(data)):
            row_data=data[i].strip().split(";")
            for j in range(len(row_data)):
                doctor_info=tkinter.Label(self.doctor_frame,bg="#EEF8FF", text=row_data[j])
                doctor_info.grid(row=i+2, column=j+1, padx=10, pady=10)



        self.display_pat_list=tkinter.Label(self.patient_frame, text="Patients List",bg="#EEF8FF", font=("",15,"underline"))
        self.display_pat_list.grid(column=5, pady=15)

        # tkinter.Label(self.patient_frame, text="Name", bg="#EEF8FF").grid(row=1, column=1, padx=10, pady=10)
        # tkinter.Label(self.patient_frame, text="Age", bg="#EEF8FF").grid(row=1, column=2, padx=10, pady=10)
        # tkinter.Label(self.patient_frame, text="Address", bg="#EEF8FF").grid(row=1, column=3, padx=10, pady=10)

        tkinter.Label(self.patient_frame, text="Username", bg="#EEF8FF", font=("",14)).grid(row=1, column=0, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Password", bg="#EEF8FF", font=("",14)).grid(row=1, column=1, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="First name", bg="#EEF8FF", font=("",14)).grid(row=1, column=2, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Last name", bg="#EEF8FF", font=("",14)).grid(row=1, column=3, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Age", bg="#EEF8FF", font=("",14)).grid(row=1, column=5, padx=4, pady=10)
        tkinter.Label(self.patient_frame, text="Phone Number", bg="#EEF8FF", font=("",14)).grid(row=1, column=5, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Postcode", bg="#EEF8FF", font=("",14)).grid(row=1, column=6, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Symptoms", bg="#EEF8FF", font=("",14)).grid(row=1, column=7, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Doctor", bg="#EEF8FF", font=("",14)).grid(row=1, column=8, padx=10, pady=10)
        tkinter.Label(self.patient_frame, text="Appointment", bg="#EEF8FF", font=("",14)).grid(row=1, column=9, padx=10, pady=10)


        with open("patient_file.txt",'r') as file:
            data=file.readlines()
        for i in range (len(data)):
            row_data=data[i].strip().split(";")
            for j in range(len(row_data)):
                patient_info=tkinter.Label(self.patient_frame, text=row_data[j], bg="#EEF8FF")
                patient_info.grid(row=i+3, column=j, padx=10, pady=10)

        self.heading.pack(side="top")
        self.doctor_frame.pack()
        self.patient_frame.pack()




        tkinter.mainloop()