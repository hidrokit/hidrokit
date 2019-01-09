![](https://img.shields.io/github/release-pre/taruma/hidrokit.svg) ![](https://img.shields.io/github/release-date-pre/taruma/hidrokit.svg) ![](https://img.shields.io/github/last-commit/taruma/hidrokit.svg)

[![](https://img.shields.io/github/issues/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/issues) ![](https://img.shields.io/github/issues-pr/taruma/hidrokit.svg)


# Hidrokit

Hidrokit adalah paket python yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data mentah, analisis, dan visualisasi. Perlu diingat, paket ini masih pada tahap pengembangan dan belum bisa digunakan secara praktis.

## Memulai

Untuk memudahkan penggunaan, pengguna disarankan menggunakan Anaconda3 sebagai distribusi Python karena sudah memiliki standar paket yang biasa digunakan dalam _data science_. Download Anaconda [disini](https://www.anaconda.com/download/)

### Persiapan

Berikut beberapa library yang harus terpasang (jika tidak menggunakan distribusi Anaconda):

```
- numpy
- matplotlib 
- pandas (openpyxl, xlrd, xlwt)
- seaborn
```

### Instalasi

Instalasi hidrokit menggunakan perintah `pip` melalui (Anaconda) command prompt:

`pip install hidrokit`

### Penggunaan

Untuk memulai penggunaan, import paket hidrokit atau import modul secara spesifik.

```python
import hidrokit
from hidrokit import prepkit, viewkit
```

Contoh penggunaan dapat lihat di notebook berikut:

- module `prepkit`: [Demo Pos Hujan](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/notebook/demo_pos_hujan.ipynb)

## Untuk Kontributor

Tertarik menjadi kontributor? Baca [Berkontribusi](https://github.com/taruma/hidrokit/wiki/Berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dan siapapun bisa berkontribusi.

[![Gitter chat](https://badges.gitter.im/hidrokit/gitter.png)](https://gitter.im/hidrokit/gitter)

## Lisensi

Proyek ini berlisensi MIT - lihat [LICENSE](https://github/taruma/hidrokit/blob/master/LICENSE) untuk lebih jelasnya.

![](https://img.shields.io/github/license/taruma/hidrokit.svg)

## Catatan

Proyek paket ini bukanlah yang terbaru, sudah tersedia paket bernama [Hydrostats](https://github.com/BYU-hydroinformatics/Hydrostats) yang dikembangkan oleh BYU Hidroinformatics. Tujuan lain paket hidrokit ini adalah membangun komunitas hidroinformatika di Indonesia. 