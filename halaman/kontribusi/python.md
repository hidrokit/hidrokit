---
layout: default
title: Python
parent: Berkontribusi
permalink: /berkontribusi/python
nav_order: 5
last_modified_date: 2022-04-03
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
- Menggunakan standar gaya tulis (style) [PEP 8](https://www.python.org/dev/peps/pep-0008/). 

### Pengembangan (Developer)
- Disarankan menggunakan _conda_ sebagai _virtual environment_. Anda bisa menggunakan instalasi menggunakan `environment.yml` di dalam direktori proyek ini.
- Testing menggunakan [pytest](https://docs.pytest.org/en/latest/).

### Layanan integrasi
- Github Actions [Pytest](https://github.com/hidrokit/hidrokit/actions/workflows/pytest-ci.yml). Digunakan untuk testing berdasarkan pytest. Pytest mengabaikan subpaket .contrib.
- Untuk proses _pull request_ berhasil, hasil dari pytest harus berhasil. 

## Struktur hidrokit

Sejak versi 0.3.x, pengembangan sementara fokus pada subpaket .contrib.

```
hidrokit@master/hidrokit        # version=0.4.0
|   __init__.py
|   __version__.py
|
+---analysis                    # direktori khusus kumpulan modul analisis data
|       __init__.py
|
+---contrib                     # direktori khusus untuk kontributor
|   |   __init__.py             # pengembangan fokus di .contrib sejak 0.3.x
|   |
|   \---taruma
|           anfrek.py
|           hk102.py
|           hk106.py
|           hk124.py
|           hk126.py
|           hk127.py
|           hk140.py
|           hk141.py
|           hk151.py
|           hk158.py
|           hk172.py
|           hk43.py
|           hk53.py
|           hk73.py
|           hk79.py
|           hk84.py
|           hk87.py
|           hk88.py
|           hk89.py
|           hk90.py
|           hk96.py
|           hk98.py
|           hk99.py
|           ujidist.py
|           __init__.py
|
+---prep                        # direktori khusus kumpulan modul persiapan data
|       excel.py
|       read.py
|       timeseries.py
|       __init__.py
|
\---viz                         # direktori khusus kumpulan modul visualisasi data
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