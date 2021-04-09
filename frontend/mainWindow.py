import tkinter as tk
from frontend.lib.components import Frame, Label, Button
from frontend.dbConfigDialog import DBConfigDialog
from frontend.personCrud import PersonCrud
from frontend.personFind import FindPerson
from frontend.lib.text import _get_texts_, get_string

texts = _get_texts_(interface="main_window", lang="PTBR")


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry('300x150')
        self.create_widgets()
        self.winfo_toplevel().title("Cadastro de Pessoas")
        self.pack()
        self.db = self.show_dbconfig()

    def create_widgets(self):
        frame = Frame(self)

        '''
        #DBConfig
        Button(
            master=self
            , texts=texts
            , button_text="env_config"
            , command=self.show_dbconfig
            , side="top"
        )
        '''

        #Novo Cadastro
        Button(
            master=self
            , texts=texts
            , button_text="new_person"
            , command=self.show_crud_person
            , side="bottom"
        )

        # Localizar Cadastro
        Button(
            master=self
            , texts=texts
            , button_text="find_person"
            , command=self.show_find_person
            , side="bottom"
        )

        frame.pack()

    def show_crud_person(self):
        #self.master.withdraw()
        person_crud_dialog = PersonCrud(self, db=self.db)
        #self.master.deiconify()

    def show_find_person(self):
        #self.master.withdraw()
        find_person_dialog = FindPerson(self, db=self.db)
        #self.master.deiconify()

    def show_dbconfig(self):
        self.master.withdraw()
        config_dialog = DBConfigDialog(self)
        self.db = config_dialog.result
        self.master.deiconify()
        return self.db


def run():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
