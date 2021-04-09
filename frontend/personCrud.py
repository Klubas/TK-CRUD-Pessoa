import tkinter as tk
from tkinter import simpledialog
from frontend.lib.text import _get_texts_, get_string
from frontend.lib.components import LabeledEntry, Label, Frame, Button
from dal.Person import Person

texts = _get_texts_(interface="crud_person", lang="PTBR")


class PersonCrud(simpledialog.Dialog):
    def __init__(self, master, db, person=None):
        self.db = db
        self.tax_id = None
        self.name = None
        self.document = None
        self.email = None
        self.phone = None
        self.street_name = None
        self.address_number = None
        self.district = None
        self.complement = None
        self.country = None

        self.value_tax_id = None
        self.value_name = None
        self.value_document = None
        self.value_email = None
        self.value_phone = None
        self.value_street_name = None
        self.value_address_number = None
        self.value_district = None
        self.value_complement = None
        self.value_country = None
        self.person = person

        super().__init__(master, title=get_string(texts, "new_person"))
    
    def ok(self, event=None):
        try:
            self.value_name = self.name.entry.get()
            self.value_tax_id = self.tax_id.entry.get()
            self.value_document = self.document.entry.get()
            self.value_email = self.email.entry.get()
            self.value_phone = self.phone.entry.get()
            self.value_street_name = self.street_name.entry.get()
            self.value_address_number = self.address_number.entry.get()
            self.value_district = self.district.entry.get()
            self.value_complement = self.complement.entry.get()
            self.value_country = self.country.entry.get()

            if self.person is None:

                if self.value_name == '' or self.value_tax_id == '' or self.value_email == '':
                    raise Exception("required_fields")

                self.person = Person(
                     db=self.db
                     , name=self.value_name
                     , tax_id=self.value_tax_id
                     , document=self.value_document
                     , email=self.value_email
                     , phone=self.value_phone
                     , street_name=self.value_street_name
                     , address_number=self.value_address_number
                     , district=self.value_district
                     , complement=self.value_complement
                     , country=self.value_country
                )

            else:
                self.person = self.person.update(
                     name=self.value_name
                     , document=self.value_document
                     , email=self.value_email
                     , phone=self.value_phone
                     , street_name=self.value_street_name
                     , address_number=self.value_address_number
                     , district=self.value_district
                     , complement=self.value_complement
                     , country=self.value_country
                )

            super(PersonCrud, self).ok()
        except Exception as e:
            from tkinter import messagebox
            messagebox.showwarning(title="Alerta", message=str(e))

    def delete(self):
        from tkinter import messagebox
        response = messagebox.askquestion(title="Confirmar exclusão"
                                          , message="Tem certeza que deseja excluir esse cadastro?"
                                          , parent=self)
        if response == 'yes':
            try:
                self.person.delete()
                self.cancel()
            except Exception as e:
                from tkinter import messagebox
                messagebox.showwarning(title="Alerta", message=str(e))
        else:
            pass

    def body(self, master):

        Label(master=self
              , label_text="new_person"
              , texts=texts)

        self.name = LabeledEntry(master=self
                                 , label_text="name"
                                 , texts=texts
                                 , required=True)

        documents_frame = Frame(master=self)
        documents_frame.pack()

        Label(master=documents_frame
              , label_text="documents"
              , texts=texts)

        self.tax_id = LabeledEntry(master=documents_frame
                                   , label_text="tax_id"
                                   , texts=texts
                                   , required=True)

        self.document = LabeledEntry(master=documents_frame
                                     , label_text="document"
                                     , texts=texts)

        contacts_frame = Frame(master=self)
        contacts_frame.pack()

        Label(master=contacts_frame
              , label_text="contact_info"
              , texts=texts)

        self.email = LabeledEntry(master=contacts_frame
                                  , label_text="email"
                                  , texts=texts
                                  , required=True)

        self.phone = LabeledEntry(master=contacts_frame
                                  , label_text="phone_number"
                                  , texts=texts)

        addresses_frame = Frame(master=self)
        addresses_frame.pack()

        Label(master=addresses_frame
              , label_text="address"
              , texts=texts)

        self.street_name = LabeledEntry(master=addresses_frame
                                        , label_text="street_name"
                                        , texts=texts)

        self.address_number = LabeledEntry(master=addresses_frame
                                           , label_text="address_number"
                                           , texts=texts)

        self.district = LabeledEntry(master=addresses_frame
                                     , label_text="district"
                                     , texts=texts)

        self.complement = LabeledEntry(master=addresses_frame
                                       , label_text="complement"
                                       , texts=texts)

        self.country = LabeledEntry(master=addresses_frame
                                    , label_text="country"
                                    , texts=texts)

        if self.person is not None:

            delete_button = Button(
                master=self
                , texts=texts
                , button_text="delete_person"
                , command=self.delete
                , side="bottom"
            )

            if self.person.tax_id:
                self.tax_id.entry.\
                    insert(0, str(self.person.tax_id))
                self.name.entry.\
                    insert(0, self.person.name)
                self.document.entry.\
                    insert(0, self.person.document)
                self.email.entry.\
                    insert(0, self.person.email)
                self.phone.entry.\
                    insert(0, self.person.phone)
                self.street_name.entry.\
                    insert(0, self.person.street_name)
                self.address_number.entry.\
                    insert(0, self.person.address_number)
                self.district.entry.\
                    insert(0, self.person.district)
                self.complement.entry.\
                    insert(0, self.person.complement)
                self.country.entry.\
                    insert(0, self.person.country)
            else:
                self.cancel()
