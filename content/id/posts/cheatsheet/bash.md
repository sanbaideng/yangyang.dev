---
judul: Bash
tanggal: 2020-11-25 18:28:43
latar belakang: bg-[#3e4548]
tags:
    - shell
    - sh
    - gema
    - skrip
    - linux
kategori:
    - Pemrograman
    - Sistem Operasi
intro: Ini adalah lembar contekan referensi cepat untuk memulai dengan skrip shell bash linux.
plugin:
    - copyCode
---

Memulai
---------------

### hello.sh

```bash
#!/bin/bash

VAR = "dunia"
echo "Halo $VAR!" # => Halo dunia!
```
Menjalankan skrip
``` skrip shell
$ bash hello.sh
```


### Variabel-variabel

```bash
NAME = "John"

echo ${NAME}    # => John (Variabel)
echo $NAME # => John (Variabel)
echo "$NAME"    # => John (Variabel)
echo '$NAME' # => $NAME (String yang tepat)
echo "${NAMA}!" # => John! (Variabel)

NAME = "John" # => Kesalahan (tentang spasi)
```



### Komentar

```bash
# Ini adalah komentar Bash sebaris.
```

```bash
: '
Ini adalah
komentar yang sangat rapi
di bash
'
```
Komentar multi-baris menggunakan `:'` untuk membuka dan ``` untuk menutup




### Argumen {.row-span-2}

| Ekspresi | Deskripsi | Deskripsi
|-------------|---------------------------------------|
| `$1` ... `$9` | Parameter 1 ... 9 |

| `$1` | Argumen pertama |
| `${10}` | Parameter posisi 10 |
| `$#` | Jumlah argumen | | `$#` | Jumlah argumen
| `$$` | Id proses dari shell |
| `$*` | Semua argumen |
| `$@` | Semua argumen, mulai dari yang pertama
| `$-` | Pilihan saat ini | | `$_` | Pilihan saat ini
| `$_` | Argumen terakhir dari perintah sebelumnya | | `$_` | Argumen terakhir dari perintah sebelumnya

Lihat: [Parameter khusus](http://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables)


### Fungsi

```bash
get_nama() {
    echo "John"
}

echo "Anda adalah $(get_nama)"
```

Lihat: [Fungsi](#bash-fungsi)

### Kondisional {#kondisional-contoh}

```bash
if [[ -z "$string" ]]; then
    echo "String kosong"
elif [ [ -n "$string" ]]; then
    echo "String tidak kosong"
fi
```

Lihat: [Kondisional](#bash-kondisional)

### Ekspansi penjepit

```bash
echo {A,B}.js
```
---

| Ekspresi | Deskripsi | Keterangan
|------------|---------------------|
| `{A,B}` | Sama seperti `A B` | | Sama seperti `A B
| `{A,B}.js` | Sama seperti `A.js B.js` | |A


Lihat: [Perluasan penjepit](http://wiki.bash-hackers.org/syntax/expansion/brace)

### Eksekusi shell

```bash
# => Saya berada di /path/of/current
echo "Saya berada di $(PWD)"

# Sama seperti:
echo "Saya di `pwd`"
```

Lihat: [Substitusi perintah](http://wiki.bash-hackers.org/syntax/expansion/cmdsubst)



Ekspansi Parameter Bash
--------------------



### Sintaks {.row-span-2}

| Kode | Deskripsi | Keterangan
|-------------------|---------------------|
| `${FOO%suffix}` | Hapus akhiran |
| `${FOO#awalan}` | Menghapus awalan |
| `${FOO%%suffix}` | Hapus akhiran panjang |
| `${FOO#awalan}` | Hapus awalan panjang |
| `${FOO/from/to}` | Ganti kecocokan pertama | | Ganti kecocokan pertama
| `${FOO//from/to}` | Ganti semua |
| `${FOO/%dari/ke}` | Ganti akhiran |
| `${FOO/#from/to}` | Ganti awalan |
#### Substring
| Ekspresi | Deskripsi |
|-----------------|--------------------------------|
| `${FOO:0:3}` | Substring _(posisi, panjang)_ | | Substring
| `${FOO:(-3):3}` | Substring dari kanan | | Substring
#### Panjang
| Ekspresi | Deskripsi | Keterangan
|------------|------------------|
| `${#FOO}` | Panjang dari `$FOO` |
#### Nilai default
| Ekspresi | Deskripsi |
|-------------------|------------------------------------------|
| `${FOO:-val}` | `$FOO`, atau `val` jika tidak disetel | |$FOO
| `${FOO:=val}` | Setel `$FOO` ke `val` jika tidak disetel | | $$FOO`, atau `val` jika tidak disetel
| `${FOO:+val}` | `val` jika `$FOO` disetel | | `$FOO` disetel
| `${FOO:?message}` | Tampilkan pesan dan keluar jika `$FOO` tidak disetel | | `${FOO:=val}` | Tampilkan pesan dan keluar jika `$FOO` tidak disetel



### Substitusi

```bash
echo ${makanan:-Kue}  #=> $makanan atau "Kue"
```


```bash
STR = "/path/to/foo.cpp"
echo ${STR%.cpp}    # /path/to/foo
echo ${STR%.cpp}.o # /path/to/foo.o
echo ${STR%/*}      # /path/to

echo ${STR##*.}     # cpp (ekstensi)
echo ${STR##*/}     # foo.cpp (jalur dasar)

echo ${STR#*/}      # path/to/foo.cpp
echo ${STR##*/}     # foo.cpp

echo ${STR/foo/bar} # /path/to/bar.cpp
```


### Mengiris

`` `bash
name = "John"
echo ${nama}           # => John
echo ${nama:0:2}       # => Jo
echo ${nama::2}        # => Jo
echo ${nama::-1} # => Joh
echo ${nama:(-1)} # => n
echo ${nama:(-2)} # => hn
echo ${nama:(-2):2}    # => hn

length = 2
echo ${nama:(0):panjang}  # => Jo
```
Lihat: [Perluasan parameter](http://wiki.bash-hackers.org/syntax/pe)



### basepath & dirpath
```bash
SRC = "/path/to/foo.cpp"
```

```bash
BASEPATH=${SRC##*/}   
echo $BASEPATH # => "foo.cpp"


DIRPATH=${SRC%$BASEPATH}
echo $DIRPATH # => "/path/to/"
```






### Transform

```bash
STR = "HALO DUNIA!"
echo ${STR,}   # => HELLO DUNIA!
echo ${STR,,}  # => halo dunia!

STR = "halo dunia!"
echo ${STR^}   # => halo dunia!
echo ${STR^^}  # => HALO DUNIA!

ARR = (halo dunia)
echo "${ARR[@],}" # => halo dunia
echo "${ARR[@]^}" # => halo dunia
```




Larik Bash
------

### Mendefinisikan larik

```bash
Buah-buahan = ('Apel' 'Pisang' 'Jeruk')

Buah-buahan [0] = "Apel"
Buah-buahan [1] = "Pisang"
Buah-buahan [2] = "Jeruk"

ARRAY1=(foo{1..2}) # => foo1 foo2
ARRAY2=({A..D}) # => A B C D

# Penggabungan => foo1 foo2 A B C D
ARRAY3=(${ARRAY1[@]} ${ARRAY2[@]})

# mendeklarasikan construct
mendeklarasikan -a Bilangan = (1 2 3)
Bilangan+=(4 5) # Menambahkan => 1 2 3 4 5
```



### Pengindeksan

| - | - |
|--------------------|---------------|
| `${Buah-buahan[0]}` | Elemen pertama |
| `${Buah-buahan[-1]}` | Elemen terakhir |
| `${Buah-buahan[*]}` | Semua elemen |
| `${Buah-buahan[@]}` | Semua elemen |
| `${#Buah-buahan[@]}` | Jumlah semua |
| `${#Buah-buahan}` | Panjang pertama |
| `${#Buah-buahan[3]}` | Panjang ke-n |
| `${Buah-buahan[@]:3:2}` | Rentang |
| `${!Buah-buahan[@]}` | Kunci dari semua |



### Iterasi

```bash
Buah-buahan = ('Apel' 'Pisang' 'Jeruk')

for e in "${Buah-buahan[@]}"; do
    echo $e
selesai
```
#### Dengan indeks
``` bash
for i in "${!Buah-buahan[@]}"; do
  printf "%s\t%s\n" "$i" "${Buah-buahan[$i]}"
selesai

```


### Operasi {.col-span-2}

``` bash
Buah-buahan=("${Buah-buahan[@]}" "Semangka") # Dorong
Buah-buahan+=('Semangka') # Juga Dorong
Buah-buahan=( ${Buah-buahan[@]/Ap*/} ) # Hapus dengan pencocokan regex
unset Buah-Buahan[2] # Hapus satu item
Buah-buahan=("${Buah-buahan[@]}") # Duplikat
Buah-buahan=("${Buah-buahan[@]}" "${Buah-buahan[@]}") # Menggabungkan
lines=(`cat "logfile"`) # Baca dari file
```

### Larik sebagai argumen
``` bash
fungsi extract()
{
    local -n myarray = $ 1
    local idx = $ 2
    echo "${myarray[$idx]}"
}
Buah-buahan = ('Apel' 'Pisang' 'Jeruk')
ekstrak Buah-buahan 2 # => Jeruk
```





Kamus Bash
------------

### Mendefinisikan

```bash
mendeklarasikan -A suara
```

```bash
suara [anjing] = "gonggongan"
suara [sapi] = "melenguh"
suara [burung] = "kicau"
suara [serigala] = "lolongan"
```


### Bekerja dengan kamus

``` bash
gema ${bunyi[anjing]} # Suara anjing
echo ${suara[@]}   # Semua nilai
echo ${!suara[@]}  # Semua kunci
gema ${#bunyi[@]}  # Jumlah elemen
unset suara[anjing] # Hapus anjing
```

### Iterasi

``` bash
for val in "${suara[@]}"; do
    echo $val
selesai
```
---
``` bash
for key in "${!sounds[@]}"; do
    menggemakan $kunci
selesai
```





Kondisi Bash
------------

### Kondisi bilangan bulat

| Kondisi | Deskripsi | Keterangan
|---------------------|---------------------------------------------|
| `[[ NUM -eq NUM ]]` | <yel>Eq</yel> sama dengan |
| `[[ NUM -ne NUM ]]` | <yel>N</yel>ot <yel>e</yel>sama |
| `[[ NUM -lt NUM ]]` | <yel>L</yel>ess <yel>t</yel>han |
| `[[ NUM -le NUM ]]` | <yel>L</yel> lebih kecil dari atau <yel>e</yel>sama |
| `[[ NUM -gt NUM ]]` | <yel>G</yel> lebih dari <yel>t</yel>han |
| `[[ NUM -ge NUM ]]` | <yel>G</yel> lebih besar dari atau <yel>e</yel>sama |
| `(( NUM < NUM )` | Kurang dari |
| `(( NUM <= NUM ))` | Kurang dari atau sama dengan |
| `(( NUM > NUM )` | Lebih besar dari |
| `(( NUM >= NUM )` | Lebih besar dari atau sama dengan |


### Kondisi string

| Kondisi | Deskripsi |
|--------------------|-----------------------------|
| `[[ -z STR ]]` | String kosong |
| ` [[[ -n STR ]]` | <yel>N</yel> bukan string kosong |
| `[[ STR == STR ]]` | Sama dengan |
| `[[ STR = STR ]]` | Sama (Sama di atas) |
| `[[ STR < STR ]]` | Kurang dari _(ASCII)_ |
| `[[ STR > STR ]]` | Lebih besar dari _(ASCII)_ |
| `[[ STR != STR ]]` | Tidak Sama
| `[[ STR =~ STR ]]` | Regexp |






### Contoh {.row-span-3}

#### String
```bash
if [[ -z "$string" ]]; then
    echo "String kosong"
elif [ [ -n "$string" ]]; then
    echo "String tidak kosong"
else
    echo "Ini tidak pernah terjadi"
fi
```

#### Kombinasi
``` bash
if [[ X && Y ]]; then
    ...
fi
```

#### Sama dengan
``` bash
if [[ "$A" == "$B" ]]; then
    ...
fi
```

#### Regex
``` bash
if [[ '1. abc' =~ ([a-z]+) ]]; then
    echo ${BASH_REMATCH[1]}
fi
```

#### Lebih kecil
``` bash
if (( $a < $b )); then
   echo "$a lebih kecil dari $b"
fi
```

#### Ada
``` bash
if [[ -e "file.txt" ]]; then
    echo "file ada"
fi
```





### Kondisi file {.row-span-2}

| Kondisi | Deskripsi | Keterangan
|-------------------|----------------------------------------|
| `[[ -e FILE ]]` | <yel>E</yel> ada |
| `[[ -d FILE ]]` | <yel>D</yel>direktori |
| ` [[[ -f FILE ]]` | <yel>F</yel>ile |
| ` [[[ -h FILE ]]` | Symlink |
| ` [[[ -s FILE ]]` | Ukuran > 0 byte |
| ` [[[ -r FILE ]]` | <yel>R</yel>dapat dibaca |
| ` [[[ -w FILE ]]` | <yel>W</yel>dapat dibaca |
| ` [[[ -x FILE ]]` | Dapat dieksekusi |
| `[[ f1 -nt f2 ]]` | f1 <yel>n</yel>ewer <yel>t</yel>han f2 |
| `[[ f1 -ot f2 ]]` | f2 <yel>o</yel>lder <yel>t</yel>han f1 |
| `[[ f1 -ef f2 ]]` | File yang sama


### Kondisi lainnya

| Kondisi | Deskripsi | Keterangan
|----------------------|----------------------|
| `[[ -o noclobber ]]` | Jika OPTION diaktifkan |
| `[[ ! EXPR ]]` | Tidak |
| `[[ X && Y ]]` | Dan |
| `[[ X || Y ]]` | Atau |


### logika dan, atau
```bash
if [ "$1" = 'y' -a $2 -gt 0 ]; then
    echo "ya"
fi

if [ "$1" = 'n' -o $2 -lt 0 ]; then
    echo "tidak"
fi
```



Bash Loops
-----

### Perulangan dasar untuk perulangan

```bash
for i in /etc/rc.*; do
    echo $i
selesai
```

### Perulangan seperti C untuk perulangan

``` bash
for ((i = 0 ; i < 100 ; i++)); do
    echo $i
selesai
```

### Rentang {.row-span-2}

``` bash
for i in {1..5}; do
    echo "Selamat datang $i"
selesai
```


#### Dengan ukuran langkah

```bash
for i in {5..50..5}; do
    echo "Selamat datang $i"
selesai
```



### Kenaikan otomatis

```bash
i=1
while [[ $i -lt 4 ]]; do
    echo "Nomor: $i"
    ((i++))
selesai
```

### Pengurangan otomatis

``` bash
i=3
while [[ $i -gt 0 ]]; do
    echo "Nomor: $i"
    ((i--))
selesai
```


### Lanjutkan

```bash {data=3,5}
for number in $(seq 1 3); do
    if [ [ $nomor == 2 ]]; then
        continue
    fi
    echo "$jumlah"
selesai
```


### Istirahat

``` bash
for number in $(seq 1 3); do
    if [[ $number == 2 ]]; then
        # Lewati seluruh sisa perulangan.
        istirahat;
    fi
    # Ini hanya akan mencetak 1
    echo "$number"
selesai
```

### Sampai
``` bash
count = 0
until [ $count -gt 10 ]; do
    echo "$hitung"
    ((count++))
selesai
```


### Selamanya

``` bash
while true; do
    # Berikut adalah beberapa kode.
done
```

### Selamanya (singkatan)
``` bash
while :; do
    # berikut adalah beberapa kode.
done
```


### Membaca baris

``` bash
cat file.txt | while baca baris; do
    echo $baris
selesai
```





Fungsi Bash
---------

### Mendefinisikan fungsi

```bash
myfunc() {
    echo "halo $1"
}
```

``` bash
# Sama seperti di atas (sintaks alternatif)
function myfunc() {
    echo "halo $1"
}
```

``` bash
myfunc "John"
```

### Mengembalikan nilai

``` bash
myfunc() {
    local myresult = 'suatu nilai'
    echo $myresult
}
```

``` bash
result = "$(myfunc)"
```

### Menimbulkan kesalahan

``` bash
myfunc() {
    return 1
}
```

``` bash
if myfunc; then
    echo "sukses"
else
    echo "kegagalan"
fi
```



Opsi Bash {.cols-2}
-------

Opsi ###

```bash
# Menghindari file overlay
# (echo "hi" > foo)
set -o noclobber

# Digunakan untuk keluar saat terjadi kesalahan
# Menghindari kesalahan yang bertingkat-tingkat
set -o errexit

# Menyingkap kegagalan yang tersembunyi
set -o pipefail

# Mengekspos variabel yang tidak diset
set -o nounset
```

### Opsi glob

``` bash
# Glob yang tidak cocok akan dihapus
# ('*.foo' => '')
shopt -s nullglob

# Kesalahan lemparan glob yang tidak cocok
shopt -s failglob

# Globs yang tidak peka huruf besar/kecil
shopt -s nocaseglob

# Karakter pengganti cocok dengan dotfile
# ("*.sh" => ".foo.sh")
shopt -s dotglob

# Izinkan ** untuk pencocokan rekursif
# ('lib/**/*.rb' => 'lib/a/b/c.rb')
shopt -s globstar
```


Riwayat Bash {.cols-2}
-------

### Perintah

| Perintah | Deskripsi |
|-----------------------|-------------------------------------------|
| `history` | Menampilkan riwayat
| `sudo !!` | Menjalankan perintah sebelumnya dengan sudo
| `shopt -s histverify` | Jangan langsung mengeksekusi hasil yang diperluas |

### Ekspansi

| Ekspresi | Deskripsi | Keterangan
|--------------|------------------------------------------------------|


| `!-n` | Perluas perintah terbaru ke-n | | n
| `!n` | Perluas perintah ke-n dalam riwayat | | `!n` | Perluas perintah ke-n dalam riwayat
| `!<perintah>` | Memperluas pemanggilan terbaru dari perintah `<perintah>` | | Memperluas

### Operasi

| Kode | Deskripsi |
|----------------------|-----------------------------------------------------------------------|

| `!!:s/<FROM>/<TO>/` | Mengganti kemunculan pertama dari `<FROM>` menjadi `<TO>` dalam perintah terakhir | | `!!:s/<FROM>/<TO>/` | Mengganti kemunculan pertama dari `<FROM>` menjadi `<TO>` dalam perintah terakhir
| `!!!:gs/<FROM>/<TO>/` | Ganti semua kemunculan `<FROM>` menjadi `<TO>` dalam perintah terbaru | | Ganti semua kemunculan `<FROM>` menjadi `<TO>` dalam perintah terbaru | | Ganti semua kemunculan `<FROM>` menjadi `<TO>` dalam perintah terbaru

| `!$:h` | Perluas hanya direktori dari parameter terakhir dari perintah terbaru | | `!$:h` | Perluas hanya direktori dari parameter terakhir dari perintah terbaru

`!!` dan `!$` dapat diganti dengan ekspansi yang valid.

### Irisan

| Kode | Deskripsi | Keterangan
|----------|------------------------------------------------------------------------------------------|



| `!!:n-m` | Perluas rentang token dari perintah terbaru | | `!$` | Perluas rentang token dari perintah terbaru
| `!!:n-$` | Memperluas token ke-n hingga terakhir dari perintah terbaru | | `!$` | Memperluas token ke-n hingga terakhir dari perintah terbaru

`!!` dapat diganti dengan ekspansi yang valid, misalnya `!cat`, `!-2`, `!42`, dll.


Lain-lain
-------------

### Perhitungan numerik

```bash
$((a + 200))      # Tambahkan 200 ke $a
```

```bash
$(($RANDOM%200))  # Angka acak 0..199
```

### Subshells

``` bash
(cd somedir; echo "Saya sekarang berada di $PWD")
pwd # masih di direktori pertama
```


### Memeriksa perintah-perintah

``` bash
perintah -V cd
#=> "cd adalah sebuah fungsi/alias/apa pun"
```


### Pengalihan {.row-span-2 .col-span-2}

``` bash
python hello.py > output.txt # stdout ke (file)
python hello.py >> output.txt # stdout to (file), append
python hello.py 2> error.log # stderr ke (file)
python hello.py 2>&1 # stderr ke stdout
python hello.py 2>/dev/null # stderr ke (null)
python hello.py &>/dev/null # stdout dan stderr ke (null)
```

```bash
python hello.py < foo.txt # mengumpankan foo.txt ke stdin untuk python
```


### Sumber relatif

``` bash
sumber "${0%/*}/../share/foo.sh"
```

### Direktori skrip

``` bash
DIR = "${0%/*}"
```

### Huruf besar/kecil

``` bash
huruf besar "$ 1" di
    mulai | naik)
    gelandangan naik
    ;;

    *)
    echo "Penggunaan: $ 0 {start|stop|ssh}"
    ;;
esac
```


### Kesalahan perangkap {.col-span-2}

``` bash
trap 'echo Kesalahan di sekitar $LINENO' ERR
```

atau

``` bash
traperr() {
    echo "KESALAHAN: ${BASH_SOURCE[1]} di sekitar ${BASH_LINENO[0]}"
}

set -o errtrace
trap traperr ERR
```


### printf

```bash
printf "Halo %s, saya %s" Sven Olga
#=> "Halo Sven, saya Olga

printf "1 + 1 = %d" 2
#=> "1 + 1 = 2"

printf "Cetak sebuah float: %f" 2
#=> "Cetak sebuah float: 2.000000"
```

### Mendapatkan opsi {.col-span-2}

``` bash
while [[ "$1" =~ ^- && ! "$1" == "--" ]]; do case $1 in
    -V | --versi )
    echo $ versi
    keluar
    ;;
    -s | --string )
    shift; string = $ 1
    ;;
    -f | --flag )
    flag = 1
    ;;
esac; shift; done
if [ [ "$1" == '--' ]]; then shift; fi
```

### Periksa hasil perintah {.col-span-2}

``` bash
if ping -c 1 google.com; then
    echo "Tampaknya Anda memiliki koneksi internet yang berfungsi"
fi
```


### Variabel khusus {.row-span-2}

| Ekspresi | Deskripsi | Keterangan
|------------|------------------------------|
| `$?` | Status keluar dari tugas terakhir |
| `$!` | PID tugas latar belakang terakhir |
| `$$` | PID dari shell |
| `$0` | Nama file dari skrip shell |

Lihat [Parameter khusus] (http://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables).


### Grep cek {.col-span-2}

```bash
if grep -q 'foo' ~/.bash_history; then
    echo "Anda sepertinya pernah mengetik 'foo' di masa lalu"
fi
```


### Backslash lolos dari {.row-span-2}

- &nbsp;
- \!
- \"
- \#
- \&
- \'
- \(
- \)
- \,
- \;
- \<
- \>
- \[
- \|
- \\
- \]
- \^
- \{
- \}
- \`
- \$
- \*
- \?
{.cols-4 .marker-none}


Melarikan diri dari karakter khusus ini dengan `\`




### Heredoc

```sh
kucing <<END
halo dunia
END
```


### Pergi ke direktori sebelumnya

``` bash
pwd # /home/user/foo
cd bar/
pwd # /home/user/foo/bar
cd -
pwd # /home/user/foo
```


### Membaca masukan

``` bash
echo -n "Lanjutkan? [y/n]: "
baca ans
echo $ans
```

```bash
read -n 1 ans # Hanya satu karakter
```


### Eksekusi bersyarat

``` bash
git commit && git push
git commit || echo "Komit gagal"
```


### Mode ketat

``` bash
set -euo pipefail
IFS = $'\n\t'
```

Lihat: [Mode ketat bash tidak resmi](http://redsymbol.net/articles/unofficial-bash-strict-mode/)


### Argumen opsional

```bash
args=("$@")
args+=(foo)
args+=(bar)
echo "${args[@]}"
```

Menempatkan argumen ke dalam larik dan kemudian menambahkan



## Lihat juga {.cols-1}
* [Devhints](https://devhints.io/bash) _(devhints.io)_
* [Bash-hackers wiki](http://wiki.bash-hackers.org/) _(bash-hackers.org)_
* [Shell vars](http://wiki.bash-hackers.org/syntax/shellvars) _(bash-hackers.org)_
* [Belajar bash dalam beberapa menit](https://learnxinyminutes.com/docs/bash/) _(learnxinyminutes.com)_
* [Panduan Bash](http://mywiki.wooledge.org/BashGuide) _(mywiki.wooledge.org)_
* [ShellCheck](https://www.shellcheck.net/) _(shellcheck.net)_
* [shell - Standard Shell](https://devmanual.gentoo.org/tools-reference/bash/index.html) _(devmanual.gentoo.org)_
