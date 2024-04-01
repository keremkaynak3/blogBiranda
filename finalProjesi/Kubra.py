print('''Manisa
Celal Bayar University''')

print("-------------------------")

lst = []
aList = ['Computer', 'Telephone', 'TV']
print(aList[0])
print(aList[2])
print(aList[-3])

print("-------------------------")

bList = ['Keyboard', 'Wifi', 'Mouse']
cList = [aList, bList]
print(cList)
print(cList[0][2])
print(cList[1][2])

print("-------------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[:])   # all list
print(numbers[2:])  # 2. indexten itibaren getir
print(numbers[:4])  # ilk 4 veriyi getir
print(numbers[1:4]) # 1. indexten başlat, 4. veriye kadar getir
print(numbers[::2]) # bir tane atlayarak getir

print("-------------------------")

names = ['Ali', 'Ayşe', 'Gökhan', 'Fatma', 'Batur', 'Mehmet', 'Ayşegül', 'Abdullah', 'Zeynep', "Zzynep"]
print(type(names))
print(max(names))   # alfabe sırasına göre arama yapar ve en sonda olanı getirir
print(min(names))   # alfabe sırasına göre arama yapar ve en başta olanı getirir
print('Ahmet' in names) #Ahmet listede var mı diye bakar

print("-------------------------")

lst = [3, 5, 7, 9, 4]
lst.append(1)       # eklenecek olan sayıyı listenin sonuna ekler
print(lst)
print(lst.count(1)) # listede kaç tane 1 olduğuna bakar
lst1=[1,2,3]
lst.append(lst1)    # lst1 listesini lst listesine ekler, parantezli kalır
print(lst)
print(lst[-1][1])   # lst1 listesine ait 1. indexteki veriyi getirir
lst.extend(lst1)    # lst1 listesini lst listesine ekler, parantezi gelmez
print(lst)

print("-------------------------")

lst.insert(2, 8)  # lst listesinin 2. indexine 8 ekler
print(lst)
del lst[2]          # lst listesinin 2. indexindeki veriyi siler
print(lst)
lst2=[4,8,9,6,7,2,1]
lst2.sort(reverse=True) # listedeki verileri büyükten küçüğe sıralar
print(lst2)

print("-------------------------")

sentence='Manisa Celal Bayar University'
print(sentence)
print(sentence.find('Cel'))                         # Cel hecesinin kaçıncı indexte başladığını yazdırır
print(sentence.find('University'))                  # University hecesinin kaçıncı indexte başladığını yazdırır
print(sentence.find('a',6,11))   # 6. ve 11. indexler arasında a hangi indexte onu yazdırır
print(sentence.capitalize())                        # İlk kelime hariç diğerlerini küçük harfle başlatır
print(sentence.upper())
print(sentence.lower())

sentence = 'MANISA Celal Bayar University'
print(sentence.count('A'))
print(sentence.lower().count('a'))
print(sentence.lower().count('a', 5, 15))
print(sentence.replace('University','Uni'))

sentence = 'MANISA Celal Bayar University'

example = '             Hello World     '
print(example)
example2 = example.strip()   # Boşlukları atar
print(example2)




