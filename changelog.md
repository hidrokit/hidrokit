---
layout: default
title: "Changelog"
description: dokumentasi perubahan proyek hidrokit
# show_add_button: false
---
# Changelog
Seluruh perubahan penting pada proyek ini akan didokumentasikan pada berkas ini.

Penulisan diadaptasi dari [Keep a Changelog](https://keepachangelog.com/id-ID/1.0.0/), dan proyek ini menggunakan penomoran [versi Semantik](https://semver.org/lang/id/spec/v2.0.0.html). 

---
## 10 Juni 2019 - v0.1.2
Modul baru `.datakit` digunakan untuk analisis dan penambahan fungsi `.dlkit.table_timesteps()` untuk mebangkitkan tabel _timesteps_ langsung dari `pandas.DataFrame`. Perubahan signifikan untuk dokumentasi non-teknis. Dokumentasi dapat diakses melalui halaman [hidrokit] atau [hidrokit-nb].
- **Penambahan**
  - modul `.datakit`.
  - fungsi `.dlkit.table_timesteps()`.
  - argumen baru pada fungsi `.dlkit.multi_column_timesteps()` untuk menyesuaikan fungsi `.dlkit.table_timesteps()`.
- **Dokumentasi - d0.1.2**
  - perubahan templat untuk isu dan PR.
  - tambah dokumen _changelog_.
  - memindahkan _notebook_ ke _repo_ [`hidrokit-nb`](https://github.com/taruma/hidrokit-nb).

---
## 14 Mei 2019 - v0.1.1
Ditambahnya modul baru bernama `dlkit` untuk membantu proses _deep learning_ pada permasalahan _time series_. Modul ini digunakan dalam membuat tabel _timesteps_. 
- **Penambahan**
  - modul `.dlkit`.

---
## 9 Januari 2019 - v0.1.0
Mengikuti standar distribusi paket Python (PyPI). Memperbaiki dokumentasi komunitas (README, Kode etik). Mengalihkan dokumentasi non-teknis ke halaman wiki.
- **Penambahan**
  - Mengubah `hidrokit` sebagai paket python.
  - Distribusi `hidrokit` melalui PyPI.
- **Dokumentasi**
  - Perubahan berkas README.
  - Templat isu
  - Kode etik menggunakan _Contributor Covenant_ berbahasa Indonesia.
  - Mengacu halaman wiki untuk panduan kontribusi.

---
## 5 Januari 2019 - v0.0.0
Memulai menandai pengembangan awal `hidrokit` yang masih berupa _module_ python. 
- **Penambahan**
  - `hidrokit` sebagai _module_.
  - Dokumentasi proyek (readme, contributing, etc.).
  - _notebook_ penggunaan `hidrokit`.

---
## 20 Oktober 2018 - n/a
Dibuatnya _repository_ `hidrokit`.
- **Penambahan**
  - Membuat _repository_ di GitHub.

---
# Daftar Padanan Kata
Daftar padanan kata yang digunakan dalam berkas catatan perubahan ini:

| Istilah      | Padanan Kata |
| ------------ | ------------ |
| _Changelog_  | Rekam Ubahan |
| _Added_      | Penambahan   |
| _Changed_    | Perubahan    |
| _Deprecated_ | Penghilangan |
| _Fixed_      | Perbaikan    |
| _Security_   | Keamanan     |
| _Unreleased_ | Belum Rilis  |

Padanan kata belum tentu sesuai kaidah ejaan Bahasa Indonesia.

[hidrokit]: https://taruma.github.io/hidrokit
[hidrokit-nb]: https://taruma.github.io/hidrokit-nb