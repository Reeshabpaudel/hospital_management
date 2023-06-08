# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    # admin = Admin('admin','123','B1 1AB') # username is 'admin', password is '123'
    # doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    # patients = [Patient('Sara','Smith', 20, '07012345678','B1 234'), Patient('Mike','Jones', 37,'07555551234','L2 2AB'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC')]
    
    discharged_patients = []
    doctors=[]
    patients=[]


    admin=Admin()
    with open("doctor_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            patient_str=data[5][13:-1].split(",")
            appoinment_str=data[6][17:-2].split(",")
            doctors.append(Doctor(data[2], data[3],data[0],data[1],data[4],patient_str,appoinment_str))
            line=file.readline()
    with open("patient_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            patients.append(Patient(data[2], data[3], data[0], data[1], data[4], data[5], data[6], data[7], data[8], data[9]))
            line=file.readline()
    with open("discharged_patients_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            discharged_patients.append(Patient(data[2], data[3], data[0], data[1], data[4], data[5], data[6]))
            line=file.readline()


        

    #try to get info form file so that each piece of info is saved
    
    usertype=login()
    # keep trying to login tell the login details are correct
    # while True:
    #     if admin.login():
    #         running = True # allow the program to run
    #         break
    #     else:
    #         print('Try again')
    if usertype[0]=="admin":
        print("You are logged in as admin")
        while True:
            # print the menu
            print('Choose the operation:')
            print(' 1- Register/view/update/delete doctor')
            print(' 2- Discharge patients')
            print(' 3- View discharged patient')
            print(' 4- Assign doctor to a patient')
            print(' 5- Update admin detais')
            print(' 6- Register/view patient')
            print(' 7- Get management report')
            print(' 8- Quit')

            # get the option
            op = input('Option: ')

            if op == '1':
                # 1- Register/view/update/delete doctor
                #ToDo1
                admin.doctor_management(doctors)

            elif op == '2':
                # 2- View or discharge patients
                #ToDo2
                while True:
                    op = input('Do you want to discharge a patient(Y/N):').lower()

                    if op == 'yes' or op == 'y':
                        #ToDo3
                        admin.discharge(patients, discharged_patients)

                    elif op == 'no' or op == 'n':
                        break

                    # unexpected entry
                    else:
                        print('Please answer by yes or no.')
            
            elif op == '3':
                # 3 - view discharged patients
                #ToDo4
                if discharged_patients==[]:
                    print("--------------No patients discharged yet------------")
                else:
                    admin.view_discharged(discharged_patients)

            elif op == '4':
                # 4- Assign doctor to a patient
                admin.assign_doctor_to_patient(patients, doctors)

            elif op == '5':
                # 5- Update admin detais
                admin.update_details()

            elif op=='6':
                admin.patient_management(patients, doctors)

            elif op == '7':
                # 6 - Quit
                #ToDo5
                admin.display_report(patients, doctors)
            
            elif op=='8':
                break

            else:
                # the user did not enter an option that exists in the menu
                print('Invalid option. Try again')
    elif usertype[0]=="doctor":
        print("Welcome! You have logged in as a doctor")
        docname=usertype[1]
        for docs in doctors:
            if docs.get_username()==docname:
                me=docs
        while True:
            print("""
    Choose operation:
    1- View patients
    2- Place patient under my care
    3- View/Update my details
    4- Change username/password
    5- quit""")
            op=input("Your option: ")
            if op=="1":
                print("-------Patient Details--------")
                admin.view(patients)
            elif op=="2":
                print("-------Patient Details------")
                admin.view(patients)
                patient_index=input("Please enter the patient ID: ")
                try:
                    patient_index=int(patient_index)-1
                    if patient_index not in range(len(patients)):
                        print('The id entered was not found.')
                        break
                except ValueError:
                    print("The id entered is not correct")
                    break
                me.add_patient(patients[patient_index].full_name())
                patients[patient_index].link(me.full_name())

            elif op=="3":
                print("1- View Details")
                print("2- Update Details")
                op_t=input("Your choice: ")
                if op_t=="1":
                    print("------Your Details----")
                    print("   |      Full name             |  Speciality   |           Patients           |         Appoinments        ")
                    print(f"{'':3}|{me}")
                elif op_t=="2":
                        print('Choose the field to be updated:')
                        print(' 1 First name')
                        print(' 2 Surname')
                        print(' 3 Speciality')
                        f_op = input('Input: ') # make the user input lowercase
                        if f_op=="1":
                            new_firstname=input("Enter the new first name: ")
                            me.update_details(me.get_first_name(), new_firstname)
                            me.set_first_name(new_firstname)
                            
                            print("Your first name is updated.")
                            print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                            admin.view(doctors)
                        elif f_op=="2":
                            new_surname=input("Enter the new surname: ")
                            me.update_details(me.get_surname(), new_surname)
                            me.set_surname(new_surname)
                            print("Your surname is updated.")
                            print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                            admin.view(doctors)
                        elif f_op=="3":
                            new_spec=input("Enter the new speciality: ")
                            me.update_details(me.get_speciality(), new_spec)
                            me.set_speciality(new_spec)
                            print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                            admin.view(doctors)
                        else:
                            print("Field not available")
                else:
                    print("Sorry! Invalid option")
            elif op=="4":
                print("1- password")
                print("2- username")
                op_s=input("input: ")
                if op_s=="1":
                    username=input('Enter the new username: ')
                    if username==input('Confirmed username again: '):
                        print("Confirmed!")
                        me.update_details(me.get_usernamem(), username)
                    else:
                        print("Sorry! couldn't be confirmed")
                elif op_s=="2":
                    password=input("Enter the new password:")
                    if password==input("Confirm password:"):
                        print("Confirmed")
                        me.update_details(me.get_password(), password)
                else:
                    print()
            elif op=="5":
                break
            else:
                print("Invalid Option! Please try again.")

    elif usertype[0]=="patient":
        print("Welcome! You have logged in as patient")
        pat_name=usertype[1]
        for patient in patients:
            if patient.get_username()==pat_name:
                me=patient
        while True:
            print("""
    Chose an option:
    1- View details
    2- Apply for appointment
    3- Update Details
    4- Change username/password
    5- quit""")
            op=input("Your option: ")
            if op=="1":
                print("----Your Details----")
                print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
                print(f"{me}")
            elif op=="2":
                print("ID |      Full name               |  Speciality   |           Patients           |         Appoinments        ")
                admin.view(doctors)
                doctor_index=input("Please enter the doctor ID: ")
                try:
                    doctor_index=int(doctor_index)-1
                    if admin.find_index(doctor_index, doctors)!=False:
                        doctors[doctor_index].add_patient(me.full_name())
                        appointment=input("Enter date and time for appointment:")
                        print("Appointment is now set!")
                        me.set_appointment(appointment)
                    else:
                        print("The entered id is not found")
                except ValueError:
                    print("The id entered is incorrect")
            elif op=="3":
                print('Choose the field to be updated:')
                print(' 1- First name')
                print(' 2- Surname')
                print(' 3- Symptoms')
                
                f_op = input('Input: ') # make the user input lowercase
                if f_op=="1":
                    new_firstname=input("Enter the new first name: ")
                    me.update_details(me.get_first_name(), new_firstname)
                    me.set_first_name(new_firstname)                
                    print("Your first name is updated.")
                    print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
                    admin.view(patients)
                elif f_op=="2":
                    new_surname=input("Enter the new surname: ")
                    me.update_details(me.get_surname(), new_surname)
                    me.set_surname(new_surname)
                    print("Your surname is updated.")
                    print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
                    admin.view(patients)
                elif f_op=="3":
                    new_symp=input("Enter the syptom: ")
                    me.update_details(me.symptoms, new_symp)
                    me.set_symptoms(new_symp)
                    print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |           Symptoms           |  Appointments   ')
                    admin.view(patients)
                else:
                    print("Field not available")
            elif op=="4":
                print("1- username")
                print("2- password")
                op_s=input("input: ")
                if op_s=="1":
                    username=input('Enter the new username: ')
                    if username==input('Confirmed username again: '):
                        print("Confirmed!")
                        me.update_details(me.get_username(), username)
                    else:
                        print("Sorry! couldn't be confirmed")
                elif op_s=="2":
                    password=input("Enter the new password:")
                    if password==input("Confirm password:"):
                        print("Confirmed")
                        me.update_details(me.get_password(), password)
                else:
                    print("Field not available")
            elif op=="5":
                break
            else:
                print("Invalid Option! Please try again.")
    

def login():
    usertype=None
    while usertype==None:
        username=input("Username:")
        for file_name in ["admin_file.txt", "doctor_file.txt", "patient_file.txt"]:
            file=open(file_name, "r")
            data=file.read().replace("\n",";").split(";")
            if username in data:
                password=input("password:")
                if data[data.index(username)+1]==password:
                    usertype=file_name.split("_")[0]
                    return usertype, username
                else:
                    print("Wrong Password!Try again")
            file.close()

            
if __name__ == '__main__':
    main()
