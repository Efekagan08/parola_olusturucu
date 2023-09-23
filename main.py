import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Parolanızın uzunluğunu seçiniz"))
parola = ""
for i in range(sayi):
    x = random.choice(karakterler)
    parola += x
print("Parolanız:", parola)
