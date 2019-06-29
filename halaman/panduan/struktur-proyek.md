---
layout: default
title: Struktur Proyek
parent: Panduan
permalink: /panduan/struktur-proyek
nav_order: 1
---

Proyek hidrokit memiliki tiga cabang utama yaitu `master`, `latest` dan `gh-pages`. Cabang `master` dan `latest` merupakan cabang untuk paket python, sedangkan cabang `gh-pages` bertanggung jawab untuk membuat situs. 
Cabang `master` digunakan sebagai versi _stable_ dan cabang `latest` digunakan sebagai versi _unstable_ atau cabang untuk _developer_.

## Cabang **master** / **latest**
```
hidrokit@master
|   CHANGELOG.md                        # 
|   CODE_OF_CONDUCT.md                  # 
|   CONTRIBUTING.md                     # 
|   LICENSE                             # 
|   README.md                           # 
|   setup.py                            # setup instalasi paket
|                                       
+---.github                             # direktori untuk pengaturan github
|   |   config.yml                      # konfigurasi todo dan bot
|   |   pull_request_template.md        #
|   |   release-drafter.yml             # konfigurasi release-drafter
|   |   stale.yml                       # konfigurasi stale-bot
|   |                                   
|   \---ISSUE_TEMPLATE                  # direktori khusus issue template
|                                       
+---docs                                # direktori dokumentasi sphinx
|
+---hidrokit                            # direktori paket python
|                                       
\---tests                               # direktori test untuk paket hidrokit
```



## Cabang **gh-pages**
```
hidrokit@gh-pages
|   index.md                            # halaman depan
|   README.md                           # 
|   _config.yml                         # konfigurasi jekyll github
|   _config_local.yml                   # konfigurasi jekyll lokal
|                                       
+---assets                              # direktori media
|   +---images                          # direktori khusus gambar
|       |                               
|       \---presskit                    # kumpulan gambar logo hidrokit
|                                       
+---halaman                             # direktori utama halaman
    |  *berkontribusi.md                # <parent page>
    |   changelog.md                    #
    |   tentang-hidrokit.md             #
    |                                   
    +---kontribusi                      # direktori halaman /berkontribusi/
    |       dokumentasi.md              # 
    |       hidrologi.md                # 
    |       kode-etik.md                #
    |       python.md                   #
    |       situs.md                    #
    |                                   
    +---panduan                         # direktori halaman /panduan/
    |       instalasi.md                #
    |      *panduan.md                  # <parent page>
    |       struktur-proyek.md          #
    |                                   
    \---serbaneka                       # direktori halaman /serbaneka/
            daftar-kata.md              #
           *serbaneka.md                # <parent page>
            sumber.md                   #
            tanya-jawab-uma.md          #
```
