Lab 1

Penggunaan end
Di dalam fungsi "print()" di dalam bahasa python terdapat parameter "end". Parameter "end" adalah parameter yang digunakan untuk memasukan string atau karakter apapun untuk mengakhiri sebuah statement. Secara default jika kita melakukan print dalam python, output akan dicetak dalam baris baru. Tapi jika kita memasukan fungsi "end" maka hasil output tidak akan langsung berada di garis baru. Contoh kode :

# Penggunaan end  
print('A', end="")  
print('B', end="")  
print('C', end="")  
print()  
print('X')  
print('Y')  
print('Z')
Output yang di dapat :

Output_end

Terlihat dari output A, B dan C dicetak dalam baris yang sama, sedangkan output X, Y dan Z dicetak dengan baris baru. Jika kalian ingin membuat garis baru menggunakan fungsi end, kalian bisa memasukan "\n".
Contoh :

print('A', end="\n") 
Penggunaan Separator
Separator "sep" dalam python digunakan sebagai pembatas antara output yang dihasilkan.

Contoh Kode :

w, x, y, z = 10, 15, 20, 25  
print(w, x, y, z, sep=',')  
print(w, x, y, z, sep='')  
print(w, x, y, z, sep=':')  
print(w, x, y, z, sep='- - - - -')
Output yang didapat :

Output_Sep

Kita bisa mengisi sep='isi_disini' dengan string atau karakter apapun.

Penggunaan string format
String format digunakan ketika kita ingin mengatur dan memposiskan print output menjadi sedemikian rupa.
Contoh kode :

# String yang belum di format
print(0, 10 ** 0)  
print(1, 10 ** 1)  
print(2, 10 ** 2)  
print(3, 10 ** 3)  
print(4, 10 ** 4)  
print(5, 10 ** 5)  
print(6, 10 ** 6)  
print(7, 10 ** 7)  
print(8, 10 ** 8)  
print(9, 10 ** 9)  
print(10, 10 ** 10)
Output :

3_Output_String-f

Kita akan membuat outputnya menjadi seperti berikut :

4_Output_String-f

Dengan Kode :

print('{0:>3} {1:>16}'.format(0, 10 ** 0))  
print('{0:>3} {1:>16}'.format(1, 10 ** 1))  
print('{0:>3} {1:>16}'.format(2, 10 ** 2))  
print('{0:>3} {1:>16}'.format(3, 10 ** 3))  
print('{0:>3} {1:>16}'.format(4, 10 ** 4))  
print('{0:>3} {1:>16}'.format(5, 10 ** 5))  
print('{0:>3} {1:>16}'.format(6, 10 ** 6))  
print('{0:>3} {1:>16}'.format(7, 10 ** 7))  
print('{0:>3} {1:>16}'.format(8, 10 ** 8))  
print('{0:>3} {1:>16}'.format(9, 10 ** 9))  
print('{0:>3} {1:>16}'.format(10, 10 ** 10))
Dalam contoh di atas terdapat { } yang berfungsi sebagai placeholder atau penempat arguments. Argument secara default urutannya adalah berurutan.

6_Output_String_f

Misalnya dalam contoh di atas, terdapat argument "0" dan "10 ** 0" didalam format(0, 10 ** 0), yang dipisah dengan tanda "," (koma), yang berarti "0" adalah argument pertama dan "10**0" adalah argument ke dua. Sedangkan angka 0 dan 1 di dalam placeholder, merupakan urutan yang kita masukan. Misalnya placeholder pada urutan pertama yaitu "{0:>3}" dan kita ingin mengganti menjadi "1" maka yang akan dicetak di placeholder pertama adalah output dari "10 ** 0". Contoh kode :

print('{1:>3} {0:>16}'.format(0, 10 ** 0))
Output yang didapat :

5_Output_String-f

Sedangkan untuk ":>3" digunakan untuk menentukan output di cetak pada urutan ke tiga. Urutan yang kosong akan menghasilkan output "spasi".
