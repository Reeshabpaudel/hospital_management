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

    with open("admin_file.txt", 'r') as file:
        data=file.readline().split(";")
        admin=Admin(data[0], data[1], data[2])
    with open("doctor_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            doctors.append(Doctor(data[2], data[3], data[4]))
            line=file.readline()
    with open("patient_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            patients.append(Patient(data[2], data[3], data[4], data[5], data[6]))
            line=file.readline()
    with open("discharged_patients_file.txt",'r') as file:
        line=file.readline()
        while line!="":
            data=line.split(";")
            discharged_patients.append(Patient(data[2], data[3], data[4], data[5], data[6]))
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
    if usertype=="admin":
        print("You are logged in as admin")
        while True:
            # print the menu
            print('Choose the operation:')
            print(' 1- Register/view/update/delete doctor')
            print(' 2- Discharge patients')
            print(' 3- View discharged patient')
            print(' 4- Assign doctor to a patient')
            print(' 5- Update admin detais')
            print(' 6- Quit')

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
                admin.view_discharged(discharged_patients)

            elif op == '4':
                # 4- Assign doctor to a patient
                admin.assign_doctor_to_patient(patients, doctors)

            elif op == '5':
                # 5- Update admin detais
                admin.update_details()

            elif op == '6':
                # 6 - Quit
                #ToDo5
                break

            else:
                # the user did not enter an option that exists in the menu
                print('Invalid option. Try again')
    elif usertype=="doctor":
        print("Now doctor does what he does")
    elif usertype=="patient":
        print("now patient does what he does")
    else:
        pass 

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
                    print("User found!")
                    usertype=file_name.split("_")[0]
                    return usertype
                else:
                    print("Wrong Password!Try again")
            file.close()

            
if __name__ == '__main__':
    main()
