---
layout: default
title: Dokumentasi
parent: Berkontribusi
permalink: /berkontribusi/dokumentasi
nav_order: 2
---

<div align="justify" markdown="1">
> "Documentation allows you to transfer the *why* behind code. Much in the same way code comments explain the *why*, and not the *how*, documentation serves the same purpose" - [Write the Docs](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/).
{: .text-delta}
</div>

Halaman ini berisi hal-hal yang perlu diketahui dalam berkontribusi dalam dokumentasi. Dokumentasi merupakan bagian penting dalam proyek ini. Jadi, kami tunggu kontribusinya. 🙏

---

Proyek [hidrokit] (dan [hidrokit-nb]) memiliki berbagai jenis dokumentasi antara lain:
1. ***Github community health file***: dokumentasi yang digunakan untuk Github menyampaikan informasi berupa dokumen README, CONTRIBUTING, CODE_of_CONDUCT, Issue Template, dll. Jenis ini lebih fokus bagaimana interaksi yang terjadi saat menggunakan Github.
2. **Situs ([hidrokit])**: dokumentasi ini membicarakan konten yang ada di situs proyek ini berupa halaman yang sedang anda baca, halaman tentang hidrokit, berkontribusi, dll. Dokumentasi situs lebih diutamakan karena target pengguna ataupun peminat bisa jadi tidak terbiasa dengan membaca dokumentasi melalui Github.
3. **Situs ([hidrokit-nb])**: serupa dengan nomor 2, akan tetapi proyek yang dimaksud adalah proyek hidrokit-nb (Hidrokit Notebook).
4. **[readthedocs] / API (Python)**: dokumentasi teknis berbahasa inggris yang dibuat berdasarkan *docstring* dalam kode python. Dokumentasi ini ditujukan untuk pengembangan kode python.

<!-- LINK -->
[hidrokit]: https://taruma.github.io/hidrokit
[hidrokit-nb]: https://taruma.github.io/hidrokit-nb
[readthedocs]: https://hidrokit.readthedocs.io

---

# DAFTAR ISI
{: .no_toc .text-delta}

1. TOC
{:toc}

---

## Bentuk kontribusi

Bentuk kontribusi dalam dokumentasi bisa berupa:
- Ide dokumentasi (ide tutorial)
- Mengoreksi tulisan (ejaan, kalimat, bahasa)
- Format penulisan (**tebal**, *miring*, `kode`)
- Memperbaiki struktur dokumen (*outline*, bab)
- Memperjelas bahasa dan penyampaian
- Menerjemahkan dokumen

## Yang dipersiapkan

Dalam memulai kontribusi dibutuhkan:
- Memahami struktur proyek (struktur direktori dan _files_). Baca [struktur proyek]({{ site.baseurl }}{% link halaman/panduan/struktur-proyek.md %}).
- Melakukan _pull request_.
- Menggunakan _markdown_.

## Cara berkontribusi

Untuk perubahan kecil seperti mengoreksi ejaan dapat dilakukan melalui tampilan Github. Untuk perubahan yang membutuhkan tahap uji coba (*testing*) dianjurkan untuk membuat _environment_ dokumentasinya. Dokumentasi situs ([hidrokit]/[hidrokit-nb]) telah menggunakan *Continous Integration* [travis-ci] sehingga setiap _pull request_ akan diperiksa kondisi *build*-nya, yang artinya Anda tidak akan direpotkan untuk mengujinya jika Anda tidak bisa memasang _environment_-nya. 

[travis-ci]: https://travis-ci.com/

## Panduan dokumentasi

Berikut panduan dokumentasi yang digunakan sebagai acuan di proyek ini:

- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)
- [A beginner’s guide to writing documentation](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)

--- 

<div align="center" markdown="1">
**Nemu yang keliru di dokumen? 😳 Gak usah ragu buat isu / PR 🦹‍♀️🦹‍♂️**
{: .text-delta .fs-2 .fw-500}

[Buat Isu](https://github.com/taruma/hidrokit/issues/new/choose){: .btn .btn-blue}
[Buat _Pull Request_](https://github.com/taruma/hidrokit/compare){: .btn .btn-green}

</div>

---

<div align="center" markdown="1">
Mata masih melek? 🔆 KLIK TOMBOL DIBAWAH INI, ANDA AKAN TERKEJUT!? 😉
{: .text-delta .fs-2 .fw-500}

[Situs]{: .btn .btn-outline}
[Hidrologi]{: .btn .btn-outline}
[Python]{: .btn .btn-outline}

<!-- LINK -->
[Situs]:        {{site.baseurl}}{% link halaman/kontribusi/situs.md %}
[Hidrologi]:    {{site.baseurl}}{% link halaman/kontribusi/hidrologi.md %}
[Python]:       {{site.baseurl}}{% link halaman/kontribusi/python.md %}

</div>