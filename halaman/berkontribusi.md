---
layout: default
title: Berkontribusi
permalink: /berkontribusi
nav_order: 2
has_children: true
has_toc: false
last_modified_date: 2019-07-09
---

<div align="center" markdown="1">
> "Discussion is welcome. Judgement is not"
{: .text-delta}
</div>

---
👋 Terima kasih sebelumnya dalam mempertimbangkan untuk berkontribusi di proyek hidrokit. hidrokit memerlukan bantuan dari Anda. Anda dapat berkontribusi dalam berbagai bentuk berupa ide, keahlian teknis, koreksi, diskusi, dan apapun yang menurut Anda bisa memajukan dan mengembangkan proyek ini.

Sebelumnya, kami harap **setiap individu dalam komunitas ini mengikuti** [**kode etik yang berlaku**]({{site.baseurl}}{% link halaman/kontribusi/kode-etik.md %}). Mari buat lingkungan yang nyaman, bersahabat, dan kondusif dalam pengembangan proyek ini. Mari belajar bersama dari satu sama lain dalam membangun proyek ini. 

# Daftar isi
{: .no_toc .text-delta }

1. TOC
{:toc}

---
## Siapapun bisa berkontribusi

Kontribusi di hidrokit tidak selalu berbentuk implementasi kode. Kontribusi dapat berupa menulis panduan (dokumentasi), mengajukan ide, ikut berdiskusi, mengusulkan fitur baru, memperbaiki tata cara penulisan, memperbaiki kode yang sudah ada, dll. Sehingga proyek ini terbuka untuk siapapun dengan latar belakang apapun.

