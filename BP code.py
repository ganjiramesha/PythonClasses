
diastolic = int(input("enter the diastolic: "))
systolic = int(input("enter the systolic: "))

if diastolic <= 59 and systolic <=80:
    print("Low BP_Immediate medical attension required")
elif diastolic <= 70 and systolic <=100:
    print("Below Normal")
elif diastolic <=80 and systolic <=120:
    print("Normal")
elif diastolic <=80 and systolic<=129 and systolic>=120:
    print("elevated")
elif diastolic >= 81  and diastolic <=89 and systolic<=139 and systolic>=130:
    print("High Blood Pressure Stage 1")
elif diastolic >=90 and systolic<=140:
    print("High Blood Pressure Stage 2")
elif diastolic >=120 and diastolic <= 140 and systolic>=180 and systolic <=250:
    print("Hyper Tensive Crisis_Emergency")
else:
    print("Invalid Input")
