---
judul: Anak panah
tanggal: 2021-11-04 10:12:25
latar belakang: bg-[#58aee9]
tags:
    - anak panah
    - berkibar
kategori:
  - Pemrograman
intro: |
    Lembar contekan Dart dengan konsep, fungsi, metode, dan banyak lagi yang paling penting. Referensi cepat yang lengkap untuk pemula.
pengaya:
    - copyCode
---




Memulai {.cols-2}
------------

### hello.dart
```dart
// fungsi tingkat atas di mana eksekusi aplikasi dimulai
void main(){
    print("Hello World!"); // Mencetak ke konsol
}
```
Setiap aplikasi memiliki fungsi main()


### Variabel

``` anak panah
int x = 2; // diketik secara eksplisit
var p = 5; // tipe yang disimpulkan - Var umum dengan inferensi tipe

dynamic z = 8; // variabel bisa mengambil tipe apa saja
z = "cool"; // dingin

// jika Anda tidak pernah berniat untuk mengubah sebuah variabel, gunakan final atau const. Sesuatu yang seperti ini:

final email = "temid@gmail.com"; // Sama seperti var tetapi tidak dapat dipindahkan
final String email = "temid@gmail.com"; // Anda tidak dapat mengubah nilainya

const qty = 5; // Konstanta waktu kompilasi
```


### Tipe data

``` anak panah

int umur = 20; // bilangan bulat, rentang -2^63 sampai 2^63 - 1
double tinggi = 1.85; // bilangan floating-point

// Anda juga bisa mendeklarasikan variabel sebagai num
num x = 1; // x dapat memiliki nilai int dan double
num += 2.5;
print(num); //Mencetak: 3.5

String nama = "Nicola";

bool isFavourite = true;
bool isLoaded = false;
```


### Interpolasi string

``` anak panah
// dapat menggunakan qoutes tunggal atau ganda untuk tipe String
var firstName = 'Nicola';
var lastName = "Tesla";

// dapat menyematkan variabel dalam string dengan $
String nama lengkap = "$nama_pertama $nama_kelapa";

// menggabungkan dengan +
var nama = "Albert " + "Einstein";

String upperCase = '${nama_pertama.toUpperCase()}';
print(upperCase); //Mencetak: NICOLA
```

### Komentar
``` anak panah
// Ini adalah komentar satu baris yang normal.

/// Ini adalah komentar dokumentasi, digunakan untuk mendokumentasikan pustaka,
/// kelas-kelas, dan anggota-anggotanya. Alat-alat seperti IDE dan dartdoc memperlakukan
/// komentar doc secara khusus.

/* Komentar seperti ini juga didukung. */
```

### Impor
``` dart
// Mengimpor pustaka inti
import 'dart:math';

// Mengimpor pustaka dari paket eksternal
import 'package:test/test.dart';

// Mengimpor berkas
import 'path/to/my_other_file.dart';
```


Operator {.cols-2}
------------

### Operator Aritmatika
```dart
print(2 + 3); //Mencetak: 5
print(2 - 3); //Mencetak: -1
print(2 * 3); //Mencetak: 6
print(5 / 2); //Cetak: 2.5 - Hasil adalah dobel
print(5 ~/ 2); //Cetak: 2 - Hasil berupa int
print(5 % 2); //Mencetak: 1 - Sisa

int a = 1, b;
// Penambahan
b = ++a; // preIncrement - Penambahan a sebelum b mendapatkan nilainya.
b = a++; // postIncrement - Penambahan a SETELAH b mendapatkan nilainya.

//Decrement
b = --a; // predecrement - Pengurangan a sebelum b mendapatkan nilainya.
b = a--; // postdecrement - Pengurangan a SETELAH b mendapatkan nilainya.
```


### Operator kesetaraan dan relasional
``` anak panah
print(2 == 2); //Mencetak: benar - Sama dengan
print(2 != 3); //Cetak: true - Tidak Sama
print(3 > 2); //Cetak: true - Lebih besar dari
print(2 < 3); //Print: true - Kurang dari
print(3 >= 3); //Print: true - Lebih besar dari atau sama dengan
print(2 <= 3); //Print: true - Kurang dari atau sama dengan
```


### Operator-operator logika
``` anak panah
// !expr membalikkan ekspresi (mengubah salah menjadi benar, dan sebaliknya)
// || logika OR
// && logika AND
bool isOutOfStock = false;
int jumlah = 3;
if (!isOutOfStock && (quantity == 2 || quantity == 3)) {
  // ... Pesan produk ...
}
```




Arus Kontrol : 2. Kondisional {.cols-2}
------------


### if dan else jika
```dart
if (usia < 18){
    print("Remaja");
} else if( umur > 18 && umur < 60){
    print("Dewasa");
} else {
    print("Tua");
}
```


### mengganti huruf besar/kecil
``` anak panah
enum Hewan Peliharaan {anjing, kucing}
Hewan peliharaan myPet = Pet.dog;
switch(myPet){
    case Pet.dog:
        print('Hewan Peliharaan saya adalah Anjing.');
        break;
    case Pet.cat:
        print('Hewan Peliharaan Saya adalah Kucing.');
        break
    default:
        print('Saya tidak memiliki Hewan Peliharaan');
}
// Mencetak: Hewan peliharaan saya adalah Anjing.
```




Mengendalikan Aliran : 1. Loop
------------


### perulangan sementara
```dart
while (!dreamsAchieved) {
  bekerjaKeras();
}
```
perulangan while memeriksa kondisi sebelum iterasi perulangan

### perulangan do-while
``` anak panah
do {
  bekerjaKeras();
} while (!mimpiCapai);
```
perulangan do-while memverifikasi kondisi setelah eksekusi pernyataan di dalam perulangan

### for loop (perulangan)
``` anak panah
for(int i=0; i<10; i++){
    print(i);
}

var angka = [1,2,3];
// perulangan for-in untuk daftar
for(var angka dalam bilangan){
    print(angka);
}
```



Koleksi {.cols-2}
------------

### Daftar

```dart
// kelompok objek yang terurut
var list = [1, 2, 3];

print(list.length); //Mencetak: 3
print(list[1]); //Mencetak: 2

// cara-cara lain untuk deklarasi dan inisialisasi daftar

List<String> kota-kota = <String>["New York", "Mumbai", "Tokyo"];

// Untuk membuat daftar yang merupakan konstanta waktu kompilasi
const constantCities = const ["New York", "Mumbai", "Tokyo"];
```


### Set

```dart
// Sebuah set di Dart adalah kumpulan item unik yang tidak terurut.
var halogen = {'fluor', 'klorin', 'bromin', 'yodium', 'astrofosfat'};

// untuk membuat himpunan kosong
var nama-nama = <String>{};
Set<String> names = {}; // Ini juga bisa digunakan.
//var nama = {}; // Membuat sebuah peta, bukan himpunan.
```


### Peta

``` anak panah
// peta adalah objek yang mengasosiasikan kunci dan nilai
var orang = Map<String, String>();
// Untuk menginisialisasi peta, lakukan ini:
person['firstName'] = 'Nicola';
person['lastName'] = 'Tesla';

print(person); //Mencetak: {nama depan: Nicola, nama belakang: Tesla}
print(person['lastName']); //Cetak: Tesla


var nobleGases = {
  // Key: Nilai
  2: 'helium',
  10: 'neon',
  18: 'argon',
};
```



Fungsi {.cols-2}
------------

### Fungsi
```dart
// fungsi-fungsi dalam dart adalah objek dan memiliki tipe
int tambah(int a, int b){
    mengembalikan a + b;
}

// fungsi-fungsi dapat ditetapkan ke variabel-variabel
int jumlah = add(2,3); // mengembalikan: 5

// dapat diberikan sebagai argumen ke fungsi lain
int totalJumlah = add(2, add(2,3)); // mengembalikan: 7
```


Sintaks Panah (=>) ### Sintaks Panah (=>)
``` anak panah
// fungsi yang hanya berisi satu ekspresi, Anda dapat menggunakan sintaksis singkatan
bool isFav(Produk produk) => favProductsList.contains(produk);
```

### Fungsi anonim (lambda)
``` anak panah
// fungsi satu baris kecil yang tidak memiliki nama
int tambah(a,b) => a+b;

// fungsi lambda kebanyakan dilewatkan sebagai parameter ke fungsi lain
const list = ['apel', 'pisang', 'jeruk'];
list.forEach(
(item) => print('${list.indexOf(item)}: $item'));
//Mencetak: 0: apel 1: pisang 2: jeruk
```

Kelas dan Objek
----------

### Kelas
``` anak panah
class Kucing {
    Nama string;

    // metode
    void suara(){
        print("Meong");
    }
}
```


### Objek
``` anak panah
// contoh dari sebuah kelas
// di bawah myCat adalah objek dari kelas Kucing

void main(){
    Kucing myCat = Kucing();
    myCat.name = "Kucing";
    myCat.voice(); // Mencetak: Meong
}
```


### Konstruktor
``` anak panah
class Kucing {
    String nama;
    Kucing(ini.nama);
}
void main(){
    Kucing myCat = Cat("Kucing");
    print(myCat.name); // Mencetak: Kitty
}
```


### Kelas Abstrak
``` anak panah
// kelas abstrak-kelas yang tidak bisa diinstansiasi
// Kelas ini dideklarasikan sebagai kelas abstrak sehingga tidak bisa diinstansiasi.
kelas abstrak AbstractContainer {
  // Mendefinisikan konstruktor, field, metode...

  void updateChildren(); // Metode abstrak.
}
```


### Pengambil Pengatur
``` anak panah
// menyediakan akses baca dan tulis ke properti objek
kelas Kucing {
    Nama string;
    
    // pengambil
    String mendapatkan nama kucing {
        mengembalikan nama;
    }

    // setter
    void set namaKucing(String nama){
        this.name = nama;
    }
}
```


Antarmuka implisit {.cols-2}
------------

### Antarmuka dasar
```dart
// Seseorang. Antarmuka implisit berisi fungsi menyapa().
class Orang {
  // Dalam antarmuka, tetapi hanya terlihat di pustaka ini.
  final String _nama;

  // Tidak ada di antarmuka, karena ini adalah konstruktor.
  Person(this._nama);

  // Di dalam antarmuka.
  String menyapa(String siapa) => 'Halo, $siapa. Saya $_nama';
}

// Sebuah implementasi dari antarmuka Person.
class Penipu mengimplementasikan Orang {
  String get _nama => '';

  String menyapa(String siapa) => 'Hai $siapa. Apakah Anda tahu siapa saya?';
}

String menyapaBob(Person orang) => orang.menyapa('Bob');

void main() {
  print(greetBob(Person('Kathy'))); // Halo, Bob. Saya Kathy.
  print(greetBob(Penipu())); // Hai Bob. Apakah Anda tahu siapa saya?
}
```

### Memperluas kelas
``` anak panah
kelas Telepon {

    void use(){
        _panggilan();
        _kirimPesan();
    }
}
// Gunakan extends untuk membuat subkelas
class SmartPhone extends Phone {
    void use(){
        // gunakan super untuk merujuk ke superclass
        super.use();
        _mengambilFoto();
        _memainkanGames();
    }
}
```

Pengecualian
------------

### Throw
```dart
// melempar atau membangkitkan dan eksepsi
throw IntegerDivisionByZeroException();

// Anda juga bisa melempar objek sembarang
melempar "Produk kehabisan stok!";
```

### Menangkap
``` anak panah

try {
    int c = 3/0;
    print(c);
} on IntegerDivisionByZeroException {
    // Pengecualian khusus
    print('Tidak dapat membagi bilangan bulat dengan 0.')
} on Exception catch (e) {
    // Hal lain yang merupakan pengecualian
    print('Pengecualian yang tidak diketahui: $e');
} catch (e) {
    // Tidak ada tipe yang ditentukan, menangani semua
    print('Sesuatu yang benar-benar tidak diketahui: $e');
}

```
### Akhirnya
``` anak panah
// Untuk memastikan bahwa beberapa kode berjalan baik ketika ada pengecualian atau tidak
try {
  masakMakanan();
} catch (e) {
  print('Error: $e'); // Tangani pengecualian terlebih dahulu.
} finally {
  cleanKitchen(); // Kemudian bersihkan.
}
```


Futures
------------
### Asinkronisasi Menunggu
```dart
// fungsi yang asinkron: fungsi ini akan kembali setelah menyiapkan operasi yang mungkin memakan waktu
// Kata kunci async dan menunggu mendukung pemrograman asinkron

Future<String> login() {
 String userName = "Temidjoy";
 return
  Future.delayed(
    Durasi(detik: 4), () => nama_pengguna);
}

// Asinkron
main() async {
 print('Mengotentikasi harap tunggu...');
 print(menunggu userName());
}
```



Lain-lain {.cols-2}
------------

### Null dan Null aware

```dart
int x; // Nilai awal dari setiap objek adalah null

// ?? operator sadar null

x ??=6; // operator penugasan, yang memberikan nilai sebuah variabel hanya jika variabel tersebut saat ini bernilai null
print(x); //Mencetak: 6

x ??=3;
print(x); // Mencetak: 6 - hasilnya tetap 6

print(null ?? 10); // Mencetak: 10. Menampilkan nilai di sebelah kiri jika bukan null, jika tidak, kembalikan nilai di sebelah kanan
```



### Operator Ternary
``` anak panah
// kondisi ? exprIfTrue : exprIfFalse
bool isAvailable;

isAvailable ? orderproduct() : addToFavourite();
```


### Operator Penyebaran (...)

``` anak panah
// untuk menyisipkan beberapa nilai ke dalam sebuah koleksi.
var list = [1, 2, 3];
var list2 = [0, ... list];

print(list2.length); //Mencetak: 4
```

### Notasi bertingkat (..)

``` anak panah
// memungkinkan Anda untuk membuat urutan operasi pada objek yang sama

// daripada melakukan ini
var user = User();
user.name = "Nicola";
user.email = "nicola@g.c";
user.age = 24;

// Anda dapat melakukan ini
var user = User()
  ..nama = "Nicola"
  ..email = "nicola@g.c"
  ..age = 24;
```

### Akses Properti Bersyarat
``` anak panah
userObject?.userName

/ / Potongan kode di atas setara dengan berikut ini:
(userObject != null) ? userObject.userName : null

//Anda dapat merantai beberapa penggunaan ?. bersama-sama dalam satu ekspresi
userObject?.userName?.toString()

// Kode sebelumnya mengembalikan nilai null dan tidak pernah memanggil toString() jika userObject atau userObject.userName bernilai null
```
