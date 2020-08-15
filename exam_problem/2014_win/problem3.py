'''
"00123456789012345678901234567890"
"00987654321098765432109876543210"

'''

a = int(input())
b = int(input())

c = a + b
cs = (str(c))
if len(cs) < 32:
    cs = "0" * (32-len(cs)) + cs

print(cs)
