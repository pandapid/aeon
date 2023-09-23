YT_HELP_MESSAGE = """
<b>Untuk menggunakan perintah, ikuti format ini:</b>
<code>/{cmd} opsi tautan</code> atau membalas tautan </b>
Opsi <code>/{cmd}</code>

<b>OPSI:</b>
<b>-s:</b> Pilih kualitas untuk tautan atau tautan tertentu.

<b>-z kata sandi:</b> Buat file zip yang dilindungi kata sandi.

<b>-n nama_baru:</b> Ganti nama file.

<b>-t thumbnail url:</b> Thumbnail khusus untuk setiap leexh.(url gambar mentah atau tg)

<b>nilai -ss:</b> Hasilkan ss untuk video lintah, maks 10 untuk setiap pelindian.

<b>-id drive_folder_link atau drive_id -index https://anything.in/0:</b> Unggah ke drive khusus.

<b>-opt playliststart:^10|fragment_retries:^inf|matchtitle:S13|writesubtitles:true|live_from_start:true|postprocessor_args:{{"ffmpeg": ["-threads", "4"]}}|wait_for_video: (5, 100):</b> Tetapkan opsi tambahan.

<b>-i 10:</b> Proses beberapa tautan.

<b>-b:</b> Lakukan pengunduhan massal dengan membalas pesan teks atau file dengan tautan yang dipisahkan dengan baris baru.

<b>Periksa semua opsi api yt-dlp dari <a href='https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/YoutubeDL.py#L184'>FILE</a > atau gunakan <a href='https://t.me/mltb_official_channel/177'>skrip</a> ini untuk mengonversi argumen cli menjadi opsi api.</b>
"""

MIRROR_HELP_MESSAGE = """
<b>Untuk menggunakan perintah, ikuti format ini:</b>
<code>/{cmd} opsi tautan</code> atau membalas tautan </b>
Opsi <code>/{cmd}</code>

<b>OPSI:</b>
<b>-n nama baru:</b> Ganti nama file atau folder.

<b>-t thumbnail url:</b> Thumbnail khusus untuk setiap leexh.(url gambar mentah atau tg)

<b>nilai -ss:</b> Hasilkan ss untuk video lintah, maks 10 untuk setiap pelindian.

<b>-z atau -z kata sandi:</b> Zip file atau folder dengan atau tanpa kata sandi.

<b>-e atau -e kata sandi:</b> Ekstrak file atau folder dengan atau tanpa kata sandi.

<b>-up upload tujuan:</b> Unggah file atau folder ke tujuan tertentu.

<b>-id drive_folder_link</b> atau <b>-id drive_id -index https://panime.id/0:</b>: Unggah ke folder atau ID Google Drive khusus.

<b>-u nama pengguna -p kata sandi:</b> Memberikan otorisasi untuk tautan langsung.

<b>-s:</b> Pilih berkas torrent.

<b>-h Header khusus tautan langsung:</b> -h
tautan <code>/cmd</code> -h Kunci: nilai Kunci1: nilai1.

<b>-d rasio:seed_time:</b> Mengatur rasio penyemaian dan waktu untuk torrent.

<b>-i jumlah tautan/file:</b> Memproses beberapa tautan atau file.

<b>-m nama folder:</b> Memproses beberapa tautan atau file dalam direktori unggahan yang sama.

<b>-b:</b> Lakukan pengunduhan massal dengan membalas pesan teks atau file dengan beberapa tautan yang dipisahkan dengan baris baru.

<b>-j:</b> Menggabungkan file terpisah sebelum mengekstraksi atau membuat zip.

<b>-rcf:</b> Setel tanda Rclone untuk perintah.

<b>main:dump/ubuntu.iso</b> atau <b>rcl:</b> Perlakukan jalur sebagai unduhan rclone.


<b>Catatan:</b>
<b>Perintah yang dimulai dengan qb khusus untuk torrent.</b>
Beberapa perintah mungkin memerlukan akses atau pengaturan pengguna tambahan.
"""

RSS_HELP_MESSAGE = """
Gunakan format ini untuk menambahkan URL feed:
Tautan Judul1 (wajib)
Tautan judul2 -c cmd -inf xx -exf xx
Judul3 tautan -c cmd -d rasio:waktu -z kata sandi

-c perintah + argumen apa pun
-inf: Untuk filter kata yang disertakan.
-exf: Untuk filter kata yang dikecualikan.

Contoh: Judul <code>https://www.rss-url.com</code> inf: 1080 atau 720 atau 144p|mkv atau mp4|hevc exf: flv atau web|xxx opt: up: mrcc:remote:path /subdir rcf: --buffer-size:8M|key|key:value
Filter ini akan mengurai tautan yang memiliki judul berisi "(1080 atau 720 atau 144p) dan (mkv atau mp4) dan hevc" dan tidak mengandung kata (flv atau web) dan xxx. Anda dapat menambahkan apa pun yang Anda inginkan.

Contoh lain: inf: 1080 atau 720p|.web. atau .webrip.|hevc atau x264
Ini akan mengurai judul yang berisi (1080 atau 720p) dan (.web. atau .webrip.) dan (hevc atau x264).
Catatan: Saya menambahkan spasi sebelum dan sesudah "1080" untuk menghindari kesalahan pencocokan. Jika ada angka seperti "10805695" pada judul, maka tidak akan cocok dengan "1080" tanpa spasi setelahnya.

<b>Catatan Filter:</b>
1.| berarti "dan."
2. Tambahkan "atau" di antara tombol serupa. Misalnya, Anda dapat menambahkannya di antara kualitas atau di antara ekstensi. Hindari filter seperti "f: 1080|mp4 atau 720|web" karena ini akan mengurai "1080" dan (mp4 atau 720) dan web, bukan (1080 dan mp4) atau (720 dan web).
3. Anda dapat menambahkan "atau" dan "|" sebanyak yang kamu mau.
4. Periksa judul untuk karakter khusus statis sebelum atau sesudah kualitas, ekstensi, atau elemen lainnya, dan gunakan dalam filter untuk menghindari kecocokan yang salah.

<b>Waktu habis:</b> 60 detik.

<b>Harap terapkan format yang sama pada pesan ini:</b>
"""

CLONE_HELP_MESSAGE = """
Kirim tautan Gdrive atau jalur rclone beserta perintah atau dengan membalas tautan /rc_path dengan perintah.

<b>Beberapa tautan hanya dengan membalas gdlink atau rclone_path pertama:</b>
<code>/{cmd}</code> -i 10 (jumlah tautan/pathies)

<b>Gdrive:</b>
<code>/{cmd}</code> tautan gdrive

<b>Unggah Drive Khusus:</b> link -id -index
-id <code>drive_folder_link</code> atau <code>drive_id</code> -index <code>https://panime.id/0:</code>
drive_id harus berupa ID folder, dan indeks harus berupa URL, jika tidak maka tidak akan diterima.

<b>Rclone:</b>
<code>/{cmd}</code> (rcl atau rclone_path) -up (rcl atau rclone_path) -rcf flagkey:flagvalue|flagkey|flagkey:flagvalue

Catatan: Jika -up tidak ditentukan, tujuan rclone adalah RCLONE_PATH dari config.env.
"""

PASSWORD_ERROR_MESSAGE = """
<b>Tautan ini memerlukan kata sandi!</b>
- Sisipkan tanda <b>::</b> setelah link dan tulis kata sandi setelah tanda tersebut.
<b>Contoh:</b> {}::kamu Asu
Catatan: Tidak boleh ada spasi di antara tanda <b>::</b>
Untuk passwordnya bisa menggunakan spasi!
"""
