class Person(object):
    total = 0

    def __init__(self, name, age):  # 기본 생성자 : __init__(self)
                                    # 생성자 오버로딩
        self.name = name
        self.age = age
    
    def getAge(self):
        return self.age

# 상속
class Man(Person):
    gender = 'male'

class Korean(Person):
    nationality = 'Korea'

# 다중 상속
class KoreanMan(Man, Korean):
    pass    # 비워둘시 오류나기 때문