
#---------------------------------

class Contact:
    all_contacts=[]
    
    def __init__(self,name='',email='', **kwargs):
        super().__init__(**kwargs)
        
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
    def __init__(self,street='',city='',state='',code='',**kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact,AddressHolder):
    def __init__(self,phone=''.**kwargs):
        super().__init__(**kwargs)
        self.phone = phone



#------------------------------------------------

class ContactList(list):
    def search(self,name):
        matching_contacts = []

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:

    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        
        self.all_contacts.append(self)



class LongNameDict(dict):
    def longest_key(self):
        longest = None
        
        for key in self:
            if not longest or len(key)>len(longest):
                longest = key
        
        return longest


class Friend_1(Contact):
    def __init__(self,name,email,phone):
        super().__init__(name,email)
        self.phone = phone




class MailSender:
    def send_mail(self,message):
        print("Sending mail to "+self.email)


class EmailableContact(Contact, MailSender):
    pass



class AddressHolder:
    def __init__(self,street,city,state,code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact,AddressHolder):

    def __init__(self,name,emial,phone,street,city,state,code):
        Contact.__init__(self,name,email)
        AddressHolder.__init__(self,street,city,state,code)
        self.phone = phone



        


def main():
    c1 = Contact("John A",'aaa')
    c2 = Contact("John B","bbb")
    c3 = Contact("Apple","ccc")

    print([ c.name for c in Contact.all_contacts.search("John") ])

    #-----------------------------------
    e = EmailableContact("John Smith","kkk")

    e.send_mail("Hello ")




if __name__== '__main__':
    main()