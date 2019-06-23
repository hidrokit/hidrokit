---
layout: default
title: Tanya Jawab (UMA)
description: Tanya jawab (taruma)
# parent: Serbaneka
permalink: /serbaneka/tanya-jawab-uma
nav_exclude: true
---

Tanya jawab ini dibuat pada tanggal 9 Januari 2019.

## Umum

### Ini proyeknya masih mentah dan bisa dibilang belum ada apa-apa, kenapa dipublikasikan kalau belum ada apa-apa?

Proyek ini mengarah ke membentuk komunitas pengguna Python dan para praktisi sumberdaya air. Dan satu sama lain memiliki keahlian yang berbeda, bisa jago di python tapi tidak begitu paham tentang sda, dan sebaliknya. Proyek ini berusaha menggabungkan kedua disiplin tersebut untuk membentuk komunitas yang menggunakan python di bidang sumberdaya air. Proyek ini juga merupakan upaya dalam membentuk komunitas hidroninformatika di Indonesia.

### Hidrologi itu sangat umum, kenapa tidak secara spesifik dalam proyek ini?

Benar bahwa analisis hidrologi itu bisa dibilang tema yang sangat luas, dan proyek hidrokit ini berupaya untuk menggabungkan beberapa potongan analisis menjadi satu tempat sehingga memudahkan dalam penggunaannya. Hal tersebut memang terkesan mustahil untuk seorang pengembang, maka dari itu proyek ini bersifat _open source_ dan _driven by community_. 

Dan dengan memberi topik yang sangat luas, para peminat tidak perlu takut bahwa suaranya diabaikan. Hanya dua tema dalam proyek ini yaitu python dan hidrologi. Topik hidrologi bisa dalam interaksi curah hujan-limpasan, aliran air tanah, banjir, dll. Topik python bisa dalam optimasi kode, pengembangan modular, version control, software development, dll. Topik luas disini tujuannya menerima segala ide terlebih dahulu, mengenali keahlian sesama kontributor. Anggap saja ini sebagai tempat temu-sapa untuk para pengembang dari sisi python ataupun hidrologi. 

### Fungsi yang ada di hidrokit sudah ada di _tools/software_ XYZ, kenapa repot mengembangkan yang baru?

Tujuan lain dari hidrokit adalah membangun komunitas dan memberi wadah bagi para _developer_ (baik dari bidang sumberdaya air ataupun komputer) yang tertarik dengan proyek opensource. Proyek hidrokit bukan digunakan untuk bersaing dengan produk lainnya. Proyek ini digunakan sebagai wadah pembelajaran penggunaan python dan sumber daya air. 

### Kalau produknya tidak bisa dipakai, percuma dong?

Tujuan utama dari proyek _open-source_ ini adalah membangun komunitas hidroinformatika. Mungkin proyek ini akan buntu di suatu saat, bukan berarti pembelajaran dalam pengembangan proyek ini tidak dapat digunakan. Untuk proyek berikutnya, para kontributor dalam proyek ini bisa membangun proyek lainnya lebih baik lagi. 

### Ini proyeknya bagian dari tugas akhir atau pekerjaan?

Proyek ini bukan bagian dari tugas akhir (skripsi/tesis/disertasi) ataupun pekerjaan saya. Saat saya membuat proyek ini, saya tidak saat bekerja dan ini murni untuk menerapkan keahlian saya dalam pengembangan program di bidang hidroinformatika. Saya menduga bahwa dengan adanya paket hidrokit akan membantu dalam proses analisis hidrologi karena saya tidak memiliki pengalaman sama sekali menjadi konsultan di bidang sumber daya air.

### Ini proyek open-source milik siapa?

Jawaban klisenya adalah milik komunitas. Akan tetapi, setiap kontributor yang memberikan ide, kode, dll memiliki hak sepenuhnya dengan apa yang mereka buat. Terkait legalitas proyek ini, saya sendiri belum paham.

### Saya mahasiswa, apakah saya boleh menggunakan proyek ini sebagai latihan?

Mahasiswa atau bukan, Anda memiliki kesempatan untuk menggunakan proyek ini sebagai latihan. Latihan dalam mengkomunikasikan ide, berkolarobasi, mendiskusikan hal teknis, dan lain-lain. Jika Anda hanya ingin berlatih menggunakan fitur di Github, tidak ada yang melarang Anda. 

### Kenapa tidak menggunakan bahasa inggris dan dipublish secara umum?

