---
layout: default
title: Situs
parent: Berkontribusi
permalink: /berkontribusi/situs
nav_order: 3
---

<div align="justify" markdown="1">
> "Anyone who has never made a mistake has never tried anything new" - Albert Einstein.
{: .text-delta}
</div>

Halaman ini mempersiapkan diri Anda untuk berkontribusi dalam situs.

---

# DAFTAR ISI
{: .no_toc .text-delta}

1. TOC
{:toc}

---

Situs hidrokit dan hidrokit-nb dibuat menggunakan Jekyll & GitHub Pages dengan menggunakan `remote-theme` dari Just the Docs oleh Patrick Marsceill. Disarankan untuk **membaca** manual penggunaan tema di [Just the Docs](https://pmarsceill.github.io/just-the-docs/) agar mengetahui fitur yang tersedia.

Dianjurkan untuk melakukan instalasi pada mesin lokal sebelum melakukan pull request agar memudahkan saat melakukan pengembangan/perbaikan. Baca bagian [instalasi lokal](#Instalasi-lokal) untuk lebih lanjut.

Untuk memulai kontribusi dalam situs, berikut yang harus dipersiapkan/diketahui:
- Terbiasa dengan penulisan Markdown, HTML, dan CSS.
- Sudah memasang/instalasi Ruby, Jekyll, dan Bundler.
- Mengetahui menggunakan Jekyll (*front matter* dan *_config.yml*)
- Diasumsikan sudah memahami menggunakan Git dan Github.

## Struktur Direktori

```
+hidrokit@gh-pages // +hidrokit-nb/docs
|   Gemfile
|   index.md
|   README.md
|   _config.yml
|   _config_local.yml
|   
+---assets
|   +---images
|   |   +---favicon
|   |   \---panduan
|   \---js
|           
\---halaman

```

Keterangan:
- `Gemfile`: file Gem yang digunakan untuk instalasi Jekyll.
- `index.md`: halaman depan situs.
- `_config.yml`: konfigurasi yang digunakan saat _deployment_ di GitHub.
- `_config_local.yml`: konfigurasi yang digunakan untuk mesin lokal.
- `assets/`: _Media Directory_ | Direktori khusus penyimpanan media.
  - `images/`: berisikan media gambar yang digunakan untuk situs.
  - `js/`: berisikan file yang digunakan untuk fitur pencarian di situs.
- `halaman/`: _Page Directory_ | Direktori khusus untuk seluruh halaman dalam situs.

Direktori/files bisa ditambahkan jika diperlukan.

## Instalasi lokal

Langkah ini tidak jauh berbeda dengan yang ada di halaman [Just the Docs](https://pmarsceill.github.io/just-the-docs/). Diasumsikan bahwa Ruby beserta Jekyll dan Bundler sudah terinstalasi, jika belum baca [Quickstart](https://jekyllrb.com/docs/) untuk informasi lebih lanjut.

1. Buka *command prompt/terminal*, pastikan sudah berada di direktori `hidrokit` cabang `gh-pages` atau `hidrokit-nb/docs/`. Masukan perintah berikut untuk melakukan instalasi:
```bash
$ bundle install
```

2. Jalankan server lokal dengan menggunakan konfigurasi lokal.

```bash
$ bundle exec jekyll serve --config _config_local.yml
```

3. Buka browser dan masukkan halaman [http://localhost:4000](http://localhost:4000)

4. *(Opsional)* Memperbarui file index untuk fitur pencarian.

```bash
$ bundle exec just-the-docs rake search:init
```

### Memeriksa kondisi Jekyll site

Sebelum melakukan _pull request_, hasil ubahan Anda bisa di cek menggunakan gem [html-proofer](https://github.com/gjtorikian/html-proofer). Sangat disarankan melakukan langkah ini terlebih dahulu sebelum meminta penggabungan. Travis-ci melakukan pengecekan dengan metode ini.

1. Dari terminal, _build_ situs anda dengan perintah:

```bash
$ bundle exec jekyll build --config _config_local.yml
```
Pastikan menggunakan `_config_local.yml` karena `_config.yml` hanya digunakan untuk GitHub-Pages.

2. Periksa kondisi hasilnya dengan menulis perintah:

```bash
$ bundle exec htmlproofer ./_site --assume-extension --disable-external
```
Hasil _build_ dianggap baik jika tidak ada pesan error.

Jika sukses, lakukan _pull request_. ✨
