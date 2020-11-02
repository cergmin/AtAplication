import sqlite3
from os.path import exists, isfile

class SQLController:
    # Если файла не существует и init_db = True, 
    # то он будет создан, а база данных инициализирована
    def __init__(self, file, init_db=False):
        file = str(file)

        if not exists(file):
            if init_db:
                pass
            else:
                raise FileExistsError('File \'' + file + '\' does not exist')
        elif not isfile(file):
            raise TypeError('File expected')

        self.file = file
        self.con = sqlite3.connect(self.file)
    
    def get_test(self, id_val):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM tests 
            WHERE id = ?""", [id_val]).fetchall()

    def get_tests(self):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM tests 
            WHERE parent = -1""").fetchall()
    
    def get_subtests(self, parent):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM tests 
            WHERE parent = ?""", [parent]).fetchall()
    
    def add_test(self, title='', subtitle='', input_type=0, output_type=0, 
                 input_val='', output_val='', parent=-1):
        cur = self.con.cursor()
        
        if parent != -1:
            results = cur.execute("""SELECT COUNT(*) FROM tests
                WHERE id = ? AND is_group = true""", [parent]).fetchone()
            
            if results[0] == 0:
                raise KeyError('Group with id=\'' + str(parent) + '\' does not exist')

        cur.execute("""INSERT 
            INTO tests(title, subtitle, input_type, output_type, 
                input, output, parent, is_group) 
            VALUES(?, ?, ?, ?, ?, ?, ?, false)""", 
            [title, subtitle, input_type, output_type, 
            input_val, output_val, parent])

        self.con.commit()

        return cur.lastrowid
    
    def add_group(self):
        cur = self.con.cursor()

        cur.execute("""INSERT 
            INTO tests(is_group) 
            VALUES(true)""")
        self.con.commit()
        
        return cur.lastrowid
    
    def set_verdict(self, id_val, verdict):
        cur = self.con.cursor()

        results = cur.execute("""SELECT COUNT(*) FROM tests
            WHERE id = ?""", [id_val]).fetchone()
            
        if results[0] == 0:
            raise KeyError('Test with id=\'' + str(id_val) + '\' does not exist')

        if len(str(verdict)) != 2:
            raise ValueError('Verdict must be 2 characters long, ' + 
                             str(len(str(verdict))) + ' were given')

        cur.execute("""UPDATE tests
            SET verdict = ?
            WHERE id = ?""", [verdict, id_val])

        self.con.commit()

        results = cur.execute("""SELECT parent FROM tests
            WHERE id = ?""", [id_val]).fetchone()
    
    def set_console_output(self, id_val, console_output):
        cur = self.con.cursor()

        results = cur.execute("""SELECT COUNT(*) FROM tests
            WHERE id = ?""", [id_val]).fetchone()
            
        if results[0] == 0:
            raise KeyError('Test with id=\'' + str(id_val) + '\' does not exist')

        cur.execute("""UPDATE tests
            SET console_output = ?
            WHERE id = ?""", [console_output, id_val])

        self.con.commit()