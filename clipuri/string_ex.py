
sir = 'Ana are mere'

print(len(sir))
print('=============')
# extra
sir_fara_spatii = sir.replace(' ', '') #inlocuieste fiecare spatiu cu un caracter gol / nimic
print(f'sirul fara spatii: {sir_fara_spatii}')

print('=============')

sir2 ='1234'
print(sir2.isnumeric())

print()
s2 = "asdasd"
type (s)
<class 'str'>
type (s2)
<class 'str'>
s3 = Ana are mere"
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\code.py", line 63, in runsource
    code = self.compile(source, filename, symbol)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\codeop.py", line 153, in __call__
    return _maybe_compile(self.compiler, source, filename, symbol)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\codeop.py", line 70, in _maybe_compile
    compiler(source + "\n", filename, symbol)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\codeop.py", line 118, in __call__
    codeob = compile(source, filename, symbol, self.flags, True)
  File "<input>", line 1
    s3 = Ana are mere"
                     ^
SyntaxError: unterminated string literal (detected at line 1)
s3 ="Ana are mere"
len(s3)
12
len(s2)
6
s3(0)
Traceback (most recent call last):
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python310\lib\code.py", line 90, in runcode
    exec(code, self.locals)
  File "<input>", line 1, in <module>
TypeError: 'str' object is not callable
len(s3)
12
s3[0]
'A'
s3[1]
'n'
s3[3]
' '
s3 [-1]
'e'
s3 [ - 2 ]
'r'
s2[0:3]
'asd'
s3 [0:3]
'Ana'
s3 [8:]
'mere'
s3 [ -1:-3]
''
s3[::]
'Ana are mere'
s3 [ 4:7:2]
'ae'
s3 [ 4:7:1]
'are'
s3 [ 4:7:3]
'a'
s3
'Ana are mere'
s3 [::2]
'Aaaemr'
s3 [::3]
'A ee'
s3 [::4]
'Aam'
s3[::-1]
'erem era anA'

