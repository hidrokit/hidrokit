![](https://img.shields.io/github/release-pre/taruma/hidrokit.svg) ![](https://img.shields.io/github/release-date-pre/taruma/hidrokit.svg) ![](https://img.shields.io/github/last-commit/taruma/hidrokit.svg) [![](https://img.shields.io/github/license/taruma/hidrokit.svg)](https://github/taruma/hidrokit/blob/master/LICENSE) ![](https://img.shields.io/github/contributors/taruma/hidrokit.svg)

[![](https://img.shields.io/github/issues/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/issues) ![](https://img.shields.io/github/issues-pr/taruma/hidrokit.svg)


# Hidrokit

Hidrokit adalah paket python yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data mentah, analisis, dan visualisasi. Perlu diingat, paket ini masih pada tahap pengembangan dan belum bisa digunakan secara praktis.

## Memulai

Untuk memudahkan penggunaan, pengguna disarankan menggunakan Anaconda3 sebagai distribusi Python karena sudah memiliki standar paket saintifik. Download Anaconda3 [disini](https://www.anaconda.com/download/).

### Instalasi

Instalasi hidrokit menggunakan perintah `pip` melalui (Anaconda) command prompt:

```
pip install hidrokit
```

### Penggunaan

Untuk memulai penggunaan, import paket hidrokit atau import modul secara spesifik.

```python
import hidrokit
from hidrokit import prepkit, viewkit
```

Lihat _notebook_ untuk melihat penggunaan `hidrokit.prepkit`.

### Notebook
Berikut _notebook_ yang telah tersedia: 

- [Demo Pos Hujan](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/notebook/demo_pos_hujan.ipynb): Penggunaan dan penjelasan fungsi dalam modul `prepkit` (disinggung juga penggunaan `viewkit`)
- [Demo Jawa Barat](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/notebook/demo_jawa_barat.ipynb): Penggunaan _pandas_ untuk mengolah data harian dari bmkg online untuk satu provinsi. Dalam _notebook_ ini fokus dalam eksplorasi data di Jawa Barat.
- [Demo Metadata BMKG](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/notebook/demo_metadata_bmkg.ipynb): Dilakukan eksplorasi metadata (informasi stasiun) untuk seluruh wilayah Indonesia yang diperoleh dari BMKG online. 

## Untuk Kontributor

Tertarik menjadi kontributor? Baca [Berkontribusi](https://github.com/taruma/hidrokit/wiki/Berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dan siapapun bisa berkontribusi.

Jangan lupa bergabung di [![Gitter chat](https://badges.gitter.im/hidrokit/gitter.png)](https://gitter.im/hidrokit/gitter).

## Catatan

Ide proyek ini bukanlah sesuatu yang baru, sudah tersedia paket bernama [Hydrostats](https://github.com/BYU-hydroinformatics/Hydrostats) yang dikembangkan oleh BYU Hidroinformatics.