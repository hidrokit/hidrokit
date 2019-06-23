---
layout: default
title: Berkontribusi
permalink: /berkontribusi
nav_order: 4
has_children: true
---

👋 Terima kasih sebelumnya dalam mempertimbangkan untuk berkontribusi di proyek hidrokit. hidrokit memerlukan bantuan dari Anda. Anda dapat berkontribusi dalam berbagai bentuk seperti ide, keahlian teknis, koreksi, diskusi, dan apapun yang menurut Anda bisa memajukan dan mengembangkan proyek ini.

Sebelumnya, saya harap** setiap individu dalam komunitas ini mengikuti** [**kode etik yang berlaku**]({{site.baseurl}}{% link halaman/kontribusi/kode-etik.md %}). Mari buat lingkungan yang nyaman, bersahabat, dan kondusif dalam pengembangan proyek ini. Mari belajar bersama dari satu sama lain dalam membangun proyek ini. 

# Daftar isi
{: .no_toc .text-delta }

1. TOC
{:toc}

---
## Siapapun bisa berkontribusi

Kontribusi di hidrokit tidak selalu berbentuk implementasi kode. Kontribusi dapat berupa menulis panduan (dokumentasi), mengajukan ide, ikut berdiskusi, mengusulkan fitur baru, memperbaiki tata cara penulisan, memperbaiki kode yang sudah ada, dll. Sehingga proyek ini terbuka untuk siapapun dengan latar belakang apapun.


Bagi yang memiliki wawasan pada bidang komputer dapat berkontribusi berupa mengusulkan tatacara pengembangan proyek ini dari sisi teknis kode; bagi yang memiliki wawasan hidrologi, bisa berkontribusi berupa pengusulan ide untuk analisis hidrologi; dan bagi yang memiliki ketertarikan dalam komunitas bisa ikut serta dalam bentuk perbaikan panduan/dokumentasi, triase, ataupun membangun komunikasi kondusif. Sekecil apapun, itu lebih baik daripada tidak sama sekali. 😊

Anda bisa menganggap proyek ini sebagai latihan Anda atau langkah awal dalam memulai kontribusi di proyek *open source* demi membangun kepercayaan diri, mengasah berkomunikasi dan berbagi hasil karya Anda.

## Roadmap

Untuk memantau status pengembangan hidrokit, Anda bisa melihatnya pada [Papan Trello](https://trello.com/b/Ii8Z5BRm/hidrokit-project) dan [Project Board Github](https://github.com/taruma/hidrokit/projects/5).

## Kategori Kontribusi

Kami membagi kontribusi menjadi empat kategori utama yaitu:
1. [Dokumentasi]\: koreksi dokumentasi, penerjemahan, penulisan/pengejaan, komunikasi, dan kerapihan, dll. Bertujuan untuk memudahkan pengguna dalam menggunakan produk.
2. [Situs]\: pengembangan situs, koreksi penulisan/pengejaan, penambahan konten, memperbagus situs, dll. Bertujuan memudahkan pengguna mencari informasi melalui situs.
3. [Hidrologi]\: mengusulkan ide pemodelan/metode, mengoreksi/memperjelas teori, dll. Bertujuan membahas aspek hidrologi/keairan/sumberdaya air dalam proyek. 
4. [Python]\: testing, koreksi implementasi kode, dll. Bertujuan membahas aspek implementasi kode/pemrograman dalam proyek. 

<!-- LINK -->
[Dokumentasi]:  {{site.baseurl}}{% link halaman/kontribusi/dokumentasi.md %}
[Situs]:        {{site.baseurl}}{% link halaman/kontribusi/situs.md %}
[Hidrologi]:    {{site.baseurl}}{% link halaman/kontribusi/hidrologi.md %}
[Python]:       {{site.baseurl}}{% link halaman/kontribusi/python.md %}

Untuk panduan berkontribusi yang lebih detail bisa mengunjungi halaman masing-masing. 

## Aturan

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

Tujuan proyek hidrokit adalah mengembangkan alat yang sederhana untuk melakukan analisis hidrologi yang dimulai dari mengolah data mentah, melakukan perhitungan/analisis, hingga menampilkan hasil analisis. hidrokit dapat digunakan sebagai alternatif *Microsoft Excel* sebagai alat dalam analisis hidrologi. hidrokit juga akan memudahkan integrasi dalam analisis hidrologi.

Filosofi dibentuknya proyek ini untuk membangun komunitas hidroinformatika di Indonesia. Dengan berkembangnya teknologi dan menumpuknya data yang dapat diolah, gabungan keahlian dalam sumber daya air dan informatika akan dibutuhkan dalam menghadapi permasalahan nyata pada di masa sekarang ataupun mendatang. hidrokit ini juga merupakan salah satu bentuk pemanfaatan *python* untuk permasalahan sumber daya air. 

Dan kami harap Anda merupakan salah satu orang yang ikut serta dalam pengembangan proyek dan komunitas ini.

Anda bisa mengunjungi tanya jawab yang seputar proyek ini di halaman wiki [Tanya Jawab]({{ site.baseurl }}{% link halaman/serbaneka/tanya-jawab-uma.md %}).
