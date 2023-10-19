---
judul: Emacs
tanggal: 2020-12-17 16:21:49
latar belakang: bg-[#7752a9]
Tag:
    - editor
    - teks
    - jalan pintas
kategori:
    - Toolkit
intro: |
    [Emacs] (https://www.gnu.org/software/emacs) adalah editor teks tampilan waktu nyata yang dapat diperluas, dapat dikustomisasi, dan mendokumentasikan sendiri.
    Referensi ini dibuat untuk Emacs 27.
plugin:
    - copyCode
---


## Memulai {.cols-3}


### Memulai Emacs
Untuk masuk ke Emacs, ketik saja namanya:
```shell script
$ emacs
```

------

| - | - |
|-------------|------------------------|
| `C-z` | Menangguhkan Emacs |
| `C-x` `C-c` | Keluar dari Emacs secara permanen |
{.shortcuts}

### Deskripsi Global {.secondary}
| - | - |
|-----------|---------------------------------------------|
| `C-<tombol>` | Berarti menahan kontrol, dan tekan `<tombol>` | |M-<tombol>` | Berarti menekan Esc satu kali, dan tekan `<tombol>` | |M-<tombol
| `M-<tombol>` | Berarti tekan tombol Esc sekali, dan tekan `<tombol>` |
{.shortcuts}

PEMBERITAHUAN: Cheatsheet ini mengikuti aturan di atas.


### Gerak {.row-span-2}

| Mundur | Maju | Entitas yang akan dipindahkan |
|-----------|-----------|--------------------------------|
| `C-b` | `C-f` | Karakter |
| `M-b` | `M-f` | Kata |
| `C-p` | `C-n` | Baris |
| `C-a` | `C-e` | Baris awal<br />_(atau akhir)_ | | Baris
| `M-a` | `M-e` | Kalimat |
| `M-{` | `M-}` | Paragraf |
| `C-x` `[` | `C-x` `]` | Halaman |
| `C-M-b` | `C-M-f` | Jenis Kelamin |
| `C-M-a` | `C-M-e` | Fungsi |
| `M-<` | `M->` | Buffer awal<br>_(atau akhir)_ | |
{.shortcuts .show-header}



### Perubahan Huruf Besar/Kecil

| - | - |
|-------------|------------------|
| `M-u` | Kata dengan huruf besar |
| `M-l` | Kata dengan huruf kecil |
| `M-c` | Kata dengan huruf besar |
| `C-x` `C-u` | Huruf besar |
| `C-x` `C-l` | Daerah huruf kecil |
{.shortcuts}



### File

| - | - |
|-------------|--------------------------------------------------|
| `C-x` `C-f` | Membaca file ke dalam Emacs |
| `C-x` `C-s` | Menyimpan file kembali ke disk |
| `C-x` `s` | Menyimpan semua file |
| `C-x` `i` | Menyisipkan isi file lain ke dalam buffer ini
| `C-x` `C-v` | Mengganti file ini dengan file Anda
| `C-x` `C-w` | Menulis buffer ke file yang ditentukan
| `C-x` `C-q` | Mengalihkan status hanya-baca dari buffer |
{.shortcuts}




### Pemulihan Kesalahan

| - | - |
|-----------------------------|--------------------------------------------|
| `C-g` | Membatalkan sebagian perintah yang diketik atau dieksekusi
| `M-x` recover-session | Memulihkan file yang hilang akibat kerusakan sistem
| `C-x` `u` <br>`C-_` <br>`C-/` | Membatalkan perubahan yang tidak diinginkan
| `M-x` revert-buffer | Mengembalikan buffer ke konten aslinya
| `C-l` | Menggambar ulang layar yang sudah dibuang |
{.shortcuts}




### Mengubah urutan {.row-span-2}

| - | - |
|-------------|----------------------|
| `C-t` | Mengubah urutan karakter |
| `M-t` | Mengubah urutan kata |
| `C-x` `C-t` | Mengubah urutan baris |
| `C-M-t` | Mengubah urutan jenis kelamin |
{.shortcuts}

#### Gulir

| - | - |
|-----------|--------------------------------------------------|
| `C-v` | Gulir ke layar berikutnya |
| `M-v` | Gulir ke layar sebelumnya |
| `C-x` `<` | Gulir ke kiri |
| `C-x` `>` | Menggulir ke kanan |
| `C-l` | Menggulir baris saat ini ke <br>_tengah, atas, bawah_ | |
{.shortcuts}

#### Goto

| - | - |
|-----------|---------------------|
| `M-g` `g` | Goto baris |
| `M-g` `c` | Goto karakter |
| `M-m` | Kembali ke lekukan |
{.shortcuts}





### Menandai

| - | - |
|-------------------|-------------------------|
| `C-@` <br /> `C-SPC` | Tandai di sini |
| `C-x` `C-x` | Tukar titik dan tandai |
| `M-@` | Tetapkan tanda kata arg menjauh |
| `M-h` | Tandai paragraf |
| `C-x` `C-p` | Tandai halaman |
| `C-M-@` | Tandai jenis kelamin |
| `C-M-h` | Tandai fungsi |
| `C-x` `h` | Tandai seluruh buffer |
{.shortcuts}




### Membunuh dan Menghapus {.row-span-2}

| Mundur | Maju | Entitas yang akan dibunuh |
|---------------|---------|--------------------------|
| `DEL` | `C-d` | Karakter |_(hapus)_ |
| `M-DEL` | `M-d` | Kata |
| `M-0` `C-k` | `C-k` | Baris <br> _(sampai akhir)_ | |
| `C-x` `DEL` | `M-k` | Kalimat |
| `M--` `C-M-k` | `C-M-k` | Sexp |
{.shortcuts .show-header}
#### Membunuh

| - | - |
|------------|--------------------------------------|
| `C-W` | Membunuh wilayah C-w |
| `M-w` | Menyalin daerah untuk membunuh cincin |
| `M-z` char | Bunuh melalui kemunculan karakter berikutnya
| `C-y` | Tarik kembali hal terakhir yang dibunuh |
| `M-y` | Mengganti tarikan terakhir dengan pembunuhan sebelumnya | | | `M-z` | Mengganti tarikan terakhir dengan pembunuhan sebelumnya
{.shortcuts}





### Mendapatkan Bantuan

| - | - |
|-----------|------------------------------------------|
| `C-x` `1` | Menghapus jendela bantuan |
| `C-M-v` | Menggulir jendela bantuan |
| `C-h` `a` | Apropos: menampilkan perintah yang cocok dengan string |
| `C-h` `k` | Menjelaskan fungsi yang dijalankan tombol
| `C-h` `f` | Menjelaskan fungsi
| `C-h` `m` | Mendapatkan informasi khusus mode
{.shortcuts}

Sistem bantuannya sederhana. Ketik `C-h` (atau `F1`) dan ikuti petunjuknya. Jika Anda adalah pengguna pertama kali, ketik `C-h` `t` untuk mendapatkan tutorial.




### Beberapa Jendela {.col-span-2}
Ketika dua perintah ditampilkan, perintah kedua adalah perintah yang serupa untuk sebuah bingkai, bukan jendela.
| - | - | - |
|---------------|-----------|-------------------------------|
| `C-x` `5` `1` | `C-x` `1` | Hapus semua jendela lain |
| `C-x` `5` `2` | `C-x` `2` | Membagi jendela, di atas dan di bawah |
| `C-x` `5` `0` | `C-x` `0` | Menghapus jendela ini |

| `C-x` `3` || Membagi jendela, berdampingan | | C-x` `3` || Membagi jendela, berdampingan
| `C-M-v` || Menggulir jendela lain |

| `C-x` `5` `o` | `C-x` `o` | Pindah kursor ke jendela lain
| `C-x` `5` `b` | `C-x` `4` `b` | Pilih buffer di jendela lain | | C-x` `4` `b` | Pilih buffer di jendela lain
| `C-x` `5` `C-o` | `C-x` `4` `C-o` | Menampilkan buffer di jendela lain |
| `C-x` `5` `f` | `C-x` `4` `f` | Cari file di jendela lain |C-x` `4` `f` | Cari file di jendela lain
| `C-x` `5` `r` | `C-x` `4` `r` | Cari file hanya-baca di jendela lain | | C-x` `4` `r` | Cari file hanya-baca di jendela lain
| `C-x` `5` `d` | `C-x` `4` `d` | Jalankan Dired di jendela lain |
| `C-x` `5` `.` | `C-x` `4` `.` | Cari tag di jendela lain |

| `C-x` `^` | | Menambah jendela lebih tinggi |
| `C-x` `{` || Mengecilkan jendela lebih sempit |
| `C-x` `}` || Membesarkan jendela lebih lebar |
{.shortcuts}




### Pemformatan

| - | - |
|-------------|------------------------------------------|

| `C-M-\` | Wilayah indentasi (bergantung pada mode) |
| `C-M-q` | Indentasi jenis kelamin (bergantung pada mode) | | | `C-M-q` | Indentasi jenis kelamin (bergantung pada mode) | | `C-M-q` | Indentasi jenis kelamin

| `M-;` | Indentasi untuk komentar |
| `C-o` | Menyisipkan baris baru setelah titik | | `C-o` | Menyisipkan baris baru setelah titik
| `C-M-o` | Memindahkan sisa baris secara vertikal ke bawah | | `C-x` | Memindahkan sisa baris secara vertikal ke bawah

| `M-^` | Menggabungkan baris dengan baris sebelumnya (dengan arg, berikutnya) | | M-^` | Menggabungkan baris dengan baris sebelumnya (dengan arg, berikutnya)
| `M-\` | Menghapus semua spasi kosong di sekitar titik
| `M-SPC` | Letakkan tepat satu spasi di titik |
| `M-q` | Mengisi paragraf |
| `C-x` `f` | Mengatur kolom isian menjadi arg |
| `C-x` `.` | Atur awalan setiap baris dimulai dengan |
| `M-o` | Mengatur wajah |
{.shortcuts}




### Info {.row-span-2}

| - | - |
|-----------|---------------------------------------------|
| `C-h` `i` | Masuk ke pembaca dokumentasi Info |
| `C-h` `S` | Temukan fungsi atau variabel tertentu di Info |
{.shortcuts}

#### Bergerak di dalam sebuah simpul

| - | - |
|-------|-------------------|
| `SPC` | Gulir ke depan |
| `DEL` | Menggulir mundur |
| `b` | Awal simpul | | Awal simpul
{.shortcuts}

#### Berpindah antar node

| - | - |
|-----|----------------------------------------|
| `n` | Simpul berikutnya |
| `p` | Simpul sebelumnya |
| `u` | Pindah ke atas |
| `m` | Pilih item menu berdasarkan nama | | `m` | Pilih item menu berdasarkan nama
| `n` | Pilih item menu ke-n berdasarkan nomor (1-9) | | `f` | Ikuti referensi
| `f` | Ikuti referensi silang (kembali dengan l) | | l
| `l` | Kembali ke simpul terakhir yang Anda lihat
| `d` | Kembali ke simpul direktori | | `d` | Kembali ke simpul direktori
| `t` | Pergi ke simpul teratas dari berkas Info
| `g` | Pergi ke simpul manapun dengan nama | | `g` | Pergi ke simpul dengan nama
{.shortcuts}

#### Lainnya

| - | - |
|-----|----------------------------------|
| `h` | Menjalankan tutorial Info |
| `i` | Mencari subjek di dalam indeks |
| `s` | Mencari simpul-simpul untuk regexp | | `s` | Mencari simpul-simpul untuk regexp
| `q` | Keluar dari Info |
{.shortcuts}




### Minibuffer
Kunci berikut ini didefinisikan dalam minibuffer.
| - | - |
|-------|-----------------------------------------|
| `TAB` | Lengkapi sebanyak mungkin |
| `SPC` | Lengkapi hingga satu kata |
| `RET` | Lengkapi dan jalankan |
| `?` | Menampilkan kemungkinan penyelesaian |
| `M-p` | Mengambil input minibuffer sebelumnya
| `M-n` | Mengambil input minibuffer selanjutnya atau default | | `M-n` | Mengambil input minibuffer berikutnya atau default
| `M-r` | Pencarian regexp mundur melalui sejarah | | `M-r` | Pencarian regexp mundur melalui sejarah
| `M-s` | Pencarian regexp maju melalui sejarah | | `M-s` | Pencarian regexp mundur melalui sejarah | | `M-s` | Pencarian regexp maju melalui sejarah
| `C-g` | Membatalkan perintah |
{.shortcuts}

Ketik `C-x` `ESC` `ESC` untuk mengedit dan mengulangi perintah terakhir yang menggunakan minibuffer. Ketik `F10` untuk mengaktifkan item bar menu pada terminal teks.





### Tag

| - | - |
|--------------------------|--------------------------------------------|
| `M-.` | Cari tag (definisi) |M-.` | Cari kemunculan berikutnya
| `C-u` `M-.` | Menemukan kemunculan tag berikutnya | | M-.` | Menemukan kemunculan tag berikutnya

| `M-x` pencarian-tag | Pencarian regexp pada semua berkas di tabel tag
| `M-x` tags-query-replace | Menjalankan query-replace pada semua file
| `M-,` | Lanjutkan pencarian tag terakhir atau ganti kueri |
{.shortcuts}



### Persegi panjang

| - | - |
|---------------|-------------------------------------|
| `C-x` `r` `r` | Salin persegi panjang untuk didaftarkan |
| `C-x` `r` `k` | Bunuh persegi panjang |
| `C-x` `r` `y` | Mencabut persegi panjang |
| `C-x` `r` `o` | Membuka persegi panjang, menggeser teks ke kanan |
| `C-x` `r` `c` | Mengosongkan persegi panjang |
| `C-x` `r` `t` | Awali setiap baris dengan sebuah string |
{.shortcuts}



### Makro Papan Ketik

| - | - |
|---------------------------|-------------------------------------|
| `C-x` `(` | Mulai mendefinisikan makro papan ketik |
| `C-x` `)` | Akhiri definisi makro papan ketik |
| `C-x` `e` | Menjalankan makro papan ketik yang terakhir didefinisikan |
| `C-u` `C-x` `(` | Menambahkan ke makro papan ketik terakhir |
| `M-x` name-last-kbd-macro | Memberi nama makro papan ketik terakhir
| `M-x` insert-kbd-macro | Menyisipkan definisi Lisp dalam buffer |
{.shortcuts}




### Buffer

| - | - |
|-------------|-----------------------|
| `C-x` `b` | Pilih buffer lain |
| `C-x` `C-b` | Daftar semua buffer |
| `C-x` `k` | Membunuh buffer |
{.shortcuts}



Emacs Search{.cols-3}
------



### Regex (umum) {.row-span-2}

| - | - |
|---------------|----------------------------------------------|
| `.` `(titik)` | Setiap karakter tunggal kecuali baris baru |
| `*` | Nol atau lebih pengulangan |
| `+` | Satu atau lebih pengulangan |
| `?` | Nol atau satu pengulangan | | ``` | Nol atau satu pengulangan
| `\` | Mengutip karakter khusus
| `\c` | Mengutip karakter khusus ekspresi reguler c |
| `\|` | Alternatif ("atau") | | `\(...,\...,\...,\)
| `\(...\)` | Pengelompokan |
| `\(:?...\)` | Pengelompokan pemalu
| `\(: NUM... \)` | Pengelompokan bernomor eksplisit |
| `\n` | Teks yang sama dengan grup ke-n | | Teks yang sama dengan grup ke-n
| `\b` | Pada jeda kata | | | Pada jeda kata
| `\B` | Tidak pada pemisah kata | | `\B` | Tidak pada pemisah kata | | `\B` | Tidak pada pemisah kata

### Regex (entri)
| Mulai | Akhir | Entitas |
|-------|-------|--------|
| `^` | `$` | Baris |
| `\<` | `\>` | Word |
| `\_<` | `\_>` | Simbol |
| `\'` | `\'` | Buffer |
{.show-header}

### Regex (konflik)

| Ini | Lainnya | kelas |
|---------|----------|---------------------------|
| `[...]` | `[^...]` | Himpunan eksplisit
| `\w` | `\W` | Karakter sintaksis kata |
| `\sc` | `\Sc` | Karakter dengan sintaks c |
| `\cc` | `\Cc` | Karakter dengan kategori c |
{.show-header}


### Pencarian Tambahan

| - | - |
|---------|-----------------------------------|
| `C-s` | Pencarian maju |
| `C-r` | Pencarian mundur |
| `C-M-s` | Pencarian ekspresi reguler |
| `C-M-r` | Membalikkan pencarian ekspresi reguler |
| `M-p` | Pilih string pencarian sebelumnya | | M-p
| `M-n` | Pilih string pencarian berikutnya |
| `RET` | Keluar dari pencarian bertahap |
| `DEL` | Membatalkan efek dari karakter terakhir
| `C-g` | Membatalkan pencarian saat ini | | `BATAL` | Membatalkan pencarian saat ini
{.shortcuts}

Gunakan `C-s` atau `C-r` lagi untuk mengulangi pencarian di salah satu arah. Jika Emacs masih mencari, `C-g` hanya membatalkan bagian yang tidak cocok.




### Query Replace

| - | - |
|--------------|--------------------------------------|
| `M-%` | Mengganti string teks secara interaktif | |M-%` regexp | Mengganti string teks secara interaktif
| `M-x` regexp | Menggunakan ekspresi reguler |
| `SPC` / `y` | Ganti yang ini, lanjutkan ke yang berikutnya
| `,` | Ganti yang ini, jangan pindah |
| `DEL` / `n` | Lompat ke berikutnya tanpa mengganti | | `!
| `!` | Ganti semua kecocokan yang tersisa
| `^` | Kembali ke pertandingan sebelumnya | | `RET` | Kembali ke pertandingan sebelumnya
| `RET` | Keluar dari penggantian kueri
| `C-r` | Masuk ke pengeditan rekursif (C-M-c untuk keluar) |
{.pintasan}



Lain-lain
----


### Kerang

| - | - |
|-------------|----------------------------------------|
| `M-!` | Menjalankan perintah shell |
| `M-&` | Menjalankan perintah shell secara asinkron
| `M-` | Menjalankan perintah shell pada wilayah | | `M-` | Menjalankan perintah shell pada wilayah
| `C-u` `M-` | Menyaring wilayah melalui perintah shell |
| `M-x` shell | Memulai shell pada window shell | | `M-x` shell
{.shortcuts}



### Set Karakter Internasional {.col-span-2}

| - | - |
|----------------------------|------------------------------------|
| `C-x` `RET` `l` | tentukan bahasa utama
| `M-x` `daftar-metode-masukan` | tampilkan semua metode masukan
| `C-\` | mengaktifkan atau menonaktifkan metode masukan
| `C-x` `RET` `c` | mengatur sistem pengkodean untuk perintah berikutnya
| `M-x` daftar-sistem-kode | menampilkan semua sistem pengkodean
| `M-x` `prefer-coding-system` | memilih sistem pengkodean yang diinginkan
{.shortcuts}


### Register

| - | - |
|-----------------|--------------------------------------|
| `C-x` `r` `s` | Menyimpan daerah dalam register |
| `C-x` `r` `i` | Memasukkan isi register ke dalam buffer |
| `C-x` `r` `SPC` | Menyimpan nilai titik dalam register |
| `C-x` `r` `j` | Melompat ke titik yang disimpan dalam register |
{.shortcuts}




### Lain-lain

| - | - |
|------------|-------------------|
| `C-u` num | Argumen numerik |
| `M--` | Argumen negatif |
| `C-q` char | Sisipan yang dikutip |
{.shortcuts}



### Perintah yang Berhubungan dengan Emacs Lisp

| - | - |
|--------------------|------------------------------------|
| `C-x` `C-e` | Eval sexp sebelum titik |
| `C-M-x` | Eval defun saat ini |
| `M-x` eval-region | Eval region |
| `M-:` | Baca dan eval minibuffer |
| `M-x` load-library | Memuat pustaka Lisp dari jalur pemuatan |
{.shortcuts}




### Kustomisasi Sederhana

| - | - |
|-------------------|-------------------------------|
| `M-x` `menyesuaikan` | menyesuaikan variabel dan wajah |

Membuat pengikatan kunci global di Emacs Lisp:

``` {.wrap}
(global-set-key (kbd "C-c g") 'cari-maju)
(global-set-key (kbd "M-#") 'query-replace-regexp)
```




### Abbrevs

| - | - |
|-------------------|------------------------------------------|
| `C-x` `a` `g` | Menambahkan singkatan global |
| `C-x` `a` `l` | Menambahkan singkatan mode-lokal |

| `C-x` `a` `i` `l` | Menambahkan ekspansi mode-lokal untuk singkatan ini
| `C-x` `a` `e` | Perluas singkatan secara eksplisit
| `M-/` | Memperluas kata sebelumnya secara dinamis
{.shortcuts}




### Pemeriksaan Ejaan

| - | - |
|---------------------|---------------------------------------|
| `M-$` | Periksa ejaan kata saat ini | |M-$` | Periksa ejaan kata saat ini
| `M-x` ispell-region | Periksa ejaan semua kata dalam region |
| `M-x` ispell-buffer | Periksa ejaan seluruh buffer |
| `M-x` flyspell-mode | Mengalihkan pemeriksaan ejaan saat terbang |
{.shortcuts}




### Perintah Penulisan {.col-span-2}

#### Sintaks
```
(defun nama-perintah (args)
"dokumentasi" (interaktif "template")
tubuh)
```

#### Contoh
```
(defun this-line-to-top-of-window (baris)
    "Mereposisi baris saat ini ke bagian atas jendela.
Dengan argumen awalan LINE, letakkan titik pada LINE."
    (interaktif "P")
    (recenter (if (null line)
                  0
              (awalan-nilai-numerik baris))))
```





Spesifikasi interaktif menjelaskan cara membaca argumen secara interaktif. Ketik `C-h` `f` interaktif `RET` untuk detail lebih lanjut.



