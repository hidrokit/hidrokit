---
layout: default
title: Berkontribusi
permalink: /berkontribusi
nav_order: 4
has_children: true
---

# Pendahuluan

Terima kasih sebelumnya dalam mempertimbangkan untuk berkontribusi di proyek `hidrokit`. `hidrokit` sangat memerlukan bantuan dari Anda. Anda dapat berkontribusi dalam bentuk apapun seperti ide, keahlian teknis, koreksi teori, diskusi, dan apapun yang menurut Anda bisa memajukan proyek ini.

Sebelumnya, saya harap setiap individu dalam komunitas ini mengikuti [**Kode Etik**](https://github.com/taruma/hidrokit/blob/master/CODE_OF_CONDUCT.md) yang berlaku. Mari buat lingkungan yang nyaman, bersahabat, dan kondusif dalam pengembangan proyek ini. Mari belajar bersama dari satu sama lain dalam membangun proyek ini. 

Ini merupakan kesempatan Anda sebagai kontributor untuk ikut serta dalam pengembangan proyek ini. 

# Siapapun bisa berkontribusi

Perlu diingat, kontribusi `hidrokit` tidak selalu berbentuk implementasi kode. Kontribusi dapat berupa menulis panduan, mengajukan ide, ikut berdiskusi, mengusulkan fitur baru, memperbaiki tata cara penulisan, memperbaiki kode yang sudah ada, dll. Untuk saat ini, dari awal tahun 2019, akan lebih fokus ke pembangunan ide `hidrokit` dan memperjelas roadmap proyek ini. Dan hal ini terbuka untuk siapapun dengan latar belakang apapun.

Bagi yang memiliki wawasan pada bidang komputer dapat berkontribusi berupa mengusulkan tatacara pengembangan proyek ini dari sisi teknis kode, bagi yang memiliki wawasan hidrologi, bisa berkontribusi berupa pengusulan ide untuk analisis hidrologi, dan bagi yang memiliki ketertarikan dalam komunitas bisa ikut serta dalam bentuk perbaikan panduan, *triage*, ataupun membangun komunikasi kondusif. Sekecil apapun, itu lebih baik daripada tidak sama sekali. :)

Anggap proyek ini sebagai latihan Anda dalam memulai kontribusi di proyek *open source*, membangun kepercayaan diri untuk komunikasi dan berbagi hasil karya Anda, mengasah komunikasi, dan membentuk komunitas yang memiliki tujuan yang sama meski dengan latar belakang yang bermacam-macam. 

# Roadmap

