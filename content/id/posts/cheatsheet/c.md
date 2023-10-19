---
judul: C
tanggal: 2022-12-30 09:51:44
latar belakang: bg-[#2a338a]
tags:
kategori:
  - Pemrograman
intro: |
    Lembar contekan referensi cepat C yang menyediakan sintaks dan metode dasar.
pengaya (plugin):
    - copyCode
---

Memulai
----



### hello.c {.row-span-2}

```c
#include <stdio.h>

int main(void) {
  printf("Hello World!\n");

  return 0;
}
```

Mengkompilasi berkas `hello.c` dengan `gcc`

``` bash
$ gcc hello.c -o hello
```

Jalankan biner `hello` yang telah dikompilasi

``` bash
$ ./hello
```

Keluaran => Hello World!



### Variabel {.row-span-2}

```c
int myNum = 15;

int myNum2; // jangan tetapkan, lalu tetapkan
myNum2 = 15;

int myNum3 = 15; // myNum3 adalah 15
myNum3 = 10; // myNum3 sekarang adalah 10

float myFloat = 5.99; // bilangan floating point
char myLetter = 'D'; // karakter

int x = 5
int y = 6; // bilangan bulat
int jumlah = x + y; // menambahkan variabel ke dalam penjumlahan

// mendeklarasikan beberapa variabel
int x = 5, y = 6, z = 50;
```



### Konstanta

```c
const int menitPerJam = 60;
const float PI = 3.14;
```

Praktik Terbaik

```c
const int TAHUN LAHIR = 1980;
```



### Komentar

```c
// ini adalah sebuah komentar
printf("Hello World!"); // Bisa berkomentar di mana saja di dalam berkas

/* Komentar multi-baris, cetak Hello World!
ke layar, itu luar biasa */
```



### Mencetak teks

```c
printf("Saya sedang belajar bahasa C.");
int testInteger = 5;
printf("Bilangan = %d", testInteger);

float f = 5.99; // bilangan floating point
printf("Nilai = %f", f);

short a = 0b1010110; // bilangan biner
int b = 02713; // bilangan oktal
long c = 0X1DAB83; // bilangan heksadesimal

// keluaran dalam bentuk oktal
printf("a=%ho, b=%o, c=%lo\n", a, b, c);
// keluaran => a = 126, b = 2713, c = 7325603

// Keluaran dalam bentuk desimal
printf("a=%hd, b=%d, c=%ld\n", a, b, c);
// keluaran => a=86, b=1483, c=1944451

// keluaran dalam bentuk heksadesimal (huruf kecil)
printf("a=%hx, b=%x, c=%lx\n", a, b, c);
// keluaran => a=56, b=5cb, c=1dab83

// Keluaran dalam bentuk heksadesimal (huruf besar)
printf("a=%hX, b=%X, c=%lX\n", a, b, c);
// keluaran => a=56, b=5CB, c=1DAB83
```



### Mengontrol jumlah spasi

```c
int a1 = 20, a2 = 345, a3 = 700;
int b1 = 56720, b2 = 9999, b3 = 20098;
int c1 = 233, c2 = 205, c3 = 1;
int d1 = 34, d2 = 0, d3 = 23;

printf("%-9d %-9d %-9d\n", a1, a2, a3);
printf("%-9d %-9d %-9d\n", b1, b2, b3);
printf("%-9d %-9d %-9d\n", c1, c2, c3);
printf("%-9d %-9d %-9d\n", d1, d2, d3);
```

hasil keluaran

``` bash
20 345 700
56720 9999 20098
233 205 1
34 0 23
```

Dalam `% -9d`, `d` berarti output dalam basis `10`, `9` berarti menempati setidaknya lebar `9` karakter, dan lebarnya tidak cukup untuk diisi dengan spasi, `-` berarti rata kiri



### String
```c
char salam[] = "Halo Dunia!";
printf("%s", salam);
```

string akses

```c
char salam[] = "Halo Dunia!";
printf("%c", salam[0]);
```

memodifikasi string

```c
char salam[] = "Hello World!";
salam[0] = 'J';

printf("%s", salam);
// mencetak "Jello World!"
```

Cara lain untuk membuat sebuah string

```c
char salam[] = {'H','e','l','l','\0'};

printf("%s", salam);
// print "Neraka!"
```

Membuat String menggunakan penunjuk karakter (String Literal)
```c
char *salam = "Halo";
printf("%s", salam);
// print "Halo!"
```
**CATATAN**: Literal string mungkin disimpan di bagian memori yang hanya dapat dibaca. Memodifikasi string literal akan memanggil perilaku yang tidak terdefinisi. Anda tidak dapat memodifikasinya!

`C` **tidak** memiliki tipe String, gunakan tipe `char` dan buatlah sebuah larik karakter



### Kondisi {.row-span-2}

```c
int waktu = 20;
if (waktu < 18) {
  printf("Selamat tinggal!");
} else {
  printf("Selamat malam!");
}
// Keluaran -> "Selamat malam!"
int waktu = 22;
if (waktu < 10) {
  printf("Selamat pagi!");
} else if (waktu < 20) {
  printf("Selamat tinggal!");
} else {
  printf("Selamat malam!");
}
// Keluaran -> "Selamat malam!"
```



### Operator Ternary {.col-span-2}

```c
int usia = 20;
(umur > 19) ? printf("Dewasa") : printf("Remaja");
```



### Beralih

```c
int hari = 4;

switch (hari) {
  case 3: printf("Rabu"); break;
  case 4: printf("Kamis"); break;
  default:
    printf("Akhir pekan!");
}
// keluaran -> "Kamis" (hari ke-4)
```



### Perulangan Sementara

```c
int i = 0;

while (i < 5) {
  printf("%d\n", i);
  i++;
}
```

**CATATAN**: Jangan lupa untuk menaikkan variabel yang digunakan dalam kondisi, jika tidak, perulangan tidak akan pernah berakhir dan menjadi "perulangan tak terbatas"!



### Perulangan Do/While

```c
int i = 0;

do {
  printf("%d\n", i);
  i++;
} while (i < 5);
```



### For Loop

```c
for (int i = 0; i < 5; i++) {
  printf("%d\n", i);
}
```



### Keluar dari loop Break/Continue {.row-span-2}

```c
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    break;
  }
  printf("%d\n", i);
}
```

keluar dari perulangan ketika `i` sama dengan `4`

```c
for (int i = 0; i < 10; i++) {
  if (i == 4) {
    lanjutkan;
  }
  printf("%d\n", i);
}
```

Contoh untuk melewatkan nilai `4`



### Contoh Sementara Istirahat

```c
int i = 0;

while (i < 10) {
  if (i == 4) {
    istirahat;
  }
  printf("%d\n", i);

  i++;
}
```



### Sementara melanjutkan contoh

```c
int i = 0;

while (i < 10) {
  i++;

  if (i == 4) {
    lanjutkan;
  }
  printf("%d\n", i);
}
```



### Array {.row-span-2}

```c
int myNumbers[] = {25, 50, 75, 100};

printf("%d", myNumbers[0]);
// keluaran 25
```

mengubah elemen larik

```c
int myNumbers[] = {25, 50, 75, 100};
myNumbers[0] = 33;

printf("%d", Bilangan saya[0]);
```

Perulangan melalui larik

```c
int myNumbers[] = {25, 50, 75, 100};
int i;

for (i = 0; i < 4; i++) {
  printf("%d\n", myNumbers[i]);
}
```

mengatur ukuran larik

```c
// Mendeklarasikan larik berisi empat buah bilangan bulat:
int myNumbers[4];

// menambahkan elemen
myNumbers[0] = 25;
myNumbers[1] = 50;
myNumbers[2] = 75;
myNumbers[3] = 100;
```



### Enumerasi Enum {.col-span-2}

```c
enum minggu { Mon = 1, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu };
```

mendefinisikan variabel enum

```c
enum minggu a, b, c;
enum minggu { Mon = 1, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu } a, b, c;
```

Dengan variabel enumerasi, Anda dapat menetapkan nilai dalam daftar ke variabel tersebut

```c
enum minggu { Mon = 1, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu };
enum minggu a = Mon, b = Wed, c = Sat;
// atau
enum minggu { Mon = 1, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu } a = Mon, b = Wed, c = Sat;
```



### Mencacah contoh aplikasi

```c
enum minggu {Mon = 1, Selasa, Rabu, Kamis} hari;

scanf("%d", &hari);

switch (hari) {
  case Mon: puts("Senin"); break;
  case Selasa: puts("Selasa"); break;
  case Rabu: puts("Rabu"); break;
  case Kamis: puts("Kamis"); break;
  default: puts("Error!");
}
```



### Masukan pengguna

```c
// Membuat variabel integer untuk menyimpan nomor yang kita dapatkan dari pengguna
int myNum;

// Meminta pengguna untuk memasukkan angka
printf("Silakan masukkan angka: \n");

// Mendapatkan dan menyimpan nomor yang dimasukkan oleh pengguna
scanf("%d", &myNum);

// Mengeluarkan angka yang dimasukkan oleh pengguna
printf("Nomor yang Anda masukkan: %d", myNum);
```



### String masukan pengguna

```c
// membuat sebuah string
char nama depan[30];
// Meminta pengguna untuk memasukkan beberapa teks
printf("Masukkan nama Anda: \n");
// mendapatkan dan menyimpan teks
scanf("%s", &nama_pertama);
// mengeluarkan teks
printf("Halo %s.", nama_pertama);
```



### alamat memori

Saat variabel dibuat, variabel tersebut diberi alamat memori

```c
int myUsia = 43;

printf("%p", &umurku);
// Output: 0x7ffe5367e044
```

Untuk mengaksesnya, gunakan operator referensi (`&`)



### membuat penunjuk

```c
int myAge = 43; // sebuah variabel int
printf("%d", umurku); // mengeluarkan nilai dari umurku(43)

// Keluarkan alamat memori dari myAge (0x7ffe5367e044)
printf("%p", &umurku);
```



### variabel penunjuk {.col-span-2}

```c
int myAge = 43; // sebuah variabel int
int * ptr = &usia saya; // variabel penunjuk bernama ptr, digunakan untuk menyimpan alamat usia saya

printf("%d\n", umurku); // mencetak nilai dari umurku (43)

printf("%p\n", &umurku); // mengeluarkan alamat memori dari umurku (0x7ffe5367e044)
printf("%p\n", ptr); // gunakan pointer (0x7ffe5367e044) untuk menampilkan alamat memori dari myAge
```



### Dereferensi

```c
int myUsia = 43; // deklarasi variabel
int*ptr = &umurku; // deklarasi pointer

// Referensi: keluaran myAge dengan sebuah pointer
// alamat memori (0x7ffe5367e044)
printf("%p\n", ptr);
// dereferensi: mengeluarkan nilai dari myAge dengan sebuah pointer (43)
printf("%d\n", *ptr);
```

Operator
---



### Operator Aritmatika

```c
int jumlah_ku = 100 + 50;
int jumlah1 = 100 + 50; // 150 (100 + 50)
int jumlah2 = jumlah1 + 250; // 400 (150 + 250)
int jumlah3 = jumlah2 + jumlah2; // 800 (400 + 400)
```

----

| Operator | Nama | Contoh | Contoh
|----------|-----------|---------|
| `+` | Menambahkan | `x + y` | | Add
| `-` | Kurangi | `x - y` |
| `*` | Mengalikan | `x * y` |
| `/` | Membagi | `x / y` |
| `%` | Modulo | `x % y` |
| `++` | Kenaikan | `++x` |
| `--` | Pengurangan | `--x` |



### Operator penugasan

| contoh | sebagai |
|-----------|----------------|
| x `=` 5 | x `=` 5 |
| x `+=` 3 | x `=` x `+` 3 |
| x `-=` 3 | x `=` x `-` 3 |
| x `*=` 3 | x `=` x `*` 3 |
| x `/=` 3 | x `=` x `/` 3 |
| x `%=` 3 | x `=` x `%` 3 |
| x `&=` 3 | x `=` x `&` 3 |
| x `|=` 3 | x `=` x `|` 3 |
| x `^=` 3 | x `=` x `^` 3 |
| x `>>=` 3 | x `=` x `>>` 3 |
| x `<<=` 3 | x `=` x `<<` 3 |



### Operator Perbandingan

```c
int x = 5
int y = 3; int y = 3

printf("%d", x > y);
// mengembalikan 1 (true) karena 5 lebih besar dari 3
```

----

| Simbol | Nama | Contoh |
| --------| -------| -------|
| `==` | sama dengan | x `==` y |
| `!=` | tidak sama dengan | x `!=` y |
| `>` | lebih besar dari | x `>` y |
| `<` | kurang dari | x `<` y |
| `>=` | lebih besar dari atau sama dengan | x `>=` y |
| `<=` | kurang dari atau sama dengan | x `<=` y |

Operator perbandingan digunakan untuk membandingkan dua nilai



### Operator Logika {.col-span-2}

| Simbol | Nama | Deskripsi | Contoh | Contoh
| --------| --------| --------| --------|


| `!` | `tidak` logis | Membalikkan hasil, mengembalikan nilai salah jika benar | `!(x < 5 && x < 10)` | | | Hasil terbalik, mengembalikan nilai salah jika benar



### Contoh Operator {.row-span-2}

```c
unsigned int a = 60; /*60 = 0011 1100 */
unsigned int b = 13; /*13 = 0000 1101 */
int c = 0

c = a & b; /*12 = 0000 1100 */
printf("Baris 1 -nilai c adalah %d\n", c);

c = a | b; /*61 = 0011 1101 */
printf("Baris 2 -nilai c adalah %d\n", c);
c = a ^ b; /*49 = 0011 0001 */
printf("Baris 3 -nilai c adalah %d\n", c);
c = ~a; /*-61 = 1100 0011 */
printf("Baris 4 -Nilai dari c adalah %d\n", c);
c = a << 2; /*240 = 1111 0000 */
printf("Baris 5 -Nilai c adalah %d\n", c);
c = a >> 2; /*15 = 0000 1111 */
printf("Baris 6 -Nilai dari c adalah %d\n", c);
```



### Operator bitwise {.col-span-2}

operator | deskripsi | contoh
:-|:-|:-
`&` | Operasi AND bitwise, operasi "AND" dengan digit biner | `(A & B)` akan mendapatkan `12` yaitu 0000 1100
`|` | Operator OR bitwise, operasi "atau" dengan digit biner | `(A | B) ` akan mendapatkan `61` yaitu 0011 1101
`^` | Operator XOR, melakukan operasi "XOR" dengan digit biner | `(A ^ B)` akan mendapatkan `49` yaitu 0011 0001
`~` | Operator inversi, melakukan operasi "inversi" dengan bit biner | `(~A) ` akan mendapatkan `-61` yaitu 1100 0011
`<<` | operator pergeseran kiri biner | `A << 2` akan mendapatkan `240` yaitu 1111 0000
`>>` | operator pergeseran kanan biner | `A >> 2` akan mendapatkan `15` yaitu 0000 1111

Tipe Data
---



### Tipe data dasar {.col-span-2}

| Tipe Data | Ukuran Ukuran | Rentang Rentang | Deskripsi Deskripsi |
| -----| -----| -----| -----|
| `char` | 1 byte | `-128` ~ `127` | karakter tunggal/alfanumerik/ASCII |
| `signed char` | 1 byte | `-128` ~ `127` | -|
| `unsigned char` | 1 byte | `0` ~ `255` | -|
| `int` | `2` sampai `4` byte | `-32.768` ~ `32.767` | menyimpan bilangan bulat










| `dobel panjang` | 10 byte | `3.4E-4932` ~ `1.1E+4932` | | |



### Tipe data

```c
// membuat variabel
int myNum = 5; // bilangan bulat
float myFloatNum = 5.99; // bilangan floating point
char myLetter = 'D'; // string
// Data atau angka floating point presisi tinggi
double myDouble = 3.2325467;
// mencetak variabel keluaran
printf("%d\n", myNum);
printf("%f\n", myFloatNum);
printf("%c\n", myHuruf);
printf("%lf\n", myDouble);
```

----

Tipe Data | Deskripsi
:-| :-
`char` | tipe karakter
`short` | bilangan bulat pendek
`int` | tipe bilangan bulat
`long` | bilangan bulat panjang
`float` | tipe floating-point presisi tunggal
`double` | tipe floating-point presisi ganda
`void` | tidak ada tipe



### Penentu format dasar

| penentu format | tipe data |
| -----| -----|
| `%d` atau `%i` | `int` bilangan bulat |
| `%f` | `float` tipe desimal presisi tunggal |
| `%lf` | `double` data atau angka floating point presisi tinggi |
| `%c` | karakter `char` | karakter
| `%s` | untuk string `string` string |



### Penentu format dasar

| | pendek | int | panjang
| ----| ----| ----| ----|
| Oktal | `%ho` | `%o` | `%lo` |
| Desimal | `%hd` | `%d` | `%ld` |
| Heksadesimal | `%hx` /`%hX` | `%x` /`%X` | `%lx` /`%lX` |



Contoh format data ### Contoh format data

```c
int myNum = 5;
float myFloatNum = 5.99; // bilangan floating point
char myHuruf = 'D'; // string
// mencetak variabel keluaran
printf("%d\n", myNum);
printf("%f\n", myFloatNum);
printf("%c\n", myHuruf);
```

C Preprocessor
---



### Arahan Preprocessor {.row-span-2}

perintah | deskripsi
----| ----
`#define` | mendefinisikan makro
`#include` | menyertakan file kode sumber
`#undef` | makro yang tidak terdefinisi
`#ifdef` | Mengembalikan nilai true jika makro didefinisikan
`#ifndef` | Mengembalikan nilai true jika makro tidak didefinisikan
`#if` | Kompilasi kode berikut jika kondisi yang diberikan benar
`#else` | Alternatif dari `#if`
`#elif` | Jika kondisi `#if` bernilai salah, kondisi saat ini bernilai `true`
`#endif` | Mengakhiri blok kompilasi bersyarat `#if...#else`
`#error` | Mencetak pesan kesalahan saat terjadi kesalahan standar
`#pragma` | Mengeluarkan perintah khusus ke kompiler menggunakan metode standar

```c
// ganti semua MAX_ARRAY_LENGTH dengan 20
#define MAX_ARRAY_LENGTH 20
// Dapatkan stdio.h dari pustaka sistem
#include <stdio.h>
// Dapatkan myheader.h di direktori lokal
#include "myheader.h"
#undef FILE_SIZE
#define FILE_SIZE 42 // undefine dan definisikan ke 42
```



### Makro yang telah ditentukan {.row-span-2}

makro | deskripsi
----| ----
`__TANGGAL__` | Tanggal saat ini, konstanta karakter dalam format "MMM DD YYYY"
`__TIME__` | Waktu saat ini, konstanta karakter dalam format "HH: MM: SS"
`__FILE__` | Ini akan berisi nama file saat ini, sebuah konstanta string
`__LINE__` | Ini akan berisi nomor baris saat ini, sebuah konstanta desimal
`__STDC__` | Didefinisikan sebagai `1` ketika kompiler mengkompilasi terhadap standar `ANSI`
<!--referensi:nama-kelas=daftar-gaya-->

`ANSI C` mendefinisikan sejumlah makro yang dapat Anda gunakan, tetapi Anda tidak dapat secara langsung memodifikasi makro yang sudah ditentukan ini



#### Contoh makro yang telah ditentukan

```c
#include <stdio.h>

int main() {
  printf("File :%s\n", __FILE__);
  printf("Tanggal :%s\n", __TANGGAL__);
  printf("Waktu :%s\n", __WAKTU__);
  printf("Baris :%d\n", __BARIS__);
  printf("ANSI :%d\n", __STDC__);
}
```



### Operator kelanjutan makro (\)

Makro biasanya ditulis pada satu baris.

```c
#define message_for(a, b) \
    printf(#a "dan" #b ": Kami mencintaimu!\n")
```

Jika makro terlalu panjang untuk dimuat dalam satu baris, gunakan operator kelanjutan makro ```



Operator Konstantisasi String ### (#)

```c
# menyertakan <stdio.h>

#define message_for(a, b) \
  printf(#a "dan" #b ": Kami mencintaimu!\n")

int main(void) {
  pesan_untuk(Carole, Debra);

  return 0;
}
```
Ketika kode di atas dikompilasi dan dieksekusi, kode tersebut menghasilkan hasil sebagai berikut:

```
Carole dan Debra: Kami mencintai kalian!
```

Saat Anda perlu mengonversi parameter makro menjadi konstanta string, gunakan operator konstanta string `#`



Operator penempelan tag ### (##)

```c
# menyertakan <stdio.h>

#define tokenpaster(n) printf ("token" #n "= %d", token##n)

int main(void) {
  int token34 = 40;
  tokenpaster(34);

  return 0;
}
```



Operator ### didefinisikan ()

```c
# menyertakan <stdio.h>

#if !defined (PESAN)
   #define MESSAGE "Anda berharap!"
#endif

int main(void) {
  printf("Ini adalah pesan: %s\n", PESAN);

  return 0;
}
```



### Makro yang diparameterkan

```c
int square(int x) {
  mengembalikan x * x;
}
```

Makro menulis ulang kode di atas sebagai berikut:

```c
#define square(x) ( (x) * (x) )
```

Tidak ada spasi yang diperbolehkan di antara nama makro dan tanda kurung pembuka

```c
#include <stdio.h>
#define MAX(x,y) ( (x) > (y) ? (x) : (y) )

int main(void) {
  printf("Maksimum antara 20 dan 10 adalah %d\n", MAX(10, 20));

  return 0
}
```

Fungsi C
----



### Deklarasi dan definisi fungsi {.row-span-2}

```c
int main(void) {
  printf("Hello World!");

  return 0;
}
```

Fungsi ini terdiri dari dua bagian

```c
void myFunction() { // deklarasi deklarasi
  // badan fungsi (kode yang akan dieksekusi) (definisi)
}
```

----
- `Deklarasi` menyatakan nama fungsi, tipe pengembalian dan parameter _(jika ada)_
- `Definisi` badan fungsi _(kode yang akan dieksekusi)_

----

```c
// deklarasi fungsi
void myFunction();
// metode utama
int main() {
  myFunction(); // --> memanggil fungsi

  return 0
}

void myFunction() {// Definisi fungsi
  printf("Selamat malam!");
}
```



### Panggil fungsi

```c
// membuat fungsi
void myFunction() {
  printf("Selamat malam!");
}

int main() {
  myFunction(); // memanggil fungsi
  myFunction(); // bisa dipanggil berkali-kali

  mengembalikan nilai 0;
}
// Keluaran -> "Selamat malam!"
// Keluaran -> "Selamat malam!"
```



### Parameter fungsi

```c
void myFunction(char nama[]) {
  printf("Halo %s\n", nama);
}

int main() {
  myFunction("Liam");
  myFunction("Jenny");

  return 0;
}
// Halo Liam
// Halo Jenny
```



### Beberapa parameter

```c
void myFunction(char nama[], int umur) {
  printf("Hai %s, Anda berusia %d tahun.\n",nama,umur);
}
int main() {
  myFunction("Liam", 3);
  myFunction("Jenny", 14);

  return 0;
}
// Hai Liam, umurmu 3 tahun.
// Hai Jenny, kamu berusia 14 tahun.
```



### Nilai balik {.row-span-2}

```c
int myFunction(int x) {
  mengembalikan 5 + x;
}

int main() {
  printf("Hasil: %d", myFunction(3));
  return 0;
}
// keluaran 8 (5 + 3)
```

dua parameter

```c
int myFunction(int x, int y) {
  mengembalikan x + y;
}

int main() {
  printf("Hasil: %d", myFunction(5, 3));
  // menyimpan hasil dalam sebuah variabel
  int hasil = myFunction(5, 3);
  printf("Hasil = %d", hasil);

  mengembalikan 0;
}
// hasil: 8 (5 + 3)
// hasil = 8 (5 + 3)
```



### Contoh rekursif

```c
int jumlah(int k);

int main() {
  int hasil = jumlah(10);
  printf("%d", hasil);

  return 0;
}

int jumlah(int k) {
  if (k > 0) {
    return k + sum(k -1);
  } else {
    return 0;
  }
}
```



### Fungsi matematika

```c
#include <math.h>

void main(void) {
  printf("%f", sqrt(16)); // akar kuadrat
  printf("%f", ceil(1.4)); // pembulatan ke atas (round)
  printf("%f", floor(1.4)); // pembulatan ke atas (round)
  printf("%f", pow(4, 3)); // x(4) pangkat dari y(3)
}
```

----

- `abs(x)` nilai absolut
- `acos(x)` nilai kosinus busur
- `asin(x)` sinus busur
- `atan(x)` garis singgung busur
- `cbrt(x)` akar pangkat dua
- `cos(x)` kosinus
- nilai dari `exp(x)` Ex
- `sin(x)` sinus dari x
- garis singgung dari sudut `tan(x)`

C Struktur
---



### Membuat struktur

```c
struct MyStructure { // deklarasi struktur
  int myNum; // anggota (variabel int)
  char myHuruf; // anggota (variabel char)
}; // mengakhiri struktur dengan titik koma
```

Membuat sebuah variabel struct bernama `s1`

```c{7}
struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  struct myStructure s1;

  return 0;
}
```



### String dalam struktur

```c{9}
struct myStructure {
  int myNum;
  char myLetter;
  char myString[30]; // String
};

int main() {
  struct myStructure s1;
  strcpy(s1. myString, "Beberapa teks");
  // mencetak nilai
  printf("string saya: %s", s1.myString);

  return 0;
}
```

Menetapkan nilai ke string menggunakan fungsi `strcpy`



### Mengakses anggota struktur {.row-span-2}

```c{11,12,16}
// membuat struktur bernama myStructure
struct myStructure {
  int myNum;
  char myLetter;
};

int main() {
  // Membuat variabel struktur bernama myStructure dengan nama s1
  struct myStructure s1;
  // Menetapkan nilai ke anggota-anggota s1
  s1.myNum = 13;
  s1.myHuruf = 'B';

  // Membuat variabel struktur dari myStructure bernama s2
  // dan berikan nilai padanya
  struct myStructure s2 = {13, 'B'};
  // mencetak nilai
  printf("Nomor saya: %d\n", s1.myNum);
  printf("Huruf saya: %c\n", s1.myHuruf);

  return 0
}
```

Membuat variabel struktur yang berbeda

```c
struct myStructure s1;
struct myStructure s2;
// Menetapkan nilai ke variabel struktur yang berbeda
s1.myNum = 13;
s1.myHuruf = 'B';

s2.myNum = 20;
s2.myHuruf = 'C';
```



### Menyalin struktur

```c{6}
struct myStructure s1 = {
  13, 'B', "Beberapa teks"
};

struct myStructure s2;
s2 = s1;
```

Pada contoh, nilai dari `s1` disalin ke `s2`



### Memodifikasi nilai

```c{6,7}
// Membuat variabel struct dan memberikannya sebuah nilai
struct myStructure s1 = {
  13, 'B'
};
// memodifikasi nilai
s1.myNum = 30;
s1.myHuruf = 'C';
// mencetak nilai
printf("%d %c %s",
    s1.myNum,
    s1.myHuruf);
```

pemrosesan file
---



### Fungsi pemrosesan file

fungsi | deskripsi Deskripsi
----| ----
`fopen()` | `membuka` file baru atau yang sudah ada
`fprintf()` | menulis data ke `file`
`fscanf()` | `membaca` data dari sebuah file
`fputc()` | menulis karakter ke `file`
`fgetc()` | `membaca` sebuah karakter dari sebuah berkas
`fclose()` | `menutup` berkas
`fseek()` ` mengatur penunjuk berkas ke `posisi yang diberikan`
`fputw()` | Menulis sebuah bilangan bulat `ke` sebuah berkas
`fgetw()` | `membaca` sebuah bilangan bulat dari sebuah berkas
`ftell()` | mengembalikan `posisi` saat ini
`rewind()` | mengatur penunjuk berkas ke awal berkas

Ada banyak fungsi dalam pustaka C untuk `membuka` / `membaca` / `menulis` / `mencari` dan `menutup` file



### Parameter mode terbuka

Mode Mode | Deskripsi Deskripsi
----| ----
`r` | Membuka file teks dalam mode `baca`, memungkinkan file untuk dibaca
`w` | Membuka file teks dalam mode `tulis`, memungkinkan penulisan ke file
`a` | Membuka file teks dalam mode `tambah`<br />Jika file tidak ada, file baru akan dibuat
`r+` | Membuka file teks dalam mode `baca-tulis`, memungkinkan pembacaan dan penulisan file
`w+` | Membuka file teks dalam mode `baca-tulis`, memungkinkan pembacaan dan penulisan file
`a+` | Membuka file teks dalam mode `baca-tulis`, memungkinkan pembacaan dan penulisan file
`rb` | Membuka file biner dalam mode `baca`
`wb` | Membuka file biner dalam mode `tulis`
`ab` | Membuka berkas biner dalam mode `tambahkan`
`rb+` | membuka file biner dalam mode `baca-tulis`
`wb+` | Buka file biner dalam mode `baca-tulis`
`ab+` | membuka file biner dalam mode `baca-tulis`



### Buka berkas: fopen()

```c{6}
#include <stdio.h>

void main() {
  FILE * fp;
  char ch;

  fp = fopen("file_handle.c", "r");

  while (1) {
    ch = fgetc(fp);
    if (ch == EOF)
      break
    printf("%c", ch);
  }
  fclose(fp);
}
```

Setelah melakukan semua operasi pada berkas, berkas harus ditutup dengan `fclose()`



### Menulis ke berkas: fprintf()

```c{7}
#include <stdio.h>

void main() {
  FILE * fp;
  fp = fopen("file.txt", "w"); // membuka file

  // menulis data ke file
  fprintf(fp, "Halo file untuk fprintf..\n");
  fclose(fp); // menutup berkas
}
```



### Baca file: fscanf()

```c{6}
#include <stdio.h>

void main() {
  FILE * fp;

  char buff[255]; // Membuat sebuah array char untuk menyimpan data file
  fp = fopen("file.txt", "r");

  while(fscanf(fp, "%s", buff) != EOF) {
    printf("%s ", buff);
  }
  fclose(fp);
}
```



### Menulis ke file: fputc()

```c{6}
#include <stdio.h>

void main() {
  FILE * fp;
  fp = fopen("file1.txt", "w"); // membuka file
  fputc('a',fp); // menulis sebuah karakter ke dalam file
  fclose(fp); // menutup berkas
}
```



### Baca file: fgetc()

```c{8}
#include <stdio.h>
#include <conio.h>

void main() {
  FILE * fp;
  char c

  clrscr();

  fp = fopen("myfile.txt", "r");

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }
  fclose(fp);

  getch();
}
```



### Menulis ke file: fputs()

```c {8}
#include <stdio.h>
#include <conio.h>

void main() {
  FILE * fp;

  clrscr();

  fp = fopen("myfile2.txt", "w");
  fputs("halo pemrograman c",fp);
  fclose(fp);

  getch();
}
```



### Baca file: fgets()

```c {10}
#include <stdio.h>
#include <conio.h>

void main() {
  FILE * fp;
  char text[300];

  clrscr();

  fp = fopen("myfile2.txt", "r");
  printf("%s", fgets(text, 200, fp));
  fclose(fp);

  getch();
}
```



### fseek()

```c{8}
#include <stdio.h>

void main(void) {
  FILE * fp;

  fp = fopen("myfile.txt", "w+");
  fputs("Ini Buku", fp);

  // Mengatur penunjuk berkas ke posisi yang diberikan
  fseek(fp, 7, SEEK_SET);

  fputs("Kenny Wong", fp);
  fclose(fp);
}
```

mengatur penunjuk berkas ke posisi yang diberikan



### memundurkan ()

```c{11}
#include <stdio.h>
#include <conio.h>

void main() {
  FILE * fp;
  char c

  clrscr();

  fp = fopen("file.txt", "r");

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }

  rewind(fp); // memindahkan penunjuk berkas ke awal berkas

  while( (c = fgetc(fp) ) != EOF) {
    printf("%c", c);
  }
  fclose(fp);

  getch();
}
// output
// Hello World! Hello World!
```



### ftell()

```c{11}
#include <stdio.h>
#include <conio.h>

void main () {
   FILE * fp;
   int panjang;

   clrscr();

   fp = fopen("file.txt", "r");

   fseek(fp, 0, SEEK_END);
   length = ftell(fp); // kembalikan posisi saat ini
   fclose(fp);

   printf("Ukuran berkas: %d byte", length);

   getch();
}
// keluaran
// ukuran file: 18 byte
```
