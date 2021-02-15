###############################################
# NAMESPACES
 
def Assign(i, f, s, b):
   # Write your code here

    w = i
    x = f
    y = s
    z = b
        
    print(i, f, s, b, dir(), sep='\n')    
 
 
############################################### 
# GET ADDITIONAL INFO
 
def docstring(functionname):
   # Write your code here

help(functionname)
 

###############################################
# PI

from math import pi

def calc(c):
    # Write your code here

    radius = c / (2*pi)
    area = (pi * (radius*radius))
    
    r  = radius
    a =  area
    return r,a
 
 
###############################################
# USING INT
 
 
def Integer_fun(a, b):
    # Write your code here

    c = int(a)
    d = int(b)
    
    print (type(a), type(b), c, d, type(c), type(d), sep="\n")
 
 
############################################### 
# OOPERATORS
 
def find(num1, num2, num3):
    # Write your code here

    true = True
    false = False
    print (true if num1 < num2 and num2 >= num3 else false, true if num1 > num2 and num2 <= num3 else false, true if num3 == num1 and num1 != num2 else false)
 
 
############################################### 
# USE INMATH OPERATORS
 
def Integer_Math(Side, Radius):
    # Write your code here

    area = Side * Side
    volumeCube = round(Side * Side * Side, 0)
    areaCircle = round(3.14 * (Radius * Radius), 2)
    volumeSphere = round((4* 3.14 * (Radius ** 3))/3, 2)
     
    print("Area of Square is " + str(area))
    print("Volume of Cube is " +  str(volumeCube))
    print("Area of Circle is " + str(areaCircle))
    print("Volume of Sphere is " + str(volumeSphere))
 
 
############################################### 
# USING FLOAT

from math import pi
  
def triangle(n1, n2, n3):
    # Write your code here

    area = (n1 * n2) / 2
    piValue = round(pi, n3)
    print(area, piValue)
    
    return area, round(pi, n3)
 

############################################### 
# SUBMIT FLOAT 2
  
def Float_fun(f1, f2, Power):
    # Write your code here

    print ("#Add")
    print(f1 + f2)
    print("#Subtract")
    print(f1 - f2)
    print("#Multiply")
    print(f1 * f2)
    print("#Divide")
    print(f2 / f1)
    print("#Remainder")
    print(f1 % f2)
    print("#To_The_Power_Of")
    print(f1 ** Power)
    print("#Round")
    print(round(f1 ** Power, 4))


############################################### 
# USING STRING OPERATORS
 
def stringoperation(fn, ln, para, number):
    # Write your code here

    print(fn)
    x = number
    while (number > 1):
        print()
        number = number - 1
    print (ln)
    print(fn, ln, sep="\t")
    print(fn * x)
    print("The sentence is " + para)
 
############################################### 
# NEWLINE AND TAB SPACING
 
def Escape(s1, s2, s3):
    # Write your code here

    print (s1, s2, s3, sep="\n")
    print(s1, s2, s3, sep="\t")
    print("Python", "Raw", sep="\t")
    print("String", "Concept", sep="\t")
    print(r"Python\tRaw\nString\tConcept") 
 
###############################################
# LIST OPERATIONS
 
def List_Op(Mylist, Mylist2):
    # Write your code here

    print(Mylist)
    print(Mylist[1])
    print(Mylist[-1])
    Mylist.append(3)
    Mylist[3] = 60
    print(Mylist)
    print(Mylist[1:5])
    Mylist.append(Mylist2)
    print(Mylist)
    Mylist.extend(Mylist2)
    print(Mylist)
    Mylist.pop()
    print(Mylist)
    print(len(Mylist))
 
###############################################
# LIST OPERATIONS
 
def tuplefunction(list1, list2, string1, n):
    # Write your code here

    tuple1 = tuple(list1)
    tuple2 = tuple(list2)
    tuple12 = (tuple1+tuple2)
    nestedTuple = ((tuple1, )+ (tuple2, ))
    tupleString = (string1, ) * n
    print (tuple12)
    print(tuple12[4])
    print(nestedTuple)
    print(len(nestedTuple))
    print(tupleString)
    print(max(tuple1))
 
###############################################
# PYTHON RANGE
 
def generateList(startvalue, endvalue):
    # Write your code here

    myList = list(range(startvalue,endvalue+1))
    seguidos = [myList[0], myList[1], myList[2]]
    seguidosInversos = [myList[-1], myList[-2], myList[-3], myList[-4], myList[-5]]
    pausas = list(range(startvalue,endvalue+1,4))
    pausasMenos = list(range(endvalue,startvalue-1,-2))
    print(seguidos)  
    print(seguidosInversos)
    print(pausas)
    print(pausasMenos)
 
 
############################################### 
# STRING OPERATOR 2
 
  first = first.strip().capitalize()
    second = second.strip().capitalize()
    parent = parent.strip().capitalize()
    city = city.strip()
    print(first, second, parent, city)
 
    if phone.isdigit():
        print(True)
    else:
        print(False)
    
    if phone.startswith(start):
        print(True)
    else:
        print(False)
        
    strings = first + second + parent + city
    print(strings.count(strfind))
    
    string1 = string1.split()
    print(string1)
    
    find = city.find(strfind)
    print(find)
    
###############################################
# DICTIONARIES
 
def myDict(key1, value1, key2, value2, value3, key3):
    myDict1 = {key1:value1}
    print(myDict1)
    myDict1[key2] = value2
    print(myDict1)
    myDict1[key1] = value3
    print(myDict1)
    del myDict1[key3]
    return((myDict1))
 
###############################################
# SET
 
def setOperation(seta, setb):
    seta = set(seta)
    setb = set(setb)
    
    union = seta.union(setb)
    intersec = seta.intersection(setb) 
    diff1 = seta.difference(setb)
    diff2 = setb.difference(seta)
    symetrycdiff = seta.symmetric_difference(setb)
    frozen = frozenset(seta)
    return(union,intersec,diff1,diff2,symetrycdiff,frozen)

###############################################
# FOR LOOP

def sumOfNFibonacciNumbers(n):
    if n == 1:
        return 0
    elif n in [0]:
        return 0
    elif n in [1,2]:
        return 1
    else:
        x = [0,1,1]
        [x.append(x[-1] + x[-2]) for n in range(n - len(x))]
        return sum(x)

###############################################
# IF CONDITIONAL 

def calculateGrade(students_marks):     
    res = []
    avg = 0
    soma = 0
    for i in range(len(students_marks)):
        for j in range(len(students_marks[i])):
            soma += students_marks[i][j]
        avg = soma / len(students_marks[i])
        soma = 0

        if (avg >= 90) and (avg < 100):
            res.append('A+')
        elif (avg >= 80) and (avg < 90):
            res.append('A')
        elif (avg >= 70) and (avg < 80):
            res.append('B')
        elif (avg >= 60) and (avg < 70):
            res.append('C')
        elif (avg >= 50) and (avg < 60):
            res.append('D')
        else:
            res.append('F')

    return(res)