tal_max = -999999999
tal_min = 999999999

tal1 = input("Vad är det första tal?")
tal1 = int(tal1)
if tal1 >= tal_max:
    tal_max = tal1
if tal1 <= tal_min:
    tal_min = tal1
print(tal1)

tal2 = input("Vad är det andra tal?")
tal2 = int(tal2)
if tal2 >= tal_max:
    tal_max = tal2
if tal2 <= tal_min:
    tal_min = tal2
print(tal2)

tal3 = input("Vad är det tredje tal?")
tal3 = int(tal3)
if tal3 >= tal_max:
    tal_max = tal3
if tal3 <= tal_min:
    tal_min = tal3
print(tal3)

if tal1 == tal2 == tal3:
    number_of_same_talen = 3
elif tal1 == tal2 or tal2 == tal3 or tal1 == tal3:
    number_of_same_talen = 2
else: number_of_same_talen = 0

summa = tal1 + tal2 + tal3
print("Summa:" + str(summa))
print(f"max tal: {tal_max}")

if number_of_same_talen != 0:
    print(f"{number_of_same_talen} av talen är lika")

if number_of_same_talen == 0: # all numbers are unique -> need find  middle
    if tal_min < tal1 < tal_max:
        mellersta_tal = tal1
    elif tal_min < tal2 < tal_max:
        mellersta_tal = tal2
    else: mellersta_tal = tal3

if number_of_same_talen == 3: # all numbers are same -> can print any
    mellersta_tal = tal1

if number_of_same_talen == 0 or number_of_same_talen == 3:
    print(f"mellersta tal: {mellersta_tal}")
