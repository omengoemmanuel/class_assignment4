#program to accept marks and their respective grading
maths = int(input("Enter maths score:"))
phyicis = int(input("Enter physics Score:"))
Geo = int(input("Enter Geography Score:"))
Chem = int(input("Enter Chemistry Score:"))
if maths >=0 and maths <=30:
    print("Maths Grade:D")
elif maths <0:
    print("Maths Grade: Invalid Scores")
elif maths > 100:
    print("Maths Grade: Invalid Scores")
elif maths <=50:
    print("Maths Grade: C")
elif maths <=70:
    print("Maths Grade:B")
elif maths <=100:
    print("Maths Grade:A")
 
if phyicis >=0 and phyicis <=30:
    print("phyicis Grade:D")
elif phyicis <0:
    print("phyicis Grade: Invalid Scores")
elif phyicis >100:
    print("phyicis Grade: Invalid SCores")
elif phyicis <=50:
    print("phyicis Grade: C")
elif phyicis <=70:
    print("phyicis Grade:B")
else:
    print("phyicis Grade:A")

if Geo >=0 and Geo <=30:
    print("Geography Grade:D")
elif Geo <0:
    print("Geography Grade: Invalid Score")
elif Geo >100:
    print("Geography Grade:Invalid Score")
elif Geo <=50:
    print("Geography Grade:C")
elif Geo <=70:
    print("Geography Grade: B")
else:
    print("Geography Grade: A")

if Chem>=0 and Chem <=30:
    print("Chemistry Grade:D")
elif Chem <0:
    print("Chemistry Grade: Invalid Score")
elif Chem >100:
    print("Chemistry Grade:Invalid Score")
elif Chem <=50:
    print("Chemistry Grade:C")
elif Chem <=70:
    print("Chemistry Grade: B")
else:
    print("Chemistry Grade: A")









