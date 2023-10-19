---
judul: Awk
tanggal: 2020-12-31 15:18:34
latar belakang: bg-slate-600
tag:
    - bash
    - teks
    - skrip
kategori:
    - Perintah Linux
intro: |
    Ini adalah sebuah lembar sontekan referensi cepat satu halaman untuk [GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html), yang mencakup ekspresi dan perintah awk yang umum digunakan.
plugin:
    - copyCode
---

Memulai
---------------

### Selamat mencoba
```shell script {.wrap}
$ awk -F: '{cetak $1, $NF}' /etc/passwd
```
----
| - | - | - |
|---|---------------|---------------------------|
| | `-F:` | Titik dua sebagai pemisah |
| | `{...}` | Program Awk



| | `/etc/passwd` | File data masukan
{.left-text}



### Program awk
```
BEGIN {<inisialisasi>}
   <pola 1> {<tindakan program>}
   <pola 2> {<tindakan program>}
   ...
AKHIR {< tindakan akhir >}
```
#### Contoh
```
awk '
    BEGIN { print "\n>>>Mulai" }
    !/(login|shutdown)/ { print NR, $0 }
    END { print "<<<END\n" }
' /etc/passwd
```


### Variabel {.row-span-2}
``` bash
          $1 $2 $2/$(NF-1) $3/$NF
           ▼ ▼ ▼
        ┌──────┬──────────────────┬───────┐
$0/NR ▶ │ ID │ WEBSITE │ URI │
        ├──────┼──────────────────┼───────┤
$0/NR ▶ │ 1 │ cheatsheets.zip │ awk │
        ├──────┼──────────────────┼───────┤
$0/NR ▶ │ 2 │ google.com │ 25 │
        └──────┴──────────────────┴───────┘
```
---

