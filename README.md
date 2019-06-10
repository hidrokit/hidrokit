# Hidrokit
[![](https://img.shields.io/github/license/taruma/hidrokit.svg)](https://github/taruma/hidrokit/blob/master/LICENSE)
![](https://img.shields.io/github/release-pre/taruma/hidrokit.svg)
![](https://img.shields.io/github/release-date-pre/taruma/hidrokit.svg)

Hidrokit adalah paket python yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data mentah, analisis, dan visualisasi. Perlu diingat, paket ini masih pada __tahap pengembangan__ dan belum bisa digunakan secara praktis.

# Status Pengembangan
![](https://img.shields.io/github/last-commit/taruma/hidrokit.svg)
[![](https://img.shields.io/github/issues/taruma/hidrokit.svg)](https://github.com/taruma/hidrokit/issues)
![](https://img.shields.io/github/issues-pr/taruma/hidrokit.svg)

Untuk memantau status pengembangan hidrokit, Anda bisa melihatnya pada [Papan Trello](https://trello.com/b/Ii8Z5BRm/hidrokit-project). 

# Module pada Hidrokit

Hidrokit terdiri dari beberapa modul yang memiliki fungsi masing-masing. Hal ini agar memudahkan dalam pengembangan terpisah lebih lanjut. Berikut module yang telah tersedia pada versi 0.1.2:
- `.dlkit`: Membantu proses dalam persiapan pemodelan dalam _deep learning_ (dl). 
- `.datakit`: Digunakan untuk mengeksplorasi dataset. 
- `.prepkit`: Membaca berkas eksternal berupa excel dan mempersiapkan berkas untuk dapat diakses dalam Python. 
- `.viewkit`: Menampilkan dataset dalam bentuk grafik atau tabel tertentu.
- `.bmkgkit`: Mengolah data khusus untuk bmkgkit. 

Untuk penggunaan fungsi-fungsi yang terdapat dalam module tersebut bisa dibaca lebih lanjut pada _notebook_. 

# Memulai

Untuk memudahkan penggunaan, pengguna disarankan menggunakan Anaconda3 sebagai distribusi Python karena sudah memiliki standar paket saintifik. Download Anaconda3 [disini](https://www.anaconda.com/download/). Atau Anda bisa menginstalasi paket tertentu untuk memastikan paket `hidrokit` berfungsi yaitu:
```
- Python >= 3.6.8
- Numpy >= 1.16.4
- Pandas >= 0.24.2
- Matplotlib >= 3.1.0
```

# Instalasi

Instalasi hidrokit cukup menggunakan perintah `pip` melalui (Anaconda) _command prompt_:

```
pip install hidrokit
```

# Penggunaan

Untuk memulai penggunaan, cukup melakukan perintah `import`.

```python
import hidrokit
from hidrokit import prepkit, viewkit
```

Lihat contoh pada _notebook_ untuk melihat penggunaan.

# Notebook

_Notebook_ dapat diakses di halaman github [hidrokit-nb](https://github.com/taruma/hidrokit-nb).

# Untuk Kontributor

Tertarik menjadi kontributor? Baca [Berkontribusi](https://github.com/taruma/hidrokit/wiki/Berkontribusi) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dan siapapun bisa berkontribusi.

# Catatan

Ide proyek ini bukanlah sesuatu yang baru, sudah tersedia paket bernama [Hydrostats](https://github.com/BYU-hydroinformatics/Hydrostats) yang dikembangkan oleh BYU Hidroinformatics.
