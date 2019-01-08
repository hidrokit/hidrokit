[![Gitter chat](https://badges.gitter.im/hidrokit/gitter.png)](https://gitter.im/hidrokit/gitter)

# Hidrokit

Hidrokit adalah paket python yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data mentah, analisis, dan visualisasi. Perlu diingat, paket ini masih bertahap pengembangan dan belum bisa digunakan secara praktis. 

## Module dalam hidrokit

Saat ini, hidrokit hanya memiliki dua module yang terbatas yaitu:
- `prepkit`: module ini digunakan untuk membaca dan mengolah data mentah untuk dilanjutkan ke proses pengolahan data
- `viewkit`: module ini berisikan fungsi yang membantu menampilkan data dalam bentuk grafik atau bentuk lainnya

## Memulai

Untuk memudahkan penggunaan, pengguna disarankan menggunakan Anaconda3 sebagai distribusi Python karena sudah memiliki standar paket yang biasa digunakan dalam _data science_. Download Anaconda [disini](https://www.anaconda.com/download/).

### Persiapan

Berikut beberapa library yang harus terinstall (jika tidak menggunakan distribusi anaconda):
- Numpy, Matplotlib, Pandas (openpyxl, xlrd, xlwt), Seaborn

### Instalasi

Instalasi hidrokit menggunakan perintah `pip` melalui (Anaconda) command prompt:

```python
pip install uma-hidrokit
```

Jika untuk memperbaharui ke versi terbaru, gunakan perintah `pip install uma-hidrokit --upgrade`

### Penggunaan

Untuk memulai penggunaan, import paket hidrokit atau import modul secara spesifik.

```python
import hidrokit
from hidrokit import prepkit, viewkit
```

Contoh penggunaan dapat lihat di demo notebook berikut:
- [Demo Pos Hujan](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/notebook/demo_pos_hujan.ipynb)

## Untuk Kontributor

Tertarik menjadi kontributor? Baca [CONTRIBUTING](https://github/taruma/hidrokit/blob/master/CONTRIBUTING.md) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dan siapapun bisa berkontribusi.

## Lisensi

Proyek ini berlisensi MIT - lihat [LICENSE](https://github/taruma/hidrokit/blob/master/LICENSE) untuk lebih jelasnya.

## Catatan

Proyek paket ini bukanlah yang terbaru, sudah tersedia paket bernama [HydroStats](https://github.com/BYU-hydroinformatics/Hydrostats) yang dikembangkan oleh BYU Hidroinformatics. Tujuan paket hidrokit adalah membangun komunitas hidroinformatika di Indonesia. 