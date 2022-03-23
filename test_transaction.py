'''
test_transaction runs unit and integration tests on the transaction module
'''

import pytest
from transaction import Transaction

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'amount':100,'category':'a', 'date': 3222022, 'description': 'a'}
    cat2 = {'amount':200,'category':'a', 'date': 4222022, 'description': 'b'}
    cat3 = {'amount':300,'category':'a', 'date': 5222022, 'description': 'c'}
    id1=empty_db.add(cat1)
    id2=empty_db.add(cat2)
    id3=empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        cat ={'amount':i,
              'category':s,
              'date':i,
              'description':s
             }
        rowid = small_db.add(cat)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])

'''Q6 Jingqian Cheng'''
@pytest.mark.delete
def test_delete(med_db):
    ''' add a transaction to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this category to the table and get the new list of rows
    cat0 ={'amount':100,
           'category':'a',
           'date':2022,
           'description':'None'
          }
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the category and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

'''Q7 Jingqian Cheng'''
@pytest.mark.transactions_by_date
def test_transactions_by_date(med_db):
    ''' add some tansactions to db, group by date, see if their results are right'''
    # first we get the initial table
    

    # then we add this category to the table and get the new list of rows
    cat0 ={'amount':100,
           'category':'a',
           'date':2020,
           'description':'None'
          }
    cat1 ={'amount':200,
           'category':'b',
           'date':2020,
           'description':'None'
          }
    cat2 ={'amount':100,
           'category':'c',
           'date':2021,
           'description':'None'
          }
    cat3 ={'amount':50,
           'category':'d',
           'date':2022,
           'description':'None'
          }
    med_db.add(cat0)
    med_db.add(cat1)
    med_db.add(cat2)
    med_db.add(cat3)
    res = med_db.transactions_by_date()
    # test whether each group has the correct aggreated amount
    for n in res:
        if n['group_by'] == 2020:
            assert n['amount'] == 300
        elif n['group_by'] == 2021:
            assert n['amount'] == 100
        elif n['group_by'] == 2022:
            assert n['amount'] == 50
