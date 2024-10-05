# Program Pertarungan Robot
Program ini ditulis dalam bahasa Python.

## CARA MAIN
1. Jalankan programnya.
    > `python Jawaban_2.py`
2. Pilih robot pertama dan robot kedua.
3. Tonton pertarungan sengit nya.

## MEKANISME & CARA KERJA
* Setiap robot dapat melakukan *damage* pada robot lain dengan rentang 1 sampai dengan ATK robot tersebut.
* Serangan robot memiliki CRIT, dimana tiap robot memiliki n persen kemungkinan untuk melakukan *damage* yang lebih besar.
    > * Rumus mekanisme CRIT ini adalah:  
    `DMG setelah CRIT = DMG tanpa CRIT + (Crit DMG × DMG tanpa CRIT)`
    > * Indikator dari serangan yang CRIT adalah terdapat emoji "💥" di sebelah kiri.
* Pengurangan HP oleh DMG memiliki rumus sebagai berikut:
    > `HP setelah diserang = HP sebelum diserang - DMG`
* Library "time" dipakai agar pertarungan tidak terlalu cepat berlalu (interval tiap serangan 0,5 detik).
* Tiap robot memiliki "*profile picture*" ([kaomoji](https://en.wikipedia.org/wiki/Kaomoji)/emoticon) sendiri