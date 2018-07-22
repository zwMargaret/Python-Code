
class BaseClass:
    num_base_calls = 0

    def call_me(self):
        print('Calling method on Base Class')
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print('Calling method on Left SubClass')
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        BaseClass.call_me(self)
        print('Calling method on Right SubClass')
        self.num_right_calls += 1

class Subclass(LeftSubclass,RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        LeftSubclass.call_me(self)
        RightSubclass.call_me(self)
        print('Calling method on SubClass')
        self.num_sub_calls += 1


s = Subclass()
s.call_me()
print(s.num_base_calls,s.num_left_calls,s.num_right_calls,s.num_sub_calls)




#######################################################


'''
Sequence of applying "super().call_me(self)" method:
Subclass()  -> super().call_me(self) 
-> LeftSubclass()  -> super().call_me(self) 
-> RightSubclass()  -> super().call_me(self)
-> BaseClass()  -> BaseClass.call_me(self)  
'''
class BaseClass:
    num_base_calls = 0

    def call_me(self):  # No "super().call_me(self)"" here!
        print('Calling method on Base Class')
        self.num_base_calls += 1

class LeftSubclass(BaseClass):
    num_left_calls = 0

    def call_me(self):
        super().call_me(self)
        print('Calling method on Left SubClass')
        self.num_left_calls += 1

class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me(self)
        print('Calling method on Right SubClass')
        self.num_right_calls += 1

class Subclass(LeftSubclass,RightSubclass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me(self)
        print('Calling method on SubClass')
        self.num_sub_calls += 1

s = Subclass()
s.call_me()
print(s.num_base_calls,s.num_left_calls,s.num_right_calls,s.num_sub_calls)


