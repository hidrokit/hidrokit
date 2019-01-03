# Pendahuluan

Terima kasih sebelumnya dalam mempertimbangkan untuk berkontribusi di proyek Hidrokit. Hidrokit sangat memerlukan bantuan dari Anda. Anda dapat berkontribusi dalam bentuk apapun seperti ide, keahlian teknis, koreksi teori, diskusi, dan apapun yang menurut Anda bisa memajukan proyek ini. Saat ini, hidrokit masih ditahap ide, sehingga implementasi 

Sebelumnya, saya harap setiap orang dalam komunitas ini mengikuti [kode etik](CODE_OF_CONDUCT.md) yang berlaku. Mari buat lingkungan yang nyaman, bersahabat, dan kondusif dalam pengembangan proyek ini. Mari belajar bersama dari satu sama lain dalam membangun proyek ini. 

Saat ini Hidrokit berada di tahap awal sekali dan bisa dibilang hanya baru sebuah ide. Ini merupakan kesempatan Anda sebagai kontributor untuk ikut serta dalam pengembangan proyek ini. 

## Siapapun bisa berkontribusi

Perlu diingat kembali bahwa kontribusi Hidrokit tidak sepenuhnya harus dalam implementasi kode. Kontribusi dapat berupa menulis panduan, mengajukan ide, ikut berdiskusi, mengusulkan fitur baru, memperbaiki tata cara penulisan, memperbaiki kode yang sudah ada, dll. Untuk saat ini, dari awal tahun 2019, akan lebih fokus ke pembangunan ide hidrokit dan memperjelas roadmap proyek ini. Dan hal ini terbuka untuk siapapun dengan latar belakang apapun.

Bagi yang memiliki latar belakang komputer dapat berkontribusi berupa mengusulkan tatacara pengembangan proyek ini, bagi yang memiliki latar belakang teknik sipil ataupun keairan/sumber daya air, bisa berkontribusi berupa mengusulkan ide untuk analisis hidrologi, dan bagi yang memiliki ketertarikan dalam komunitas bisa ikut serta memperbaiki panduan kontributor, triage, ataupun membangun komunikasi kondusif. Dan banyak bentuk kontribusi lainnya. Sekecil apapun, itu lebih baik daripada tidak sama sekali. :)

Anggap proyek ini sebagai latihan Anda dalam memulai kontribusi di proyek open source, membangun kepercayaan diri untuk komunikasi dan berbagi hasil karya Anda, mengasah komunikasi, dan membentuk komunitas yang memiliki tujuan yang sama meski dengan latar belakang yang bermacam-macam. 

## Roadmap

Dalam proyek Hidrokit ini akan dipisah menjadi tiga proses utama yaitu 
- _data preparation_ : bagian persiapan mengubah data mentah jadi data siap olah (modul: `prepkit`)
- _data processing_ : bagian utama dalam pemrosesan data dan implentasi teori
- _data visualization_ : bagian menampilkan informasi yang diperoleh (modul: `viewkit`)

## Bentuk kontribusi

Saat ini bentuk kontribusi yang diharapkan adalah:

- Ide Roadmap proyek
- Mengevaluasi dan memperbaiki dokumentasi (koreksi penulisan, memperjelas kalimat, menambah informasi)
- Mengusulkan perbaikan dalam proses pengembangan proyek ini (workflow, versioning, packaging)
- Memberikan ide dalam pengembangan proyek ini dan ikut serta dalam diskusinya
- Mengembangkan kode implementasi dari teori yang digunakan
- Mencoba kode yang sudah ada dan memeriksa kegunaannya

# Aturan

Segala komunikasi harus mengikuti [Kode Etik](CODE_OF_CONDUCT.md).

# Kontribusi Pertamamu

Untuk memulai kontribusi pertama kamu bisa mengunjungi diskusi di issue berikut terkait pengembangan proyek ini.
- Terkait non-teknis dan umum (ide, saran, kritik) terkait pengembangan proyek Hidrokit, kunjungi (#2)
- Terkait teknis dalam bidang keahlian keairan/sumberdaya air, kunjungi (#3)
- Terkait teknis dalam bidang komputer dan/atau informatika, bisa mengunjungi isu (#4)

Saat ini label yang tersedia dalam proyek ini antara lain:
- Pemula: Isu mengenai hal non-teknis dan umum
- Python: Isu mengenai hal implementasi teori (Hidro) ke dalam bentuk Python, dapat berupa perbaikan kode (struktur maupun dokumentasi)
- Hidro: Isu mengenai hal sumberdaya air seperti teori yang digunakan, paper/jurnal referensi

Label akan ditambahkan sesuai kebutuhan proyek.

Karena proyek ini menggunakan Git sebagai version control yang ditampung di GitHub, kontributor diharapkan memahami cara kerja berkontribusi menggunakan Git/Github. Jika ini pertama kalinya Anda menggunakan Git/Github, Anda bisa mengikuti kursus/latihan yang disediakan oleh Github di [Github Lab Training](https://lab.github.com/courses).

Beberapa tutorial lainnya antara lain: http://makeapullrequest.com/ and http://www.firsttimersonly.com/

Jangan ragu untuk bertanya dan mendiskusikan jika mengalami kesulitan (baik pertanyaan terkait proyek, atau cara berkontribusi). 

## Environment Python

Jika anda tidak menggunakan distribusi python Anaconda, berikut library yang digunakan:
- numpy, pandas, matplotlib, seaborn, xlrd, xlwt, openpyxl
(paket ini harus ada untuk dapat menjalankan demo [Pos Hujan](https://nbviewer.jupyter.org/github/taruma/hidrokit/blob/master/src/Demo%20Pos%20Hujan.ipynb)

# Filosofi hidrokit

Tujuan proyek hidrokit adalah mengembangkan alat yang sederhana untuk melakukan analisis hidrologi yang dimulai dari mengolah data mentah, melakukan perhitungan/analisis, hingga menampilkan hasil analisis. Hidrokit dapat digunakan sebagai alternatif menggunakan excel sebagai alat dalam analisis hidrologi. Hidrokit juga akan memudahkan integrasi dalam analisis hidrologi.

Filosofi dibentuknya proyek ini untuk membangun komunitas hidroinformatika di Indonesia. Dengan berkembangnya teknologi dan menumpuknya data yang dapat diolah, gabungan keahlian dalam sumber daya air dan informatika akan dibutuhkan dalam menghadapi permasalahan nyata pada di masa sekarang ataupun mendatang. Hidrokit ini juga merupakan salah satu bentuk pemanfaatan python untuk permasalahan sumber daya air. 

Dan kami harap Anda merupakan salah satu orang yang ikut serta dalam pengembangan proyek dan komunitas ini.

Anda bisa tanya jawab yang saya buat seputar proyek ini di [tanyajawab](docs/tanyajawab.md)

# Komunitas Hidrokit

Ayo bergabung di [gitter.im](https://gitter.im/hidrokit/community)