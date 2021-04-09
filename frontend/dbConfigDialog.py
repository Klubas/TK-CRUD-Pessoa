import os
import tkinter as tk
from frontend.lib.components import Label, LabeledEntry, Frame, Button
from tkinter import simpledialog
from dotenv import load_dotenv
from frontend.lib.text import _get_texts_, show_message
from dal.dataBaseEngine import connect
from tkinter import messagebox

texts = _get_texts_(interface="dbconfig", lang="PTBR")


class DBConfigDialog(simpledialog.Dialog):
    def __init__(self, master):
        super().__init__(master, title="Configurar conexão")
        self.db = None

    def buttonbox(self):
        pass

    def cancel(self, event=None):
        super(DBConfigDialog, self).cancel()

    def apply(self):
        self.result = self.db

    def body(self, master):
        def load_defaults():
            load_dotenv()
            username_entry.entry.insert(0, os.getenv("DBUSERNAME"))
            password_entry.entry.insert(0, os.getenv("DBPASS"))
            hostname_entry.entry.insert(0, os.getenv("DBHOST"))
            port_entry.entry.insert(0, os.getenv("DBPORT"))
            pass

        def use_config():
            db = connect(
                host=hostname_entry.entry.get()
                , port=port_entry.entry.get()
                , username=username_entry.entry.get()
                , password=password_entry.entry.get()
            )

            if db[0]:
                self.db = db[1]
                self.ok()
            else:
                show_message(title="alert", message=db[1], parent=self)

        Label(
            master=self
            , texts=texts
            , label_text="env_config")

        hostname_entry = LabeledEntry(
            master=self
            , label_text="hostname"
            , texts=texts
            , required=True)

        port_entry = LabeledEntry(
            master=self
            , label_text="port"
            , texts=texts
            , required=True)

        username_entry = LabeledEntry(
            master=self
            , label_text="username"
            , texts=texts
            , required=True)

        password_entry = LabeledEntry(
            master=self
            , label_text="password"
            , texts=texts
            , required=True)

        buttons_frame = tk.Frame(self)

        Button(
            master=buttons_frame
            , texts=texts
            , button_text="confirm"
            , command=use_config
            , width=10
        )

        Button(
            master=buttons_frame
            , texts=texts
            , button_text="cancel"
            , command=self.cancel
            , width=10
        )

        buttons_frame.pack(side="bottom", padx=5, pady=15)
        load_defaults()