Untuk memantau status pengembangan hidrokit, Anda bisa melihatnya pada [Papan Trello](https://trello.com/b/Ii8Z5BRm/hidrokit-project).

# Struktur `hidrokit`

`hidrokit` terdiri dari beberapa modul yang memiliki fungsi masing-masing. Hal ini agar memudahkan dalam pengembangan terpisah lebih lanjut. Berikut module yang telah tersedia pada versi 0.1.2:
- `.dlkit`: Membantu proses dalam persiapan pemodelan dalam _deep learning_ (dl). 
- `.datakit`: Digunakan untuk mengeksplorasi dataset. 
- `.prepkit`: Membaca berkas eksternal berupa excel dan mempersiapkan berkas untuk dapat diakses dalam Python. 
- `.viewkit`: Menampilkan dataset dalam bentuk grafik atau tabel tertentu.
- `.bmkgkit`: Mengolah data khusus untuk bmkgkit. 

## Gambaran Besar `hidrokit`

Rancangan gambaran besar dari `hidrokit` adalah mengembangkan _tool_ yang mampu membantu pada proses _data preparation_, _data analysis_, dan _data visualization_. Dalam mengembangkan fitur baru selalu menjawab tiga permasalahan tersebut. Berikut contohnya (dari versi 0.1.2):

- _data prepapration_ / persiapan data: `.dlkit`, `.datakit`, `.prepkit`, `.bmkgkit`.
- _data analysis_ / analisis data: (belum ada)
- _data visualization_ / visualisasi data: `.viewkit`.

# Bentuk Kontribusi

Saat ini bentuk kontribusi yang diharapkan adalah:

1. Ide _Roadmap_ proyek.
2. Mengevaluasi dan memperbaiki dokumentasi (koreksi penulisan, memperjelas kalimat, menambah informasi).
3. Mengusulkan perbaikan dalam proses pengembangan proyek ini (workflow, versioning, packaging).
4. Memberikan ide dalam pengembangan proyek ini dan ikut serta dalam diskusinya.
5. Mengembangkan implementasi kode dari teori yang digunakan.
6. Mencoba kode yang sudah ada dan memeriksa kegunaannya.

Bentuk kontribusi yang tidak tertera pada daftar diatas bukan berarti tidak dibutuhkan, jika ada bentuk kontribusi selain yang disebutkan jangan ragu untuk membuat isu/diskusi. 

# Aturan

Segala bentuk komunikasi harus mengikuti [Kode Etik](https://github.com/taruma/hidrokit/blob/master/CODE_OF_CONDUCT.md).

# Kontribusi Pertamamu

Untuk memulai kontribusi, kamu bisa mengunjungi diskusi di *issue* berikut terkait pengembangan proyek ini.

- Terkait non-teknis dan umum (ide, saran, kritik) terkait pengembangan proyek hidrokit, kunjungi [***issue #2***](https://github.com/taruma/hidrokit/issues/2).
- Terkait teknis dalam bidang keahlian keairan/sumberdaya air, kunjungi [***issue #3***](https://github.com/taruma/hidrokit/issues/3).
- Terkait teknis dalam bidang komputer dan/atau informatika, bisa mengunjungi isu [***issue #4***](https://github.com/taruma/hidrokit/issues/4).

Saat ini label yang tersedia dalam proyek ini antara lain:

- Idea: Isu mengenai diskusi ide.
- Python: Isu mengenai hal implementasi teori (Hidro) ke dalam bentuk Python, dapat berupa perbaikan kode (struktur maupun dokumentasi).
- Hidro: Isu mengenai hal sumberdaya air seperti teori yang digunakan, paper/jurnal referensi.

Label akan ditambahkan sesuai kebutuhan proyek.

# *Version Control*: Git

Karena proyek ini menggunakan Git sebagai *version control* yang ditampung di GitHub, kontributor diharapkan memahami cara kerja berkontribusi menggunakan Git/Github. Jika ini pertama kalinya Anda menggunakan Git/Github, Anda bisa mengikuti kursus/latihan yang disediakan oleh Github di [Github Lab Training](https://lab.github.com/courses).

Beberapa tutorial lainnya antara lain: [Make a Pull Request](http://makeapullrequest.com/) and [First Timer Only](http://www.firsttimersonly.com/)

Jangan ragu untuk bertanya dan mendiskusikan jika mengalami kesulitan (baik pertanyaan terkait proyek, atau cara berkontribusi). 

# Environment Python

Jika anda tidak menggunakan distribusi python Anaconda, berikut library yang digunakan:
```
- Python >= 3.6.8
- Numpy >= 1.16.4
- Pandas >= 0.24.2
- Matplotlib >= 3.1.0
```

# Filosofi hidrokit

Tujuan proyek `hidrokit` adalah mengembangkan alat yang sederhana untuk melakukan analisis hidrologi yang dimulai dari mengolah data mentah, melakukan perhitungan/analisis, hingga menampilkan hasil analisis. `hidrokit` dapat digunakan sebagai alternatif *Microsoft Excel* sebagai alat dalam analisis hidrologi. `hidrokit` juga akan memudahkan integrasi dalam analisis hidrologi.

Filosofi dibentuknya proyek ini untuk membangun komunitas hidroinformatika di Indonesia. Dengan berkembangnya teknologi dan menumpuknya data yang dapat diolah, gabungan keahlian dalam sumber daya air dan informatika akan dibutuhkan dalam menghadapi permasalahan nyata pada di masa sekarang ataupun mendatang. `hidrokit` ini juga merupakan salah satu bentuk pemanfaatan *python* untuk permasalahan sumber daya air. 

Dan kami harap Anda merupakan salah satu orang yang ikut serta dalam pengembangan proyek dan komunitas ini.

Anda bisa mengunjungi tanya jawab yang seputar proyek ini di halaman wiki [Tanya Jawab]({{ site.baseurl }}{% link halaman/serbaneka/tanya-jawab-uma.md %}).
