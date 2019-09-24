from core import engine


def truncate_db():
    con = engine.connect()
    con.execute('TRUNCATE TABLE gitlab RESTART IDENTITY')
    print('Cleaned')