```
# Bidang pertama dan terakhir
awk -F: '{cetak $1,$NF}' /etc/passwd

# Dengan nomor baris
awk -F: '{cetak NR, $0}' /etc/passwd

# Kolom terakhir kedua
awk -F: '{cetak $(NF-1)}' /etc/passwd

# String khusus
awk -F: '{cetak $1 "=" $6}' /etc/passwd
```
Lihat: [Variabel] (#awk-variabel)




### Contoh program awk {.col-span-2 .row-span-2}
```
awk 'BEGIN {cetak "halo dunia"}'        # Mencetak "halo dunia"
awk -F: '{cetak $1}' /etc/passwd # -F: Menentukan pemisah bidang

# /pola/ Eksekusi aksi hanya untuk pola yang cocok
awk -F: '/root/ {cetak $1}' /etc/passwd

# Blok BEGIN dieksekusi sekali di awal
awk -F: 'BEGIN { print "uid"} { print $1 }' /etc/passwd

# Blok END dieksekusi sekali di akhir
awk -F: '{print $1} END { print "-selesai-"}' /etc/passwd
```


### Kondisi
```
awk -F: '$3>30 {cetak $1}' /etc/passwd
```
Lihat: [Kondisi](#awk-kondisi)


### Menghasilkan 1000 spasi
```
awk 'BEGIN{
    while (a++ < 1000)
        s = s " ";
    print s
}'
```
Lihat: [Perulangan](#awk-loop)



### Array
```
awk 'BEGIN {
   buah-buahan["mangga"] = "kuning";
   buah-buahan["jeruk"] = "oranye"
   for (buah dalam buah-buahan) {
     print "Warna dari " buah " adalah " buah-buahan[buah]
   }
}'
```
Lihat: [Larik](#awk-array)



### Fungsi-fungsi
```
# => 5
awk 'BEGIN{print length("halo")}'
# => HELLO
awk 'BEGIN{cetak toupper("halo")}'
# => hel
awk 'BEGIN{cetak substr("halo", 1, 3)}'
```
Lihat: [Fungsi](#awk-fungsi)




Variabel Awk
---------


### Variabel bawaan
| - | - |
|----------------|-----------------------------------------------------|
| `$0` | Seluruh baris |
| `$1, $2... $NF` | Bidang pertama, kedua... terakhir |
| `NR` | `N` jumlah rekaman `R` |
| `NF` | `Numlah `F` bidang |
| `OFS` | `O`keluaran `F`bidang `S`pemisah | _(default " ")_ | |O`keluaran `F`bidang `S`pemisah | |O`keluaran `F`bidang `S`pemisah
| `FS` | masukan `F`field `S`eparator <br> _(default " ")_ |
| `ORS` | `O`output `R`record `S`eparator <br> _(default "\n")_ | |
| `RS` | masukan `R`Rekam `S`pemisah <br> _(default "\n")_ | |
| `FILENAME` | Nama file |



Ekspresi ###
| - | - |
|---------------------|------------------------------------|
| `$1 == "root"` | Bidang pertama sama dengan root |
| `{cetak $(NF-1)}` | Bidang terakhir kedua |
| `NR!=1{cetak $0}` | Dari record kedua | | Dari record kedua
| `NR > 3` | Dari catatan ke-4 | | Dari catatan ke-4
| `NR == 1` | Catatan pertama | | Catatan pertama
| `END{cetak NR}` | Total rekaman |
| `BEGIN{cetak OFMT}` | Format keluaran |
| `{cetak NR, $0}` | Nomor baris |
| `{cetak NR " " $0}` | Nomor baris (tab) |
| `{$1 = NR; print}` | Mengganti bidang pertama dengan nomor baris | | $NF
| `$NF > 4` | Bidang terakhir > 4 |
| `NR % 2 == 0` | Catatan genap | | Catatan genap
| `NR = 10, NR = 20` | Catatan 10 sampai 20 |
| `BEGIN{cetak ARGC}` | Total argumen |
| `ORS=NR%5?",":"\n"` | Rekaman gabungan |




### Contoh
Mencetak jumlah dan rata-rata
```
awk -F: '{jumlah += $3}
     END { cetak jumlah, jumlah/NR }
' /etc/passwd
```
Mencetak parameter
```
awk 'BEGIN {
    for (i = 1; i < ARGC; i++)
        print ARGV[i] }' a b c
```
Pemisah bidang keluaran sebagai koma
```
awk 'BEGIN { FS=":";OFS=","}
    {print $1,$2,$3,$4} '/etc/passwd
```
Posisi kecocokan
```
awk 'BEGIN {
    if (match("Satu Dua Tiga", "Tw"))
        print RSTART }'
```
Panjang dari kecocokan
```
awk 'BEGIN {
    if (match("Satu Dua Tiga", "re"))
        print RLENGTH }'
```





### Variabel Lingkungan
| - | - |
|-----------|-----------------------------------------------------------|
| `ARGC` | Angka atau argumen |
| `ARGV` | Larik argumen |
| `FNR` | `F`ile `N`jumlah `R`record |
| `OFMT` | Format untuk angka | _(default "%.6g")_ | | | Format untuk angka
| `RSTART` | Lokasi dalam string | | | `RSTART` | Lokasi dalam string
| `RLENGTH` | Panjang pencocokan |

| `ARGIND` | Indeks Argumen | | Indeks Argumen



### Hanya GNU awk
| - | - |
|---------------|-----------------------|
| `ENVIRON` | Variabel lingkungan
| `IGNORECASE` | Mengabaikan huruf besar/kecil
| `CONVFMT` | Format konversi |
| `ERRNO` | Kesalahan sistem |
| `FIELDWIDTHS` | Bidang dengan lebar tetap



### Mendefinisikan variabel
```
awk -v var1="Hello" -v var2="Wold" '
    END {cetak var1, var2}
' </dev/null
```

#### Menggunakan variabel shell
```
awk -v varName="$PWD" '
    END {cetak varName}' </dev/null
```



Operator Awk
---------

### Operator

| - | - |
|------------------|-------------|
| `{cetak $1}` | Bidang pertama |
| `$2 == "foo"` | Sama dengan |
| `$2 != "foo"` | Tidak sama dengan |
| `"foo" dalam larik` | Dalam larik |
#### Ekspresi reguler
| - | - |
|-----------------|-------------------|
| `/regex/` | Baris cocok dengan |
| `!/regex/` | Baris tidak cocok dengan |
| `$1 ~ /regex/` | Bidang cocok dengan |
| `$1 !~ /regex/` | Bidang tidak cocok |
#### Ketentuan lebih lanjut
| - | - |
|------------------------|-----|
| `($2 <= 4 || $3 < 20)` | Atau |
| `($1 == 4 && $3 < 20)` | Dan |

Operasi ###
#### Operasi aritmatika
- `+`
- `-`
- `*`
- `/`
- `%`
- `++`
- `--`
{.cols-3 .marker-none}
#### Penugasan singkatan
- `+=`
- `-=`
- `*=`
- `/=`
- `%=`
{.cols-3 .marker-none}
#### Operator perbandingan
- `==`
- `!=`
- `<`
- `>`
- `<=`
- `>=`
{.cols-3 .marker-none}



### Contoh
```
awk 'BEGIN {
    if ("foo" ~ "^fo+$")
        print "Fooey!";
}'
```
#### Tidak cocok
```
awk 'BEGIN {
    if ("boo" !~ "^fo+$")
        print "Boo!";
}'
```
#### if in array
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("foo" in assoc)
        print "Fooey!";
}'
```




