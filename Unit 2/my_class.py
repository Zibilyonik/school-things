

class Academy: # Class names start with capital letter and have capital word. (Naming Conventions)
    def __init__(self, name): #OR double under functions aka Dunder functions, is when we do default without requiring users input
        self.name = name
        self.notes = []
        self.teachers = []
        self.topics= []
        self.score=0
        self.test=None
    def show_score(self):
        print(f"Your score in academy is  {self.score} ")
    def take_test(self):
        if self.test=="Passed":
            self.score+=50
            print(f"You  passed your test , +50 points to the score")
        else:
            print(f"You didnt pass your test")
    def study():
        print("Studying, studying....")
    def learn_implement(self):
        self.score+=10
        print("You studied new thing and increased your score by 10")
    def get_certificate(self):
        if self.score == 100:
            print(f"You only have {self.score}  you can get a certificate")
        else:
            self.score < 100
            print(f"You dont have enough points for a certificate")
    def teacher_anket(self):
        print(self.teachers)
        print("Choose your teacher")


my_academy = Academy("Senya")
my_academy.score