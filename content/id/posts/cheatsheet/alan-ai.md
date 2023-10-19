---
judul: Alan AI
tanggal: 2023-03-03 6:00:00
latar belakang: bg-[#4aa181]
Tag:
    - AI
    - AlanAI
    - Petunjuk
    - Tips
kategori:
    - Toolkit
intro: Lembar contekan ini mencakup semua konsep skrip utama, metode API klien, penangan, dan alat lain untuk menciptakan pengalaman percakapan multimodal dengan Alan AI
---

### Legenda

- ``pola`` - frasa untuk memanggil perintah suara/teks atau respons yang akan dimainkan
- ``nilai`` - nilai yang ditentukan
- ``params`` - parameter yang dilewatkan
- ``action`` - tindakan yang akan dilakukan
- ``output`` - hasil data
- ``[...]`` - data atau parameter opsional

Skrip dialog
-------------

### Maksud & pola

Menentukan perintah suara/teks untuk memainkan respons

``` {.wrap}
maksud('pola'[, 'polaN'], balas('pola'))
```

Menentukan perintah suara/teks untuk memainkan respons atau melakukan tindakan
``` {.wrap}
intent('pattern'[, 'patternN'], p => { action })
```

Menentukan alternatif
``` {.wrap}
intent('frase1|frase2')
```

Menentukan kata dan frasa opsional
``` {.wrap}
intent('pola (frasa opsional|)')
```



### Fungsi respons

Memainkan respons (jika ada beberapa pola, respons dipilih secara acak)
``` {.wrap}
balas ('pola'[, 'polaN'])
```

Memainkan respons
``` {.wrap}
p.play('pattern')
```

Menetapkan pengaturan suara untuk balasan asisten: ``aksen (en, fr, de, it, ru, es)``, ``jenis kelamin (pria/wanita)``, ``jenis suara``, ``nada suara``, ``kecepatan suara``
``` {.wrap}
p.play([suara(kode, jenis kelamin, jenis, nada, kecepatan), ]'pola')
```

Menetapkan opsi pemutaran: ``force:true`` (jalankan jika tombol tidak aktif), ``activate:true`` (aktifkan tombol sebelumnya), ``deactivate:true`` (nonaktifkan tombol setelahnya)
``` {.wrap}
p.play('pattern'[, opts(options)])
```

Mengirim perintah ke aplikasi
``` {.wrap}
p.play({perintah:data})
```

### Slot yang ditentukan pengguna

Tentukan daftar statis nilai yang diharapkan dalam input

``` {.wrap}
$(SLOTNAME nilai1|nilai2) => p.SLOTNAME.value
```

Berikan label untuk mengklasifikasikan atau mengidentifikasi nilai slot

``` {.wrap}
$(NAMA SLOT nilai1 ~ label1 ~ nilai2 ~ label2) => p.NAMA SLOT.label
```

Aktifkan pencocokan fuzzy untuk menangkap varian yang serupa

``` {.wrap}
$(NAMA LOT ~ nilai1|nilai2) => p.NAMA LOT.nilai
```

Membuat slot menjadi opsional

``` {.wrap}
$(NAMA SLOT nilai1|nilai2|)
```

Menangkap beberapa nilai slot

``` {.wrap}
intent('$(SLOTNAME nilai1|nilai2) dan $(SLOTNAME nilai1|nilai2)') => p.SLOTNAME_ (array), p.SLOTNAME_[0].value, p.SLOTNAME_[1].value
```

### Slot yang telah ditentukan sebelumnya

Menangkap nilai tanggal

``` {.wrap}
$(DATE) => p.DATE.value, p.DATE.moment, p.DATE.luxon
```

Menangkap nilai waktu

``` {.wrap}
$(TIME) => p.TIME.value, p.TIME.moment
```

Menangkap angka-angka utama

``` {.wrap}
$(NUMBER) => p.NUMBER.value, p.NUMBER.number
```

Menangkap nomor urut

``` {.wrap}
$(ORDINAL) => p.ORDINAL.value, p.ORDINAL.number
```

Lokasi pengambilan gambar

``` {.wrap}
$(LOC) => p.LOC.value
```

Menangkap nama

``` {.wrap}
$(NAME) => p.NAME.value
```

### Slot dinamis

Menentukan slot dinamis di tingkat proyek

``` {.wrap}
project.name = {en: "value1|value2|value3"}
$(SLOTNAME p: nama) => p.SLOTNAME.value
```

Tentukan slot dinamis pada tingkat sesi dialog

``` {.wrap}
p.userData.name = {en: "nilai1|nilai2|nilai3"}
$(SLOTNAME u: nama) => p.SLOTNAME.value
```

Dapatkan data untuk slot dinamis dengan status visual

``` {.wrap}
let nama = ["nilai1|nilai2|nilai3"]
p.visual.data = {en: nama};
$(SLOTNAME v: nama) => p.SLOTNAME.value
```

Mendefinisikan slot dinamis dalam bentuk singkat

``` {.wrap}
project.name = {en: "value1|value2|value3"}
$(p: nama) => p.SLOTNAME.value
```

Tentukan label untuk slot dinamis: lihat [Slot yang ditentukan pengguna] (#user-defined-slots).

Mengaktifkan pencocokan fuzzy untuk slot dinamis: lihat [Slot yang ditentukan pengguna] (#user-defined-slots).

Membuat slot dinamis menjadi opsional: lihat [Slot yang ditentukan pengguna](#user-defined-slots).

Menangkap beberapa nilai slot: lihat [Slot yang ditentukan pengguna](#user-defined-slots).


### Slot RegEx

Menangkap kombinasi angka dan/atau huruf

``` {.wrap}
const reg = "([A-Za-z]{1}\\s?){6}"
$(SLOTNAME* ${reg}) => p.SLOTNAME.value
```

Menangkap setiap masukan dari pengguna

``` {.wrap}
$(SLOTNAME* .+) => p.SLOTNAME.value
```

### Konteks

Mendefinisikan sebuah konteks

``` {.wrap}
let contextName = context(() => { action })
```

Mengaktifkan sebuah konteks

``` {.wrap}
intent('pattern', p => {..., p.then(contextName)}
```

Mengoper data ke konteks

``` {.wrap}
p.then(contextName, state: {data: yourData}) => p.state.data
```

Menyelesaikan sebuah konteks

``` {.wrap}
p.resolve([data:yourData])
```


Menyetel ulang konteks

``` {.wrap}
p.resetContext()
```

Tentukan maksud yang akan dicocokkan kapan saja tanpa mengganti konteks saat ini

``` {.wrap}
intent(noctx, 'pattern', ...) atau noContext(() => {intent(...)})
```

Memainkan prompt untuk masukan yang diharapkan

``` {.wrap}
fallback('pattern1'[, 'patternN'])
```

Memberi judul sebuah konteks

``` {.wrap}
title('namaKonteks')
```

### Objek yang telah ditentukan sebelumnya

Menyimpan data statis perangkat dan data khusus pengguna yang dikirimkan dari aplikasi klien

``` {.wrap}
authData.data => p.authData.data
```

Menyimpan data status agar tersedia secara global di lingkup proyek

``` {.wrap}
project.info = {data:yourData} => project.info.data
```

Menyimpan skor kecocokan maksud

``` {.wrap}
p.score
```

Menyimpan data yang akan diteruskan antar konteks

``` {.wrap}
p.state.data
```

Menyimpan data konteks visual yang akan diteruskan dari aplikasi klien dengan ``setVisualState()``

``` {.wrap}
p.visual.data
```

Menyimpan data status khusus pengguna agar dapat diakses selama sesi dialog

``` {.wrap}
p.userData.data
```

### Panggilan balik yang telah ditentukan sebelumnya

Tentukan tindakan yang akan dilakukan ketika skrip disimpan dan model dialog dibuat

``` {.wrap}
onCreateProject(() => { action })
```

Tentukan tindakan yang akan dilakukan saat sesi dialog dimulai

``` {.wrap}
onCreateUser((p) => { action })
```

Tentukan tindakan yang akan dilakukan saat sesi dialog berakhir

``` {.wrap}
onCleanupUser((p) => { action })
```

Tentukan tindakan yang akan dilakukan saat status visual diatur

``` {.wrap}
onVisualState((p, s) => { action })
```

Tentukan tindakan yang akan dilakukan ketika peristiwa pengguna dipicu di aplikasi klien: ``buttonReady``, ``buttonClicked``, ``micPermissionPrompt``, ``micAllowed``, ``firstActivate``, ``showPopup``, ``popupCloseClicked``, ``recognized``

``` {.wrap}
onUserEvent((p, e) => { action })
```

Mendefinisikan tindakan yang akan dilakukan ketika konteks diaktifkan

``` {.wrap}
onEnter((p) => { action })
```


### Layanan Tanya Jawab

Menentukan URL sumber daya yang akan diindeks

``` {.wrap}
corpus({url: url, depth: depthLevel})
```

Tentukan korpus teks yang akan digunakan oleh asisten dalam dialog
``` {.wrap}
corpus('text')
```

### Pustaka JS bawaan

Membuat panggilan API

``` {.wrap}
axios, request
```

Bekerja dengan waktu

``` {.wrap}
moment-timezone, luxon
```

Bekerja dengan larik, angka, objek, string, dan sebagainya

``` {.wrap}
lodash
```

### Lainnya

Menyediakan daftar petunjuk untuk membantu mengenali istilah tertentu

``` {.wrap}
recognitionHints('hint'[, 'hintN'])
```

Menulis pesan info ke log Alan Studio

``` {.wrap}
console.log(data)
```

Menulis pesan kesalahan ke log Alan Studio

``` {.wrap}
console.error(data)
```

SDK Klien
----------

### Metode API Klien

Mengirimkan informasi tentang status visual dari aplikasi klien ke skrip dialog

``` {.wrap}
setVisualState(visualStateData:object)
```

Mengirim data atau melakukan tindakan tanpa perintah suara/teks

``` {.wrap}
projectAPI.method = function(p, param, callback) {
  p.userData.data = param.data;
  callback();
};

callProjectApi(method: string, data: object, callback: function)
```

Memutar pesan teks di aplikasi klien

``` {.wrap}
playText(teks:string)
```

Mengirim pesan teks ke Alan sebagai masukan dari pengguna

``` {.wrap}
sendText(teks:string)
```

Menjalankan perintah di aplikasi klien

``` {.wrap}
playCommand(perintah:objek)
```

### Metode API Klien (lanjutan)

Mengaktifkan tombol Alan secara terprogram

``` {.wrap}
mengaktifkan()
```

Menonaktifkan tombol Alan secara terprogram

``` {.wrap}
menonaktifkan()
```

Memeriksa status tombol Alan

``` {.wrap}
isActive()
```

Menghapus tombol Alan dari elemen induk, halaman (didukung di Web, Ionic)

``` {.wrap}
hapus()
```

Memeriksa status kata bangun (didukung di iOS, Android)

``` {.wrap}
getWakewordEnabled()
```

Mengatur status kata pengaktifan (didukung di iOS, Android)

``` {.wrap}
setWakewordEnabled(enabled:boolean)
```

### Penangan

// Contoh disediakan untuk platform Web

Menangani perintah yang dikirim dari skrip dialog ke aplikasi klien

``` {.wrap}
onCommand: function (commandData) { action }
```

Menangani perubahan status tombol Alan

``` {.wrap}
onButtonState: function (e) { action }
```

Menangani status koneksi ke proyek asisten virtual di Alan Cloud

``` {.wrap}
onConnectionStatus: function (e) { action }
```

Menangani peristiwa yang diterima dari Alan

``` {.wrap}
onEvent: fungsi (e) { action }
```




Lihat juga
--------

- [Situs web Alan AI](https://alan.app)
- [Tentang Platform Alan](https://alan.app/platform)
- [Dokumentasi Alan AI](https://alan.app/docs)



<style
em { font-size: 0.785em; }
strong {font-weight: 400; }
ul.collapsible > li > pre { padding-kiri: 0; padding-kanan: 0; font-size: 0.925em;}
</style>
