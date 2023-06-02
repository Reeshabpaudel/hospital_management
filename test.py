from Doctor import Doctor
from Patient import Patient
import os
# def login():
#     user=None
#     while user==None:
#         username=input("Username:")
#         for file_name in ["admin_file.txt", "doctor_file.txt", "patient_file.txt"]:
#             file=open(file_name, "r")
#             data=file.read().replace("\n",";").split(";")
#             if username in data:
#                 password=input("password:")
#                 if data[data.index(username)+1]==password:
#                     print("User found!")
#                     user=file_name.split("_")[0]
#                     return user
#                 else:
#                     print("Wrong Password!Try again")
#             file.close()





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

# def get_data():
#     with open("admin_file.txt",'r') as file:
#         data=file.read().split(";")
#         username=data[0]
#         password=data[1]
#         address=data[2]
#     return username, password, address

# def updatate_details(old, new):
#     file=open("admin_file.txt","r")
#     data=file.read()
#     print(data)
#     data_temp=data.replace(old, new)
#     print(data)
#     file.close()
#     temp=open("temp_file.txt","w")
#     temp.write(data_temp)
#     temp.close()
#     os.remove("admin_file.txt")
#     os.rename("temp_file.txt","admin_file.txt")
# def update_data():
#     old_uname, old_pass, old_add=get_data()
#     print("""
#     Menu:
#     1, username
#     2, password
#     3, address""")
#     op=input("Select : ")
#     # file=open("admin_file.txt","r")
#     # temp_file=open("temp_file.txt",'w')
#     # data=file.read().split(';')
#     if op=="1":
#         new_name=input("Enter new name: ")
#         updatate_details(old_uname, new_name)
#         # for item in data:
#         #     if(item==old_uname):
#         #         temp_file.write(f"{new_name};")
#         #     else:
#         #         temp_file.write(f"{item};")
#         # file.close()
#         # temp_file.close()
#         # os.remove("admin_file.txt")
#         # os.rename("temp_file.txt","admin_file.txt")

#     elif op=="2":
#         new_pass=input("new pass: ")
#         updatate_details(old_pass, new_pass)
#     elif op=="3":
#         new_add=input("new add:")
#         updatate_details(old_add, new_add)
#     else:
#         print("Invalid Choice")
# update_data()
# print(get_data())

# with open("doctor_file.txt") as file:
    # data=file.readline().split(";")
    # print(data)
    # patient_str=data[6][13:-1].split(",")
    # print(patient_str)
    # file.close()

# my_doc=Doctor('reeshab',"paudel","heart",["sara"],["3pm","sara"])
# print(my_doc)
# my_patient=Patient("first","anu",23,8787,"999")
# print(my_patient)

# with open("doctor_file.txt",'a') as file:
#     file.write("\nname;bla;bla")

# my_list=["ka",'kha','ga','ghaa']
# print(my_list.index())
# my_list.insert(my_list.index("kha"),"papaya")