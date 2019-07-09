---
layout: default
title: Instalasi
parent: Panduan
permalink: /panduan/instalasi
nav_order: 2
---

Halaman ini menjelaskan bagaimana memasang/instalasi paket hidrokit.

---

# DAFTAR ISI
{: .no_toc .text-delta}

1. TOC
{:toc}

---

## Memulai

Untuk memudahkan penggunaan, disarankan menggunakan **Anaconda3** sebagai distribusi *python*. Download **Anaconda3** [disini](https://www.anaconda.com/download/). 

## Catatan penting
- hidrokit hanya mendukung python versi 3.6 ke atas.
- Pemasangan `xlrd` dibutuhkan jika menggunakan module `excel` untuk membaca bilah _Excel_.
- Versi 0.2.x tidak memiliki *backward-compatibility* dengan versi 0.1.x.

## Instalasi / Pemasangan

Untuk memasang hidrokit, Anda bisa memperoleh paket hidrokit melalui PyPI atau Github. Instalasi dimudahkan dengan menggunakan perintah `pip`. Lakukan perintah dibawah ini dalam terminal/command prompt atau bisa langsung dari jupyter notebook. Instalasi membutuhkan akses internet.

### Memperoleh dari PyPI

```bash
pip install hidrokit
```

### Memperoleh dari Github

- Versi stabil (_stable_) pada cabang `master`.

```bash
pip install git+https://github.com/taruma/hidrokit.git
```

- Versi tidak stabil/pengembangan (_unstable_) pada cabang `latest`.

```bash
pip install git+https://github.com/taruma/hidrokit.git@latest
```

### Melalui Jupyter Notebook

Anda dapat melakukan instalasi langsung melalui Jupyter Notebook (Google Colab/Azure Notebook) dengan menambah tanda seru (`!`) di depan perintah `pip` seperti:
```
!pip install git+https://github.com/taruma/hidrokit.git@latest
```

## Penggunaan

Baca halaman [penggunaan untuk lebih lanjut]({{ site.baseurl }}{% link halaman/panduan/penggunaan.md %}).
