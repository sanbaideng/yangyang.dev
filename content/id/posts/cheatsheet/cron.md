---
Judul: Cron
tanggal: 2020-12-16 18:28:43
latar belakang: bg-red-500
tags:
    - jadwal
    - crontab
    - waktu
kategori:
    - Perintah Linux
intro: |
    [Cron](https://en.wikipedia.org/wiki/Cron) paling cocok untuk menjadwalkan tugas yang berulang. Penjadwalan tugas satu kali dapat dilakukan dengan menggunakan utilitas at yang terkait.
plugin:
    - copyCode
---


Format Crontab {.cols-2}
------

Format ###

```
Min Jam Hari Senin Hari Kerja
```

-------

```
* * * * * * perintah yang akan dieksekusi
```

```
┬ ┬ ┬ ┬ ┬
│ │ │ │ └─ Hari dalam seminggu (0 = Minggu .. 6 = Sabtu)
│ │ │ └────── Bulan (1..12)
│ │ └─────────── Hari dalam Bulan (1..31)
│ └──────────────── Jam (0..23)
└───────────────────── Menit (0..59)
```

------
------

| Bidang | Rentang | Karakter khusus
|--------------|--------|--------------------|
| Menit | 0 - 59 | , - * / |
| Jam | 0 - 23 | , - * / |
| Hari dalam Bulan | 1 - 31 | , - * / | ? / L W |
Bulan | 1 - 12 | , - * / | | Bulan
| Hari dalam Minggu | 0 - 6 | , - * ? / L # |
{.show-header}


### Contoh

| Contoh | Deskripsi
|----------------|------------------------|
| `*/15 * *` | Setiap 15 menit | |.
| `0 * * *` | Setiap jam | |.
| `0 */2 * *` | Setiap 2 jam
| `15 2 * * *` | Pada pukul 2:15 pagi setiap hari ||.
| `15 2 * * * ` | Pada pukul 2:15 dini hari setiap hari | |.

| `10 9 * * * 5` | Pukul 09:10 setiap hari Jumat | ?
| `0 0 * * 0` | Pada tengah malam setiap hari Minggu | ?

| `15 2 * * * 1L` | Pada pukul 2:15 pagi pada hari Senin terakhir setiap bulan ||.
| `15 0 * * 4#2` | Pada pukul 00:15 pada hari Kamis kedua setiap bulan | |.
| `0 0 1 * *` | Setiap tanggal 1 setiap bulan (bulanan) | |.
| | `0 0 1 1 *` | Setiap tanggal 1 Januari (tahunan) | |.




### String khusus

| String Khusus | Arti
|----------------|----------------------------------------------------|
| @reboot | Jalankan sekali, saat pengaktifan sistem _(non-standar)_ |
| @tahunan | Jalankan sekali setiap tahun, "0 0 1 1 *". _(non-standar)_ | | @tahunan
| @tahunan | (sama seperti @tahun) _(non-standar)_ | |
| @bulanan | Jalankan sekali setiap bulan, "0 0 1 1 * *" _(non-standar)_ | | @minggu
| @mingguan | Jalankan sekali setiap minggu, "0 0 * * 0" _(non-standar)_ | | @mingguan
| @daily | Jalankan sekali setiap hari, "0 0 * * * *" _(non-standar)_ | | @malam | (tidak standar)
| @tengah malam | (sama seperti @hari-hari) _(non-standar)_ | |
| @hourly | Jalankan sekali dalam satu jam, "0 0 * * * *" _(non-standar)_ | | @malam


### Perintah crontab


| - | - |
|--------------|-------------------------------------------------------------------------|
| `crontab -e` | Mengedit atau membuat file crontab jika belum ada.
| `crontab -l` | Menampilkan file crontab.                                               
| `crontab -r` | Menghapus file crontab.                                                |
| `crontab -v` | Menampilkan waktu terakhir kali Anda mengedit file crontab.
{.shortcuts}


### Karakter khusus {.col-span-2}
| Karakter Khusus | Deskripsi | Keterangan
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Asterik(*)` | Mencocokkan semua nilai dalam bidang atau nilai apa pun yang mungkin.                                                                                               
| `Hyphen (-)` | Digunakan untuk mendefinisikan rentang. Contoh: 1-5 di bidang ke-5 (Hari Dalam Seminggu) Setiap Hari Kerja yaitu, Senin hingga Jumat
| `Slash (/)` | Bidang pertama (Menit) /15 yang berarti setiap lima belas menit atau kenaikan rentang.                                                                            
| `Koma (,) ` | Digunakan untuk memisahkan item. Contoh: 2,6,8 di bidang ke-2 (Jam) dieksekusi pada jam 2 pagi, 6 pagi dan 8 pagi
| `L` | Hanya diperbolehkan untuk bidang Hari dalam Bulan atau Hari dalam Minggu, 2L dalam Hari dalam minggu menunjukkan hari selasa terakhir setiap bulan
| `Hash (#)` | Hanya diperbolehkan untuk bidang Hari Minggu, yang harus diikuti dalam rentang 1 hingga 5. Sebagai contoh, 4#1 berarti "Hari Kamis pertama" pada bulan tertentu. 
| `Tanda tanya (?)` | Dapat digunakan sebagai pengganti '*' dan diperbolehkan untuk Hari Bulan dan Hari Minggu. Penggunaannya terbatas pada Hari Bulan atau Hari Minggu dalam ekspresi cron.  



## Lihat juga {.cols-1}

* [Devhints](https://devhints.io/cron) _(devhints.io)_
* [Crontab Generator](https://crontab-generator.org/) _(crontab-generator.org)_
* [Crontab guru](https://crontab.guru/) _(crontab.guru)_
