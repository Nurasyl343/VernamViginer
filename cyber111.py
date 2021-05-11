from random import randint

#vernam	
text = input("Исходное сообщение: ").upper()
crypt=""
keys=""

for c in text:
	key=randint(0,25)
	keys += str(key) + " "
	gg=ord(c)+key-13
	crypt += chr((gg%26) + ord("A"))
print("Ключ: ",keys)
print("Ваша криптограмма(После Вернама): ",crypt)

#viginer
m = crypt
k = input("Второй ключ(Вижинер): ").upper()
k *= len(m) // len(k) + 1
c = ''

for i, j in enumerate(m):
	gg = (ord(j) + ord(k[i]))
	c += chr(gg % 26 + 65)
print("Ваша финальная криптограмма(После Виженера):",c)

print("------------------------------------------------------------\nDECRYTER")

#viginer
c = input("Криптограмма: ").upper()
k = input("Второй ключ(Вижинер): ").upper()
d = ''

for i, j in enumerate(c):
	gg = (ord(j) - ord(k[i]))
	chr(gg % 26 + 65)
	d += chr(gg % 26 + 65)

print("Сообщение(До Вижинера):",d)


#vernema
crypt=d
arr = []
key=""
for k in keys:
	if k != " ":
		key += k
	else:
		arr.append(key)
		key=""
		continue

decrypt = ""
for k,c in enumerate(crypt):
	gg = ord(c) - int(arr[k]) - 13
	decrypt += chr( (gg%26) + ord("A") )
print("Входящее сообщение: ", decrypt)