#ödev-1: Kullanıcıdan veri alarak; Bir küpün hacmini ve yüzey alanını hesaplayan program
KupAyrit = float(input("Küpün ayrıt uzunluğunu giriniz: "))
KupHacim = KupAyrit**3
KupYuzeyAlani = 6 * KupAyrit**2
print("Küpün hacmi: ", KupHacim)
print("Küpün yüzey alanı: ", KupYuzeyAlani)
input() # .py dosyasını cmd'den açtıktan sonra input'u yazdıktan sonra hemen kapanmaması için yeni bir input koyuyoruz

#ödev-2: Kullanıcıdan veri alarak; Dairenin alanını ve çevresini hesaplayan program
r = float(input("Dairenin yarıçapını giriniz: "))
pi = 3.14
DaireninAlani = pi * r**2
DaireninCevresi = 2*pi * r
print("Dairenin Alanı: ", DaireninAlani)
print("Dairenin Çevresi: ", DaireninCevresi)
input() # .py dosyasını cmd'den açtıktan sonra input'u yazdıktan sonra hemen kapanmaması için yeni bir input koyuyoruz
