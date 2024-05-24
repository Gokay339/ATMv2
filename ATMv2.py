
kullanıcılar = {"Gökay":1234 ,"Onur":4321,"Berkay":262626,"Sedo":3113,"Emre":3131}
bakiyeler = {"Gökay":100 ,"Onur":111,"Berkay":50,"Sedo":42,"Emre":31}
gecmis = {"Gökay":[],"Onur":[],"Berkay":[],"Sedo":[],"Emre":[]}
def kayit():
    print("ESAŞ Bank Hoşgeldiniz\n1)Kayıt Ol\n2)Giriş Yap\n3)Çıkış Yap ")

    islemler = int(input("Lütfen İşlem Seçin : "))

    if islemler == 1 :
        ad = input("Lütfen Kullanıcı Adı Girin : ")
        sifre = input("Lütfen Sifre Girin : ")
        
        if ad in kullanıcılar:
            print("Böyle Bir Kullanıcı Adı Mevcut Lütfen Tekrar Deneyin")       #B U SİSTEM AYNI İSİMDE BİRİNİN KAYIT OLMASINI ENGELLİYOR
            kayit()
            
        else:
            kullanıcılar[ad] = int(sifre)                                       # AYNI İSİMDE BİRİSİ YOKSA KAYDINI YAP
            bakiyeler[ad] = 0
            gecmis[ad] = []
            print(kullanıcılar)
            print(bakiyeler)
            kayit()
    
    elif islemler == 2 :
        ad = input("Lütfen Kullanıcı Adı Girin : ")
        sifre = input("Lütfen Sifre Girin : ")
        
        if ad in kullanıcılar and kullanıcılar[ad] == int(sifre):               # GİRİŞ YAPMA KISMI
            anaislem(ad)
        else:
            print("Kullanıcı Adı Veya Parola Yanlış\n")
            kayit()
    elif islemler == 3 :
        exit()
    else:
        print("Lütfen Geçerli Bir İşlem Tuşlayınız\n")
        kayit()
    


def anaislem(ad):


    print(f"\nHoşgeldin, {ad}! Ana menüye yönlendiriliyorsunuz...")
    while True:
        import datetime
        x = datetime.datetime.now()
        saat = print(x.strftime(" ------------------ \n      %x \n      %X \n ------------------ "))
        islemler = input("""\nESAŞ Bank Ana Menüsüne Hoşgeldiniz
Lütfen Yapmak İstediğiniz İşlemi Seçiniz:\n
1. Para Çekme
2. Para Yatırma
3. Para Transferi
4. Hesap Bilgilerim
5. Çıkış Yap\n""")
        if islemler == '1':
            print("Para Çekme Sistemine Hoşgeldiniz\n")
            miktar = int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz: \n"))                    # PARA ÇEKME
            if miktar <= bakiyeler[ad]:
                bakiyeler[ad] -= miktar
                islem_zamani = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                gecmis[ad].append(f"{islem_zamani} - {miktar} TL Çekildi")
                print(f"Çekilen Miktar: {miktar}. Güncel Bakiye: {bakiyeler[ad]}")
                anaislem(ad)
            else:
                print("Bakiyeniz Yetersiz Lütfen Tekrar Deneyin\n")
                
        elif islemler == '2':                                                                       # PARA YATIRMA
            print("Para Yatırma Sistemine Hoşgeldiniz.\n") 
            miktar = int(input("Lütfen Yatırmak İstediğiniz Miktarı Giriniz: "))
            bakiyeler[ad] += miktar
            islem_zamani = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            gecmis[ad].append(f"{islem_zamani} - {miktar} TL Yatırıldı")
            print(f"Yatırılan Miktar: {miktar}. Güncel Bakiye: {bakiyeler[ad]}")
            anaislem(ad)
            
        elif islemler == '3':                                                                       # PARA TRANSFERİ
            print("Para Transferi Sistemine Hoşgeldiniz.\n")
            yenikullanici = input("Para Göndermek İstediğiniz Kişinin Adını Girin : ")
            miktar = int(input("Göndermek İstediğiniz Miktarı Girin : "))
            if yenikullanici in bakiyeler and miktar <= bakiyeler[ad]:
                bakiyeler[yenikullanici] += miktar
                bakiyeler[ad] -= miktar
                print("Gerçekleşti")
                islem_zamani = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                gecmis[ad].append(f"{islem_zamani} - {yenikullanici} Kişisine {miktar} TL Gönderildi")
                gecmis[yenikullanici].append(f"{islem_zamani} - {ad} Kişisinden {miktar} TL Alındı")
                print(f"Gönderilen Miktar: {miktar}. Güncel Bakiye: {bakiyeler[ad]}")
                anaislem(ad)
            else:
                print("İşleminiz Başarısız Lütfen Tekrar Deneyin.")
                
        elif islemler == '4':                                                                       # HESAP BİLGİLERİ
            print(f"Hesap Bilgilerim: {ad}, Bakiye: {bakiyeler[ad]}")
            print("Yapılan İşlemler:")
            for islem in gecmis[ad]:
                print(islem)
            anaislem(ad)
        elif islemler == '5':
            print("Hesaptan Çıkış Yapılıyor.")
            kayit()
        else:
            print("Geçersiz işlem numarası. Lütfen tekrar deneyin.\n")

kayit()
