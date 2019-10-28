Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a =input(masukkan nilai a:")
	 
SyntaxError: invalid syntax
>>> a =input("masukkan nilai a:")
masukkan nilai a:20
>>> b =input("masukkan nilai b:")
masukkan nilai b:5
>>> print("variable a=" ,a)
variable a= 20
>>> print("variable b=" ,b)
variable b= 5
>>> print("hasil peggabungan (1)&(0)=&d" .format(a,b) &(20+5))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("hasil peggabungan (1)&(0)=&d" .format(a,b) &(20+5))
TypeError: unsupported operand type(s) for &: 'str' and 'int'
>>> print("hasil penggabungan {1}&{0}=%d".format(20,5) %(20+5))
hasil penggabungan 5&20=25
>>> #Konversi nilai variable
>>> a=int(20)
>>> b=int(5)
>>> print("hasil penjumlahan {1}&{0}=%d".format(20,5) %(20+5))
hasil pejumlahan 5&20=25
>>> print("hasil pembagian {1}/{0}=%d".format(20,5) %(20/5))
hasil pembagian 5/20=4
>>> 
