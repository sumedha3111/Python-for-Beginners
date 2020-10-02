 import sys
import numpy as np
def cipher_encryption():
msg = input("Enter message: ").upper() msg = msg.replace(" ", "")
len_chk = 0
if len(msg) % 2 != 0:
msg += "0" len_chk = 1
row = 2
col = int(len(msg)/2)
msg2d = np.zeros((row, col), dtype=int) itr1 = 0
itr2 = 0
for i in range(len(msg)):
if i % 2 == 0:
msg2d[0][itr1] = int(ord(msg[i])-65) itr1 += 1
else:
msg2d[1][itr2] = int(ord(msg[i])-65) itr2 += 1
key = input("Enter 4 letter Key String: ").upper() key = key.replace(" ", "")
key2d = np.zeros((2, 2), dtype=int)
itr3 = 0
    for i in range(2):
        for j in range(2):
deter = deter =
key2d[i][j] = ord(key[itr3])-65 itr3 += 1
key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0] deter % 26
mul_inv
for i in range(26):
temp_inv = deter * i if temp_inv % 26 == 1:
mul_inv = i break
else:
continue
if mul_inv == -1: print("Invalid key") sys.exit()
encryp_text = ""
itr_count = int(len(msg)/2) if len_chk == 0:
for i in range(itr_count):
temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1] encryp_text += chr((temp1 % 26) + 65)
temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1] encryp_text += chr((temp2 % 26) + 65)
else:
for i in range(itr_count-1):
temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1] encryp_text += chr((temp1 % 26) + 65)
temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1] encryp_text += chr((temp2 % 26) + 65)
print("Encrypted Text: {}".format(encryp_text))
def cipher_decryption():
msg = input("Enter message: ").upper() msg = msg.replace(" ", "")
len_chk = 0
if len(msg) % 2 != 0:
msg += "0"
len_chk = 1 row = 2
col = int(len(msg) / 2)
msg2d = np.zeros((row, col), dtype=int) itr1 = 0
itr2 = 0
for i in range(len(msg)):
if i % 2 == 0:
msg2d[0][itr1] = int(ord(msg[i]) - 65) itr1 += 1
else:
msg2d[1][itr2] = int(ord(msg[i]) - 65) itr2 += 1
key = input("Enter 4 letter Key String: ").upper() key = key.replace(" ", "")
key2d = np.zeros((2, 2), dtype=int)
itr3 = 0
for i in range(2):
	for j in range(2):
		key2d[i][j] = ord(key[itr3]) - 65
		itr3 += 1
 deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
 deter = deter % 26
 mul_inv
for i in range(26):
= -1
temp_inv = deter * i if temp_inv % 26 == 1:
mul_inv = i
break else:
continue
key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0] key2d[0][1] *= -1
key2d[1][0] *= -1
key2d[0][1] = key2d[0][1] % 26
key2d[1][0] = key2d[1][0] % 26
    for i in range(2):
        for j in range(2):
key2d[i][j] *= mul_inv for i in range(2):
for j in range(2):
key2d[i][j] = key2d[i][j] % 26
decryp_text = ""
itr_count = int(len(msg) / 2) if len_chk == 0:
for i in range(itr_count):
temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1] decryp_text += chr((temp1 % 26) + 65)
temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1] decryp_text += chr((temp2 % 26) + 65)
else:
for i in range(itr_count - 1):
temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1] decryp_text += chr((temp1 % 26) + 65)
temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1] decryp_text += chr((temp2 % 26) + 65)
print("Decrypted Text: {}".format(decryp_text)) def main():
z=0
 while(z==0):
choice = int(input("1. Encryption\n2. Decryption\n3.Exit\n Choose: ")) if choice == 1:
print("---Encryption---")
cipher_encryption() elif choice == 2:
print("---Decryption---")
cipher_decryption() elif choice==3:
z=1 else:
            print("Invalid Choice")
if __name__ == "__main__": main()
