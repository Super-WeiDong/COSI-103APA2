# Weidong's script

Script started on 2022-03-23 18:50:14-04:00 [TERM="xterm-256color" TTY="/dev/pts/0" COLUMNS="120" LINES="30"]

wwd@DESKTOP-PJ0A953:~$ pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:103:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:130:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:143:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:159:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:45:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:109:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:146:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:149:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:37:0: W0611: Unused import sys (unused-import)
tracker.py:37:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 8.23/10 (previous run: 8.23/10, +0.00)


wwd@DESKTOP-PJ0A953:~$ pylint transaction.py
************* Module transaction
transaction.py:16:0: C0301: Line too long (135/100) (line-too-long)
transaction.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:66:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:73:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:90:0: C0304: Final newline missing (missing-final-newline)
transaction.py:13:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:19:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:24:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:30:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:38:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:48:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:59:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:74:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:82:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.33/10 (previous run: 7.33/10, +0.00)


wwd@DESKTOP-PJ0A953:~$ pytest -v -m add_select
================================================= test session starts =================================================
platform win32 -- Python 3.7.11, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- C:\Users\wangw\miniconda3\envs\py37\python.exe
cachedir: .pytest_cache
rootdir: D:\课程学习\Semester 2\103A-Fundamentals of Software Engineering\pa02\COSI-103APA2, configfile: pytest.ini
plugins: anyio-3.5.0
collected 7 items / 6 deselected / 1 selected

test_transaction.py::test_add_select PASSED                                                                      [100%]

=========================================== 1 passed, 6 deselected in 0.29s ===========================================

wwd@DESKTOP-PJ0A953:~$ python tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 4


item #     amount     category   date       description
--------------------------------------------------
1          100        food       20220322   sbh
2          200        toy        20220323   jellycat
3          300        car        20220325   gas fee
> 5
transaction amount: 200
transaction category: food
transaction date (yyyymmdd): 20220323
transaction description: mulan
> 4


item #     amount     category   date       description
--------------------------------------------------
1          100        food       20220322   sbh
2          200        toy        20220323   jellycat
3          300        car        20220325   gas fee
4          200        food       20220323   mulan
>
wwd@DESKTOP-PJ0A953:~$ exit
exit

Script done on 2022-03-23 18:50:21-04:00 [COMMAND_EXIT_CODE="0"]


#Jingqian's script

PS C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2> pylint .\transaction.py
************* Module transaction
transaction.py:16:0: C0301: Line too long (135/100) (line-too-long)
transaction.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:66:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:73:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:100:0: C0304: Final newline missing (missing-final-newline)
transaction.py:13:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:19:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:24:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:30:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:38:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:48:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:59:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:74:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:82:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:92:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:93:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.25/10 (previous run: 7.25/10, +0.00)

PS C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2> pylint .\tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:108:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:135:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:148:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:150:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:161:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:181:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:45:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:114:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:131:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:136:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:144:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:149:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:157:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:162:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:168:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:169:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:171:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:172:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:37:0: W0611: Unused import sys (unused-import)
tracker.py:37:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 7.50/10, +0.00)

PS C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2> pytest -v -m 'delete' .\test_transaction.py
================================================= test session starts =================================================
platform win32 -- Python 3.10.1, pytest-7.1.1, pluggy-1.0.0 -- C:\Users\Cheng Jingqian\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2, configfile: pytest.ini
plugins: anyio-3.5.0
collected 4 items / 3 deselected / 1 selected

test_transaction.py::test_delete PASSED                                                                          [100%]

=========================================== 1 passed, 3 deselected in 0.09s ===========================================

PS C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2> pytest -v -m 'transactions_by_date' .\test_transaction.py
================================================= test session starts =================================================
platform win32 -- Python 3.10.1, pytest-7.1.1, pluggy-1.0.0 -- C:\Users\Cheng Jingqian\AppData\Local\Programs\Python\Python310\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2, configfile: pytest.ini
plugins: anyio-3.5.0
collected 4 items / 3 deselected / 1 selected

test_transaction.py::test_transactions_by_date PASSED                                                            [100%]

=========================================== 1 passed, 3 deselected in 0.09s ===========================================

PS C:\Users\Cheng Jingqian\desktop\cs103a\pa02\COSI-103APA2> python .\tracker.py

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 4


item #     amount     category   date       description
--------------------------------------------------
1          100        food       20220324   nuts
2          200        drink      20220322   cola
3          150        food       20220209   rice
4          150        fruit      20220308   apple
5          100        food       20220324   noodle
> 6
deleting transaction
rowid: 3
> 4


item #     amount     category   date       description
--------------------------------------------------
1          100        food       20220324   nuts
2          200        drink      20220322   cola
4          150        fruit      20220308   apple
5          100        food       20220324   noodle
> 7


date       amount
--------------------------------------------------
20220308   150
20220322   200
20220324   200










