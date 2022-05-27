# variables

a = 5 
b = 6 
c = b'this line was converted to hex before output'
 
# ############
# 8 hex values 
# b - indivates hex encoding
# \x - hex value identifier 
# ############
d = bytes(8)

# output 

print(a == b) # False
print(a != b) # True
print(c)
print(a < b) # True
print(a >= b) #False
print(d)