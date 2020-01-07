from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String)


engine = create_engine('postgres://****', echo=False)

metadata = MetaData(bind=engine)

data_gitlab = Table(
                    'gitlab', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('autor', String),
                    Column('descricao', String),
                    Column('codigo', String),
                    Column('data', String)
                    )
