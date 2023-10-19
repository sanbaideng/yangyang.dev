---
title: C++
date: 2021-06-01 11:51:44
latar belakang: bg-[#6d94c7]
tag:
kategori:
  - Pemrograman
intro: |
    Lembar contekan referensi cepat C++ yang menyediakan sintaks dan metode dasar.
pengaya (plugin):
    - copyCode
---


Memulai
--------

### hello.cpp

```cpp
#include <iostream>

int main() {
    std::cout << "Halo CheatSheets\n";
    return 0
}
```

Mengkompilasi dan menjalankan

``` skrip shell
$ g++ hello.cpp -o hello
$ ./hello
Halo CheatSheets
```

### Variabel-variabel

``` cpp
int jumlah = 5; // Bilangan bulat
float f = 0.95; // Bilangan mengambang
double PI = 3.14159; // Bilangan mengambang
char ya = 'Y'; // Karakter
std::string s = "SAYA"; // String (teks)
bool isRight = true; // Boolean

// Konstanta
const float RATE = 0.8;
```

----

``` cpp
int umur {25}; // Sejak C++11
std::cout << umur; // Cetak 25
```

### Tipe-tipe Data Primitif

| Tipe Data | Ukuran | Rentang |
|-----------|----------------|---------------------|
| `int` | 4 byte | -2^31^ ^to^ 2^31^-1 |
| `float` | 4 byte | _N/A_ |
| `double` | 8 byte | _N/A_ |
| `char` | 1 byte | -128 ^to^ 127 |
| `bool` | 1 byte | benar / salah |
| `void` | _N/A_ | _N/A_ |
| `wchar_t` | 2 ^or^ 4 byte | 1 karakter lebar |
{.show-header}

### Masukan Pengguna

```cpp
int num;

std::cout << "Ketik sebuah angka: ";
std::cin >> num;

std::cout << "Anda memasukkan " << num;
```

### Tukar

``` cpp
int a = 5, b = 10;
std::swap(a, b);

// Keluaran: a = 10, b = 5
std::cout << "a=" << a << ", b=" << b;
```

### Komentar

``` cpp
// Satu komentar satu baris dalam C++

/* Ini adalah komentar beberapa baris
   dalam bahasa C++ */
```

### Pernyataan Jika

``` cpp
if (a == 10) {
    // melakukan sesuatu
}
```

Lihat: [Kondisional](#c-kondisional)

### Perulangan

```cpp
for (int i = 0; i < 10; i++) {
    std::cout << i << "\n";
}
```

Lihat: [Perulangan](#c-perulangan)

### Fungsi

```cpp
#include <iostream>
 
void halo(); // Mendeklarasikan
 
int main() { // fungsi utama
    hello(); // Memanggil
}
 
void halo() { // Mendefinisikan
    std::cout << "Hello CheatSheets!\n";
}
```

Lihat: [Fungsi] (#c-fungsi)

### Referensi

```cpp
int i = 1;
int & ri = i; // ri adalah sebuah referensi ke i

ri = 2; // i sekarang diubah menjadi 2
std::cout << "i=" << i;

i = 3; // i sekarang berubah menjadi 3
std::cout << "ri=" << ri;
```

`ri` dan `i` merujuk ke lokasi memori yang sama.

### Ruang nama

```cpp
#include <iostream
namespace ns1 {int val(){return 5;}}
int main()
{
    std::cout << ns1::val();
}
```

---

``` cpp
#include <iostream>
namespace ns1 {int val(){return 5;}}
menggunakan namespace ns1;
menggunakan namespace std;
int main()
{
    cout << val();
}
```

Ruang nama memungkinkan pengenal global di bawah sebuah nama

Larik C++
------

### Deklarasi

```cpp
std::array<int, 3> marks; // Definisi
marks[0] = 92;
marks[1] = 97;
marks[2] = 98;

// Mendefinisikan dan menginisialisasi
std::array<int, 3> = {92, 97, 98};

// Dengan anggota-anggota yang kosong
std::array<int, 3> nilai = {92, 97};
std::cout << nilai[2]; // Keluaran: 0
```

### Manipulasi

``` cpp
┌─────┬─────┬─────┬─────┬─────┬─────┐
| 92 | 97 | 98 | 99 | 98 | 94 |
└─────┴─────┴─────┴─────┴─────┴─────┘
   0 1 2 3 4 5
```

---

``` cpp
std::array<int, 6> nilai = {92, 97, 98, 99, 98, 94};

// Mencetak elemen pertama
std::cout << nilai[0];

// Mengubah elemen kedua menjadi 99
marks[1] = 99;

// Mengambil masukan dari pengguna
std::cin >> marks[2];
```

### Menampilkan

``` cpp
char ref [5] = {'R', 'e', 'f'};

// Perulangan for berbasis rentang
for (const int &n : ref) {
    std::cout << std::string(1, n);
}

// Perulangan for tradisional
for (int i = 0; i < sizeof(ref); ++i) {
    std::cout << ref[i];
}
```

### Multidimensi

``` cpp
     j0 j1 j2 j3 j4 j5
   ┌────┬────┬────┬────┬────┬────┐
i0 | 1 | 2 | 3 | 4 | 5 | 6 |
   ├────┼────┼────┼────┼────┼────┤
i1 | 6 | 5 | 4 | 3 | 2 | 1 |
   └────┴────┴────┴────┴────┴────┘
```

---

``` cpp
int x[2][6] = {
    {1,2,3,4,5,6}, {6,5,4,3,2,1}
};
for (int i = 0; i < 2; ++i) {
    for (int j = 0; j < 6; ++j) {
        std::cout << x[i][j] << " ";
    }
}
// Keluaran: 1 2 3 4 5 6 6 5 4 3 2 1
```

C++ Kondisional
------------

### Klausa Jika

```cpp
if (a == 10) {
    // melakukan sesuatu
}
```

---

``` cpp
int jumlah = 16;

if (jumlah % 2 == 0)
{
    std::cout << "genap";
}
else
{
    std::cout << "ganjil";
}

// Keluaran: genap
```

### Pernyataan Lain Jika

``` cpp
int skor = 99;
if (skor == 100) {
    std::cout << "Luar biasa";
}
else if (skor >= 90) {
    std::cout << "Luar biasa";
}
else if (skor >= 80) {
    std::cout << "Sangat Baik";
}
else if (skor >= 70) {
    std::cout << "Baik";
}
else if (skor >= 60)
    std::cout << "OK";
else
    std::cout << "Apa?";
```

### Operator {.row-span-2}

#### Operator Relasional

| | |
|----------|------------------------------|
| `a == b` | a sama dengan b |
| `a != b` | a TIDAK sama dengan b |
| `a < b` | a lebih kecil dari b |
| `a > b` | a lebih besar dari b |
| `a <= b` | a kurang dari atau sama dengan b |
| `a >= b` | a lebih besar atau sama dengan b |

#### Operator Penugasan

| Contoh | Setara dengan |
|----------|-----------------|
| `a += b` | _Aka_ a = a + b |
| `a -= b` | _Aka_ a = a - b |
| `a *= b` | _Aka_ a = a * b |
| `a /= b` | _Aka_ a = a / b |
| `a %= b` | _Aka_ a = a % b |

#### Operator Logika

| Contoh | Arti |
|----------------|------------------------|
| `exp1 && exp2` | Keduanya benar _(AND)_ | | Keduanya benar
| `exp1 || exp2` | Salah satu bernilai benar _(OR)_ |
| `!exp` | `exp` adalah salah _(NOT)_ | | Exp

#### Operator Bitwise

| Operator | Deskripsi |
|----------|-------------------------|
| `a & b` | Biner AND |
| `a | b` | Biner OR |
| `a ^ b` | Biner XOR | Biner
| `~ a` | Komplemen Biner Satu | Komplemen Biner
| `a << b` | Pergeseran Biner ke Kiri | | `a << b` | Pergeseran Biner
| `a >> b` | Pergeseran Biner Kanan | | `a >> b` | Pergeseran Biner Kanan

### Operator Ternary

```
           ┌── Benar ──┐
Hasil = Kondisi ? Exp1 : Exp2;
           └───── False ─────┘
```

---

``` cpp
int x = 3, y = 5, max;
max = (x > y) ? x : y;

// Keluaran: 5
std::cout << max << std::endl;
```

---

``` cpp
int x = 3, y = 5, max;
if (x > y) {
    max = x;
} else {
    max = y;
}
// Keluaran: 5
std::cout << max << std::endl;
```

### Pernyataan Peralihan

``` cpp
int num = 2;
switch (num) {
    case 0:
        std::cout << "Nol";
        istirahat;
    case 1
        std::cout << "Satu";
        istirahat;
    kasus 2:
        std::cout << "Dua";
        istirahat;
    kasus 3:
        std::cout << "Tiga";
        break;
    default:
        std::cout << "Apa?";
        break;
}
```

Perulangan C++
------------

### While

```cpp
int i = 0;
while (i < 6) {
    std::cout << i++;
}

// Keluaran: 012345
```

### Do-while

``` cpp
int i = 1;
do {
    std::cout << i++;
} while (i <= 5);

// Keluaran: 12345
```

### Lanjutkan pernyataan

``` cpp
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) {
        lanjutkan;
    }
    std::cout << i;
} // Keluaran: 13579
```

### Perulangan tak terbatas

``` cpp
while (true) { // benar atau 1
    std::cout << "perulangan tak hingga";
}
```

---

``` cpp
for (;;) {
    std::cout << "perulangan tak terbatas";
}
```

---

``` cpp
for(int i = 1; i > 0; i++) {
    std::cout << "perulangan tak terbatas";
}
```

### for_each (Sejak C++11)

``` cpp
#include <iostream>

int main()
{
    auto print = [](int num) { std::cout << num << std::endl; };

    std::array<int, 4> arr = {1, 2, 3, 4};
    std::for_each(arr.begin(), arr.end(), print);
    return 0;
}
```

### Berbasis rentang (Sejak C++11)

``` cpp
for (int n : {1, 2, 3, 4, 5}) {
    std::cout << n << " ";
}
// Keluaran: 1 2 3 4 5
```

---

``` cpp
std::string halo = "CheatSheets.zip";
for (char c: halo)
{
    std::cout << c << " ";
}
// Keluaran: Q u i c k R e f . M E
```

### Memecah pernyataan

``` cpp
int password, kali = 0;
while (password != 1234) {
    if (times++ >= 3) {
        std::cout << "Terkunci!\n";
        break;
    }
    std::cout << "Password: ";
    std::cin >> kata sandi; // masukan
}
```

### Beberapa variasi

``` cpp
for (int i = 0, j = 2; i < 3; i++, j--){
    std::cout << "i=" << i << ",";
    std::cout << "j=" << j << ";";
}
// Keluaran: i=0,j=2;i=1,j=1;i=2,j=0;
```

Fungsi-fungsi C++
------------

### Argumen & Pengembalian

```cpp
#include <iostream>

int add(int a, int b) {
    mengembalikan a + b;
}

int main() {
    std::cout << add(10, 20);
}
```

`add` adalah sebuah fungsi yang mengambil 2 buah int dan mengembalikan int

### Kelebihan beban

```cpp
void fun(string a, string b) {
    std::cout << a + " " + b;
}
void fun(string a) {
    std::cout << a;
}
void fun(int a) {
    std::cout << a;
}
```

### Fungsi Bawaan

``` cpp
#include <iostream> // import library
#include <cmath> // mengimpor pustaka
 
int main() {
    // sqrt() berasal dari cmath
    std::cout << sqrt(9);
}
```

Kelas & Objek C++ {.cols-2}
-----------------

### Mendefinisikan Kelas

```cpp
class MyClass {
  public:             // Penentu akses
    int myNum; // Atribut (variabel int)
    string myString; // Atribut (variabel string)
};

```

### Membuat sebuah Objek

``` cpp
MyClass myObj; // Membuat objek dari MyClass

myObj.myNum = 15; // Mengatur nilai myNum menjadi 15
myObj.myString = "Hello"; // Mengatur nilai myString menjadi "Hello"

cout << myObj.myNum << endl; // Keluaran 15
cout << myObj.myString << endl; // Keluaran "Halo"

```

### Konstruktor

``` cpp
kelas MyClass {
  public
    int myNum;
    string myString;
    MyClass() { // Konstruktor
      myNum = 0;
      myString = "";
    }
};

MyClass myObj; // Membuat objek dari MyClass

cout << myObj.myNum << endl; // Keluaran 0
cout << myObj.myString << endl; // Keluaran ""

```

### Destruktor

``` cpp
kelas MyClass {
  public
    int myNum;
    string myString;
    MyClass() { // Konstruktor
      myNum = 0;
      myString = "";
    }
    ~MyClass() { // Destruktor
      cout << "Objek dihancurkan." << endl;
    }
};

MyClass myObj; // Membuat objek dari MyClass

// Kode di sini...

// Objek akan dihancurkan secara otomatis ketika program keluar dari scope


```


### Metode Kelas

``` cpp
kelas MyClass {
  public
    int myNum;
    string myString;
    void myMethod() { // Metode/fungsi yang didefinisikan di dalam kelas
      cout << "Halo Dunia!" << endl;
    }
};

MyClass myObj; // Membuat objek dari MyClass
myObj.myMethod(); // Memanggil metode
```


### Pengubah Akses

``` cpp
kelas MyClass {
  public:     // Penentu akses publik
    int x; // Atribut publik
  private:    // Penentu akses privat
    int y; // Atribut privat
  protected  // Penentu akses yang dilindungi
    int z; // Atribut yang dilindungi
};

MyClass myObj;
myObj.x = 25; // Diizinkan (publik)
myObj.y = 50; // Tidak diperbolehkan (private)
myObj.z = 75; // Tidak diizinkan (dilindungi)

```


### Pengambil dan Pengatur

``` cpp
class MyClass {
  private
    int myNum;
  public:
    void setMyNum(int num) { // Pengatur
      myNum = num;
    }
    int getMyNum() { // Pengambil
      kembalikan myNum;
    }
};

MyClass myObj;
myObj.setMyNum(15); // Mengatur nilai myNum menjadi 15
cout << myObj.getMyNum() << endl; // Keluaran 15

```


### Pewarisan

``` cpp
kelas Kendaraan {
  public
    string merek = "Ford";
    void membunyikan klakson() {
      cout << "Tuut, tuut!" << endl;
    }
};

class Mobil : public Kendaraan {
  public
    string model = "Mustang";
};

Mobil myCar;
myCar.membunyikan klakson(); // Keluaran "Tuut, tuut!"
cout << myCar.brand + " " + myCar.model << endl; // Keluaran "Ford Mustang"
```



Preprocessor C++
------------

### Preprocessor {.row-span-3}

- [if](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [elif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [else](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [endif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifdef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifndef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [define](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [undef](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [include](https://en.cppreference.com/w/cpp/preprocessor/include)
- [line](https://en.cppreference.com/w/cpp/preprocessor/line)
- [error](https://en.cppreference.com/w/cpp/preprocessor/error)
- [pragma](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [defined](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [__has_include](https://en.cppreference.com/w/cpp/feature_test)
- [__has_cpp_attribute](https://en.cppreference.com/w/cpp/feature_test)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [import](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/import&amp;action=edit&amp;redlink=1)
- [module](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/module&amp;action=edit&amp;redlink=1)
{.marker-none .cols-2}

### Termasuk

```cpp
#include "iostream"
#include <iostream>
```

### Mendefinisikan

``` cpp
#define FOO
#define FOO "halo"

#undef FOO
```

### If {.row-span-2}

``` cpp
#ifdef DEBUG
  console.log('hi');
#elif didefinisikan VERBOSE
  ...
#else
  ...
#endif
```

### Kesalahan

``` cpp
#if VERSI == 2.0
  #error Tidak didukung
  #peringatan Tidak benar-benar didukung
#endif
```

### Makro

``` cpp
#define DEG(x) ((x) * 57.29)
```

### Token concat

``` cpp
#define DST(nama) nama##_s nama##_t
DST(object); #=> object_s object_t;
```

### Stringifikasi

``` cpp
#define STR(nama) #nama
char * a = STR(object); #=> char * a = "object";
```

### berkas dan baris

``` cpp
#define LOG(msg) console.log(__FILE__, __LINE__, msg)
#=> console.log("file.txt", 3, "hey")
```

Lain-lain
-------------

### Urutan Pelarian

| Urutan Pelarian | Karakter |
|------------------|-----------------------|
| `\b` | Backspace |
| `\f` | Umpan formulir |
| `\n` | Baris Baru |
| `\r` | Return |
| `\t` | Tab horizontal |
| `\v` | Tab vertikal |
| `\\` | Garis miring |
| `\'` | Tanda petik tunggal |
| `\"` | Tanda petik ganda | | Tanda petik ganda
| `\"` | Tanda tanya |
| `\0` | Karakter Null |

### Kata kunci {.col-span-2 .row-span-2}

- [alignas](https://en.cppreference.com/w/cpp/keyword/alignas)
- [alignof](https://en.cppreference.com/w/cpp/keyword/alignof)
- [and](https://en.cppreference.com/w/cpp/keyword/and)
- [and_eq](https://en.cppreference.com/w/cpp/keyword/and_eq)
- [asm](https://en.cppreference.com/w/cpp/keyword/asm)
- [atomic_cancel](https://en.cppreference.com/w/cpp/keyword/atomic_cancel)
- [atomic_commit](https://en.cppreference.com/w/cpp/keyword/atomic_commit)
- [atomic_noexcept](https://en.cppreference.com/w/cpp/keyword/atomic_noexcept)
- [auto](https://en.cppreference.com/w/cpp/keyword/auto)
- [bitand](https://en.cppreference.com/w/cpp/keyword/bitand)
- [bitor](https://en.cppreference.com/w/cpp/keyword/bitor)
- [bool](https://en.cppreference.com/w/cpp/keyword/bool)
- [break](https://en.cppreference.com/w/cpp/keyword/break)
- [case](https://en.cppreference.com/w/cpp/keyword/case)
- [catch](https://en.cppreference.com/w/cpp/keyword/catch)
- [char](https://en.cppreference.com/w/cpp/keyword/char)
- [char8_t](https://en.cppreference.com/w/cpp/keyword/char8_t)
- [char16_t](https://en.cppreference.com/w/cpp/keyword/char16_t)
- [char32_t](https://en.cppreference.com/w/cpp/keyword/char32_t)
- [class](https://en.cppreference.com/w/cpp/keyword/class)
- [compl](https://en.cppreference.com/w/cpp/keyword/compl)
- [concept](https://en.cppreference.com/w/cpp/keyword/concept)
- [const](https://en.cppreference.com/w/cpp/keyword/const)
- [consteval](https://en.cppreference.com/w/cpp/keyword/consteval)
- [constexpr](https://en.cppreference.com/w/cpp/keyword/constexpr)
- [constinit](https://en.cppreference.com/w/cpp/keyword/constinit)
- [const_cast](https://en.cppreference.com/w/cpp/keyword/const_cast)
- [continue](https://en.cppreference.com/w/cpp/keyword/continue)
- [co_menunggu](https://en.cppreference.com/w/cpp/keyword/co_await)
- [co_return](https://en.cppreference.com/w/cpp/keyword/co_return)
- [co_yield](https://en.cppreference.com/w/cpp/keyword/co_yield)
- [decltype](https://en.cppreference.com/w/cpp/keyword/decltype)
- [default](https://en.cppreference.com/w/cpp/keyword/default)
- [delete](https://en.cppreference.com/w/cpp/keyword/delete)
- [do](https://en.cppreference.com/w/cpp/keyword/do)
- [double](https://en.cppreference.com/w/cpp/keyword/double)
- [dynamic_cast](https://en.cppreference.com/w/cpp/keyword/dynamic_cast)
- [else](https://en.cppreference.com/w/cpp/keyword/else)
- [enum](https://en.cppreference.com/w/cpp/keyword/enum)
- [explicit](https://en.cppreference.com/w/cpp/keyword/explicit)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [extern](https://en.cppreference.com/w/cpp/keyword/extern)
- [false](https://en.cppreference.com/w/cpp/keyword/false)
- [float](https://en.cppreference.com/w/cpp/keyword/float)
- [for](https://en.cppreference.com/w/cpp/keyword/for)
- [friend](https://en.cppreference.com/w/cpp/keyword/friend)
- [goto](https://en.cppreference.com/w/cpp/keyword/goto)
- [if](https://en.cppreference.com/w/cpp/keyword/if)
- [inline](https://en.cppreference.com/w/cpp/keyword/inline)
- [int](https://en.cppreference.com/w/cpp/keyword/int)
- [long](https://en.cppreference.com/w/cpp/keyword/long)
- [mutable](https://en.cppreference.com/w/cpp/keyword/mutable)
- [namespace](https://en.cppreference.com/w/cpp/keyword/namespace)
- [new](https://en.cppreference.com/w/cpp/keyword/new)
- [noexcept](https://en.cppreference.com/w/cpp/keyword/noexcept)
- [not](https://en.cppreference.com/w/cpp/keyword/not)
- [not_eq](https://en.cppreference.com/w/cpp/keyword/not_eq)
- [nullptr](https://en.cppreference.com/w/cpp/keyword/nullptr)
- [operator](https://en.cppreference.com/w/cpp/keyword/operator)
- [or](https://en.cppreference.com/w/cpp/keyword/or)
- [or_eq](https://en.cppreference.com/w/cpp/keyword/or_eq)
- [private](https://en.cppreference.com/w/cpp/keyword/private)
- [protected](https://en.cppreference.com/w/cpp/keyword/protected)
- [public](https://en.cppreference.com/w/cpp/keyword/public)
- [reflexpr](https://en.cppreference.com/w/cpp/keyword/reflexpr)
- [register](https://en.cppreference.com/w/cpp/keyword/register)
- [reinterpret_cast](https://en.cppreference.com/w/cpp/keyword/reinterpret_cast)
- [requires](https://en.cppreference.com/w/cpp/keyword/requires)
- [return](https://en.cppreference.com/w/cpp/language/return)
- [short](https://en.cppreference.com/w/cpp/keyword/short)
- [signed](https://en.cppreference.com/w/cpp/keyword/signed)
- [sizeof](https://en.cppreference.com/w/cpp/keyword/sizeof)
- [static](https://en.cppreference.com/w/cpp/keyword/static)
- [static_assert](https://en.cppreference.com/w/cpp/keyword/static_assert)
- [static_cast](https://en.cppreference.com/w/cpp/keyword/static_cast)
- [struct](https://en.cppreference.com/w/cpp/keyword/struct)
- [switch](https://en.cppreference.com/w/cpp/keyword/switch)
- [synchronized](https://en.cppreference.com/w/cpp/keyword/synchronized)
- [template](https://en.cppreference.com/w/cpp/keyword/template)
- [this](https://en.cppreference.com/w/cpp/keyword/this)
- [thread_local](https://en.cppreference.com/w/cpp/keyword/thread_local)
- [throw](https://en.cppreference.com/w/cpp/keyword/throw)
- [true](https://en.cppreference.com/w/cpp/keyword/true)
- [try](https://en.cppreference.com/w/cpp/keyword/try)
- [typedef](https://en.cppreference.com/w/cpp/keyword/typedef)
- [typeid](https://en.cppreference.com/w/cpp/keyword/typeid)
- [typename](https://en.cppreference.com/w/cpp/keyword/typename)
- [union](https://en.cppreference.com/w/cpp/keyword/union)
- [unsigned](https://en.cppreference.com/w/cpp/keyword/unsigned)
- [using](https://en.cppreference.com/w/cpp/keyword/using)
- [virtual](https://en.cppreference.com/w/cpp/keyword/virtual)
- [void](https://en.cppreference.com/w/cpp/keyword/void)
- [volatile](https://en.cppreference.com/w/cpp/keyword/volatile)
- [wchar_t](https://en.cppreference.com/w/cpp/keyword/wchar_t)
- [while](https://en.cppreference.com/w/cpp/keyword/while)
- [xor](https://en.cppreference.com/w/cpp/keyword/xor)
- [xor_eq](https://en.cppreference.com/w/cpp/keyword/xor_eq)
- [final](https://en.cppreference.com/w/cpp/language/final)
- [menimpa](https://en.cppreference.com/w/cpp/language/override)
- [transaction_safe](https://en.cppreference.com/w/cpp/language/transactional_memory)
- [transaction_safe_dynamic](https://en.cppreference.com/w/cpp/language/transactional_memory)
{.marker-none .cols-5}

### Preprocessor

- [if](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [elif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [else](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [endif](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifdef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [ifndef](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [define](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [undef](https://en.cppreference.com/w/cpp/preprocessor/replace)
- [include](https://en.cppreference.com/w/cpp/preprocessor/include)
- [line](https://en.cppreference.com/w/cpp/preprocessor/line)
- [error](https://en.cppreference.com/w/cpp/preprocessor/error)
- [pragma](https://en.cppreference.com/w/cpp/preprocessor/impl)
- [defined](https://en.cppreference.com/w/cpp/preprocessor/conditional)
- [__has_include](https://en.cppreference.com/w/cpp/feature_test)
- [__has_cpp_attribute](https://en.cppreference.com/w/cpp/feature_test)
- [export](https://en.cppreference.com/w/cpp/keyword/export)
- [import](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/import&amp;action=edit&amp;redlink=1)
- [module](https://en.cppreference.com/mwiki/index.php?title=cpp/keyword/module&amp;action=edit&amp;redlink=1)
{.marker-none .cols-2}

## Lihat juga

- [Infografis C++ & Cheat Sheets](https://hackingcpp.com/cpp/cheat_sheets.html) _(hackingcpp.com)_

- [Referensi C++](https://en.cppreference.com/w/) _(cppreference.com)_
- [Tutorial Bahasa C](http://www.cplusplus.com/doc/tutorial/) _(cplusplus.com)_
