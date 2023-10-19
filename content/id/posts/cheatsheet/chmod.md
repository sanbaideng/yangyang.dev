---
judul: Chmod
tanggal: 2021-07-01 10:51:44
latar belakang: bg-emerald-600
tags:
    - izin
kategori:
    - Perintah Linux
intro: |
    Lembar contekan referensi cepat ini memberikan gambaran singkat mengenai perizinan file, dan pengoperasian perintah chmod
plugin:
    - copyCode
---


Memulai
--------


### Sintaks
```skrip shell
$ chmod [options] <perizinan> <file>
```
#### Contoh
```shell
$ chmod 755 foo.txt
$ chmod +x cheatsheets.py
$ chmod u-x cheatsheets.py
$ chmod u=rwx,g=rx,o= cheatsheets.sh
```
#### Mengubah berkas dan direktori secara rekursif
``` shell
$ chmod -R 755 my_directory
```
Perintah `chmod` adalah singkatan dari "ubah mode"


### Generator Chmod
<widget name="chmod"/>

Chmod Generator memungkinkan Anda membuat perizinan secara cepat dan visual dalam bentuk numerik dan simbolik.


### Izin Umum
| Perintah | s | Arti |
|---------|-----------|------------------------------|
| `400` | r-------- | Hanya dapat dibaca oleh pemilik |
| `500` | r-x------ | Hindari Pengubahan |
| `600` | rw------- | Dapat diubah oleh pengguna |
| `644` | rw-r--r-- | Baca dan ubah oleh pengguna |
| `660` | rw-rw---- | Dapat diubah oleh pengguna dan grup |
| `700` | rwx------ | Hanya pengguna yang memiliki akses penuh |
| `755` | rwxr-xr-x | Hanya dapat diubah oleh pengguna |
| `775` | rwxrwxr-x | Mode berbagi untuk grup |
| `777` | rwxrwxrwx | Semua orang dapat melakukan segalanya |


### Menjelaskan
```shell
$ ls -l
-rw-r--r-- 1 root root 3 Jun 29 15:35 a.log
drwxr-xr-x 2 root root 2 Jun 30 18:06 dir
```
#### Analisis perizinan "dir"
``` teks
d rwx r-x r-x
┬ ─┬─ ─┬─ ─┬─
│ │ │ │
│ │ │ └─ 4. Lain-lain │ 5 (4 + 0 + 1)
│ │ └────── 3. Kelompok ｜ 5 (4 + 0 + 1)
│ └─────────── 2. Pengguna ｜7 (4+2+1)
└─────────────── 1. Jenis File | direktori
```


### Mode Izin {.col-span-2}
| Izin | Deskripsi | Oktal | Desimal |
|------------|-------------------------|-------|-----------|
| `---` | Tidak Ada Izin | 000 | 0 (0+0+0) |
| `--x` | Jalankan | 001 | 1 (0+0+1) |
| `-w-` | Tulis | 010 | 2 (0+2+0) |
| `-wx` | Jalankan dan Tulis | 011 | 3 (0+2+1) |
| `r--` | Baca | 100 | 4 (4+0+0) |
| `r-x` | Baca dan Jalankan | 101 | 5 (4+0+1) |
| `rw-` | Baca dan Tulis | 110 | 6 (4+2+0) | | | `rwx` | Baca dan Eksekusi | 110 | 6 (4+2+0) |
| `rwx` | Baca, Tulis, dan Jalankan | 111 | 7 (4+2+1) |
{.show-header}



### Objek
| Siapa (abbr.) | Arti |
|-------------|--------------------|
| `u` | `U`pengguna |
| `g` | `G` kelompok |
| `o` | `O`orang lain |
| `a` | `A`semua, sama seperti ugo |
{.show-header}


### Izin
| Singkatan | Izin | Nilai |
|--------------|---------------|-------|
| `r` | `R`Baca | 4 |
| `w` | `W` Write | 2 |
| `x` | E`x`eksekusi | 1 |
| `-` | Tidak ada izin | 0 |
{.show-header}


