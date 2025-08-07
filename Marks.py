try:
    marksheet={"Alice":85}
    name=str(input("Enter name of the student: ")) #to input data as string
    print(name,"'s marks: ",marksheet[name])

except:
    print("Student not found") #not very conversent with get() function hence used try except method


