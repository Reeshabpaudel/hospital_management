from Doctor import Doctor
from Patient import Patient
def login():
    user=None
    while user==None:
        username=input("Username:")
        for file_name in ["admin_file.txt", "doctor_file.txt", "patient_file.txt"]:
            file=open(file_name, "r")
            data=file.read().replace("\n",";").split(";")
            if username in data:
                password=input("password:")
                if data[data.index(username)+1]==password:
                    print("User found!")
                    user=file_name.split("_")[0]
                    return user
                else:
                    print("Wrong Password!Try again")
            file.close()





# doctors=[]
# doctors2 = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
        
# with open("admin_file.txt", 'r') as file:
#     data=file.readline().split(";")
#     u_name=data[0]
#     pass_w=data[1]
#     add=data[2]

# print(u_name, pass_w, add)
    
# with open("doctor_file.txt",'r') as file:
#     line=file.readline()
#     while line!="":
#         data=line.split(";")
#         fname=data[0]
#         lname=data[1]
#         spec=data[2]
#         doctors.append(Doctor(fname, lname, spec))
#         line=file.readline()

# print(doctors)
# print(doctors2)
# print(doctors[1].get_first_name())
# print(doctors2[1].get_first_name())



# patients=[]

# with open("patient_file.txt",'r') as file:
#     line=file.readline()
#     while line!="":
#         data=line.split(";")
#         f_name=data[0]
#         l_name=data[1]
#         age=data[2]
#         num=data[3]
#         add=data[4]
#         patients.append(Patient(f_name, l_name, age, num, add))
#         line=file.readline()

# print(patients[2].full_name())
# print(patients[2])

# def main():
#         print("i am in main")
#         not_main()

# def not_main():
#     print("I AM NOT IN MAIN")

# if __name__ == '__main__':
#     main()