### Jenis File
| Singkatan | Jenis File |
|--------------|-----------------|
| `d` | `D`direktori |
| `-` | File biasa |
| `l` | Tautan Simbolik `L` |
{.show-header}



Contoh Chmod
--------


### Operator
| Simbol | Deskripsi | Keterangan
|--------|-------------|
| `+` | Menambahkan |
| `-` | Menghapus |
| `=` | Mengatur |


### chmod 600
```shell
$ chmod 600 example.txt
$ chmod u=rw,g=,o= example.txt
$ chmod a+rwx,u-x,g-rwx,o-rwx example.txt
```


### chmod 664
``` shell
$ chmod 664 example.txt
$ chmod u=rw,g=rw,o=r example.txt
$ chmod a+rwx,u-x,g-x,o-wx example.txt
```

### chmod 777
``` shell
$ chmod 777 example.txt
$ chmod u=rwx,g=rwx,o=rwx example.txt
$ chmod a=rwx example.txt
```


### Mode simbolik {.row-span-3}
Menolak izin eksekusi untuk semua orang.
``` shell
$ chmod a-x chmodExampleFile.txt
```
Izinkan izin baca untuk semua orang.
```shell
$ chmod a+r chmodExampleFile.txt
```
Membuat sebuah berkas dapat dibaca dan ditulis oleh grup dan orang lain.
```shell
$ chmod go+rw chmodExampleFile.txt
```
Membuat skrip shell yang dapat dieksekusi oleh pengguna/pemilik.
```shell
$ chmod u+x chmodExampleScript.sh
```
Izinkan semua orang untuk membaca, menulis, dan mengeksekusi berkas dan mengaktifkan group-ID yang ditetapkan.
```shell
$ chmod =rwx,g+s chmodExampleScript.sh
```

### Menghapus Izin {.row-span-3}
Untuk menghapus hak akses baca tulis yang diberikan pada sebuah berkas, gunakan sintaks berikut ini:
``` shell
$ chmod o-rw contoh.txt
```
Untuk berkas example.txt, kita dapat menghapus perizinan baca tulis menggunakan chmod for group dengan menjalankan perintah berikut:
```shell
$ chmod g-rx example.txt
```
Untuk menghapus izin baca tulis chmod dari grup sekaligus menambahkan izin baca tulis ke publik/lainnya, kita dapat menggunakan perintah berikut:
```shell
$ chmod g-rx, o+rx example.txt
```
Namun, jika Anda ingin menghapus semua perizinan untuk grup dan lainnya, Anda dapat melakukannya dengan menggunakan perintah go=:
```shell
$ chmod go= example.txt
```

### Dapat dieksekusi
```shell
$ chmod +x ~/example.py
$ chmod u+x ~/example.py
$ chmod a+x ~/example.py
```

### chmod 754
``` shell
$ chmod 754 foo.sh
$ chmod u=rwx,g=rx,o=r foo.sh
```



Praktik-praktik Chmod
---------------

### Izin SSH
```skrip shell
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
$ chmod 600 ~/.ssh/id_rsa
$ chmod 600 ~/.ssh/id_rsa.pub
$ chmod 400 /path/to/access_key.pem
```

### Izin Web
``` skrip shell
$ chmod -R 644 /var/www/html/
$ chmod 644 .htaccess
$ chmod 644 robots.txt
$ chmod 755 /var/www/uploads/
$ find /var/www/html -type d -exec chmod 755 {} \;
```

### Perubahan Batch
``` skrip shell
$ chmod -R 644 /path Anda
$ find /path -type d -exec chmod 755 {} \;
$ find /path -type f -exec chmod 644 {} \;
```
Lihat: [Pergantian Perintah](https://tldp.org/LDP/abs/html/commandsub.html)


## Lihat juga
* [Ubah Izin Berkas dengan chmod](https://www.linode.com/docs/guides/modify-file-permissions-with-chmod/) _(linode.com)_
