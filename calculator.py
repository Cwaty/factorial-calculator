number_one = int(input("Faktöriyelini bulmak istediğiniz sayıyı girin."))

if number_one <0:
    print("Faktöriyelini bulmak istediğiniz sayı 0 dan küçük olamaz.")
else:

    one = 1
    for i in range(number_one):
        one = one * (i+1)

    print(range(number_one))
    print(number_one,"!")
    print(number_one,"Sayısının faktöriyeli",one)
    print("Sherwood: https://github.com/Cwaty")
