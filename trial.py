encryp="PHHW PH DIWHU WKH WRJD SDUWB" for k in range (1,26):
decryp=""
for i in encryp:
if ord(i)==32: decryp+=" "
elif (ord(i)-k<65): decryp+=chr(ord(i)-k+26)
else: decryp+=chr(ord(i)-k)
print("Key=",k,"->",decryp)