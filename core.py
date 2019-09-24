from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String)


engine = create_engine('postgres://omjtfuaf:QPHQzVOng0MbUxZWBxpoYgek7Y40GDJf@salt.db.elephantsql.com:5432/omjtfuaf', echo=False)

metadata = MetaData(bind=engine)

data_gitlab = Table(
                    'gitlab', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('autor', String),
                    Column('descricao', String),
                    Column('codigo', String),
                    Column('data', String)
                    )
