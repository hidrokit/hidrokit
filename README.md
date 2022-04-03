
<div align="center">
<a href="https://hidrokit.github.io/hidrokit"><img src="https://hidrokit.github.io/hidrokit/assets/images/presskit/hidrokit-800x200.jpg" alt="logo hidrokit"></a><br>

[![Sponsored by PT. FIAKO Enjiniring Indonesia](https://img.shields.io/badge/sponsored%20by-PT.%20FIAKO%20Enjiniring%20Indonesia-blue.svg)](http://www.fiako.co.id/)

![PyPI - Status](https://img.shields.io/pypi/status/hidrokit.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hidrokit.svg)
[![GitHub license](https://img.shields.io/github/license/hidrokit/hidrokit.svg)](https://github.com/hidrokit/hidrokit/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/145389179.svg)](https://zenodo.org/badge/latestdoi/145389179)

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

Untuk penggunaan baca halaman [penggunaan](https://hidrokit.github.io/hidrokit/panduan/penggunaan). Untuk contoh penggunaan paket hidrokit dan manual bisa lihat di [kumpulan notebook situs hidrokit/notebook](https://hidrokit.github.io/notebook/kumpulan-notebook).

## Untuk Kontributor

Tertarik menjadi kontributor? Baca [**berkontribusi**](https://hidrokit.github.io/hidrokit/berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dengan berbagai latar belakang.

## Lisensi

Paket hidrokit menggunakan [lisensi MIT](LICENSE.txt). Dokumentasi yang disertai pada proyek ini menggunakan lisensi [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/deed.id). 
## Acknowledgement

- Terima kasih untuk [PT. FIAKO Enjiniring Indonesia](http://www.fiako.co.id/) (FIAKO ENGINEERING) yang telah mensponsori proyek ini sejak Februari 2022.
- Terima kasih untuk **LKO** yang telah mensponsori proyek ini sejak versi 0.2.x hingga 0.3.6.
- Terima kasih untuk tim hidrokit-syndicate (_Cahya Suryadi_, _Christine Dorty Hadi_, dan _Dicky Muhammad Fadli_) atas dukungannya dalam pengembangan hidrokit. 
