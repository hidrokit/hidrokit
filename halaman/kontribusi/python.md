---
layout: default
title: Python
parent: Berkontribusi
permalink: /berkontribusi/python
nav_order: 5
---
<div align="justify" markdown="1">
> "One of my most productive days was throwing away 1000 lines of code." - Ken Thompson.
{: .text-delta}
</div>

Halaman ini berisi hal-hal yang perlu diketahui dalam berkontribusi dalam Python.

---

# DAFTAR ISI
{: .no_toc .text-delta}

1. TOC
{:toc}

---

## Standar dan Rekomendasi

### Penulisan Kode/Dokumentasi (_docstring_)
- Usahakan menulis se-Python mungkin (*pythonic way*). 
- Untuk penulisan _docstring_, proyek ini menggunakan format numpydoc. Baca [panduan penulisannya](https://numpydoc.readthedocs.io/en/latest/format.html).
- Jika anda menggunakan Visual Studio Code, gunakan extension [AutoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) dengan pengaturan untuk numpydoc.
- Menggunakan standar gaya tulis (style) [PEP 8](https://www.python.org/dev/peps/pep-0008/). Proyek ini di periksa dengan _linting_ autopep8 dan flake8. (Belum diintegrasikan dengan travis-ci)
- Kualitas kode diperiksa juga menggunakan [Codacy](https://www.codacy.com/). Pemeriksaan hanya berlaku pada direktori hidrokit (direktori tests tidak dievaluasi).

### Pengembangan (Developer)
- Disarankan menggunakan _conda_ sebagai _virtual environment_. Anda bisa menggunakan instalasi menggunakan `environment.yml` di dalam direktori proyek ini.
- Testing menggunakan [pytest](https://docs.pytest.org/en/latest/).

### Layanan integrasi
- [Travis-ci](https://travis-ci.com/). Travis-ci digunakan untuk testing berdasarkan pytest dan menyampaikan informasi _code coverage_ ke codecov dan codacy.
- [Codacy](https://www.codacy.com/). Codacy digunakan untuk mengevaluasi kualitas kode. Ditargetkan untuk memperoleh nilai A.
- [Codecov](https://codecov.io/). Codecov digunakan untuk melihat _code coverage_ dalam proyek ini. 
- Untuk proses _pull request_ berhasil, hasil dari travis-ci harus berhasil. 

## Struktur hidrokit

```
hidrokit@master/hidrokit
|   __init__.py
|   __version__.py
|   
+---analysis            # direktori khusus kumpulan modul data analysis
|       __init__.py
|       
+---prep                # direktori khusus kumpulan modul data preparation
|       excel.py        
|       read.py
|       timeseries.py
|       __init__.py
|           
\---viz                 # direktori khusus kumpulan modul data visualization
        graph.py
        table.py
        __init__.py
```

Perubahan pada direktori dimungkinkan jika diperlukan. 

---
<div align="center" markdown="1">
Masih mau baca tentang cara berkontribusi? 
{: .text-delta .fs-2 .fw-500}

[Dokumentasi]{: .btn .btn-outline}
[Situs]{: .btn .btn-outline}
[Hidrologi]{: .btn .btn-outline}

<!-- LINK -->
[Dokumentasi]:  {{site.baseurl}}{% link halaman/kontribusi/dokumentasi.md %}
[Situs]:        {{site.baseurl}}{% link halaman/kontribusi/situs.md %}
[Hidrologi]:    {{site.baseurl}}{% link halaman/kontribusi/hidrologi.md %}

</div>