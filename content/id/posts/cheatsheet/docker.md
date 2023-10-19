---
title: Docker
date: 2020-12-30 10:55:24
latar belakang: bg-[#488fdf]
tags:
    - wadah
    - virtual
kategori:
    - Pemrograman
intro: |
    Ini adalah lembar contekan referensi cepat untuk [Docker](https://docs.docker.com/get-started/). Dan Anda dapat menemukan perintah Docker yang paling umum di sini.
plugin:
    - copyCode
---

Memulai {.cols-2}
---------------

### Memulai
Membuat dan menjalankan kontainer di latar belakang

```skrip shell
$ docker run -d -p 80:80 docker/getting-started
```

----

- `-d` - Jalankan kontainer dalam mode terpisah
- `-p 80:80` - Memetakan porta 80 ke porta 80 di dalam kontainer
- `docker/getting-started` - Gambar yang akan digunakan
{.marker-none}


Membuat dan menjalankan kontainer di latar depan
```shell script
$ docker run -it -p 8001:8080 --name my-nginx nginx
```

----

- `-it` - Mode bash interaktif
- `-p 8001:8080` - Memetakan port 8001 ke port 8080 di dalam kontainer
- `--nama my-nginx` - Tentukan nama
- `nginx` - Gambar yang akan digunakan
{.marker-none}



### Perintah umum
| Contoh | Deskripsi | Keterangan
|-------------------------------------|--------------------------------------------------|
| `docker ps` | Daftar kontainer yang sedang berjalan
| `docker ps -a` | Daftar semua kontainer |
| `docker ps -s` | Daftar kontainer yang sedang berjalan<br>_(dengan CPU / memori)_ | | | Daftar semua kontainer
| `docker images` | Daftar semua image | | Daftar semua image
| `docker exec -it <kontainer> bash` | Menghubungkan ke kontainer |
| `docker logs <container>` | Menampilkan log konsol kontainer |
| `docker stop <container>` | Menghentikan kontainer
| `docker restart <container>` | Memulai ulang kontainer
| `docker rm <container>` | Menghapus kontainer
| `docker port <container>` | Menampilkan pemetaan port kontainer |
| `docker top <container>` | Membuat daftar proses
| `docker kill <container>` | Membunuh kontainer |

Parameter `<container>` dapat berupa id atau nama kontainer




Kontainer Docker {.cols-2}
----------


### Memulai & Menghentikan
| Deskripsi | Contoh | Contoh
|-------------------------------|-------------------------------------|
| `docker start my-nginx` | Memulai |
| `docker stop my-nginx` | Menghentikan |
| `docker restart my-nginx` | Memulai ulang
| `docker pause my-nginx` | Menjeda
| `docker unpause my-nginx` | Menghentikan jeda
| `docker wait my-nginx` | Memblokir Kontainer |
| `docker kill my-nginx` | Mengirimkan SIGKILL |
| `docker attach my-nginx` | Menghubungkan ke Kontainer yang Sudah Ada



Informasi ###

| Contoh | Deskripsi | Keterangan
|-------------------------------|----------------------------------------|
| `docker ps` | Daftar kontainer yang sedang berjalan
| `docker ps -a` | Daftar semua kontainer |
| `docker logs my-nginx` | Log Kontainer
| `docker inspect my-nginx` | Memeriksa Kontainer |
| `docker events my-nginx` | Peristiwa Kontainer |
| `docker port my-nginx` | Port Publik |
| `docker top my-nginx` | Menjalankan Proses |
| `docker stats my-nginx` | Penggunaan Sumber Daya Kontainer |
| `docker diff my-nginx` | Daftar perubahan yang dilakukan pada kontainer. |


### Membuat

```yaml
docker membuat [opsi] IMAGE
  -a, --attach # lampirkan stdout/err
  -i, --interactive # pasang stdin (interaktif)
  -t, --tty # pseudo-tty
      --name NAME # beri nama gambar Anda
  -p, --publish 5000:5000 # peta porta (host:container)
      --expose 5432 # mengekspos sebuah port ke kontainer
  -p, --publish-all # publikasikan semua port
      --link container:alias # penautan
  -v, --volume `pwd`:/app # mount (jalur absolut yang dibutuhkan)
  -e, --env NAME = halo # env vars
```
#### Contoh
``` skrip shell
$ docker create --name my_redis --expose 6379 redis:3.0.2
```


### Memanipulasi
Mengganti nama kontainer
``` skrip shell
docker ganti nama my-nginx my-nginx
```
Menghapus sebuah Kontainer
```shell script
docker rm my-nginx
```
Memperbarui kontainer
```shell script
docker update --cpu-shares 512 -m 300M my-nginx
```




Gambar Docker {.cols-2}
------

### Memanipulasi
| `Contoh` | Deskripsi |
|------------------------------------|---------------------------------|
| `docker images` | Mendaftarkan gambar |
| `docker rmi nginx` | Menghapus citra |
| `docker load < ubuntu.tar.gz` | Memuat repositori yang di-tar
| `docker load --input ubuntu.tar` | Memuat repositori yang di-tar` | Memuat repositori yang di-tar
| `docker save busybox > ubuntu.tar` | Menyimpan citra ke arsip tar
| `docker history` | Menampilkan riwayat sebuah citra
| `docker commit nginx` | Menyimpan kontainer sebagai citra.   |
| `docker tag nginx eon01/nginx` | Menandai sebuah citra
| `docker push eon01/nginx` | Mendorong sebuah citra


### Membangun Citra
```shell script
$ docker build .
$ docker build github.com/creack/docker-firefox
$ docker build - < Dockerfile
$ docker build - < context.tar.gz
$ docker build -t eon/my-nginx .
$ docker build -f myOtherDockerfile .
$ curl example.com/remote/Dockerfile | docker build -f - .
```



Jaringan Docker {.cols-2}
----------




### Memanipulasi

Menghapus jaringan
```script shell
docker network rm MyOverlayNetwork
```
Mendaftarkan jaringan
``` skrip shell
jaringan docker ls
```
Mendapatkan informasi tentang jaringan
```shell script
docker network memeriksa MyOverlayNetwork
```
Menghubungkan kontainer yang sedang berjalan ke jaringan
```shell script
docker network hubungkan MyOverlayNetwork nginx
```
Menghubungkan kontainer ke jaringan saat dimulai
```shell script
docker run -it -d --network=MyOverlayNetwork nginx
```
Memutuskan kontainer dari jaringan
```shell script
docker network putuskan koneksi MyOverlayNetwork nginx
```



### Membuat Jaringan
``` skrip shell
docker network create -d overlay MyOverlayNetwork

docker network create -d bridge MyBridgeNetwork

docker network create -d overlay \
  --subnet=192.168.0.0/16 \
  --subnet=192.170.0.0/16 \
  --gateway=192.168.0.100 \
  --gateway=192.170.0.100 \
  --ip-range=192.168.1.0/24 \
  --aux-address="my-router=192.168.1.5" \
  --aux-address="my-switch=192.168.1.6" \
  --aux-address="my-printer=192.170.1.5" \
  --aux-address="my-nas=192.170.1.6" \
  MyOverlayNetwork
```



Bersihkan {.cols-2}
-------------


### Bersihkan Semua
Membersihkan gambar, kontainer, volume, dan jaringan yang menggantung (yaitu, tidak terkait dengan kontainer)
```shell
pemangkasan sistem docker
```

-------

Selain itu, hapus semua kontainer yang berhenti dan semua citra yang tidak digunakan (bukan hanya citra yang menggantung)

```shell
docker system prune -a
```



### Wadah

Menghentikan semua kontainer yang sedang berjalan
```shell
docker stop $(docker ps -a -q)
```

Menghapus kontainer yang dihentikan
```shell
pemangkasan kontainer docker
```

### Gambar

Menghapus semua gambar yang menggantung (tidak ditandai dan tidak terkait dengan kontainer):
``` cangkang
pemangkasan citra docker
```

Menghapus semua citra yang tidak digunakan oleh kontainer yang ada
```shell
docker image prune -a
```


### Volume

``` cangkang
pemangkasan volume docker
```
Hapus semua volume yang tidak digunakan oleh setidaknya satu kontainer



Lain-lain {.cols-2}
-------------


### Docker Hub
| Sintaks Docker | Deskripsi | Deskripsi
|-----------------------------|-------------------------------------|
| `docker search search_word` | Cari docker hub untuk gambar.       
| `docker pull user/image` | Mengunduh citra dari docker hub. 
| `docker login ` | Mengautentikasi ke docker hub
| `docker push user/image ` | Mengunggah citra ke docker hub.     |





### Perintah registri {.row-span-3}

Masuk ke Registry

```skrip shell
$ docker login
$ docker login localhost:8080
```

Keluar dari Registri

``` skrip shell
$ docker logout
$ docker logout localhost:8080
```

Mencari Gambar

``` skrip shell
$ docker cari nginx
$ docker search nginx --stars=3 --no-trunc busybox
```

Menarik Gambar

``` skrip shell
$ docker pull nginx
$ docker pull eon01/nginx localhost:5000/myadmin/nginx
```

Mendorong Citra

``` skrip shell
$ docker push eon01/nginx
$ docker push eon01/nginx localhost:5000/myadmin/nginx
```



### Batch bersih
| Contoh | Deskripsi | Keterangan
|-------------|---------------------------------------------|
`docker stop -f $(docker ps -a -q)` | Menghentikan semua kontainer
`docker rm -f $(docker ps -a -q)` | Menghapus semua kontainer
`docker rmi -f $(docker images -q)` | Menghapus semua image





### Volume

Memeriksa volume
```shell script
$ docker volume ls
```
Membersihkan volume yang tidak terpakai
```shell script
$ docker volume prune
```
