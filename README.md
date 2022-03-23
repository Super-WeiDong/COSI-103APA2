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







