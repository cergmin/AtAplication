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
    
    def is_id_exists(self, id_val, is_group=None):
        cur = self.con.cursor()
        if is_group is None:
            result = cur.execute("""SELECT COUNT(*) FROM tests
                WHERE id = ?""", [id_val]).fetchone()
        else:
            result = cur.execute("""SELECT COUNT(*) FROM tests
                    WHERE id = ? AND is_group = ?""", [id_val, is_group]).fetchone()
            
        return result[0] != 0
    
    def is_group(self, id_val):
        cur = self.con.cursor()

        if not self.is_id_exists(id_val):
            raise KeyError('Test or group with id=\'' + 
                           str(id_val) + 
                           '\' does not exist')

        result = cur.execute("""SELECT COUNT(*) FROM tests
            WHERE id = ? AND is_group""", [id_val]).fetchone()
            
        return result[0] != 0
    
    def get_test(self, test_id):
        cur = self.con.cursor()

        if not self.is_id_exists(test_id, is_group=False):
            raise KeyError('Test with id=\'' + str(test_id) + '\' does not exist')

        return cur.execute("""SELECT * FROM tests 
            WHERE id = ?""", [test_id]).fetchall()

    def get_tests(self):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM tests 
            WHERE parent = -1""").fetchall()
    
    def get_subtests(self, group_id):
        cur = self.con.cursor()

        if not self.is_id_exists(group_id, is_group=True):
            raise KeyError('Group with id=\'' + str(group_id) + '\' does not exist')

        return cur.execute("""SELECT * FROM tests 
            WHERE parent = ?""", [group_id]).fetchall()
    
    def add_test(self, title='', subtitle='', input_type=0, output_type=0, 
                 input_val='', output_val='', parent=-1):
        cur = self.con.cursor()
        
        if parent != -1 and not self.is_id_exists(parent, is_group=True):
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
    
    # OK - Okey
    # WA - Wrong Answer
    # PE - Presentation Error
    # TL - Time Limit
    # ML - Memory Limit
    # RE - Runtime Error
    # CE - Compilation Error
    # FL - Fall
    # NP - Ne provereno :)
    def update_group_verdict(self, group_id):
        cur = self.con.cursor()
        verdict_priority = ['FL', 'CE', 'RE', 'WA', 'PE', 'TL', 'ML', 'NP', 'OK']
        if not self.is_id_exists(group_id, is_group=True):
            raise KeyError('Group with id=\'' + str(group_id) + '\' does not exist')

        results = cur.execute("""SELECT verdict FROM tests
            WHERE parent = ?""", [group_id]).fetchall()
        results = set(results)

        final_verdict = 'NP'

        for verdict in verdict_priority:
            if tuple([verdict]) in results:
                final_verdict = verdict
                break
        
        self.set_verdict(group_id, final_verdict)
        return final_verdict

    def set_verdict(self, id_val, verdict):
        cur = self.con.cursor()

        if not self.is_id_exists(id_val):
            raise KeyError('Test or group with id=\'' + 
                           str(id_val) + 
                           '\' does not exist')

        if len(str(verdict)) != 2:
            raise ValueError('Verdict must be 2 characters long, ' + 
                             str(len(str(verdict))) + ' were given')

        cur.execute("""UPDATE tests
            SET verdict = ?
            WHERE id = ?""", [verdict, id_val])

        self.con.commit()

        result = cur.execute("""SELECT parent FROM tests
            WHERE id = ?""", [id_val]).fetchone()
        
        if result[0] != -1:
            self.update_group_verdict(result[0])
    
    def set_console_output(self, id_val, console_output):
        cur = self.con.cursor()

        if not self.is_id_exists(id_val, is_group=False):
            raise KeyError('Test with id=\'' + str(id_val) + '\' does not exist')

        cur.execute("""UPDATE tests
            SET console_output = ?
            WHERE id = ?""", [console_output, id_val])

        self.con.commit()