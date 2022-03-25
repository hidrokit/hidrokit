
<div align="center">
<a href="https://hidrokit.github.io/hidrokit"><img src="https://hidrokit.github.io/hidrokit/assets/images/presskit/hidrokit-800x200.jpg" alt="logo hidrokit"></a><br>

![PyPI - Status](https://img.shields.io/pypi/status/hidrokit.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hidrokit.svg)
[![GitHub license](https://img.shields.io/github/license/hidrokit/hidrokit.svg)](https://github.com/hidrokit/hidrokit/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/145389179.svg)](https://zenodo.org/badge/latestdoi/145389179)

[![Sponsored by PT. FIAKO Enjiniring Indonesia](https://img.shields.io/badge/sponsored%20by-PT.%20FIAKO%20Enjiniring%20Indonesia-blue.svg)](http://www.fiako.co.id/)

<a href="https://hidrokit.github.io/hidrokit"><b>Kunjungi situs resmi hidrokit.</b></a>
</div>

`hidrokit` adalah proyek _open source_ paket *python* yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data, analisis data, dan visualisasi data. [Baca lebih lanjut mengenai hidrokit](https://hidrokit.github.io/hidrokit/tentang-hidrokit).

## Release

<table>
  <tr align="center">
    <th>Release</th>
    <th>PyPI</th>
    <th>Github</th>
    <th>Github (Pre-release)</th>
  </tr>
  <tr>
    <td></td>
    <td><img alt="PyPI" src="https://img.shields.io/pypi/v/hidrokit.svg?logo=pypi"></td>
    <td><img alt="GitHub release" src="https://img.shields.io/github/release/hidrokit/hidrokit.svg?logo=github"></td>
    <td><img alt="GitHub release" src="https://img.shields.io/github/release-pre/hidrokit/hidrokit.svg?logo=github"></td>
  </tr>
  <tr>
    <td>Date</td>
    <td></td>
    <td><img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/hidrokit/hidrokit.svg?logo=github"></td>
    <td><img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/hidrokit/hidrokit.svg?logo=github"></td>
  </tr>

</table>

## Memulai

Untuk memudahkan penggunaan, disarankan menggunakan **Anaconda3** sebagai distribusi *python*. Download **Anaconda3** [disini](https://www.anaconda.com/download/). Baca panduan di halaman [instalasi untuk lebih detail](https://hidrokit.github.io/hidrokit/panduan/instalasi).

## Instalasi / Pemasangan

`hidrokit` didistribusikan melalui [PyPI](https://pypi.org/). Pemasangan dilakukan dengan perintah `pip` pada _(Anaconda) command prompt_:

```bash
pip install hidrokit
```
*(akses internet diperlukan saat melakukan pemasangan)*

### Versi terbaru (_latest_)

Untuk versi paling terbaru bisa melakukan pemasangan berdasarkan cabang _latest_.
```bash
pip install git+https://github.com/hidrokit/hidrokit.git@latest
```

## Catatan penting
- Sejak versi 0.3.7, hidrokit hanya mendukung python versi 3.6 ke atas.
- Pemasangan `xlrd` dibutuhkan jika menggunakan module `excel` untuk membaca bilah _Excel_.
- Versi 0.2.x tidak memiliki *backward-compatibility* dengan versi 0.1.x.
- Baca halaman [pemasangan untuk lebih detail](https://hidrokit.github.io/hidrokit/panduan/instalasi).

## Penggunaan

Untuk memulai penggunaan, gunakan perintah `import`. Contoh:

```python
from hidrokit.prep import read

# untuk penggunaan subpaket .contrib
# from hidrokit.contrib.[nama user] import [modul]
from hidrokit.contrib.taruma import anfrek
from hidrokit.contrib.taruma import hk88, hk102
```

Untuk penggunaan baca halaman [penggunaan](https://hidrokit.github.io/hidrokit/panduan/penggunaan).

### Laporan Implementasi

Penggunaan hidrokit juga bisa dilihat dari [_Laporan Implementasi_](https://taruma.github.io/vivaldi/laporan-implementasi). Berikut daftar laporan implementasi yang telah dibuat:

no laporan | tanggal | versi hidrokit | judul | lihat (nbviewer) | pdf
:- | :- | :- | :- | :- | :-
**LI-04** | 11 Februari 2020 | `0.3.5` | Perbandingan Model Variasi _Recurrent Neural Networks_ Pada Kasus Prediksi Debit Aliran | [nbviewer](https://nbviewer.org/gist/taruma/9d1ef5c6d629c792bed0c3f68b324675) | [pdf](https://1drv.ms/b/s!AmxSTa4UunElhoVm7i0EuKdPkPlzVg?e=rjXNpf) 
**LI-03** | 16 Januari 2020 | `0.3.5` | Analisis Hidrologi Menggunakan hidrokit | [nbviewer](https://nbviewer.jupyter.org/gist/taruma/4c1ed1212290965ecda056f45d7aaea2) | [pdf](https://1drv.ms/b/s!AmxSTa4UunElhoU3ehyoy45_RG6hjA?e=5wUb8d)
**LI-02** | 22 Oktober 2019 | `0.3.2` | Prediksi Debit Aliran Menggunakan Long Short-Term Memory (LSTM) | [nbviewer](https://nbviewer.jupyter.org/gist/taruma/8186dba212875f6b3f1677a5e2f9a70f) | [pdf](https://1drv.ms/b/s!AmxSTa4UunElhoU1sISX0gc4BammwQ?e=MGHcwT)
**LI-01** | 13 Juli 2019 | `0.2.0` | Prediksi Kualitas Air Menggunakan Artificial Neural Networks | [nbviewer](https://nbviewer.jupyter.org/gist/taruma/12bf06ab7307340525eecf5b3c8beb9c) | [pdf](https://1drv.ms/b/s!AmxSTa4UunElhoU27FZ3pMHVvWeMsA?e=ouC2KK)


## Untuk Kontributor

Tertarik menjadi kontributor? Baca [**berkontribusi**](https://hidrokit.github.io/hidrokit/berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dengan berbagai latar belakang.

## Lisensi

Paket hidrokit menggunakan [lisensi MIT](LICENSE.txt). Dokumentasi yang disertai pada proyek ini menggunakan lisensi [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/deed.id). 
## Acknowledgement

- Terima kasih untuk [PT. FIAKO Enjiniring Indonesia](http://www.fiako.co.id/) (FIAKO ENGINEERING) yang telah mensponsori proyek ini sejak Februari 2022.
- Terima kasih untuk **LKO** yang telah mensponsori proyek ini sejak versi 0.2.x hingga 0.3.6.
- Terima kasih untuk tim hidrokit (Cahya Suryadi, Christine Dorty Hadi, dan Dicky Muhammad Fadli) atas dukungannya dalam pengembangan hidrokit. 
