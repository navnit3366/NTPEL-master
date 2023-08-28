line=''
course=[]
student=[]
grade=[]

try:
    infile=open("input.txt","w")
    outfile=open("output.txt","w")
except:
    print("Could'nt open the file:",EOFError)
    exit()
while(line!='EndOfInput\n'):
       line=input()+'\n'
       infile.write(line) 
infile.close()

def mark(gp):
    if gp=='A':
        return 10.0
    elif gp=='AB':
        return 9.0
    elif gp=='B':
        return 8.0
    elif gp=='BC':
        return 7.0
    elif gp=='C':
        return 6.0
    elif gp=='CD':
        return 5.0
    elif gp=='D':
        return 4.0
    else:
        return 0

f=open("input.txt","r")
f.readline().rstrip()

while True:
    line=f.readline().rstrip()
    if line=='Students':
        break
    course.append(line)
j=0
for i in course:
    a=str(i).split('~')
    course[j]=a[0]
    j+=1
#print(course)

while True:
    line=f.readline().rstrip()
    if line=='Grades':
        break
    student.append(line)
j=0
for i in student:
    a=str(i).split('~')
    student[j]=[a[0],a[1]]
    j+=1
#print(student)

while True:
    line=f.readline().rstrip()
    if line=='EndOfInput':
        break
    grade.append(line)
j=0
for i in grade:
    a=str(i).split('~')
    grade[j]=[a[0],a[3],a[4]]
    j+=1
#print(grade)

for i in grade:
    j=0
    while i[1] not in student[j][0]:
        j+=1
    student[j].append(mark(i[2]))
#print(student)

for index, i in enumerate(student):
    if len(i)==2:
        student[index].append(0)
    else:
        sum=0
        for j in range(2,len(i)):
            sum+=student[index][j]
        student[index]=i[:2]+[round((sum/(len(i)-2)),2)]
student.sort()
for i in student:
    p=i[0]+'~'+i[1]+'~'+str(i[2])+'\n'
    outfile.write(p)
outfile.close()
