---
layout: default
title: Penggunaan
parent: Panduan
permalink: /panduan/penggunaan
nav_order: 3
last_modified_date: 2019-07-14
---

Halaman ini menjelaskan bagaimana menggunakan paket hidrokit.

---

# DAFTAR ISI
{: .no_toc .text-delta}

1. TOC
{:toc}

---

Penggunaan paket hidrokit sama dengan penggunaan paket python pada umumnya. 

<div align="center" markdown="1">
Pengembangan fungsi utama pada hidrokit dialihkan ke pengembangan pada subpaket .contrib sejak versi 0.3.x
{: .text-delta .fs-2 .bg-red-100 .text-grey-lt-100}
</div>

## Contoh

```python
from hidrokit.prep import read
from hidrokit.prep import timeseries
from hidrokit.viz import table
import pandas as pd
import numpy as np

dataset = pd.read_csv('data.csv', index_col=0, parse_dates=True)

# Membaca data yang hilang
missing_row = read.missing_row(dataset, date_format="%m%d")

# menampilkan data dalam bentuk pivot
pivot = table.pivot(dataset, column='stasiun A', lang='en')

# membuat tabel timestep untuk pemodelan ANN
timestep = timeseries.timestep_table(dataset, timesteps=3, keep_first=False)

# subpaket contrib (baru sejak versi 0.3.x)
from hidrokit.contrib.taruma import anfrek

gumbel = anfrek.freq_gumbel(dataset, col='hujan')
```

## Daftar modul dan fungsi hidrokit

<div align="center" markdown="1">
Pengembangan fungsi utama pada hidrokit dialihkan ke pengembangan pada subpaket .contrib sejak versi 0.3.x
{: .text-delta .fs-2 .bg-red-100 .text-grey-lt-100}
</div>

Dokumentasi lengkap daftar modul dan fungsi bisa dilihat di [dokumentasi teknis hidrokit](https://hidrokit.readthedocs.io).

## Daftar modul dan manual hidrokit.contrib

Semenjak versi 0.3.x, hidrokit memiliki subpaket bernama `contrib`. Daftar manual `hidrokit.contrib`, dapat dilihat di situs [hidrokit/notebook](https://hidrokit.github.io/notebook/kumpulan-notebook).

## Contoh penggunaan

Untuk contoh penggunaan dalam jupyter notebook bisa dilihat pada situs [Hidrokit Notebook](https://hidrokit.github.io/notebook/kumpulan-notebook).
