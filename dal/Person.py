from sqlalchemy import MetaData, Table, Column, String
from sqlalchemy import insert, update, delete, select


class Person:

    def __init__(self, db=None
                     , name=None
                     , tax_id=None
                     , document=None
                     , email=None
                     , phone=None
                     , street_name=None
                     , address_number=None
                     , district=None
                     , complement=None
                     , country=None
                     , select_by_tax_id=None
                 ):
        self.db = db
        self.engine = db.engine
        self.person_table = self._create_table_()

        self.name = name
        self.tax_id = tax_id
        self.document = document
        self.email = email
        self.phone = phone
        self.street_name = street_name
        self.address_number = address_number
        self.district = district
        self.complement = complement
        self.country = country

        if select_by_tax_id:
            self.tax_id = select_by_tax_id
            self.select()
        else:
            self.insert()

    def select(self):
        stmt = select(
            self.person_table.c.name
            , self.person_table.c.tax_id
            , self.person_table.c.document
            , self.person_table.c.email
            , self.person_table.c.phone
            , self.person_table.c.street_name
            , self.person_table.c.address_number
            , self.person_table.c.district
            , self.person_table.c.complement
            , self.person_table.c.country
        ).where(self.person_table.c.tax_id == self.tax_id)
        result = self.db.execute_stmt(sql=stmt)

        result = (result[1].fetchone())

        if result:
            self.name = result[0]
            self.tax_id = result[1]
            self.document = result[2]
            self.email = result[3]
            self.phone = result[4]
            self.street_name = result[5]
            self.address_number = result[6]
            self.district = result[7]
            self.complement = result[8]
            self.country = result[9]
            return self
        else:
            self.tax_id = None
            return None

    def update(
        self
        , name=None
        , document=None
        , email=None
        , phone=None
        , street_name=None
        , address_number=None
        , district=None
        , complement=None
        , country=None
    ):
        stmt = (
            update(self.person_table).
            where(self.person_table.c.tax_id == self.tax_id).values(
                name=name
                , document=document
                , email=email
                , phone=phone
                , street_name=street_name
                , address_number=address_number
                , district=district
                , complement=complement
                , country=country
            )
        )
        result = self.db.execute_stmt(sql=stmt, confirm_to_commit=True)
        if not result[0]:
            raise Exception(str(result[1]))
        return self

    def delete(self):
        stmt = (
            delete(self.person_table).
            where(self.person_table.c.tax_id == self.tax_id)
        )
        result = self.db.execute_stmt(sql=stmt, confirm_to_commit=True)
        if not result[0]:
            raise Exception(str(result[1]))
        return result

    def insert(self):
        stmt = (
            insert(self.person_table).values(
                name=self.name
                , tax_id=self.tax_id
                , document=self.document
                , email=self.email
                , phone=self.phone
                , street_name=self.street_name
                , address_number=self.address_number
                , district=self.district
                , complement=self.complement
                , country=self.country
            )
        )
        result = self.db.execute_stmt(sql=stmt, confirm_to_commit=True)
        if not result[0]:
            raise Exception(str(result[1]))
        return result

    def _create_table_(self):
        with self.engine.begin():
            metadata = MetaData(bind=self.engine, schema="public")
            person_table = Table('person', metadata,
                                 Column('tax_id',         String(16),  nullable=False, primary_key=True),
                                 Column('name',           String(90),  nullable=False),
                                 Column('document',       String(9),   nullable=True),
                                 Column('email',          String(60),  nullable=False),
                                 Column('phone',          String(16),  nullable=True),
                                 Column('street_name',    String(120), nullable=True),
                                 Column('address_number', String(5),   nullable=True),
                                 Column('district',       String(120), nullable=True),
                                 Column('complement',     String(120), nullable=True),
                                 Column('country',        String(60),  nullable=True),
                                 )
            metadata.create_all()
        return person_table


