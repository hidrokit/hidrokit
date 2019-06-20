---
title: "hidrokit"
description: paket python untuk analisis hidrologi
---
<div align="center">
  <img src="https://github.com/taruma/hidrokit/wiki/logo/hidrokit-400x100-trans.png"><br>
</div>
--------

# hidrokit: analisis hidrologi dengan python
[![PyPI](https://img.shields.io/pypi/v/hidrokit.svg)](https://pypi.org/project/hidrokit/)
[![GitHub](https://img.shields.io/github/license/taruma/hidrokit.svg)](/LICENSE)
[![Maintenance](https://img.shields.io/maintenance/yes/2019.svg)](#hidrokit)

`hidrokit` adalah proyek _open source_ paket *python* yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data, analisis data, dan visualisasi data.

# Status Pengembangan
[![GitHub release](https://img.shields.io/github/release/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date/taruma/hidrokit.svg)](#status-pengembangan)
[![GitHub last commit](https://img.shields.io/github/last-commit/taruma/hidrokit.svg)](#status-pengembangan)
[![GitHub issues](https://img.shields.io/github/issues/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/pulls)

Status pengembangan `hidrokit` dan _roadmap_ tersedia di [**papan Trello**](https://trello.com/b/Ii8Z5BRm/hidrokit-project). Tertarik berkontribusi? Baca bagian [kontributor](#untuk-kontributor).

--------
# *Module* pada Hidrokit

Hidrokit terdiri dari beberapa *module* yang memiliki fungsi masing-masing. Berikut *module* yang telah tersedia pada versi 0.1.2:
- `.dlkit`: Membantu persiapan pemodelan dalam _deep learning_ / _artificial neural networks_. 
- `.datakit`: Digunakan untuk mengeksplorasi dataset. 
- `.prepkit`: Membaca berkas eksternal. 
- `.viewkit`: Menampilkan *dataset* dalam bentuk grafik atau tabel tertentu.
- `.bmkgkit`: Mengolah data dari situs bmkg. 

--------
# Memulai

Untuk memudahkan penggunaan, disarankan menggunakan **Anaconda3** sebagai distribusi *python*. Download **Anaconda3** [disini](https://www.anaconda.com/download/).

## Syarat
Paket ini menggunakan `Python 3.6.x` ke atas. Berikut daftar paket yang diperlukan untuk menjalankan `hidrokit`:
```
- pandas==0.24.2
- matplotlib==3.1.0
- numpy==1.16.4
```
*(daftar diatas dibuat menggunakan [pipreqs](https://github.com/bndr/pipreqs))*

# Instalasi / Pemasangan

`hidrokit` didistribusikan melalui [PyPI](https://pypi.org/). Pemasangan dilakukan dengan perintah pada _(Anaconda) command prompt_:

```
pip install hidrokit
```
*(akses internet diperlukan saat melakukan pemasangan)*

Gunakan perintah ```pip install git+https://github.com/taruma/hidrokit.git``` jika ingin menggunakan versi rilis terakhir dari github. 

# Penggunaan

Untuk memulai penggunaan, gunakan perintah `import`. Contoh:

```python
import hidrokit
from hidrokit import datakit as dk
from hidrokit.dlkit import table_timesteps
```

Untuk contoh penggunaan baca bagian [_notebook_](#notebook).

--------
# Notebook

Daftar contoh _notebook_ dapat diakses di halaman [hidrokit-nb](https://taruma.github.io/hidrokit-nb/) ([repo](https://github.com/taruma/hidrokit-nb)).

# Untuk Kontributor

Tertarik menjadi kontributor? Baca [**berkontribusi**](https://github.com/taruma/hidrokit/wiki/Berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dengan berbagai latar belakang.