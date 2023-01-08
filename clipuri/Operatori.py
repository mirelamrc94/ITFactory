'''
operatori:
aritmetici: +,-,/,%,*
de comparare : < > , ==, !=, >=, <=
logici: and , or, !
'''

a = 3
b = 5

print(a + b) # 3 + 5 => 8
print(a == b) # a este egal cu b ? False
print(a < b and a <4) # 3 < 5 and 3 < 4  => True si True
print(a < b or a < 2) # true sau false => true

# cu mama sau tata sau ( cu bunicu si bunica)
mama = True
tata = True
bunicu = True
bunica = True
print(mama or tata or (bunicu and bunica ))