import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


class DataBase:

    def __init__(
            self
            , host=None
            , port=None
            , username=None
            , password=None
            , dbname='postgres'
            , schema='public'
    ):

        load_dotenv()

        self.dbname = dbname
        self.schema = schema
        self.username = os.getenv("DBUSERNAME") if username is None else username
        password = os.getenv("DBPASS") if password is None else password
        self.host = os.getenv("DBHOST") if host is None else host
        self.port = os.getenv("DBPORT") if port is None else port

        self.dbinfo = \
            'postgresql://' + str(self.username) + ':' + str(password) + '@' \
            + str(self.host) + ':' + str(self.port) + '/' + str(self.dbname)

        self.engine = create_engine(
            self.dbinfo,
            echo=True,
            future=True
        )

        self.engine = \
            self.engine.execution_options(isolation_level="READ UNCOMMITTED")

        with self.engine.connect() as conn:
            pass

        '''
        self.repeatable_read_engine = \
            self.engine.execution_options(isolation_level="REPEATABLE READ")
        self.read_committed_autocommit_engine = \
            self.engine.execution_options(isolation_level="READ COMMITTED")
        self.read_uncommitted_engine = \
            self.engine.execution_options(isolation_level="READ UNCOMMITTED")
        self.autocommit_engine = \
            self.engine.execution_options(isolation_level="AUTOCOMMIT")
        '''

    def execute_stmt(self, sql, confirm_to_commit=False):
        # https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html
        # https://docs.sqlalchemy.org/en/14/dialects/postgresql.html
        try:
            with self.engine.connect() as conn:
                conn = conn.execution_options(
                    isolation_level="READ UNCOMMITTED"
                )
                with conn.begin():
                    try:
                        result = conn.execute(sql)
                        if confirm_to_commit:

                            from tkinter import messagebox

                            response = messagebox.askquestion(
                                title="COMMIT", message="COMMIT?")

                            if response == 'yes':
                                conn.commit()
                                prc = True, result, str(sql)
                            else:
                                conn.rollback()
                                prc = False, 'Commit blocked by user', str(sql)

                        else:
                            conn.commit()
                            prc = True, result, str(sql)
                    except Exception as e:
                        result = str(e)
                        conn.rollback()
                        prc = False, result, str(sql)
        except Exception as e:
            result = list()
            result.append(e)
            prc = False, result, str(sql)
        print(prc)
        return prc


def connect(host, port, username, password):
    try:
        db = DataBase(
            host=host
            , port=port
            , username=username
            , password=password
            , dbname='postgres'
            , schema='public'
        )
        print("DB connection OK.")
        db = True, db
    except Exception as e:
        print("DB connection failed...")
        print(str(e))
        db = False, str(e)
    return db
