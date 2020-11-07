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
        self.con.row_factory = self.dict_factory 
        # dict_factory позволяет получать словарь, а не список,
        # когда мы выполгняем cur.execute("...").fetchall(),
        # где ключами являются названия столбцов таблицы

    def dict_factory(self, cur, row):
        d = {}

        for id_val, col in enumerate(cur.description):
            d[col[0]] = row[id_val]

        return d
    
    def is_test_exists(self, test_id):
        cur = self.con.cursor()
        result = cur.execute("""SELECT COUNT(*) FROM tests
            WHERE id = ?""", [test_id]).fetchone()

        return result['COUNT(*)'] != 0
    
    def is_group_exists(self, group_id):
        cur = self.con.cursor()
        result = cur.execute("""SELECT COUNT(*) FROM groups
            WHERE id = ?""", [group_id]).fetchone()
            
        return result['COUNT(*)'] != 0
    
    def is_subtest(self, test_id):
        cur = self.con.cursor()

        if not self.is_test_exists(test_id):
            raise KeyError('Test with id=\'' + 
                           str(test_id) + 
                           '\' does not exist')

        result = cur.execute("""SELECT COUNT(*) FROM tests
            WHERE id = ? AND group_id != -1""", [test_id]).fetchone()
            
        return result['COUNT(*)'] != 0

    def get_groups(self):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM groups""").fetchall()
    
    def get_test(self, test_id):
        cur = self.con.cursor()

        if not self.is_test_exists(test_id):
            raise KeyError('Test with id=\'' + str(test_id) + '\' does not exist')

        return cur.execute("""SELECT * FROM tests 
            WHERE id = ?""", [test_id]).fetchone()

    def get_tests(self, show_subtests=False):
        cur = self.con.cursor()

        if show_subtests:
            return cur.execute("""SELECT * FROM tests""").fetchall()
        else:
            return cur.execute("""SELECT * FROM tests 
                WHERE group_id = -1""").fetchall()
    
    def get_subtests(self, group_id):
        cur = self.con.cursor()

        if not self.is_group_exists(group_id):
            raise KeyError('Group with id=\'' + str(group_id) + '\' does not exist')

        return cur.execute("""SELECT * FROM tests 
            WHERE group_id = ?""", [group_id]).fetchall()
    
    def get_checker(self, test_id):
        cur = self.con.cursor()

        return cur.execute("""SELECT ch.id, ch.name, ch.arg_1_title, ch.arg_2_title,
            ch.arg_1_description, ch.arg_2_description, ts.checker_arg_1, ts.checker_arg_2 
            FROM checkers ch, tests ts
            WHERE ts.id = ? AND ch.id = ts.checker""", [test_id]).fetchone()
    
    def get_checkers(self):
        cur = self.con.cursor()
        return cur.execute("""SELECT * FROM checkers""").fetchall()
    
    def add_test(self, title='', subtitle='', checker=1, checker_arg_1='',
                 checker_arg_2='', group=-1):
        cur = self.con.cursor()
        
        if group != -1 and not self.is_group_exists(group):
            raise KeyError('Group with id=\'' + str(group) + '\' does not exist')

        cur.execute("""INSERT 
            INTO tests(group_id, title, subtitle, checker, checker_arg_1, checker_arg_2) 
            VALUES(?, ?, ?, ?, ?, ?)""", 
            [group, title, subtitle, checker, checker_arg_1, checker_arg_1])

        self.con.commit()

        return cur.lastrowid
    
    def add_group(self):
        cur = self.con.cursor()

        cur.execute("""INSERT INTO groups DEFAULT VALUES""")
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

        if not self.is_group_exists(group_id):
            raise KeyError('Group with id=\'' + str(group_id) + '\' does not exist')

        results = cur.execute("""SELECT verdict FROM tests
            WHERE group_id = ?""", [group_id]).fetchall()
        results = set(results)

        final_verdict = 'NP'

        for verdict in verdict_priority:
            if tuple([verdict]) in results:
                final_verdict = verdict
                break

        cur.execute("""UPDATE groups
            SET verdict = ?
            WHERE id = ?""", [final_verdict, group_id])

        self.con.commit()

        return final_verdict

    def set_verdict(self, test_id, verdict):
        cur = self.con.cursor()

        if not self.is_test_exists(test_id):
            raise KeyError('Test with id=\'' + 
                           str(test_id) + 
                           '\' does not exist')

        if len(str(verdict)) != 2:
            raise ValueError('Verdict must be 2 characters long, ' + 
                             str(len(str(verdict))) + ' were given')

        cur.execute("""UPDATE tests
            SET verdict = ?
            WHERE id = ?""", [verdict, test_id])

        self.con.commit()

        result = cur.execute("""SELECT group_id FROM tests
            WHERE id = ?""", [test_id]).fetchone()
        
        if result[0] != -1:
            self.update_group_verdict(result[0])
    
    def set_console_output(self, test_id, console_output):
        cur = self.con.cursor()

        if not self.is_test_exists(test_id):
            raise KeyError('Test with id=\'' + str(test_id) + '\' does not exist')

        cur.execute("""UPDATE tests
            SET console_output = ?
            WHERE id = ?""", [console_output, test_id])

        self.con.commit()
    
    def set_test_info(self, test_id, title=None, subtitle=None, path=None,
                      checker=None, checker_arg_1=None, checker_arg_2=None):
        cur = self.con.cursor()

        values = {
            'title': title,
            'subtitle': subtitle,
            'path': path,
            'checker': checker,
            'checker_arg_1': checker_arg_1,
            'checker_arg_2': checker_arg_2
        }

        for key in values:
            if values[key] is not None:
                cur.execute("""UPDATE tests
                    SET """ + key + """ = ?
                    WHERE id = ?""", [values[key], test_id])
        
        self.con.commit()