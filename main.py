import random
buyukharf = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
kucukharf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sayi = ['0','1','2','3','4','5','6','7','8','9']
ozel = ['+','-','/','*','!','&','$','#','?','=','@']
karakterler = buyukharf + kucukharf + sayi + ozel
soru = int(input("Şifrenin uzunluğu ne olsun? (En az 20 karakter): "))
while soru < 20:
    print("Parolanın uzunluğu en az 20 karakter olmalıdır.")
    soru = int(input("Tekrar girin: "))
parola = ''
for i in range(5):
    parola += random.choice(buyukharf)
    parola += random.choice(kucukharf)
    parola += random.choice(sayi)
    parola += random.choice(ozel)

for i in range(soru - 20):
    parola += random.choice(karakterler)

parola_liste = list(parola)
random.shuffle(parola_liste)
parola = ''.join(parola_liste)

print("Oluşturulan parola:", parola)
