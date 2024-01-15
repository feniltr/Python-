import sqlite3

cnt = sqlite3.connect("mydb.db")

def create_table():
    cnt.execute('''create table gfg(
        Name text,
        surname text,
        age text);
        ''')
    print('Table created')
        
def insert():
    data_to_insert = [
        ('viraj','Trivedi','89'),
        ('krunal','ajudia','84'),
        ('bhim','karna','15'),
        ('ajendra','varia','56'),
        ('ajay','nagar','47')
    ]
    cnt.executemany('''
        insert into gfg values(?,?,?);
    ''',data_to_insert)
    print('Record inserted')
    cnt.commit()

def select():
    cursor = cnt.execute('''
        select * from gfg  ;
    ''')

    print('Name' + '\t\t' + 'Surname' + '\t\t'+ 'Age')
    for i in cursor:
        print(i[0] + "\t\t" + i[1] + "\t\t" + i[2])

    print('')

def update():
    cnt.execute('''update gfg set Name='Fenil' where surname='Trivedi' 
    ''')
    cnt.commit()


select()