---
judul: Temukan
tanggal: 2020-12-28 16:52:20
tag:
    - mencari
    - file
    - direktori
kategori:
    - Perintah Linux
intro: |
    Ini adalah daftar referensi cepat dari lembar contekan untuk perintah find linux, berisi opsi dan contoh umum.
plugin
    - copyCode
---


Memulai
---------------

### Penggunaan

```shell script
$ find [path ...] [options] [expression]
```

Wildcard
```shell script
$ find . -nama "*.txt"
$ find . -nama "2020*.csv"
$ find . -name "json_*"
```

----
- [Referensi regex] (/regex) _(cheatsheets.zip)_
- [Temukan lembar contekan](https://gist.github.com/gr1ev0us/3a9b9d9dbdd38f6379288eb2686fc538) _(gist.github.com)_

### Contoh Opsi {.col-span-2}
| Opsi | Contoh | Deskripsi | Keterangan
|-------------|-------------------------------------------|---------------------------------------------|
| `-tipe` | cari . 
| `-nama` | cari . -type f -name "*.txt" | Cari file berdasarkan nama | | `-nama` | cari .
| `-iname` | cari . -type f -iname "halo" | Cari berkas berdasarkan nama (tidak peka huruf besar/kecil) | | `size` | cari .
| `-ukuran` | cari . -size +1G | Menemukan file yang lebih besar dari 1G | | `-user` | menemukan .
| `-pengguna` | cari . -type d -user jack | Cari file jack | | `-regex
| `-regex` | find /var -regex '.\*/tmp/.\*[0-9]*.file' | Menggunakan Regex dengan find. 
| `-maxdepth` | find . -maxdepth 1 -name "a.txt" | Di direktori dan subdirektori saat ini | | `-mindepth
| `-mindepth` | find / -mindepth 3 -maxdepth 5 -name pass | Di antara subdirektori level 2 dan 4 |
{.show-header}


### Tipe
| | |
|-----------|----------------------|
| `tipe d` | Direktori |
| `-ketik f` | File |
| `-tipe l` | Tautan simbolik | | Tautan simbolik
| `-jenis b` | Blok yang disangga | Blok
| `-jenis c` | Karakter tanpa buffer |
| `-jenis p` | Pipa bernama | | Pipa
| `-jenis s` | Soket |



Ukuran ###
| | |
|-----------|---------------------------|
| `ukuran b` | blok 512-byte (default) | | blok
| `-size c` | Byte |
| `ukuran k` | Kilobyte | Kilobyte
| `ukuran M` | Megabyte
| `ukuran G` | Gigabyte
| `ukuran T` | Terabyte _(hanya BSD)_ | | Terabyte
| `ukuran P` | Petabyte _(hanya BSD) _ | Petabyte

### Ukuran +/-

Temukan semua file yang lebih besar dari 10MB
```shell script
$ find / -size +10M
```

Temukan semua file yang lebih kecil dari 10MB
```shell script
$ find / -size -10M
````

Temukan semua berkas yang berukuran tepat 10M
```shell script
$ find / -size 10M
```

Menemukan Ukuran antara 100MB dan 1GB
```shell script
$ find / -size +100M -size -1G
```

Awalan `+` dan `-` menandakan lebih besar dari dan kurang dari, seperti biasa.




### Nama

Menemukan file menggunakan nama di direktori saat ini
```shell script
$ find . -nama tecmint.txt
```

Menemukan berkas di bawah direktori home

``` skrip shell
$ find /home -nama tecmint.txt
```

Mencari berkas menggunakan nama dan mengabaikan huruf besar/kecil
```shell script
$ find /home -nama tecmint.txt
```

Menemukan direktori menggunakan nama
```shell script
$ find / -tipe d -nama tecmint
```

Menemukan berkas php menggunakan nama
```shell script
$ find . -type f -name tecmint.php
```

Menemukan semua berkas php dalam direktori
``` skrip shell
$ find . -type f -name "*.php"
```


### Izin

Temukan file yang izinnya 777.

```shell script
$ find . -type f -perm 0777 -print
```

Menemukan berkas-berkas tanpa izin 777.

``` skrip shell
$ find / -type f ! -perm 777
```

Mencari file kumpulan SUID.

``` skrip shell
$ find / -perm /u=s
```

Menemukan file set SGID.

``` skrip shell
$ find / -perm /g=s
```

Menemukan berkas Hanya Baca.

``` skrip shell
$ find / -perm /u=r
```

Menemukan berkas yang dapat dieksekusi.

``` skrip shell
$ find / -perm /a=x
```


### Pemilik dan Grup

Menemukan file tunggal berdasarkan pengguna
```script shell
$ find / -user root -name tecmint.txt
```
Menemukan semua berkas berdasarkan pengguna
```shell script
$ find /home -user tecmint
```
Menemukan semua berkas berdasarkan grup
```shell script
$ find /home -group developer
```
Menemukan berkas tertentu dari pengguna
```shell script
$ find /home -user tecmint -iname "*.txt"
```


### Beberapa nama berkas
``` skrip shell {.wrap}
$ find . -type f \( -nama "*.sh" -o -nama "*.txt" \)
```
Menemukan file dengan ekstensi `.sh` dan `.txt`


### Beberapa dir


```shell script {.wrap}
$ find /opt /usr /var -nama foo.scala -tipe f
```
Menemukan berkas dengan beberapa dir


### Kosong
``` skrip shell
$ find . -ketik d -kosong
```

Menghapus semua berkas kosong dalam sebuah direktori
``` skrip shell
$ find . -ketik f -kosong -hapus
```


Menemukan Tanggal dan Waktu
-------------


### Berarti {.col-span-2}
| Opsi | Deskripsi | Keterangan
|---------|-----------------------------------------------------------------|
| `atime` | waktu akses (terakhir kali file <yel>dibuka</yel>) |
| `mtime` | waktu modifikasi (terakhir kali file <yel>konten dimodifikasi</yel>) |
| `ctime` | waktu perubahan (terakhir kali berkas <yel>inode diubah</yel>) |
#### Contoh
| Opsi | Deskripsi | Keterangan
|-----------------|------------------------------------------------------------|
| `-mtime +0` | Dimodifikasi lebih dari 24 jam yang lalu | |

| `-mtime -1` | Diubah kurang dari 1 hari yang lalu (sama dengan `-mtime 0`) | | `-mtime 1` | Diubah kurang dari 1 hari yang lalu (sama dengan `-mtime 0`)
| `-mtime 1` | Diubah antara 24 dan 48 jam yang lalu | | `-mtime 1` | Diubah antara 24 dan 48 jam yang lalu
| `-mtime +1` | Diubah lebih dari 48 jam yang lalu | | | `-mtime +1w` | Diubah lebih dari 48 jam yang lalu
| `-mtime +1w` | Terakhir diubah lebih dari 1 minggu yang lalu | | `-mtime 0` | Terakhir diubah lebih dari 48 jam yang lalu
| `-atime 0` | Terakhir diakses antara sekarang dan 24 jam yang lalu | | | `-atime 0` | Terakhir diakses antara sekarang dan 24 jam yang lalu



| `-atime -1` | Diakses kurang dari 24 jam yang lalu (sama dengan `-atime 0`)
| `-ctime -6h30m` | Status file berubah dalam 6 jam dan 30 menit terakhir


### Contoh
 Menemukan file yang diubah dalam 50 hari terakhir
```skrip shell
$ find / -mtime 50
```
 menemukan berkas-berkas yang diakses 50 hari terakhir
```shell script
$ find / -atime 50
```
 mencari berkas yang dimodifikasi 50-100 hari terakhir
```shell script
$ find / -mtime +50 -mtime -100
```
 menemukan file yang diubah dalam 1 jam terakhir
```shell script
$ find / -cmin -60
```
 menemukan berkas yang diubah dalam 1 jam terakhir
```shell script
$ find / -mmin -60
```
 menemukan berkas yang diakses dalam 1 jam terakhir
```shell script
$ find / -amin -60
```


Cari dan {.cols-2}
--------


### Temukan dan hapus {.row-span-2}

Menemukan dan menghapus beberapa file

```shell script
$ find . -type f -name "*.mp3" -exec rm -f {} \;
```

Menemukan dan menghapus file tunggal

``` skrip shell
$ find . -type f -name "tecmint.txt" -exec rm -f {} \;
```


Menemukan dan menghapus berkas berukuran 100MB
``` skrip shell
$ find / -type f -size +100m -exec rm -f {} \;
```

Menemukan berkas tertentu dan menghapusnya
``` skrip shell
$ find / -type f -name *.mp3 -size +10m -exec rm {} \;
```

### Temukan dan ganti

Temukan semua file dan ubah konten `const` menjadi `biarkan`

```shell script {.wrap}
$ find ./ -type f -exec sed -i 's/const/let/g' {} \;
```

Menemukan berkas yang dapat dibaca dan ditulis dan memodifikasi konten `lama` menjadi `baru`

```skrip shell {.wrap}
$ find ./ -type f -readable -writable -exec sed -i "s/old/new/g" {} \;
```
Lihat juga: [sed lembar contekan](/sed)
 

### Menemukan dan mengganti nama

Menemukan dan akhiran (menambahkan `.bak`)

```skrip shell {.wrap}
$ find . -type f -name 'file*' -exec mv {} {}.bak\;
```

Menemukan dan mengganti nama ekstensi (`.html` => `.gohtml`)
```shell script {.wrap}
$ find ./ -depth -name "*.html" -exec sh -c 'mv "$1" "${1%.html}.gohtml"' _ {} \;
```

### Temukan dan pindahkan
``` skrip shell
$ find . -name '*.mp3' -exec mv {} /tmp/music \;
```
Temukan dan pindahkan ke direktori tertentu (`/tmp/music`)

### Temukan dan salin
``` skrip shell
$ find . -name '*2020*.xml' -exec cp -r "{}" /tmp/backup \;
```
Temukan berkas yang cocok dan salin ke direktori tertentu (`/tmp/backup`)


### Temukan dan gabungkan

Gabungkan semua file csv dalam direktori unduhan ke dalam `gabungan.csv`

```skrip shell
$ find download -type f -iname '*.csv' | xargs cat > merged.csv
```

Gabungkan semua berkas csv yang telah diurutkan dalam direktori unduhan ke dalam `merged.csv`

```shell script {.wrap}
$ find download -type f -iname '*.csv' | sort | xargs cat > merged.csv
```


### Menemukan dan mengurutkan

Menemukan dan mengurutkan secara menaik

```skrip shell
$ find . -ketik f | mengurutkan
```

mencari dan mengurutkan secara menurun

``` skrip shell
$ find . -type f | sort -r
```


### Find dan chmod {.row-span-1}

Temukan file dan atur izin ke 644.

Skrip ```shell
$ find / -type f -perm 0777 -print -exec chmod 644 {} \;
```

Cari direktori dan setel izin ke 755.

``` skrip shell
$ find / -type d -perm 777 -print -exec chmod 755 {} \;
```


### Temukan dan kompres

Temukan semua file `.java` dan kompres menjadi `java.tar`

Skrip ```shell
$ find . -type f -name "*.java" | xargs tar cvf java.tar
```

Cari semua berkas `.csv` dan kompres ke dalam `cheatsheets.zip`

``` skrip shell
$ find . -tipe f -nama "*.csv" | xargs zip cheatsheets.zip
```


