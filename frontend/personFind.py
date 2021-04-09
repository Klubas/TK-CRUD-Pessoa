import tkinter as tk
from tkinter import simpledialog
from frontend.lib.text import _get_texts_, get_string, show_message
from frontend.lib.components import LabeledEntry, Frame
from frontend.personCrud import PersonCrud
from dal.Person import Person
from tkinter import messagebox

texts = _get_texts_(interface="find", lang="PTBR")


class FindPerson(simpledialog.Dialog):
    def __init__(self, master, db=None):
        self.db = db
        super().__init__(master, title=get_string(texts=texts, key="person"))
        self.tax_id = None
        self.tax_id_entry = None
        self.person = None

    def show_crud_person(self):
        #self.master.withdraw()
        self.tax_id = self.tax_id_entry.entry.get()

        if not self.tax_id:
            show_message(title="alert", message="tax_id_not_supplied", parent=self)
            return False

        try:
            self.person = Person(select_by_tax_id=self.tax_id, db=self.db)
        except Exception as e:
            show_message(title="alert", message=str(e), parent=self)
            print(e)
            return False

        if self.person.tax_id:
            dialog = PersonCrud(master=self, db=self.db, person=self.person)
            return True

        show_message(title="alert", message="person_not_found", parent=self)
        return False

        #self.master.deiconify()

    def ok(self, event=None):
        if self.show_crud_person():
            super(FindPerson, self).ok()
        else:
            self.tax_id = None
            self.person = None

    def body(self, master):
        frame = Frame(master=self)
        frame.pack(padx=10, pady=10)
        self.tax_id_entry = LabeledEntry(master=frame, label_text="find", texts=texts, width=30)
