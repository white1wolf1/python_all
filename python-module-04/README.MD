The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist ( içinde bişi varsa arkasına ekler )

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

NOTE : "t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


EX:f = open("demofile.txt") = f = open("demofile.txt", "rt")

open() function returns a file object, which has a read() method for reading the content of the file:


with open("demofile.txt") as f:
with key word  closes the file so no neef for close()


good exemle :

f = open("demofile.txt")
print(f.readline())
f.close()


read: funk can be spesifyed = print(f.read(5)) reeds only first 5 char
or readline()= only first line

with open("demofile.txt") as f:
  for x in f:
    print(x)

loops all the file !

To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

open("sa.txt,x) =creates empty file

To delete a file, you must import the OS module, and run its os.remove() function:

if os.path.exists("demofile.txt"): = checks if the file is exist

To delete an entire folder, use the os.rmdir() method but ou can only remove empty folders!

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶

Note :If the file cannot be opened, an OSError is raised


   file içini read ile okunur :
f = open("demofile.txt")
print(f.read())

 eğer dosya farklı bir  lokasyonda ise :

f = open("D:\\myfiles\welcome.txt")
print(f.read())

 read da kaç satır  okuyacağıını da söyleyebilr ;

whit ile açılan dosyayı kapatmak için uğraşmana gerekyok
with open("demofile.txt") as f:
  print(f.read(5))
  mesela ilk 5 stır 

  with open("demofile.txt") as f:
  print(f.readline()) satır okur sadece bir tane
  /n  karaakretini dahil eder


  os.remuve ile  file silebilirixzzz


  import os
os.remove("demofile.txt")


o delete an entire folder, use the os.rmdir() method:

import os
os.rmdir("myfolder")

You can only remove empty folders.


open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


file: Açılacak dosyanın adı veya yolu. Bir dosya tanımlayıcı (sayı) da verilebilir.
mode: Dosyanın nasıl açılacağı. Varsayılan "r" yani metin olarak okuma.
---
("demo.txt", "C:/klasor/demo.txt")
----


buffering: Verinin diske ya da diskten ne zaman ve hangi parçalar halinde aktarılacağını belirler. Genelde değiştirilmez. -1 varsayılan ayardır.
---
-1 (varsayılan), 0 (tamponu kapatır, yalnızca ikili modda çalışır), 1 (satır tamponu, yalnızca metin modunda) ya da 2 veya daha büyük bir sayı (tampon boyutu, bayt olarak).
---


encoding: Metnin hangi karakter kodlamasıyla okunup yazılacağı. Örneğin "utf-8". Verilmezse işletim sistemine göre değişir.
---
encoding: "utf-8", "cp1254" (Türkçe Windows), "latin-1" gibi Python’un desteklediği herhangi bir kodlama adı. Ayrıca None de olabilir. Yalnızca metin modunda kullanılmalıdır.
---

errors: Kodlama hatalarında ne yapılacağı. Varsayılan None hata fırlatır. "ignore" hatalı karakterleri atlar, ama bu veri kaybına yol açabilir.
---
errors: None (varsayılan, hata fırlatır), "strict" (aynı şey), "ignore" (hatalı karakteri atlar), "replace" (hatalı karakteri ? gibi bir karakterle değiştirir) ya d
----



newline: Satır sonlarının nasıl işleneceği. Genelde None bırakılır ve bu, \n, \r ve \r\n farklarını otomatik düzenler.

None (varsayılan): Okurken \n, \r ve \r\n hepsi \n’ye çevrilir. Yazarken \n, işletim sisteminin satır sonuna çevrilir. Çoğu durumda bunu değiştirmenize gerek yoktur.
"": Okurken satır sonları olduğu gibi bırakılır. Yazarken çeviri yapılmaz.
"\n": Okurken yalnızca \n satır sonu kabul edilir. Yazarken \n olduğu gibi yazılır.
"\r" ve "\r\n": Bunlar satır sonu olarak kullanılan belirli karakterlerdir. Eski Mac dosyaları ve bazı özel formatlar için kullanılır.


closefd: Dosya tanımlayıcıyı, dosya kapatılınca kapatıp kapatmayacağı. Normal dosya adı verildiğinde her zaman True olmalıdır.
---
closefd: True (varsayılan) ya da False. False yalnızca bir dosya tanımlayıcısı verildiğinde anlamlıdır.
opener: Dosyayı kendi yönteminizle açmak istiyorsanız kullanılan özel bir fonksiyon. Normalde kullanmazsınız.









OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError

chod 00 dosya.txt = butun herşeyi erişilmez yapar!


file = open(file_name,"r")
file ve file_name farkı nedir 
file = dosya nesnesi (İşletim sisteminin bu açık dosyayı tanıdığı numara.)
Konum (imleç): Dosyada şu an hangi noktada olduğunuz. read() çağırdığınızda okuma bu noktadan devam eder.
Mod ve kodlama: "r", "w" gibi mod ve encoding bilgisi.
Tampon: Yazılacak veya okunacak verinin geçici olarak tutulduğu alan.


file name = file_name yalnızca “hangi dosya” sorusunun cevabıdır. open bu adı alıp dosyayı açar ve bağlantıyı file değişkenine koyar. Sonrasında file üzerinden okuma ve kapatma yaparsınız.

Yani file_name adresi, file ise o adrese giderek kurduğunuz bağlantıdır. Adres yazılmadan bağlantı kurulamaz, bağlantı olmadan da dosyanın içeriğine ulaşılamaz.