Fungsi Awk
----------
### Fungsi umum {.col-span-2}
| Fungsi | Deskripsi | Keterangan
|-----------------------|---------------------------------------------------------------------------------|
| `index(s,t)` | Posisi dalam string s di mana string t muncul, 0 jika tidak ditemukan
| `length(s)` | Panjang string s (atau $0 jika tidak ada arg) | | `length` | Panjang string s (atau $0 jika tidak ada arg)
| `rand` | Angka acak antara 0 dan 1 | | `rand` | Angka acak antara 0 dan 1
| `substr(s,index,len)` | Kembalikan substring len-char dari s yang dimulai dari indeks (dihitung dari 1) | | `substr(s,index,len)` | Kembalikan substring len-char dari s yang dimulai dari indeks (dihitung dari 1)
| `srand` | Menetapkan seed untuk rand dan mengembalikan seed sebelumnya
| `int(x)` | Memotong x menjadi nilai bilangan bulat
| `split(s,a,fs)` | Memisahkan string s menjadi larik a yang dibagi dengan fs, mengembalikan panjang a
| `match(s,r)` | Posisi dalam string s di mana regex r muncul, atau 0 jika tidak ditemukan
| `sub(r,t,s)` | Pengganti t untuk kemunculan pertama regex r dalam string s (atau $0 jika s tidak diberikan)
| `gsub(r,t,s)` | Gantikan t untuk semua kemunculan regex r dalam string s |
| `system(cmd)` | Jalankan cmd dan kembalikan status keluar
| `tolower(s)` | String s menjadi huruf kecil | | String s menjadi huruf besar
| `tinggi(s)` | String s menjadi huruf besar | | String s menjadi huruf besar
| `getline` | Menetapkan $0 ke rekaman input berikutnya dari file input saat ini.                            |


### Fungsi yang ditentukan pengguna
```
awk '
    # Mengembalikan angka minimum
    function find_min(num1, num2){
       if (num1 < num2)
       return num1
       return num2
    }
    # Mengembalikan angka maksimum
    function find_max(num1, num2){
       if (num1 > num2)
       return num1
       return num2
    }
    # Fungsi utama
    function main(num1, num2) {
       hasil = find_min(num1, num2)
       print "Minimum =", hasil
      
       hasil = find_max(num1, num2)
       print "Maksimum =", hasil
    }
    # Eksekusi skrip dimulai di sini
    BEGIN {
       main(10, 60)
    }
'
```




Susunan Awk
---------



### Larik dengan indeks
```
awk 'BEGIN {
    arr[0] = "foo";
    arr[1] = "bar";
    print(arr[0]); # => foo
    hapus arr[0];
    print(arr[0]); # => ""
}'
```

### Larik dengan kunci
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    print("baz" in assoc); # => 0
    print("foo" in assoc); # => 1
}'
```


### Larik dengan pemisahan
```
awk 'BEGIN {
    split("foo:bar:baz", arr, ":");
    for (key in arr)
        print arr[key];
}'
```

### Larik dengan asort
```
awk 'BEGIN {
    arr [0] = 3
    arr[1] = 2
    arr[2] = 4
    n = asort(arr)
    for (i = 1; i <= n ; i++)
        print(arr[i])
}'
```



### Multi-dimensi
```
awk 'BEGIN {
    multidim[0,0] = "foo";
    multidim[0,1] = "bar";
    multidim[1,0] = "baz";
    multidim[1,1] = "boo";
}'
```

### Iterasi multi-dimensi
```
awk 'BEGIN {
    array[1,2]=3;
    array[2,3]=5;
    for (comb in array) {
        split(comb,sep,SUBSEP);
        print sep[1], sep[2],
        array[sep[1], sep[2]]
    }
}'
```



Kondisi Awk
----------

### pernyataan if-else
```
awk -v count = 2 'BEGIN {
    if (count == 1)
        print "Ya";
    else
        print "Hah?";
}'
```
#### Operator Ternary
```
awk -v count=2 'BEGIN {
    print (count==1) ? "Ya" : "Hah?";
}'
```


### Ada
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("foo" in assoc)
        print "Fooey!";
}'
```
#### Tidak ada
```
awk 'BEGIN {
    assoc["foo"] = "bar";
    assoc["bar"] = "baz";
    if ("Huh" in assoc == 0 )
        print "Hah!";
}'
```


### switch
```
awk -F: '{
    switch (NR * 2 + 1) {
        kasus 3:
        case "11":
            print NR - 1
            break
        
        case /2[[:digit:]]+/:
            cetak NR
        
        default:
            cetak NR + 1
        
        huruf besar -1:
            cetak NR * -1
    }
}' /etc/passwd
```