Halaman [*How to Contribute to Open Source*](https://opensource.guide/how-to-contribute) menjelaskan secara umum dan detail apa saja yang bisa kamu kontribusikan dalam proyek open-source dan manfaatnya bagi Anda. 

Anda juga bisa menganggap proyek ini sebagai latihan Anda atau langkah awal dalam memulai kontribusi di proyek *open source* demi membangun kepercayaan diri, mengasah berkomunikasi dan keahlian Anda, dan berbagi hasil karya Anda.

## Roadmap

Untuk memantau status pengembangan hidrokit, Anda bisa melihatnya pada [halaman isu di github](https://github.com/hidrokit/hidrokit/issues) atau [halaman _project_ github](https://github.com/hidrokit/hidrokit/projects).

## Kategori Kontribusi

Kami membagi kontribusi menjadi empat kategori utama yaitu:
1. [Dokumentasi]\: koreksi dokumentasi, penerjemahan, penulisan/pengejaan, komunikasi, dan kerapihan, dll. Bertujuan untuk memudahkan pengguna dalam menggunakan produk.
2. [Situs]\: pengembangan situs, koreksi penulisan/pengejaan, penambahan konten, memperbagus situs, dll. Bertujuan memudahkan pengguna mencari informasi melalui situs.
3. [Hidrologi]\: mengusulkan ide pemodelan/metode, mengoreksi/memperjelas teori, dll. Bertujuan membahas aspek hidrologi/keairan/sumberdaya air dalam proyek. 
4. [Python]\: testing, koreksi implementasi kode, dll. Bertujuan membahas aspek implementasi kode/pemrograman dalam proyek. 

Untuk panduan berkontribusi yang lebih detail bisa mengunjungi halamannya masing-masing. 

## _Issue_ dan _Pull request_

Ada dua istilah yang akan sering digunakan dalam proyek ini yaitu isu (_issue_) dan _pull request_ (PR) saat berbicara berkontribusi. Isu bisa dibilang seperti tiket, yang dibuat untuk membahas suatu ide/masalah. Ketika isu dibuat, orang lain bisa melihat isu Anda. Jika ada kontributor yang tertarik mengatasi isu Anda, kontributor akan _forking_ _repo_ utama dan mulai mengubah kode/data untuk menyelesaikan isu Anda. Setelah kontributor selesai dengan perubahannya, kontributor akan meminta _pull request_ atau PR untuk menggabungkan hasil kerjaan kontributor ke _repo_ utama. Ilustrasi proses ini bisa dilihat di video berikut:

<div align="center">
<iframe width="100%" height="315" src="https://www.youtube.com/embed/w3jLJU7DT5E" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div><br>

<div align="center" markdown="1">
**Langsung ada ide? 🙀 Buruan buat _isu_ / _pull request_ sebelum idenya terbang. 💸💸 ️**
{: .text-delta .fs-2 .fw-500}

[Buat Isu](https://github.com/hidrokit/hidrokit/issues/new/choose){: .btn .btn-blue}
[Buat _Pull Request_](https://github.com/hidrokit/hidrokit/compare){: .btn .btn-green}

</div>

---
<div align="center" markdown="1">
## Aturan
</div>

**Segala bentuk komunikasi harus mengikuti** [**kode etik yang berlaku**]({{ site.baseurl }}{% link halaman/kontribusi/kode-etik.md %}).

Kami **menyarankan** mengikuti beberapa saran berikut ini saat berkomunikasi di Github dan/atau di dalam komunitas hidrokit:
- Menggunakan bahasa Indonesia atau bahasa Inggris (utamakan bahasa yang Anda kuasai). Penggunaan bahasa Indonesia sangat dianjurkan.
- Hindari menggunakan bahasa daerah, bahasa gaul, atau menyingkat kata/kalimat yang tidak umum.
- Menggunakan panggilan netral dan inklusif. Hindari menggunakan panggilan seperti pak/bu/kak/mas/bos. (Dinyatakan pada [kode etik]({{ site.baseurl }}{% link halaman/kontribusi/kode-etik.md %}) paragraf pertama bagian janji kami)

---
<div align="center" markdown="1">
## Yang perlu Anda ketahui
</div>

Berikut daftar yang sebaiknya Anda ketahui saat berkontribusi. Git dan Github memiliki tahapan awal *learning curve* yang lumayan (belum lagi python 😅), sehingga sangat diwajari jika suatu waktu Anda mentok/buntu. Diharapkan hal tersebut tidak membuat Anda mundur untuk memulai/melanjutkan berkontribusi. Jangan ragu untuk menanyakan atau menceritakan pengalaman Anda di komunitas hidrokit.

<div align="justify" markdown="1">
> "If everyone waited to become an expert before starting, no one would become an expert. To become an EXPERT, you must have EXPERIENCE. To get EXPERIENCE, you must EXPERIMENT! Stop waiting. Start stuff." - Richie Norton
{: .text-delta}
</div>

### Git

Karena proyek ini menggunakan Git sebagai *version control* yang ditampung di GitHub, kontributor diharapkan memahami cara kerja berkontribusi menggunakan Git/Github. Jika ini pertama kalinya Anda menggunakan Git/Github, Anda bisa mengikuti kursus/latihan yang disediakan oleh Github di [Github Lab Training](https://lab.github.com/courses). Anda juga bisa mengunjungi masing-masing halaman kategori kontribusi untuk memperoleh panduan lebih detail. 

Bacaan lebih lanjut:
- [Github Lab Training](https://lab.github.com/courses)
- [Make a Pull Request](http://makeapullrequest.com/)
- [First Timer Only](http://www.firsttimersonly.com/)

Jangan ragu untuk bertanya dan mendiskusikan jika mengalami kesulitan (baik pertanyaan terkait proyek, atau cara berkontribusi). 

### Github

Proyek ini akan menggunakan wadah Github sebagai alat komunikasi utama, sehingga diharapkan untuk membiasakan dan menyesuaikan bentuk komunikasi. Github menggunakan sintaks penulisan _Markdown_. Oh 💡, penggunaan emoji 🙌 sangat dianjurkan. 🎉

Baca lebih lanjut:
- [Github - Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [ikatyang - Emoji Cheat Sheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

### Lisensi

Dalam berkontribusi harap mengingat dan mematuhi lisensi yang berlaku pada sebuah produk yang dimasuk. Jika Anda menyertakan potongan kode, harap menyertakan lisensinya dan menyertakan pemiliknya. Lisensi proyek hidrokit sendiri mengikuti [lisensi MIT](https://choosealicense.com/licenses/mit/). Untuk sumber yang digunakan dalam proyek ini bisa dilihat di halaman [Sumber]({{ site.baseurl }}{% link halaman/serbaneka/sumber.md %}).

---

<div align="center" markdown="1">
**Tunggu apa lagi? 🤔 Ayo langsung buat _issue_ atau _pull request_! 🏃‍♂️**
{: .text-delta .fs-2 .fw-500}

[Buat Isu](https://github.com/hidrokit/hidrokit/issues/new/choose){: .btn .btn-blue}
[Buat _Pull Request_](https://github.com/hidrokit/hidrokit/compare){: .btn .btn-green}

</div>

---

<div align="center" markdown="1">
Mau baca lagi? 😲 Saya kasih yang lebih detail! 😉
{: .text-delta .fs-2 .fw-500}

[Dokumentasi]{: .btn .btn-outline}
[Situs]{: .btn .btn-outline}
[Hidrologi]{: .btn .btn-outline}
[Python]{: .btn .btn-outline}

<!-- LINK -->
[Dokumentasi]:  {{site.baseurl}}{% link halaman/kontribusi/dokumentasi.md %}
[Situs]:        {{site.baseurl}}{% link halaman/kontribusi/situs.md %}
[Hidrologi]:    {{site.baseurl}}{% link halaman/kontribusi/hidrologi.md %}
[Python]:       {{site.baseurl}}{% link halaman/kontribusi/python.md %}

</div>
