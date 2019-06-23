---
layout: default
title: Python
parent: Berkontribusi
permalink: /berkontribusi/python
nav_order: 5
---

# Struktur hidrokit

hidrokit terdiri dari beberapa modul yang memiliki fungsi masing-masing. Hal ini agar memudahkan dalam pengembangan terpisah lebih lanjut. Berikut module yang telah tersedia pada versi 0.1.2:
- `.dlkit`: Membantu proses dalam persiapan pemodelan dalam _deep learning_ (dl). 
- `.datakit`: Digunakan untuk mengeksplorasi dataset. 
- `.prepkit`: Membaca berkas eksternal berupa excel dan mempersiapkan berkas untuk dapat diakses dalam Python. 
- `.viewkit`: Menampilkan dataset dalam bentuk grafik atau tabel tertentu.
- `.bmkgkit`: Mengolah data khusus untuk bmkgkit. 

## Gambaran Besar hidrokit

Rancangan gambaran besar dari hidrokit adalah mengembangkan _tool_ yang mampu membantu pada proses _data preparation_, _data analysis_, dan _data visualization_. Dalam mengembangkan fitur baru selalu menjawab tiga permasalahan tersebut. Berikut contohnya (dari versi 0.1.2):

- _data prepapration_ / persiapan data: `.dlkit`, `.datakit`, `.prepkit`, `.bmkgkit`.
- _data analysis_ / analisis data: (belum ada)
- _data visualization_ / visualisasi data: `.viewkit`.

## Environment Python

Jika anda tidak menggunakan distribusi python Anaconda, berikut library yang digunakan:
```
- Python >= 3.6.8
- Numpy >= 1.16.4
- Pandas >= 0.24.2
- Matplotlib >= 3.1.0
```
