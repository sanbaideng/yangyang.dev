---
judul: CSS 3
tanggal: 2020-12-25 20:22:47
latar belakang: bg-[#3473b5]
tag:
    - web
    - css
    - gaya
kategori:
    - Pemrograman
intro: |
    Ini adalah lembar sontekan referensi cepat untuk kebaikan CSS, daftar sintaks pemilih, properti, unit, dan informasi berguna lainnya.
pengaya (plugin):
    - copyCode
---



Memulai
------------

### Pendahuluan {.row-span-3}
CSS kaya akan kemampuan dan lebih dari sekadar menata halaman.

#### Lembar gaya eksternal
```html {.wrap}
<link href="./path/to/stylesheet/style.css" rel="stylesheet" type="text/css">
```

#### Lembar gaya internal
```html
<style
body {
    latar-belakang-warna: linen;
}
</style>
```

#### Gaya sebaris
```html {.wrap}
<h2 style="text-align: center;">Teks di tengah</h2>

<p style="color: blue; font-size: 18px;">Biru, teks 18 poin</p>
```


### Tambahkan kelas

```html
<div class="nama kelas"></div> </div
<div class="class1 ... classn"></div>
```
Mendukung beberapa kelas pada satu elemen.



### !penting

```css
.post-title {
    color: blue !important;
}
```

Mengesampingkan semua aturan gaya sebelumnya.


### Pemilih

```css
h1 { }
#job-title { }
div.hero { }
div > p { }
```

Lihat: [Pemilih](#css-pemilih)



### Warna teks

```css
warna: #2a2aff;
warna: hijau;
color: rgb(34, 12, 64, 0.6);
color: hsla(30 100% 50% / 0.6);
```

Lihat: [Warna] (#css-warna)




### Latar Belakang

```css
background-color: biru;
background-image: url("nyan-cat.gif");
background-image: url("../image.png");
```

Lihat: [Latar Belakang](#css-latar belakang)



### Font

```css
.page-title {
    jenis huruf: tebal;
    font-size: 30px;
    font-family: "Kurir Baru";
}
```
Lihat: [Font] (#css-fonts)




### Posisi

```css
.box {
    posisi: relatif;
    top: 20px;;
    kiri: 20px;
}
```

Lihat juga: [Posisi](https://learn-the-web.algonquindesign.ca/topics/css-layout-cheat-sheet/)



### Animasi
```css

animasi: 300ms linier 0 detik tak terbatas;

animasi: pantulan 300ms linier tak terbatas;

```
Lihat: [Animasi](#css-animasi)


### Komentar
```css

/* Ini adalah komentar satu baris */

/* Ini adalah
   komentar multi-baris */
```


### Tata letak fleksibel

```css
div {
    display: flex;
    justify-content: center;
}
div {
    display: flex;
    rata kanan-kiri: rata kiri;
}
```

Lihat: [Flexbox](#css-flexbox) | [Trik Flex](#css-flexbox-tricks)




### Tata letak kisi-kisi

```css
#container {
  display: grid;
  grid: repeat(2, 60px) / mengalir otomatis 80px;
}

#container > div {
  warna latar belakang: #8ca0ff;
  width: 50px;
  height: 50px;
}
```

Lihat: [Tata Letak Kisi](#css-grid-layout)



### Variabel & Penghitung
```css
counter-set: subbagian;
counter-increment: subbagian;
penghitung-reset: subbagian 0;

:root {
  --bg-color: coklat;
}
element {
  warna-background: var(--bg-warna);
}
```

Lihat: [Konten dinamis] (#css-konten-dinamis)


Pemilih CSS
-----------


### Contoh {.row-span-2}

#### Pemilih Grup
```css
h1, h2 {
    warna: merah;
}
```
#### Pemilih Rantai
```css
h3.section-heading {
    warna: biru;
}
```
#### Pemilih Atribut
```css
div [attribute = "SomeValue"] {
    latar-belakang-warna: merah;
}
```
#### Pemilih Anak Pertama
```css
p: anak-pertama {
    font-berat: tebal;
}
```
#### No Children Selector
```css
.box:empty {
  latar belakang: kapur;
  height: 80px;;
  width: 80px;
}
```


### Dasar

| | |
|--------------|-----------------------------|
| `*` | Semua elemen
| `div` | Semua tag div |
| `.classname` | Semua elemen dengan kelas | Semua elemen dengan kelas
| `#idname` | Elemen dengan ID |
| `div,p` | Semua div dan paragraf | Semua
| `#idname *` | Semua elemen di dalam #idname |
Lihat juga: Pemilih [Tipe](https://developer.mozilla.org/en-US/docs/Web/CSS/Type_selectors) / [Kelas](https://developer.mozilla.org/en-US/docs/Web/CSS/Class_selectors) / [ID](https://developer.mozilla.org/en-US/docs/Web/CSS/ID_selectors) / [Universal](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors)


### Kombinator

| Pemilih | Deskripsi |
|-----------------|---------------------------------------|
| `div.classname` | Div dengan nama kelas tertentu |Div dengan nama kelas tertentu
| `div#idname` | Div dengan ID tertentu |

| `div > p` | Semua tag p yang berada satu tingkat di dalam div_ |
| `div + p` | Tag p segera setelah div |
| `div ~ p` | Tag P yang diawali dengan div |
Lihat juga: Pemilih [Bersebelahan](https://developer.mozilla.org/en-US/docs/Web/CSS/Adjacent_sibling_combinator) / [Bersaudara](https://developer.mozilla.org/en-US/docs/Web/CSS/General_sibling_combinator) / [Anak](https://developer.mozilla.org/en-US/docs/Web/CSS/Child_combinator)



### Pemilih atribut

| | |
|----------------------|------------------------------------|
| `a[target]` | Dengan atribut <yel>target</yel> | | | | | | | Dengan atribut <yel>target</yel> | | Dengan atribut <yel>target</yel

| `a[href^="/index"]` | Dimulai dengan <yel>/index</yel> |
| `[class|="chair"]` | Dimulai dengan <yel>kursi</yel> | | Dimulai dengan <yel>kursi</yel> |
| `[kelas*="kursi"]` | berisi <yel>kursi</yel> | | Mengandung <yel>kursi</yel> |
| `[title~="kursi"]` | Berisi kata <yel>kursi</yel> | | Berisi kata <yel>kursi</yel> | | Berisi kata <yel>kursi</yel
| `a[href$=".doc"]` | Berakhiran dengan <yel>.doc</yel> |
| `[type="button"]` | Jenis yang ditentukan | | Jenis yang ditentukan

Lihat juga: [Pemilih atribut](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors)




### Kelas-kelas semu tindakan pengguna
| | |
|--------------|-------------------------|
| `a:link ` | Tautan dalam keadaan normal | | Tautan dalam keadaan normal
| `a:active ` | Tautan dalam keadaan diklik |

| `a:visited ` | Tautan yang dikunjungi | | Tautan yang dikunjungi



### Kelas semu
| | |
|-------------------|-----------------------------------------------------------------------------------------|
| `p::after` | Menambahkan konten setelah p |
| `p::before` | Menambahkan konten sebelum p |
| `p::first-letter` | Huruf pertama pada p |
| `p::first-line` | Baris pertama dalam p |
| `::selection` | Dipilih oleh pengguna | | `p::selection` | Dipilih oleh pengguna
| `::placeholder` | Atribut [Placeholder](https://developer.mozilla.org/en-US/docs/Web/CSS/::placeholder)
| `:root` | Elemen akar dokumen | | `:root` | Elemen akar dokumen
| `:target` | Sorot jangkar yang aktif |
| `div:empty` | Elemen tanpa anak |
| `p:lang(en)` | P dengan atribut bahasa en
| `:not(span)` | Elemen yang bukan merupakan span |



### Memasukkan kelas semu
| | |
|-----------------------|---------------------------------------------------------------------------------------------|
| `input:checked` | Input yang dicentang |
| `input:disabled` | Input yang dinonaktifkan |
| `input:enabled` | Input yang diaktifkan |
| `input:focus` | Input memiliki fokus
| `input:in-range` | Nilai dalam rentang |
| `input:out-of-range` | Nilai input di luar jangkauan |
| `input:valid` | Masukan dengan nilai yang valid
| `input:invalid` | Masukan dengan nilai yang tidak valid
| `input:optional` | Tidak ada atribut yang diperlukan
| `input:required` | Masukan dengan atribut wajib
| `input:read-only` | Dengan atribut hanya-baca
| `input:read-write` | Tanpa atribut hanya-baca
| `input:indeterminate` | Dengan status [indeterminate](https://developer.mozilla.org/en-US/docs/Web/CSS/:indeterminate)



### Kelas-kelas semu struktural
| | |
|-------------------------|----------------------------|
| `p:anak-pertama` | Anak pertama |
| `p:last-child` | Anak terakhir |
| `p:first-of-type` | Anak pertama dari suatu tipe | | `p:first-of-type` | Anak pertama dari suatu tipe
| `p:last-of-type` | Anak terakhir dari beberapa tipe |
| `p:anak-ke-n(2)` | Anak kedua dari induknya
| `p:anak-ke-n(3n42)` | Rumus anak-ke-n (an + b)
| `p:anak-terakhir-ke-n(2)` | Anak kedua dari belakang |
| `p:anak-ke-n(2)` | Anak kedua dari induknya | | p:anak-ke-n(2)` | Anak kedua dari induknya
| `p:anak-terakhir-ke-n(2)` | ... dari belakang |
| `p:only-of-type` | Unik dari induknya
| `p:only-child` | Hanya anak dari induknya | | Hanya anak dari induknya



Font CSS
------


### Properties {.row-span-3}

| Properti | Deskripsi | Deskripsi
|-------------------|-----------------|
| `font-family:` | \<font> <fontN> |
| `ukuran-font:` | \<ukuran> |
| `spasi-huruf:` | \<size> |
| `ketinggian-baris:` | \<number> |

| `bobot-font:` | \<number> / tebal / normal |
| `gaya-font:` | miring / normal |
| `text-decoration:` | garis bawah / tidak ada |

| `text-align:` | left / right / center / justify |
| `text-transform:` | huruf besar / huruf besar / huruf kecil |
{.left-text}

Lihat juga: [Font](https://developer.mozilla.org/en-US/docs/Web/CSS/font)

### Singkatan {.secondary .col-span-2}

| | style | weight | ukuran (wajib) | | line-height | family |
|---------|----------|--------|-----------------|-----|-------------|-------------------|
| `font:` | `italic` | `400` | `14px` | `/` | `1.5` | `sans-serif` |
| | style | weight | size (wajib) | | line-height | family (wajib) |

### Contoh

```css
font-family: Arial, sans-serif;
ukuran huruf: 12pt;
spasi huruf: 0.02em;
```


### Case {.row-span-2}

```css

/* Halo */
text-transform: huruf besar;

/* HELLO */
text-transform: huruf besar;

/* halo */
text-transform: huruf kecil;
```


### @font-face

```css
@font-face {
    font-family: 'Glegoo';
    src: url('../Glegoo.woff');
}
```




Warna CSS
------------


### Warna yang diberi nama

```css
warna: merah;
warna: oranye;
warna: cokelat;
warna: rebeccapurple;
```


### Warna heksadesimal

```css
warna: #090;
warna: #009900;
warna: #090a;
warna: #009900aa;
```



### rgb() Warna

```css
color: rgb(34, 12, 64, 0.6);
color: rgba(34, 12, 64, 0.6);
color: rgb(34 12 64 / 0.6);
color: rgba(34 12 64 / 0.3);
color: rgb(34.0 12 64 / 60%);
color: rgba(34.6 12 64 / 30%);
```


### Warna HSL

```css
color: hsl(30, 100%, 50%, 0.6);
color: hsla(30, 100%, 50%, 0.6);
color: hsl(30 100% 50% / 0.6);
color: hsla(30 100% 50% / 0.6);
color: hsl(30.0 100% 50% / 60%);
color: hsla(30.2 100% 50% / 60%);
```

### Lain-lain
```css
color: mewarisi;
color: inisial;
color: unset;
warna: transparan;

color: currentcolor; /* kata kunci */
```







Latar Belakang CSS
----------

### Properties {.row-span-2}

| Properti | Deskripsi | Deskripsi
|---------------|---------------|
| `latar belakang:` | _(Singkatan)_ | |

| `warna-latar:` | Lihat: 
| `gambar-latar:` | url(...) |
| `posisi-latar:` | kiri/tengah/kanan<br />atas/tengah/bawah |
| `background-size:` | cover X Y |
| `klip-latar:` | kotak-batas<br/>kotak-pengisi<br/>kotak-isi |
| `background-repeat:` | no-repeat<br />repeat-x<br />repeat-y |
| `latar-lampiran:` | gulir/tetap/lokal |
{.left-text}

### Singkatan {.secondary .col-span-2}

| | warna | gambar | posisiX | posisiY | | ukuran | ulangi | lampiran |
|---------------|--------|--------------|-----------|-----------|-----|----------------|-------------|------------|
| `background:` | `#ff0` | `url(a.jpg)` | `kiri` | `top` | `/` | `100px` `auto` | `non-repeat` | `tetap;` |
| `background:` | `#abc` | `url(b.png)` | `center` | `center` | `/` | `cover` | `repeat-x` | `local;` | |
| | color | image | posX | posY | | size | repeat | attach ..   |

### Contoh {.col-span-2}

```css {.wrap}
latar belakang: url(img_man.jpg) tidak ada pengulangan di tengah;

latar belakang: url(img_flwr.gif) kanan bawah tanpa pengulangan, url(paper.gif) kiri atas pengulangan;

background: rgb(2,0,36);
background: linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(13,232,230,1) 35%, rgba(0,212,255,1) 100%);
```




CSS Model Kotak
------------


### Maksimum/Minimum

```css
.column {
    max-width: 200px;
    width: 500px;
}
```
Lihat juga: [max-lebar](https://developer.mozilla.org/en-US/docs/Web/CSS/max-width) / [min-lebar](https://developer.mozilla.org/en-US/docs/Web/CSS/min-width) / [max-tinggi](https://developer.mozilla.org/en-US/docs/Web/CSS/max-height) / [min-tinggi](https://developer.mozilla.org/en-US/docs/Web/CSS/min-height)



### Margin / Padding

```css
.block-one {
    margin: 20px;
    padding: 10px;
}
```
Lihat juga: [Margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) / [Padding](https://developer.mozilla.org/en-US/docs/Web/CSS/padding)


### Ukuran kotak

```css
.container {
    ukuran-kotak: kotak-batas;
}
```
Lihat juga: [Ukuran kotak](https://developer.mozilla.org/en-US/docs/Web/CSS/Box-sizing)



### Visibilitas

```css
.invisible-elements {
    visibilitas: tersembunyi;
}
```
Lihat juga: [Visibilitas](https://developer.mozilla.org/en-US/docs/Web/CSS/visibility)


### Kata kunci otomatis

```css
div {
    margin: auto;
}
```
Lihat juga: [Margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin)


### Melimpah

```css
.small-block {
    melimpah: gulir;
}
```
Lihat juga: [Melimpah](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow)




Animasi CSS {.cols-5}
---------


### Singkatan {.col-span-5 .secondary}

| | nama | durasi | fungsi-waktu | penundaan | hitungan | arah | mode-pengisian | status-pemutaran |
|--------------|----------|----------|-----------------|---------|------------|---------------------|-----------|------------|
| `animasi:` | `pantulan` | `300ms` | `linier` | `100ms` | `tak terbatas` | `bolak-balik` | `keduanya` | `membalikkan` |
| | nama | durasi | fungsi-waktu | penundaan | hitungan | arah | mode-pengisian | status-pemutaran |

### Properties {.row-span-2 .col-span-2}

| Properti | Nilai |
|------------------------------|--------------------------------------------------------|
| `animasi:` | _(singkatan)_ | |
| `nama-animasi:` | \<nama> |
| `durasi-animasi:` | \<waktu>ms |
| `fungsi-pengaturan-waktu:` | kemudahan / linear / kemudahan masuk / kemudahan keluar / kemudahan keluar |
| `jeda-animasi:` | \<time>ms |
| `jumlah-iterasi-animasi:` | tak terbatas / \<number> |
| `animation-direction:` | normal / reverse / alternate / alternate-reverse |
| `animation-fill-mode:` | tidak ada / maju / mundur / keduanya / awal / mewarisi |
| `animation-play-state:` | normal / reverse / alternate / alternate-reverse |
{.left-text}

Lihat juga: [Animasi](https://developer.mozilla.org/en-US/docs/Web/CSS/animation)


### Contoh {.col-span-3}

```css
/* @keyframe durasi | fungsi-waktu | penundaan |
   jumlah-iterasi | arah | mode-pengisian | status-pemutaran | nama */
animasi: 3 detik mudah masuk 1 detik 2 mundur kedua jeda geser;

/* @keyframes duration | timing-function | delay | name */
animasi: 3s linear 1s slidein;

/* @keyframes durasi | nama */
animasi: 3s slidein;

animasi: 4s linear 0s infinite alternate move_eye;
animasi: pantulan 300ms linear 0s infinite normal;
animasi: pantulan 300ms linier tak terbatas;
animasi: pantulan 300ms linier tak terbatas bergantian-balik;
animasi: memantul 300ms linear 2s tak terbatas bolak-balik maju normal;
```

### Javascript Event {.col-span-3}

```js
.one('webkitAnimasiAkhir oanimasiAkhir msAnimasiAkhir animasiAkhir')
```



CSS Flexbox {.cols-2}
-------


### Contoh sederhana

```css
.container {
  display: flex;
}
```

```css
.container > div {
  flex: 1 1 auto;
}
```

### Container {.row-span-2}

.container {

```css
  display: flex;
  display: inline-flex;
```

```css
  flex-direction: row; /* ltr - default */
  flex-direction: row-reverse; /* rtl */
  flex-direction: column; /* top-bottom */
  flex-direction: column-reverse; /* bottom-top */
```

```css
  flex-wrap: nowrap; /* satu baris */
  flex-wrap: wrap; /* banyak baris */
```

```css
  align-items: flex-start; /* rata kanan atas */
  align-items: flex-end; /* rata kanan-kiri vertikal ke bawah */
  align-items: center; /* rata kiri-kanan ke tengah */
  align-items: stretch; /* tinggi yang sama pada semua (default) */
```

```css
  justify-content: flex-start; /* [xxx ] */
  justify-content: center; /* [ xxx ] */
  justify-content: flex-end; /* [ xxx ] */
  justify-content: spasi-between; /* [x x x] */
  justify-content: spasi-sekitar; /* [ x x x ] */
  justify-content: spasi-merata; /* [ x x x ] */
```

}

### Anak

.container > div {

```css
  /* Ini: */
  flex: 1 0 auto;

  /* Setara dengan ini: */
  flex-tumbuh: 1;
  flex-shrink: 0;
  flex-basis: auto;
```

```css
  order: 1;
```

```css
  align-self: flex-start; /* left */
  margin-kiri: auto; /* kanan */
```

}


Trik CSS Flexbox
--------------

### Pusat vertikal

```css
.container {
  display: flex;
}

.container > div {
  width: 100px;
  height: 100px;
  margin: auto;
}
```

### Pusat vertikal (2)

```css
.container {
  display: flex;

  /* vertikal */
  align-items: center;

  /* horizontal */
  justify-content: center;
}
```

### Menyusun ulang

```css
.container > .top {
 order: 1;
}

.container > .bottom {
 order: 2;
}
```

### Tata letak seluler


```css
.container {
  display: flex;
  arah-lentur: kolom;
}

.container > .top {
  flex: 0 0 100px;
}

.container > .content {
  flex: 1 0 auto;
}
```

Bilah atas dengan tinggi tetap dan area konten dengan tinggi dinamis.

### Tabel-seperti {.col-span-2}

```css

.container {
  display: flex;
}


/* nilai 'px' di sini hanyalah persentase yang disarankan */
.container > .checkbox { flex: 1 0 20px; }
.container > .subject { flex: 1 0 400px; }
.container > .date { flex: 1 0 120px; }
```

Ini membuat kolom yang memiliki lebar berbeda, namun ukurannya sesuai
sesuai dengan keadaan.

### Vertikal


```css
.container {
  align-items: center;
}
```

Memusatkan semua item secara vertikal.

### Kiri dan kanan {.col-span-2}

```css
.menu > .left { align-self: flex-start; }
.menu > .right { align-self: flex-end; }
```




Tata Letak Kisi CSS
------------


### Kolom Template Kisi

```css
#kisi-kisi-wadah {
    display: grid;
    width: 100px;
    kolom-kolom templat-kisi: 20px 20% 20% 60%;
}
```


### fr Satuan Relatif

```css
.grid {
    display: grid;
    width: 100px;
    kolom-kolom templat-kisi: 1fr 60px 1fr;
}

```


### Grid Gap

```css
/* Jarak antar baris adalah 20px*/
/* Jarak antar kolom adalah 10px*/
#grid-container {
    display: grid;
    jarak-kisi: 20px 10px;
}
```


### Kisi-kisi Tingkat Blok CSS

```css
#grid-container {
    display: blok;
}
```


### Baris kisi-kisi CSS

Sintaks CSS:
- grid-baris: grid-baris-awal / grid-baris-akhir;
#### Contoh
```css
.item {
    grid-baris: 1 / span 2;
}
```


### Kisi Tingkat Sebaris CSS

```css
#grid-container {
    display: inline-grid;
}
```


### minmax() Fungsi

```css {.wrap}
.grid {
    display: kisi-kisi;
    kolom-kolom templat-kisi: 100px minmax(100px, 500px) 100px;
}

```


### grid-baris-awal & grid-baris-akhir

Sintaks CSS:
- grid-baris-mulai: auto|baris-baris;<br>
- grid-baris-akhir: auto|baris-baris|span n;

#### Contoh
```css
grid-row-start: 2;
grid-baris-akhir: rentang 2;
```


### CSS celah-baris-kisi

```css
grid-row-gap: length;
```
Nilai panjang yang sah, seperti px atau %. 0 adalah nilai default


### Area kisi-kisi CSS

```css
.item1 {
    area-kisi: 2 / 1 / span 2 / span 3;
}
```


### Membenarkan Item

```css
#container {
    display: grid;
    justify-items: center;
    kolom-kolom template-grid: 1fr;
    grid-template-baris: 1fr 1fr 1fr 1fr;
    grid-gap: 10px;
}
```

### CSS grid-template-areas

```css
.item {
    grid-area: nav;
}
.grid-container {
    display: grid;
    area-template-kisi-kisi:
    'nav nav . .'
    'nav nav . .';
}
```


### Membenarkan diri sendiri

```css
#grid-container {
    display: grid;
    justify-items: start;
}

.grid-items {
    justify-self: end;
}
```
Item kisi diposisikan di sebelah kanan (akhir) baris.

### Meratakan Item

```css
#container {
    display: grid;
    align-items: start;
    kolom-kolom template-grid: 1fr;
    grid-template-baris: 1fr 1fr 1fr 1fr;
    grid-gap: 10px;
}
```



Konten Dinamis CSS
------------

### Variabel

Mendefinisikan Variabel CSS
```css
:root {
  --warna pertama: #16f;
  --warna-kedua: #ff7;
}
```
Penggunaan Variabel
```css
#firstParagraph {
  warna-background: var(--warna-pertama);
  warna: var(--warna-kedua);
}
```
Lihat juga: [Variabel CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

### Penghitung

```css
/* Set "my-counter" menjadi 0 */
counter-set: my-counter;
```

```css
/* Menambah "penghitung-saya" dengan 1 */
kenaikan-counter: penghitung-saya;
```

```css
/* Pengurangan "penghitung-ku" dengan 1 */
counter-increment: my-counter -1;
```

```css
/* Setel ulang "penghitung-ku" ke 0 */
counter-reset: my-counter;
```

Lihat juga: [Set penghitung](https://developer.mozilla.org/en-US/docs/Web/CSS/counter-set)

### Menggunakan penghitung
```css
body { counter-reset: section; }

h3::before {
  counter-penambahan: bagian;
  konten: "Bagian." counter (bagian);
}
```

```css
ol {
  counter-reset: bagian;
  tipe-daftar-penanda: tidak ada;
}

li::before {
  penghitung-penambahan: bagian;
  konten: penghitung (bagian, ".") " ";
}
```


Trik Css 3
------------

### Bilah gulir halus
```css
html {
    perilaku gulir: halus;
}
```
[Klik saya] (#css-memulai), halaman akan bergulir dengan mulus ke Memulai




Lihat juga {.cols-1}
---------

- [Lembar contekan pemilih CSS](https://frontend30.com/css-selectors-cheatsheet/) _(frontend30.com)_
- [MDN: Menggunakan CSS flexbox](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Flexible_boxes)
- [Lembar contekan flexbox utama](http://www.sketchingwithcss.com/samplechapter/cheatsheet.html)
- [GRID: Lembar kerja visual yang sederhana](http://grid.malven.co/)
- [Trik CSS: Panduan Lengkap untuk Grid](https://css-tricks.com/snippets/css/complete-guide-grid/)
- [Dukungan peramban](https://caniuse.com/#feat=css-grid)
