# Hidrokit

Hidrokit adalah package/module python yang dapat digunakan untuk membantu proses analisis hidrologi dimulai dari pengolahan data mentah, analisis, dan visualisasi. 

## Memulai

Saat ini, hidrokit belum dirilis dalam package/module yang langsung dapat digunakan dan dilakukan instalasi ataupun update. Untuk mulai menggunakan module hidrokit, _download_ folder `hidrokit` pada `./src/` dan simpan folder tersebut di folder proyek yang akan digunakan.

## Module dalam hidrokit

Untuk sementara, hidrokit hanya memiliki dua module yaitu:
- `prepkit`: module ini digunakan untuk membaca dan mengolah data mentah untuk dilanjutkan ke proses pengolahan data
- `viewkit`: module ini berisikan fungsi yang membantu menampilkan data dalam bentuk grafik atau bentuk lainnya

### Persiapan

Untuk memudahkan penggunaan, pengguna disarankan menggunakan Anaconda3 sebagai distribusi Python karena sudah memiliki standar paket yang biasa digunakan dalam _data science_. Download Anaconda [disini](https://www.anaconda.com/download/).

### Instalasi dan Penggunaan

Saat ini, instalasi hanya berupa meng-_copy_ folder `hidrokit` ke dalam folder proyek yang akan digunakan. 

Contoh penggunaan dapat lihat di demo notebook berikut:
- [Demo Pos Hujan](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/src/Demo%20Pos%20Hujan.ipynb)

## Struktur folder

- `./src/` berisi folder `hidrokit` beserta demo ataupun _notebook_ percobaan penggunaan hidrokit
- `./docs/` berisikan berkas dokumentasi
- `./testdata/` berisikan berkas data uji berupa berkas excel curah hujan, debit. Catatan: **folder ini tidak tersedia untuk publik, hubungi @taruma untuk memperoleh data uji**

## Untuk KONTRIBUTOR

Tertarik menjadi kontributor? Baca [CONTRIBUTING](CONTRIBUTING.md) untuk kode etik, melakukan _pull request_, dan penjelasan lebih rinci hal lainnya. Proyek _open-source_ ini terbuka untuk siapa saja dan siapapun bisa berkontribusi.

Punya keahlian atau ketertarikan di bidang hidrologi atau python tapi masih bingung memulai berkontribusi, kunjungi isu #2 untuk diskusi lebih lanjut. 

## Penyusun

* **Taruma** - *Initial work* - [taruma](https://github.com/taruma)

Lihat juga daftar para [kontributor](https://github.com/taruma/hidrokit/contributors) yang berpartisipasi dalam proyek ini.

## Lisensi

Proyek ini berlisensi MIT - lihat [LICENSE](LICENSE) untuk lebih jelasnya.
