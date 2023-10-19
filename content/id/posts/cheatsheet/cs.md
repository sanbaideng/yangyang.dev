---
judul: C#
tanggal: 2021-12-14 12:22:00
latar belakang: bg-[#8c4c8a]
tags:
    - berorientasi objek
    - kelas
kategori:
    - Pemrograman
intro: |
    Lembar contekan referensi cepat C# yang menyediakan sintaks dan metode dasar.
pengaya (plugin):
    - copyCode
---


Memulai
--------

### Hello.cs
```cs
class Hello {
  // metode utama
  static void Main(string[] args)
  {
    // Keluaran: Halo, dunia!
    Console.WriteLine("Halo, dunia!");
  }
}
```

Membuat direktori proyek untuk aplikasi konsol baru
```cs
$ dotnet konsol baru
```

membuat daftar semua template aplikasi
```cs
$ dotnet daftar baru
```

Mengkompilasi dan menjalankan (pastikan Anda berada di direktori proyek)
```shell script
$ dotnet run
Halo, dunia!
```



### Variabel
```cs
int intNum = 9;
long longNum = 9999999;
float floatNum = 9.99F;
double doubleNum = 99.999;
decimal decimalNum = 99.9999M;
char huruf = 'D';
bool @bool = true;
string site = "cheatsheets.zip";

var num = 999;
var str = "999";
var bo = false;
```


### Tipe Data Primitif
| Tipe Data | Ukuran | Rentang |
| --------- | ---------------- | ----------------------- |
| `int` | 4 byte | -2^31^ ^to^ 2^31^-1 |
| `long` | 8 byte | -2^63^ ^to^ 2^63^-1 |
| `float` | 4 byte | 6 ^to^ 7 digit desimal |
| `double` | 8 byte | 15 digit desimal |
| `decimal` | 16 byte | 28 ^to^ 29 digit desimal |
| `char` | 2 byte | 0 ^to^ 65535 |
| `bool` | 1 bit | benar / salah |
| `string` | 2 byte per karakter | _N/A_ |
{.show-header}



### Komentar
```cs
// Komentar satu baris

/* Multi-baris
   komentar */

// TODO: Menambahkan komentar ke daftar tugas di Visual Studio

///Komentar satu baris yang digunakan untuk dokumentasi

/// Komentar multi-baris
    digunakan untuk dokumentasi **/

```


### String
```cs
string pertama = "John";
string terakhir = "Doe";

// penggabungan string
string nama = pertama + " " + terakhir;
Console.WriteLine(nama); // => John Doe
```
Lihat: [String](#c-string)

### Masukan Pengguna
```cs
Console.WriteLine("Masukkan nomor:");
if(int.TryParse(Console.ReadLine(),out int input))
{
  // Masukan divalidasi
  Console.WriteLine($"Anda memasukkan {masukan}");
}
```


### Kondisi
```cs
int j = 10;

if (j == 10) {
  Console.WriteLine("Saya mendapatkan hasil cetak");
} else if (j > 10) {
  Console.WriteLine("Saya tidak");
} else {
  Console.WriteLine("Saya juga tidak");
}
```


### Array
```cs
char[] chars = new char[10];
chars[0] = 'a';
chars[1] = 'b';

string[] huruf = {"A", "B", "C"};
int[] daftar_ku = {100, 200};
bool[] jawaban = {true, false};
```


### Perulangan
```cs
int[] angka = {1, 2, 3, 4, 5};

for(int i = 0; i < angka.Length; i++) {
  Console.WriteLine(angka[i]);
}
```
---
``` cs
foreach(int num in numbers) {
  Console.WriteLine(num);
}
```





String C#
----------------

### Penggabungan string
```cs
string pertama = "John";
string terakhir = "Doe";

string nama = pertama + " " + terakhir;
Console.WriteLine(nama); // => John Doe
```

### Interpolasi string
``` ###
string pertama = "John";
string terakhir = "Doe";

string nama = $"{pertama} {terakhir}";
Console.WriteLine(nama); // => John Doe
```

### String Anggota {.row-span-2}
| Anggota | Deskripsi |
|------------ |-------------|
| Panjang | Properti yang mengembalikan panjang string.         |
| Compare() | Metode statis yang membandingkan dua buah string.  |
| Contains() | Menentukan apakah string berisi substring tertentu. |
| Equals() | Menentukan apakah dua string memiliki data karakter yang sama. |
| Format() | Memformat string melalui notasi {0} dan dengan menggunakan primitif lainnya. |
| Trim() | Menghapus semua contoh karakter tertentu dari karakter di belakang dan di depan. Secara default menghapus spasi di depan dan di belakang. |
| Split() | Menghapus karakter yang disediakan dan membuat larik dari karakter yang tersisa di kedua sisi. |
{.show-header}


### String kata demi kata
```cs {.wrap}
string longString = @"Saya bisa mengetikkan karakter apa pun di sini !#@$%^&*()__+ '' \n \t kecuali tanda kutip ganda dan saya akan dianggap secara harfiah. Saya bahkan bekerja dengan beberapa baris.";
```


### Contoh Anggota
```cs
// Menggunakan properti dari System.String
string lengthOfString = "Berapa panjangnya?";
lengthOfString.Length // => 9

// Menggunakan metode dari System.String
lengthOfString.Contains("Bagaimana"); // => true
```




Lain-lain
-----------

### Ketentuan Umum .NET {.col-span-2}

| Istilah | Definisi | Definisi
|------------|------------|
| Runtime | Kumpulan layanan yang diperlukan untuk menjalankan unit kode yang dikompilasi. |
| Common Language Runtime (CLR) | Terutama menempatkan, memuat, dan mengelola objek .NET. CLR juga menangani manajemen memori, hosting aplikasi, koordinasi utas, melakukan pemeriksaan keamanan, dan detail tingkat rendah lainnya. |
| Kode yang dikelola | Kode yang dikompilasi dan berjalan pada waktu proses .NET. C# / F# / VB adalah contohnya. |
| Kode yang tidak dikelola | Kode yang dikompilasi langsung ke kode mesin dan tidak dapat secara langsung dihosting oleh runtime .NET. Tidak mengandung manajemen memori bebas, pengumpulan sampah, dll. DLL yang dibuat dari C / C adalah contohnya. |
{.show-header}


