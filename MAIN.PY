#.....................................................
#            SCHOOL MANAGEMENT SYSTEM
#.....................................................
#1.Total number of students
#2.Display student details
#3.Add new students
#4.Update student details
#5.Delet student details
#6.Exit

students={
'ID1':{'name':'alfaiz','DOB':'26-6-2006','class':'12'},
'ID2':{'name':'faizal','DOB':'22-9-2009','class':'11'},
'ID3':{'name':'parth','DOB':'12-5-2007','class':'11'},
}
Teachers={
'ID1':{'name':'MR. Alfaiz Abbas','DOB':'26-6-2006','Adress':'Mahyesh Nagar'},
'ID2':{'name':'MR. faizal abbas','DOB':'22-9-2009','Adress':'PNT colony'},
'ID3':{'name':'MR.Parth Meena','DOB':'12-5-2007','Adress':'laxman Pura'},
}

while True :
    print(''' .....................................................
            SCHOOL MANAGEMENT SYSTEM
.....................................................
1.Total number of students
2.Display student details
3.Add new students
4.Update student details
5.Delete student details
6.Admin Panel
7.Exit ''')

    choice=int(input())

    if choice==1:
        print(f"total number of students:{len(students)}")
    elif choice==2:
        s_id=input("enter student ID:")
        print("student details")
        s_d=students[s_id]
        print(f'name:{s_d["name"]}')
        print(f'DOB:{s_d["DOB"]}')
        print(f'class:{s_d["class"]}')
    elif choice==3:
            print ("add students")
            name=input('enter name:')
            dob=input('enter DOB:')
            class_1=input('enter class:')
            sid=input('enter ID:')
            students[sid]={'name':name,'dob':dob,'class':class_1}
    elif choice==4:
        print("update student")
        s_id=input("enter student ID:")
        print("student details")
        s_d=students[s_id]
        print(f'name:{s_d["name"]}')
        print(f'DOB:{s_d["dob"]}')
        print(f'class:{s_d["class"]}')
        s_d["name"]=input('update name:')
        s_d["DOB"]=input('update DOB:')
        s_d["class_1"]=input('update class:')
    elif choice==5:
        print("delet student")
        s_id=input("enter student ID:")
        print("student details")
        s_d=students[s_id]
        print(f'name:{s_d["name"]}')
        print(f'DOB:{s_d["DOB"]}')
        print(f'class:{s_d["class"]}')
        s_d["name"]=input('delet name:')
        s_d["dob"]=input('delet DOB:')
        s_d["class"]=input('delet class:')
    elif choice==6:
        print("you have chossen admin pannel")
        id_admin=input('Enter Your ID:- ')
        password=input("Enter Your password:- ")
        if id_admin=="admin123" and password=="123":
            while True :
                 print(''' .....................................................
               Admin Pannel
.....................................................
1.Total number of Teachers
2.Display Teachers details
3.Add new Teachers
4.Update Teachers details
5.Delete Teachers details
6.Admin Panel
7.Exit ''')
                 Admin=int(input())

                 if Admin==1:
                   print(f"total number of Teacher:{len(Teachers)}")
                 elif Admin==2:
                    T_ID=input("enter teacher ID:")
                    print("teacher details")
                    T_D=Teachers[T_ID]
                    print(f'name:{T_D["name"]}')
                    print(f'DOB:{T_D["DOB"]}')
                 elif Admin==3:
                    print ("add Teachers")
                    name=input('enter name:')
                    dob=input('enter DOB:')
                    Adress=input('enter Adress:')
                    T_ID=input('enter ID:')
                    Teachers[T_ID]={'name':name,'dob':dob,'Adress':Adress}
                 elif Admin==4:
                    print("update teacher")
                    T_ID=input("enter teacher ID:")
                    print("teachers details")
                    T_D=Teachers[T_ID]
                    print(f'name:{T_D["name"]}')
                    print(f'DOB:{T_D["DOB"]}')
                    print(f'Adress:{T_D["Adress"]}')
                    T_D["name"]=input('update name:')
                    T_D["Adress"]=input('update Adress:')
                 elif Admin==5:
                    print("delete Teacher")
                    T_ID=input("enter teacher ID:")
                    print("Teachers details")
                    T_D=Teachers[T_ID]
                    print(f'name:{T_D["name"]}')
                    print(f'DOB:{T_D["DOB"]}')
                    print(f'Adress:{T_D["Adress"]}')
                    T_D["name"]=input('delete name:')
                    T_D["DOB"]=input('delete DOB:')
                    T_D["Adress"]=input('delete Adress:')
        else:
           print("******incorrect password*********")
    else:
        break 

    