#Jian's Script
(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ cat typescript 
Script started on Wed Mar 23 20:25:57 2022
Restored session: Wed Mar 23 20:25:04 EDT 2022
(base) ➜  COSI-103APA2 git:(main) ✗ conda env list
# conda environments:
#
                         /Users/Jeremy/opt/miniconda3
                         /Users/Jeremy/opt/miniconda3/envs/L10cs103a
base                  *  /opt/miniconda3
                                                                                                                /Users/Jeremy/opt/miniconda3/envs/L10cs103aactivate /Users/Jeremy/opt/miniconda3/envs/L10cs103a
(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ pytest test_transaction.py 
============================= test session starts ==============================
platform darwin -- Python 3.10.0, pytest-6.2.4, py-1.9.0, pluggy-0.13.1
rootdir: /Users/Jeremy/Desktop/103a-fundamental/COSI-103APA2, configfile: pytest.ini
plugins: anyio-3.5.0
collected 4 items                                                              

test_transaction.py ....                                                 [100%]

============================== 4 passed in 0.06s ===============================
(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ pylint tracker.py
************* Module tracker
tracker.py:29:61: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:108:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:135:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:148:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:150:0: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:161:37: C0303: Trailing whitespace (trailing-whitespace)
tracker.py:181:0: C0305: Trailing newlines (trailing-newlines)
tracker.py:45:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:114:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:131:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:136:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:144:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:149:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:157:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:162:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:168:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:169:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:171:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:172:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:37:0: W0611: Unused import sys (unused-import)
tracker.py:37:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 7.50/10 (previous run: 7.50/10, +0.00)

(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ pylint transaction.py 
************* Module transaction
transaction.py:16:0: C0301: Line too long (135/100) (line-too-long)
transaction.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:66:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:73:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:100:0: C0304: Final newline missing (missing-final-newline)
transaction.py:13:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:19:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:24:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:30:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:38:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:48:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:59:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:74:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:82:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:92:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:93:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 7.25/10 (previous run: 7.25/10, +0.00)

(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ python3 tracker.py    

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 4


item #     amount     category   date       description                   
--------------------------------------------------
1          1          a          20220101   aaa                           
2          2          b          20220102   bbb                           
3          3          c          20220201   cc                            
4          2          a          1          a                             
> 10


category   amount    
--------------------------------------------------
a          3         
b          2         
c          3         
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 0
bye
(L10cs103a) ➜  COSI-103APA2 git:(main) ✗ exit

Saving session...completed.

Script done on Wed Mar 23 20:28:18 2022
(L10cs103a) ➜  COSI-103APA2 git:(main) ✗   


# Katherine Cheng's script
Script started on Thu Mar 24 21:34:26 2022
[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004hppylint tracker.py[?2004l

************* Module tracker
tracker.py:114:0: C0325: Unnecessary parens after 'return' keyword (superfluous-parens)
tracker.py:45:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:63:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:63:0: R0912: Too many branches (13/12) (too-many-branches)
tracker.py:120:4: W0105: String statement has no effect (pointless-string-statement)
tracker.py:200:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:203:0: C0116: Missing function or method docstring (missing-function-docstring)
tracker.py:37:0: W0611: Unused import sys (unused-import)
tracker.py:37:0: C0411: standard import "import sys" should be placed before "from category import Category" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 9.10/10 (previous run: 9.10/10, +0.00)

[0m[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004hpylint tracker.py          transaction.py[?2004l

************* Module transaction
transaction.py:16:0: C0301: Line too long (135/100) (line-too-long)
transaction.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:66:0: C0301: Line too long (130/100) (line-too-long)
transaction.py:73:0: C0303: Trailing whitespace (trailing-whitespace)
transaction.py:13:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:19:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:24:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:30:0: W0105: String statement has no effect (pointless-string-statement)
transaction.py:38:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:48:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:59:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:74:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:75:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:82:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:83:4: C0116: Missing function or method docstring (missing-function-docstring)
transaction.py:112:4: W0105: String statement has no effect (pointless-string-statement)
transaction.py:113:4: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.00/10 (previous run: 8.00/10, +0.00)

[0m[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004h[7mpytest[27m[27mp[27my[27mt[27me[27ms[27mt[?2004l

[1m================================== test session starts ==================================[0m
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/cxy/cosi103/PA/COSI-103APA2, configfile: pytest.ini
plugins: anyio-2.2.0
[1mcollecting ... [0m[1m
collected 10 items                                                                      [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                             [ 40%][0m
test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                        [100%][0m

[32m================================== [32m[1m10 passed[0m[32m in 0.28s[0m[32m ===================================[0m
[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004h[7mtracker.py[27m[10D[27mt[27mr[27ma[27mc[27mk[27me[27mr[27m.[27mp[27my[?2004l

zsh: command not found: tracker.py
[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004hppython [7mtracker.py[27m[10D[27mt[27mr[27ma[27mc[27mk[27me[27mr[27m.[27mp[27my[?2004l


0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 8


month      amount    
--------------------------------------------------
3          200       
12         5         
> 9


year       amount    
--------------------------------------------------
2021       5         
2022       200       
> 0
bye
[1m[7m%[27m[1m[0m                                                                                        
 
]7;file://hodoshinamesmbp.dyn.brandeis.edu/Users/cxy/cosi103/PA/COSI-103APA2
[0m[27m[24m[J(base) cxy@hodoshinamesmbp COSI-103APA2 % [K[?2004h