Perulangan Awk
----------

### untuk ... i
```
awk 'BEGIN {
    for (i = 0; i < 10; i++)
        print "i=" i;
}'
```
#### Pangkat dua antara 1 dan 100
```
awk 'BEGIN {
    for (i = 1; i <= 100; i *= 2)
        print i
}'
```


### untuk ... di
```
awk 'BEGIN {
    assoc["key1"] = "val1"
    assoc["key2"] = "val2"
    for (key in assoc)
        print assoc[key];
}'
```
#### Argumen
```
awk 'BEGIN {
    for (argnum in ARGV)
        print ARGV[argnum];
'}' a b c
```



### Contoh {.row-span-3}
#### Membalikkan catatan
```
awk -F: '{ x[NR] = $0 }
    END {
        for (i = NR; i > 0; i--)
        print x[i]
    }
' /etc/passwd
```

#### Membalikkan bidang
```
awk -F: '{
    for (i = NF; i > 0; i--)
        printf("%s ",$i);
    print ""
}' /etc/passwd
```

#### Jumlahkan berdasarkan record
```
awk -F: '{
    s=0;
    for (i = 1; i <= NF; i++)
        s += $i;
    print s
}' /etc/passwd
```


#### Jumlahkan seluruh berkas
```
awk -F: '
    {for (i = 1; i <= NF; i++)
        s += $i;
    };
    END{cetak s}
' /etc/passwd
```



### while {.row-span-2}
```
awk 'BEGIN {
    while (a < 10) {
        print "- " " penggabungan: " a
        a++;
    }
}'
```
#### do... while
```
awk '{
    i = 1
    do {
        print $0
        i++
    } while (i <= 5)
}' /etc/passwd
```



### Istirahat
```
awk 'BEGIN {
    break_num = 5
    for (i = 0; i < 10; i++) {
        print i
        if (i == break_num)
            break
    }
}'
```



### Lanjutkan
```
awk 'BEGIN {
    for (x = 0; x <= 10; x++) {
        if (x == 5 || x == 6)
            continue
        printf "%d ", x
    }
    print ""
}'
```



Pencetakan Berformat Awk
---------

Penggunaan ###
#### Rata kanan
```
awk 'BEGIN{printf "|%10s|\n", "hello"}'

| halo
```
#### Rata kiri
```
awk 'BEGIN{printf "|%-10s|\n", "hello"}'

|hello |
```

### Penentu umum
| Karakter | Deskripsi |
|---------------|-----------------------|
| `c` | Karakter ASCII | Karakter
| `d` | Bilangan bulat desimal |
| `e`, `E`, `f` | Format titik mengambang | | `f` | Format titik mengambang | | `e`, `E`, `f` | Format titik mengambang
| `o` | Nilai oktal tidak bertanda tangan | | Nilai oktal tidak bertanda tangan
| `s` | String
| `%` | Literal % |




### Spasi
```
awk -F: '{
    printf "%-10s %s\n", $1, $(NF-1)
}' /etc/passwd | head -n 3
```
Keluaran
``` skrip shell
root /root
bin /bin
daemon /sbin
```



### Header
```
awk -F: 'BEGIN {
    printf "%-10s %s\n", "User", "Home"
    printf "%-10s %s\n", "----","----"}
    { printf "%-10s %s\n", $1, $(NF-1) }
' /etc/passwd | head -n 5
```
Keluaran
```
Beranda Pengguna
---- ----
root /root
bin /bin
daemon /sbin
```



Lain-lain
-------------

### Metakarakter Regex
- `\`
- `^`
- `$`
- `.`
- `[`
- `]`
- `|`
- `(`
- `)`
- `*`
- `+`
- `?`
{.cols-3 .marker-none}

### Urutan Pelarian
| - | - |
|------|---------------------|
| `\b` | Backspace |
| `\f` | Umpan formulir |

| `\r` | Pengembalian ke belakang (carriage return)
| `\t` | Tab horizontal | | Tab horizontal
| `\v` | Tab vertikal |


### Jalankan skrip
```shell script
$ cat demo.awk
#!/usr/bin/awk -f
BEGIN { x = 23 }
      { x += 2 }
END { print x }
$ awk -f demo.awk /etc/passwd
69
```


Lihat juga
--------

- [Panduan Pengguna GNU Awk](https://www-zeuthen.desy.de/dv/documentation/unixguide/infohtml/gawk/gawk.html) (www-zeuthen.desy.de)_
- [Lembar kerja AWK](https://gist.github.com/Rafe/3102414) _(gist.github.com)_


