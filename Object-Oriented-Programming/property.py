

class Property:
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        
        super().__init__(**kwargs)

        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    
    def display(self):
        print('square footage:{}'.format(self.square_feet))
        print('bedrooms:{}'.format(self.num_bedrooms))
        print('baths:{}'.format(self.num_baths))
        print()


    def prompt_init():
        return dict(square_feet=input("Enter square feet:"),beds=input("Enter number of bedrooms"),baths=input("Enter number of baths"))

    prompt_init = staticmethod(prompt_init)






class Apartment(Property):
    valid_laundries = ('a','b','none')
    valid_balconies = ('yes','no','sloarium')

    def __init__(self,balcony='',laundry='',**kwargs):
        super().__init__(**kwargs)

        self.balcony = balcony
        self.laundry = laundry   

    
    def display(self):
        super().display()

        print("laundry: %s"%self.laundry)
        print("has balcony: %s"%self.balcony)

        parent_init = Property.prompt_init()
        laundry = ''

        return parent_init

    prompt_init = staticmethod(prompt_init)

    