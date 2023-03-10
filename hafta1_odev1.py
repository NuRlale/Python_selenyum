"""Python veri tipleri:

    •	Integer : Sayisal verilerdir
    •	String : Metinsel veya karakter tipleridir.
    •	Float : Ondalikli sayi tipleridir.
    •	Boolean : True ve false değer döndürür.
    •	List : Birden çok ögeyi tutan yapidir "[]" kullanilir.
    •	Dictionary: Key ve values çiftinden oluşur ve "{}" kullanilir.

Kodlama.io sitesinde değişken olarak kullanildiğini düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz:

    •	Kategori ve eğitimler listedir.
    •	Ders tamamlama yüzdeleri integer.
    •	Kurs programi listedir.
    •	Kurs isimleri stringdir."""


email_address="lalesedanur@gmail.com"
password=1234

email=input("please enter your e-mail address:")
password1=int(input("please enter your password:\n "))

if email_address==email and password==password1:
    print ("login successsful")
else:
    print("email or password is wrong try again")

# yazılan kodun çalıştırılmış hali

"""please enter your e-mail address:lalesedanur@gmail.com
please enter your password:
 1236
email or password is wrong try again"""

"""please enter your e-mail address:lalesedanur@gmail.com
please enter your password:
 1234
login successsful"""