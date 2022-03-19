# Changelog
Seluruh perubahan penting pada proyek ini akan didokumentasikan pada bilah ini. Dokumentasi ini hanya untuk perubahan pada paket python.

Penulisan diadaptasi dari [Keep a Changelog](https://keepachangelog.com/id-ID/1.0.0/), dan proyek ini menggunakan penomoran [versi Semantik](https://semver.org/lang/id/spec/v2.0.0.html) dengan catatan setiap perubahan pada subpaket `.contrib` yang berubah hanya _patch version_. 

---

## Belum Rilis

**Added/Ditambahkan**
- Penambahan modul `.contrib.taruma`:
  - #102 `hk102`: upsampling dataset
  - #151 `hk151`: uji outlier
  - #158 `hk158`: perhitungan parameter statistik
  - Modul Uji Kecocokan Distribusi:
    - #140 `hk140`: uji kolmogorov-smirnov
    - #141 `hk141`: uji chi-square
  - Modul Analisis Frekuensi:
    - #124 `hk124`: distribusi log normal 2 parameter
    - #126 `hk126`: distribusi log pearson tipe III
    - #127 `hk127`: distribusi gumbel
    - #172 `hk172`: distribusi normal
  - #179 Fungsi CDF `.calc_prob()` untuk setiap analisis frekuensi.

**Fixed/Diperbaiki**
- #169 Perbaikan fungsi test `test_prep_excel.test__dataframe_table()`.
- #115 Penambahan argumen `verbose=False` pada modul `.contrib.taruma.hk98`.
- #162 Pembaruan fungsi `.contrib.taruma.hk88.read_workbook()` untuk membaca seluruh _sheet_ tanpa memasukan nama stasiun/_sheet_. 

**Changed/Diubah**
- #162 Luaran argumen `as_df=False` pada fungsi `.contrib.taruma.hk88.read_workbook()` berubah dari luaran berupa `list` menjadi `dictionary`. 

---

## Telah Rilis

### 2020-07-13 - 0.3.6

**Fixed/Diperbaiki**
- Perbaikan argumen `keep_first=False` pada fungsi `timeseries.timestep_table()`.

### 2020-01-15 - 0.3.5

**Added/Ditambahkan**
- Penambahan modul `.contrib.taruma`:
  - `hk87`: perhitungan debit andalan menggunakan kurva durasi debit
  - `hk88`: ambil dataset hujan harian dari excel
  - `hk89`: pemodelan NRECA
  - `hk90`: kalibrasi model (NRECA/FJMOCK)
  - `hk99`: perhitungan curah hujan dengan metode poligon thiessen
  - `hk98`: rekap dataset deret waktu
  - `hk96`: pemodelan F.J. Mock
  - `hk102`: upsampling dataset
  - `hk106`: perhitungan evapotranspirasi

### 2019-12-09 - 0.3.4

**Added/Ditambahkan**
- Penambahan modul `.contrib.taruma`:
  - `hk84`: meringkas informasi data hujan jam-jaman

### 2019-11-30 - 0.3.3

**Added/Ditambahkan**
- Penambahan modul `.contrib.taruma`:
  - `hk79`: mengekstrak informasi data jam-jaman dari excel
- Penambahan `makefile` untuk memudahkan publikasi

**Changed/Diubah**
- Memperbaiki file sitasi (.cff)
- Memperbaiki pemanggilan `hidrokit.__version__`
- Memperbaiki _lint_, yaitu baris yang terlalu panjang
- 

### 2019-10-15 - 0.3.2

**Added/Ditambahkan**
- Penambahan subpaket `.contrib.taruma` dengan modul sebagai berikut:
  - `.hk43`: ubah pivot table ke dataframe
  - `.hk53`: buat table/tensor untuk pemodelan deep learning LSTM
  - `.hk73`: mengolah berkas dari bmkg
- Penambahan subpaket `.contrib` yang digunakan untuk tempat khusus kontributor tanpa pengecekan CI.
- Penambahan file .cff untuk sitasi dan pembacaan oleh zenodo.

**Changed/Diubah**
- Perubahan penulisan _tag_ yang berawal dari "v0.3.2" menjadi "0.3.2". Terkait pembacaan otomatis oleh Zenodo.

---
### 2019-07-26 - v0.2.1

**Changed/Diubah**
- Added/Ditambahkan argumen `template=` pada fungsi `prep.timeseries.timestep_table`
- Changed/Diubah penggunaan f-string menjadi `.format` terkait kompatibilitas dengan python 3.5
- Changed/Diubah konfigurasi codecov.
- Changed/Diubah konfigurasi travis-ci. Added/Ditambahkan pemeriksaan dengan python 3.5.  


### 2019-07-11 - v0.2.0

**Added/Ditambahkan**
- Penamaan modul dan fungsi yang lebih mudah dibaca dan diingat. 
- Paket dibagi menjadi tiga bagian utama yaitu persiapan (`prep`), analisis (`analysis`), dan visualisasi (`viz`). Penamaan modul dan fungsi juga diubah dan disesuaikan dengan standar agar lebih jelas dan mudah diingat.
  - Modul untuk membaca data dan manipulasi data seperti `dlkit`, `datakit`, `prepkit` akan dibawah modul `prep` dan digantikan namanya menjadi `timeseries`, `read`, `excel`.
  - Modul untuk menampilkan data seperti `viewkit` dan fungsi plot dari `dlkit` akan dibawah modul `viz` dan berganti nama menjadi `table` dan `graph`. 
  - Beberapa nama fungsi juga berubah menjadi lebih jelas seperti `datakit.dict_null_data` menjadi `prep.read.missing_row()`. 
- Integrasi travis-ci, codecov, codacy.
- Testing menggunakan pytest dengan target 90% _coverage_.
- Rilisnya website [hidrokit] dan [hidrokit-nb] yang telah disertai panduan berkontribusi dan mengenai proyek pada umumnya. 

**Fixed/Diperbaiki**
- Dokumentasi [hidrokit.readthedocs.io] diperbaiki dengan membagi menjadi tiga halaman yaitu data preparation, data analysis, dan data visualization.

**Removed/Dihilangkan**
- Modul `bmkgkit` dihapuskan dan belum ada penggantinya.
- Modul berikut ini telah dihapus/digantikan sehingga tidak akan digunakan lagi:
  - `dlkit`, `viewkit`, `bmkgkit`, `prepkit`, `datakit`.

---
### 2019-06-25 - v0.1.3

**Added/Ditambahkan**
- Situs dokumentasi teknis di [readthedocs](https://hidrokit.rtfd.io).
- `docstring` untuk setiap metode.

### 2019-06-10 - v0.1.2

**Added/Ditambahkan**
- modul `.datakit`.
- fungsi `.dlkit.table_timesteps()`.
- argumen baru pada fungsi `.dlkit.multi_column_timesteps()` untuk menyesuaikan fungsi `.dlkit.table_timesteps()`.

**Dokumentasi - d0.1.2**
- Changed/Diubah templat untuk isu dan PR.
- tambah dokumen _changelog_.
- memindahkan _notebook_ ke _repo_ [`hidrokit-nb`](https://github.com/taruma/hidrokit-nb).

### 2019-05-14 - v0.1.1

**Added/Ditambahkan**
- modul `.dlkit`.

### 2019-01-09 - v0.1.0

**Added/Ditambahkan**
- Mengubah `hidrokit` sebagai paket python.
- Distribusi `hidrokit` melalui PyPI.

**Dokumentasi**
- Changed/Diubah berkas README.
- Templat isu
- Kode etik menggunakan _Contributor Covenant_ berbahasa Indonesia.
- Mengacu halaman wiki untuk panduan kontribusi.

### 2019-01-05 - v0.0.0

**Added/Ditambahkan**
- `hidrokit` sebagai _module_.
- Dokumentasi proyek (readme, contributing, etc.).
- _notebook_ penggunaan `hidrokit`.

### 2018-10-20 - n/a

**Added/Ditambahkan**
- Membuat _repository_ di GitHub.

---

[hidrokit]: https://hidrokit.github.io/hidrokit
[hidrokit-nb]: https://hidrokit.github.io/notebook
[hidrokit.readthedocs.io]: https://hidrokit.rtfd.io