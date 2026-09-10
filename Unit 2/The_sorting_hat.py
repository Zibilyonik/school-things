Red=[]
Green=[]
White=[]
Blue=[]


Tech_knowladgebased=["math","computer science", "geometry"]
Humanities_Social=["business","geography","tok","history"]
Artistic_communicational=["psychology","advisory","english","pe"]



def sort(students):
    all_groups=[Red,Green,White,Blue]
    global group
    global group1
    for group in all_groups:
        for student in group:
            for hobby in student ["hobbies"]:
                hobby_group=[]
                hobby_group.append(hobby)
                for learn_style in student ["learning_style"]:
                    learning_allg=[]
                    learning_allg.append(learn_style)
                if hobby in hobby_group or learn_style in learning_allg >1:
                    group.remove(student)
                    group1.append(student)
    print (*((f"{student} is in " f"{group1}" or f"{group}" ) for student in students), sep="\n")

        



def student_color1(student):
        subs=student["subjects"]
        tech_approach=sum(1 for s in subs if s in Tech_knowladgebased)
        humanities_approach=sum(1 for s in subs if s in Humanities_Social)
        artistic_approach=sum(1 for s in subs if s in Artistic_communicational)
        mix_approach=sum(1 for s in subs if s in Tech_knowladgebased+Humanities_Social+Artistic_communicational)
        if tech_approach>=1:
            color1="Red"
        elif humanities_approach>=1:
            color1="Green"
        elif artistic_approach>=1:
            color1="Blue"
        elif mix_approach==2:
            color1="White"
        student["group1"]=color1
        return student


def student_color(student):
        subs=student["subjects"]
        tech_approach=sum(1 for s in subs if s in Tech_knowladgebased)
        humanities_approach=sum(1 for s in subs if s in Humanities_Social)
        artistic_approach=sum(1 for s in subs if s in Artistic_communicational)
        mix_approach=sum(1 for s in subs if s in Tech_knowladgebased+Humanities_Social+Artistic_communicational)
        if tech_approach>=2:
            color="Red"
        elif humanities_approach>=2:
            color="Green"
        elif artistic_approach>=2:
            color="Blue"
        elif mix_approach==3:
            color="White"
        student["group"]=color
        student_color1(student)
        def student_color1(student):
            subs=student["subjects"]
            tech_approach=sum(1 for s in subs if s in Tech_knowladgebased)
            humanities_approach=sum(1 for s in subs if s in Humanities_Social)
            artistic_approach=sum(1 for s in subs if s in Artistic_communicational)
            mix_approach=sum(1 for s in subs if s in Tech_knowladgebased+Humanities_Social+Artistic_communicational)
            if tech_approach>=1:
                color="Red"
            elif humanities_approach>=1:
                color="Green"
            elif artistic_approach>=1:
                color="Blue"
            elif mix_approach==2:
                color="White"
            student["group1"]=color
            return student
        
        return student

def subjects_list(name):
    global sub1,sub2,sub3,hobby,hobby2,learn_style,Tech_knowladgebased,Humanities_Social,Artistic_communicational
    sub1=input("What is your first favorite subject?:").lower()
    sub2=input("What is your second favorite subject?:").lower()
    sub3=input("What is your third favorite subject?:").lower()
    subs=[sub1,sub2,sub3]
    
    hobby=input("What is your favorite hobby?:").lower()
    hobby2=input("Do you have any other hobbies? (yes/no):").lower()
    if hobby2=="yes":
        hobby2=input("What is your other favorite hobby?:").lower()
    else:None
    
    learn_style=input("What is your preferred learning style? (visual/auditory/kinesthetic):").lower()

    student={
        "subjects":subs,
        "hobbies": [hobby,hobby2],
        "learning_style": learn_style
    }

    student= student_color(student)
    return student

group_whole=int(input(("How many students in the class?")))
students=[]
for s in range(group_whole):
    name=input("What is your name?:").lower()
    student_data=subjects_list(name)
    student_data=student_color(student_data)
    students.append(student_data)

#students=[
#    {
#        "students": student ,
#        "subjects":[sub1,sub2,sub3],
#       "hobbies": [hobby,hobby2],
#        "learning_style": learn_style
#    },....
#]


