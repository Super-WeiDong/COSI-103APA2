'''
transaction.py is a Object Relational Mapping to the categories table

The ORM will work map SQL rows with the schema
    (rowid,name,description)
to Python Dictionaries.

This app will store the data in a SQLite database ~/tracker.db

'''
import sqlite3

'''Written by Weidong wang'''
def to_tran_dict(tran_tuple):
    ''' tran is a category tuple (rowid, amount, category, date, description)'''
    tran = {'rowid':tran_tuple[0], 'amount':tran_tuple[1], 'category':tran_tuple[2], 'date':tran_tuple[3], 'description':tran_tuple[4]}
    return tran

'''Written by Weidong wang'''
def to_tran_dict_list(tran_tuples):
    ''' convert a list of transaction tuples into a list of dictionaries'''
    return [to_tran_dict(tran) for tran in tran_tuples]

'''Written by Jingqian Cheng'''
def to_tran_dict2(tran_tuple):
    ''' helper method for group by situations'''
    tran = {'group_by':tran_tuple[0], 'amount':tran_tuple[1]}
    return tran

'''Written by Jingqian Cheng'''
def to_tran_dict_list2(tran_tuples):
    ''' helper method for group by situations'''
    return [to_tran_dict2(tran) for tran in tran_tuples]

class Transaction():
    ''' Transaction represents a table of transactions'''

    '''Written by Weidong wang'''
    def __init__(self,dbfile):
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (amount int, category text, date int, description text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    '''Written by Weidong wang'''
    def select_all(self):
        ''' return all of the transactions as a list of dicts.'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT rowid,* from transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)
        
    '''Written by Weidong wang'''
    def add(self,item):
        ''' add a transaction to the transactions table.
            this returns the item_id of the inserted element
        '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?)",(item['amount'],item['category'],item['date'],item['description']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]
    
    '''Written by Jingqian Cheng'''
    def delete(self, rowid):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE rowid=(?);''',(rowid,))
        con.commit()
        con.close()

    '''Written by Jingqian Cheng'''
    def transactions_by_date(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date, sum(amount) FROM transactions GROUP BY date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list2(tuples)

    def transactions_by_month(self):
        '''Written by Katherine Cheng'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date/100%100, sum(amount) FROM transactions GROUP BY date/100%100''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list2(tuples)

    def transactions_by_year(self):
        '''Written by Katherine Cheng'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT date/10000, sum(amount) FROM transactions GROUP BY date/10000''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list2(tuples)

    '''Written by Jian He'''
    def transactions_by_category(self):
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT category, sum(amount) FROM transactions GROUP BY category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list2(tuples)
