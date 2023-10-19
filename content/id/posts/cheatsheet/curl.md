---
title: Keriting
date: 2023-01-03 15:18:34
latar belakang: bg-slate-600
tags:
    - url
    - permintaan
kategori:
    - Perintah Linux
intro: |
    Lembar contekan [Curl] (https://github.com/curl/curl) ini berisi perintah dan contoh beberapa trik Curl yang umum.
plugin:
    - copyCode
---

Memulai
---------------


### Pendahuluan

`Curl` adalah alat untuk mentransfer data antar server, mendukung protokol, termasuk:
- HTTP
- HTTPS
- FTP
- IMAP
- LDAP
- POP3
- SCP
- SFTP
- SMB
- SMTP
- dll...
{.cols-3 .marker-none}

----------------------------------------------------------------

- [Repositori sumber Curl GitHub](https://github.com/curl/curl) _(github.com)_
- [Situs web resmi Curl](https://curl.se/) _(curl.se)_


### Opsi {.col-span-2 row-span-2}

```bash
-o <file> # --output: menulis ke berkas
-u user:pass # --user: autentikasi
```

---

``` bash
-v # --verbose: Membuat curl menjadi verbose selama operasi
-vv # lebih banyak kata yang bertele-tele
-s # --silent: jangan tampilkan pengukur kemajuan atau kesalahan
-s # --show-error: tampilkan kesalahan: Ketika digunakan dengan --silent (-sS), tampilkan kesalahan tetapi tidak ada pengukur kemajuan
```

---

``` bash
-i # --include: menyertakan header HTTP dalam keluaran
-I # --head: hanya header saja
```



### Permintaan

```bash
-X POST # --request
-L # Jika halaman dialihkan, ikuti tautan
-F # --form: Data HTTP POST untuk data multipart/formulir
```
<!--rehype:className=wrap-text -->



### data

```bash
# --data: Data posting HTTP
# Pengkodean URL (misalnya, status = "Halo")
-d 'data'

# --data melewatkan berkas
-d @file

# --get: mengirim -d data melalui get
-G
```



### Informasi tajuk Header Header

```bash
-A <str> # --user-agent

-b name=val # --cookie

-b, --cookie FILE # Memuat cookie dari berkas yang ditentukan untuk URL
-c, --cookie-jar FILE # Menyimpan kuki ke berkas yang ditentukan dari URL

-H "X-Foo: y" # --header

--kompresi # gunakan deflate/gzip
```



### SSL

```bash
    --cacert <file>
    --capath <dir>
```

```bash
-E, --cert <cert> # --cert: berkas sertifikat klien
    --cert-type # der/pem/eng
-k, --insecure # Untuk sertifikat yang ditandatangani sendiri
```



#### Instal

```bash
apk add --update curl # instal di alpine linux
```

Contoh {.cols-6}
----
<!--rehype:body-class=cols-6-->


### CURL GET/HEAD {.col-span-4 .row-span-2}

perintah | deskripsi
:-| :-
`curl -I https://cheatsheets.zip` | `curl` mengirimkan permintaan
`curl -v -I https://cheatsheets.zip` | `curl` permintaan dengan detail
`curl -X GET https://cheatsheets.zip` | menggunakan metode http eksplisit untuk `curl`
`curl --noproxy 127.0.0.1 http://www.stackoverflow.com` | `curl` tanpa proxy http
`curl --connect-timeout 10 -I -k https://cheatsheets.zip` | `curl` tidak memiliki batas waktu secara default
`curl --verbose --header "Host: www.mytest.com:8182" cheatsheets.zip` | `curl` mendapatkan header tambahan
`curl -k -v https://www.google.com` | `curl` dapatkan respons dengan header
<!--rehype:class=auto-wrap-->



### Unggahan beberapa berkas {.col-span-2}

```bash
$ curl -v --include \
--form key1 = nilai1 \
    --form upload=@localfilename URL
```



### Mempercantik keluaran json untuk respons curl {.col-span-2}

```bash
$ curl -XGET http://${elasticsearch_ip}:9200/_cluster/nodes | python -m json.tool
```
<!--rehype:className=wrap-text -->



### CURL POST {.col-span-4}

perintah | deskripsi
:-| :-
`curl -d "name=username&password=123456" <URL>` | `curl` mengirim permintaan
`curl <URL> -H "content-type: application/json" -d "{ \"guk\": \"menggonggong\"}"` | `curl` mengirim json
<!--rehype:class=auto-wrap-->
### Skrip CURL instal rvm {.col-span-2}

```shell
curl -sSL https://get.rvm.io | bash
```



### CURL Lanjutan {.col-span-6}

perintah | deskripsi
:-| :-
`curl -L -s http://ipecho.net/plain, curl -L -s http://whatismijnip.nl` | mendapatkan `IP` publik saya
`curl -u $username:$password http://repo.dennyzhang.com/README.txt` | `curl` dengan kredensial
`curl -v -F key1=value1 -F upload=@localfilename <URL>` | `curl` upload
`curl -k -v --http2 https://www.google.com/` | gunakan http2 curl
`curl -T cryptopp552.zip -u test:test ftp://10.32.99.187/` | curl `ftp` upload
`curl -u test:test ftp://10.32.99.187/cryptopp552.zip -o cryptopp552.zip` | curl `ftp` unduh
`curl -v -u admin:admin123 --upload-file package1.zip http://mysever:8081/dir/package1.zip` | unggah dengan kredensial `curl`
<!--rehype:class=auto-wrap-->



### Periksa waktu respons situs web {.col-span-4}

```shell
curl -s -w \
'\nWaktu pencarian:\t%{waktu_nama_pencarian}\nWaktu koneksi:\t%{waktu_koneksi}\nWaktu AppCon:\t%{waktu_appconnect}\nWaktu pengalihan:\t%{waktu_redirect}\nWaktu PreXfer:\t%{waktu_pretransfer}\nWaktu StartXfer:\t%{waktu_starttransfer}\n\nWaktu Total:\t%{waktu_total}\n' \
     -o /dev/null https://www.google.com
```
<!--rehype:className=wrap-text -->



### Gunakan Curl untuk memeriksa apakah sumber daya jarak jauh tersedia {.col-span-2}

```bash
curl -o /dev/null --silent -Iw "%{http_code}" https://example.com/my.remote.tarball.gz
```
<!--rehype:className=wrap-text -->



### Mengunduh berkas {.col-span-3}

```bash
curl https://example.com | \'
grep --only-matching 'src="[^"]*.[png]"' | \
cut -d \" -f2 | \
while read i; do curl https://example.com/"${i}" \
-o "${i##*/}"; done
```

Unduh semua berkas PNG dari situs (menggunakan GNU grep)



### Unduh berkas, simpan berkas tanpa mengubah namanya {.col-span-3}

```bash
curl --remote-name "https://example.com/linux-distro.iso"
```

ganti nama berkas

``` bash
curl --remote-name "http://example.com/index.html" --output foo.html
```



### lanjutkan pengunduhan sebagian {.col-span-3}

```bash
curl --remote-name --continue-at - "https://example.com/linux-distro.iso"
```
<!--rehype:className=wrap-text -->



### Unduh berkas dari beberapa domain {.col-span-3}

```bash
curl "https://www.{contoh,w3,iana}.org/index.html" --output "file_#1.html"
```
<!--rehype:className=wrap-text -->



### Unduh serangkaian file {.col-span-3}

```bash
curl "https://{foo,bar}.com/file_[1-4].webp" --output "#1_#2.webp"
```
<!--rehype:className=wrap-text -->

Mengunduh serangkaian berkas (keluaran `foo_file1.webp`, `foo_file2.webp ... bar_file1_webp`, dst.)
### Alihkan keluaran ke berkas {.col-span-3}

```bash
$ curl http://url/file > file
```



### Otentikasi Dasar {.col-span-3}

```bash
$ curl --user nama pengguna:kata sandi http://example.com/
$ curl -u nama pengguna:kata sandi http://example.com/
```



### Menulis ke berkas, bukan stdout {.col-span-2}

```bash
$ curl -o berkas http://url/file
$ curl --output file http://url/file
```



### Unduh informasi header

```bash
$ curl -I url
# menampilkan informasi header
```



### Tulis keluaran ke file bernama remote_file {.col-span-2}

```bash
$ curl -o berkas http://url/file
$ curl --output berkas http://url/file
```
### Jalankan skrip jarak jauh {.col-span-2}

``` bash
$ curl -s http://url/myscript.sh
```



### File konfigurasi {.col-span-2}

```bash
curl -K file
# baca konfigurasi dari berkas
curl --config file
$HOME/.curlrc # berkas konfigurasi default pada sistem seperti UNIX
```