Jujur, saya belum siap mengkomunikasikannya untuk umum. Selain keterbatasan kemampuan bahasa saya, proyek ini untuk mengajak komunitas yang ada di Indonesia. Untuk konsumsi internasional, sudah ada paket bernama Hydrostats yang dikembangkan oleh BYU-Hydroinformatics, reponya bisa dikunjungi [disini](https://github.com/BYU-hydroinformatics/Hydrostats)

### Proyek ini sebenarnya ditujukan untuk siapa?

Terlepas nama proyek ini, proyek ini bisa digunakan secara umum dalam pengolahan data dari excel hingga visualisasi. Proyek hidrokit dengan tema hidrologi dan python ditujukan untuk orang yang tertarik berkontribusi dalam kedua bidang tersebut. Proyek ini juga akan menggabungkan dua keahlian yaitu hidrologi dan informatika (atau sekarang sudah disebut sebagai hidroinformatika). 

## Python

### Kenapa python dan tidak bahasa lain semisal R, matlab, fortran, java, dll?

Gratis dan tidak terbatas. Berbeda dengan matlab yang harus berbayar, mengembangkan dengan matlab akan membatasi dalam hal kolaborasi (yang tidak punya matlab tidak bisa ikut serta). Alasan lainnya adalah Python memiliki sumber pembelajaran yang sangat banyak dari kuliah online, kursus, dan komunitasnya yang sangat aktif. Jadi, bagi yang tidak mengetahui Python, bisa belajar sendiri (gratis), dan hanya membutuhkan waktu dan dedikasi anda. Python juga dikenal sebagai bahasa yang lebih cepat dan mudah dipahami dibandingkan bahasa lainnya. 
Analisis hidrologi juga lebih fokus ke pengolahan data, analisis data, dan visualisasi data. Dan fokus tersebut menyinggung _data science_ (_machine learning_, _deep learning_), dan bahasa yang sering digunakan untuk _data science_ adalah python. 

### Saya punya ide atau saran, tapi saya tidak mengerti pakai Python ataupun implementasinya?

Jangan takut memberikan ide atau saran tersebut di proyek ini. Tuangkan ide atau saran anda sedetail mungkin terutama dalam algoritmanya atau gambaran besarnya. Lakukan pemaparan ide sebaik yang Anda bisa, kontributor lain mungkin akan membantu Anda dalam memperjelas ide atau saran Anda. 

### Saya punya program/script python, apakah bisa digunakan untuk proyek ini?

Jika Anda pernah mengembangkan script/program python dan bersedia untuk membagikannya, tentu bisa digunakan untuk proyek ini. Tentunya akan ada penyesuaiannya untuk proyek ini. Saya menyarankan bahwa Anda membuat repository/gist sendiri dan menguploadnya di profil Anda, dari situ kami bisa menghormati karya anda dan mengintegrasikannya ke dalam proyek ini. Atau Anda bisa melakukan _pull request_ untuk menggabungkan hasil kerjaan Anda ke proyek ini (untuk penyesuaian bisa diatur lebih lanjut lagi). 

### Kenapa hanya bisa membaca dari excel dan tidak dari PDF?

Saat ini membaca dari excel lebih mudah dibandingkan dari PDF. Membaca data pdf sebenarnya dimungkinkan (saya sudah pernah coba), akan tetapi dengan keragaman jenis-jenis pdf yang saya peroleh membuat pengembangan untuk membaca dari PDF sulit. Bagi yang ingin mencoba mengembangkan membaca data dari PDF, saya cukup berhasil menggunakan library `tabula-py` dan `camelot`.  

## Hidrologi

### Kenapa belum ada analisis hidrologinya?

Saya tidak memiliki pengalaman praktis dalam bidang sumberdaya air, sehingga saya belum tahu bagian/fungsi mana yang diprioritaskan. Dan ini kesempatan Anda, untuk memberikan ide Anda dan akan saya kembangkan nantinya dengan bantuan kontributor lainnya.

Hal ini juga dikarenakan, saya yakin sudah banyak yang pernah mengembangkan metode atau analisis hidrologi dalam bentuk pemrograman, jika pembuatnya memberikan akses tersebut dan membukanya untuk publik, proyek ini tidak perlu mengulangi pengembangan yang sudah ada. 

### Apakah fungsi yang ada di proyek ini benar dan bisa dipakai?

Fungsi di proyek ini harus dievaluasi kembali oleh para penggunanya, itupun termasuk dalam analisis hidrologinya. Oleh karena itu, dokumentasi dalam proyek ini sangat penting daripada kodenya sendiri. 