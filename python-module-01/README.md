
if __name__== "__main__" yapısı ir Python dosyasının doğrudan çalıştırılıp çalıştırılmadığını kontrol etmek için kullanılır.

Her import edilen Python modülünün kendi __name__ değeri vardır.
import ahmet
import mehmet

print(ahmet.__name__)
print(mehmet.__name__)
print(__name__)

------------------------------------------
Shebang teoremi : Bir dosyanın ilk satırına yazılan özel bir ifadedir
#!/usr/bin/env python3
   Python'u bul
   ve bununla çalıştır 
bu ifade dosyayı çalşıştırılabilen dosya yapar sadece  ch mode ile x yani çalıştırma izni vermeliyiz 

./program.py -ile çarıştırılır 

Note :python3 program.py
Yani Python programını çalıştıran Python yorumlayıcısı başlıyor.
-----------------------------------------
plant1 = Plant("Cactus", 25, 30)

plant1 Plant clasının bir instance si 
-----------------------------------------
range() -methodu
round() -methodu
----------------------------------
name mangling self._Plant__name yapar ve class dışı erişemezsin 
protected self._name  mainden ulaşamazsın 
--------------------------------------------------
static method 
class method 