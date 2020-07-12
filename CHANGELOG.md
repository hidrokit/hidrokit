# Changelog
Seluruh perubahan penting pada proyek ini akan didokumentasikan pada bilah ini. Dokumentasi ini hanya untuk perubahan pada paket python.

Changelog ini sudah kadaluarsa dan belum diperbarui lagi.

Penulisan diadaptasi dari [Keep a Changelog](https://keepachangelog.com/id-ID/1.0.0/), dan proyek ini menggunakan penomoran [versi Semantik](https://semver.org/lang/id/spec/v2.0.0.html). 

---

## Belum Rilis

---

## Telah Rilis
### 11 Juli 2019 - v0.2.0
Ini merupakan perubahan sangat signifikan dari versi sebelumnya dan dimulainya penggunaan layanan integrasi dan _code review_. Perubahan nama fungsi dan modul sangat signifikan sehingga fungsi/metode yang digunakan sebelumnya tidak berfungsi sama sekali (***no backward-compatibility***). Rilis ini disertakan dengan dirilisnya website untuk [hidrokit] dan [hidrokit-nb]. 

**Baru**
- Penamaan modul dan fungsi yang lebih mudah dibaca dan diingat. 
- Paket dibagi menjadi tiga bagian utama yaitu persiapan (`prep`), analisis (`analysis`), dan visualisasi (`viz`). Penamaan modul dan fungsi juga diubah dan disesuaikan dengan standar agar lebih jelas dan mudah diingat.
  - Modul untuk membaca data dan manipulasi data seperti `dlkit`, `datakit`, `prepkit` akan dibawah modul `prep` dan digantikan namanya menjadi `timeseries`, `read`, `excel`.
  - Modul untuk menampilkan data seperti `viewkit` dan fungsi plot dari `dlkit` akan dibawah modul `viz` dan berganti nama menjadi `table` dan `graph`. 
  - Beberapa nama fungsi juga berubah menjadi lebih jelas seperti `datakit.dict_null_data` menjadi `prep.read.missing_row()`. 
- Integrasi [travis-ci], [codecov], [codacy].
- Testing menggunakan pytest dengan target 90% _coverage_.
- Rilisnya website [hidrokit] dan [hidrokit-nb] yang telah disertai panduan berkontribusi dan mengenai proyek pada umumnya. 

**Perbaikan**
- Dokumentasi [hidrokit.readthedocs.io] diperbaiki dengan membagi menjadi tiga halaman yaitu data preparation, data analysis, dan data visualization.

**Penghilangan**
- Modul `bmkgkit` dihapuskan dan belum ada penggantinya.
- Modul berikut ini telah dihapus/digantikan sehingga tidak akan digunakan lagi:
  - `dlkit`, `viewkit`, `bmkgkit`, `prepkit`, `datakit`.

[travis-ci]: https://travis-ci.com
[codecov]: https://codecov.io/
[codacy]: https://www.codacy.com/

---

### 25 Juni 2019 - v0.1.3
Versi ini fokus ke dokumentasi teknis. Dari versi ini, hidrokit memiliki dokumentasi teknis otomatis yang dibuat menggunakan sphinx dan readthedocs. Situsnya adalah [hidrokit.readthedocs.io].
- **Penambahan**
  - Situs dokumentasi teknis di [readthedocs](https://hidrokit.rtfd.io).
  - `docstring` untuk setiap metode.

### 10 Juni 2019 - v0.1.2
Modul baru `.datakit` digunakan untuk analisis dan penambahan fungsi `.dlkit.table_timesteps()` untuk mebangkitkan tabel _timesteps_ langsung dari `pandas.DataFrame`. Perubahan signifikan untuk dokumentasi non-teknis. Dokumentasi dapat diakses melalui halaman [hidrokit] atau [hidrokit-nb].
- **Penambahan**
  - modul `.datakit`.
  - fungsi `.dlkit.table_timesteps()`.
  - argumen baru pada fungsi `.dlkit.multi_column_timesteps()` untuk menyesuaikan fungsi `.dlkit.table_timesteps()`.
- **Dokumentasi - d0.1.2**
  - perubahan templat untuk isu dan PR.
  - tambah dokumen _changelog_.
  - memindahkan _notebook_ ke _repo_ [`hidrokit-nb`](https://github.com/taruma/hidrokit-nb).

### 14 Mei 2019 - v0.1.1
Ditambahnya modul baru bernama `dlkit` untuk membantu proses _deep learning_ pada permasalahan _time series_. Modul ini digunakan dalam membuat tabel _timesteps_. 
- **Penambahan**
  - modul `.dlkit`.

### 9 Januari 2019 - v0.1.0
Mengikuti standar distribusi paket Python (PyPI). Memperbaiki dokumentasi komunitas (README, Kode etik). Mengalihkan dokumentasi non-teknis ke halaman wiki.
- **Penambahan**
  - Mengubah `hidrokit` sebagai paket python.
  - Distribusi `hidrokit` melalui PyPI.
- **Dokumentasi**
  - Perubahan berkas README.
  - Templat isu
  - Kode etik menggunakan _Contributor Covenant_ berbahasa Indonesia.
  - Mengacu halaman wiki untuk panduan kontribusi.

### 5 Januari 2019 - v0.0.0
Memulai menandai pengembangan awal `hidrokit` yang masih berupa _module_ python. 
- **Penambahan**
  - `hidrokit` sebagai _module_.
  - Dokumentasi proyek (readme, contributing, etc.).
  - _notebook_ penggunaan `hidrokit`.

### 20 Oktober 2018 - n/a
Dibuatnya _repository_ `hidrokit`.
- **Penambahan**
  - Membuat _repository_ di GitHub.

---

[hidrokit]: https://taruma.github.io/hidrokit
[hidrokit-nb]: https://taruma.github.io/hidrokit-nb
[hidrokit.readthedocs.io]: https://hidrokit.rtfd.io
