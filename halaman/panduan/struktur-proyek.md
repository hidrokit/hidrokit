---
layout: default
title: Struktur Proyek
parent: Panduan
permalink: /panduan/struktur-proyek
---

Proyek hidrokit memiliki dua cabang utama yaitu `master` dan `gh-pages`. Cabang `master` merupakan cabang pengembangan paket python, sedang cabang `gh-pages` bertanggung jawab untuk membuat situs. 

## Cabang **master**
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
\---hidrokit                            # direktori paket python
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
    |       daftar-kata.md              #
    |       instalasi.md                #
    |      *panduan.md                  # <parent page>
    |       struktur-proyek.md          #
    |                                   
    \---serbaneka                       # direktori halaman /serbaneka/
           *serbaneka.md                # <parent page>
            sumber.md                   #
            tanya-jawab-uma.md          #
```
