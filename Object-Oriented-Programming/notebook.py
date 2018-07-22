
import datetime
import sys

last_id = 0

'''
Objects:
1) Note(): most basic objects
           a) __init__(memo,tags)
           b) match(filter)
2) Notebook(): Notebook.notes = [multiple Note()]
               a) __init__()
               b) new_note(memo,tags)
               c) _find_note(note_id)
               d) modify_memo(note_id,memo)
               e) modify_tags(note_id,tags)
               f) search(filter)
3) Menu(): Menu.notebook = Notebook()
           a) __init__()
           b) display_menu()
           c) run()
           d) show_notes(notes) # "notes" here is a list of Note
           e) search_notes(filter) -> return a list of Note that match(filter)
                                   -> As menu.notebook = Notebook(), menu.notebook.search(filter) is used here.
           f) add_note(memo,tags)  -> menu.notebook.new_note(memo,tags)
           g) modify_note(note_id,memo,tags) -> menu.notebook.modify_memo(note_id,memo)
                                             -> menu.notebook.modify_tags(note_id,tags)          
'''

class Note:
    def __init__(self,memo,tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        
        global last_id
        last_id += 1
        self.id = last_id
    
    # "match" func: if note.memo or note.tags include 'filter', return True
    def match(self,filter):
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self,memo,tags=''):
        self.notes.append(Note(memo,tags))
    

    # _find_note: if there is note with note_id in self.notes, return note.
    #             Otherwise, return None
    def _find_note(self,note_id):
        for note in self.notes:
            if str(note.note_id) == str(note_id):
                return note
        return None

    def modify_memo(self,note_id,memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        else:
            return False

    def modify_tags(self,note_id,tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        else:
            return False

    def search(self,filter):
        return [ note for note in self.notes if note.match(filter)]



class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {"1":self.show_notes,"2":self.search_notes,"3":self.add_note,"4":self.modify_note,"5":self.quit}

    def display_menu(self):
        print('....')

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))


    def show_notes(self,notes=None):
        if not notes:
            notes = self.notebook.notes
        
        for note in notes:
            print("{0}:{1} \n {2}".format(note.id,note.tags,note.memo))

    
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")

    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")

        if memo:
            self.notebook.modify_memo(id,memo)
        
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == '__main__':
    Menu.run()

