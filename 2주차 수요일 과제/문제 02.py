import random
class 캐릭터:
    int_ = random.randint(6,8)
    str_ = random.randint(6,8)
    class_ = None

    def __init__(self,argname):
        self.name = argname

    def define_class(self):
        if self.str_ > self.int_:
            self.class_ = "전사"
        elif self.str_ < self.int_:
            self.class_ = "법사"
        else:
            self.class_ = "궁수" 

    def display_info(self):
        print('\n캐릭터 이름: %s'%self.name)
        print('\n캐릭터 정보: 힘(%d), 지력(%d)'%(self.str_,self.int_))
        print('\n캐릭터 직업: %s'%(self.class_))







n = input("캐릭터의 이름을 입력하세요: ")

_ = 캐릭터(n)

_.define_class()

_.display_info()

    
