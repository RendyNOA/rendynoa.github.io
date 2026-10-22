# Daftar gambar situs

Cara mengganti gambar:
1. Taruh foto baru di folder yang sesuai (misalnya `assets/work/`).
2. Ubah path `image:` di `js/data.js` ke nama file baru.
3. Simpan, lalu cek di Live Server.

Tips: perkecil foto sebelum dipakai (lebar ±800–1200 px, di bawah ±300 KB).
Nama file sebaiknya huruf kecil tanpa spasi: GitHub Pages membedakan `foto.JPG` dan `foto.jpg`.

## Ditulis langsung di HTML

| Gambar | Dipakai di | Keterangan |
|---|---|---|
| `assets/img/profile.jpg` | `index.html` (hero) | 800×1000 px, dipotong dari `profile-original.JPG` (asli, tidak di-commit) |
| `assets/cv/CV_Rendy_Ryan_Renaldi.pdf` | `index.html` (tombol Download CV) | Bukan gambar, tapi juga aset yang perlu diganti kalau CV diperbarui |

## Diatur di `js/data.js`

`PLACEHOLDER` = `assets/img/placeholder.svg` (gambar sementara abu-abu).

| Bagian di data.js | Item | Gambar sekarang |
|---|---|---|
| feeds | Work Experience | `assets/work/mersi-praktikum.jpg` |
| feeds | Projects | `assets/projects/pump-field.jpg` |
| feeds | Certificates | `assets/certificates/pelatihan-3.jpg` |
| feeds | Blog | "Coming soon" dengan latar `assets/img/blog.jpg` (diatur di `css/style.css` bagian 5i, bukan di data.js) |
| work | Measurement and Instrumentation Lab | `assets/work/mersi-praktikum.jpg` |
| work | PUI-PT Intelligent Sensing-IoT | `assets/work/puiptiot-logo.png` |
| work | PT SAS Aero Sishan | `assets/work/sasaero-banner.jpg` |
| work | Instrumentation System Lab (TA) | `assets/work/praktikum-kegiatan.jpg` |
| work | SILO Recruitment Chair | PLACEHOLDER |
| work | Basic Computing Lab | `assets/work/daskom-praktikan.jpg` |
| organizations | Engineering Physics Student Council | `assets/work/oversight-council.jpg` |
| organizations | Engineering Service Community | PLACEHOLDER |
| organizations | HMTF Unitel | PLACEHOLDER |
| organizations | Kalibrasi 2024 | PLACEHOLDER |
| organizations | Student English Society | PLACEHOLDER |
| projects | Pump RPM Monitoring | `assets/projects/pump-field.jpg` |
| projects | Sensor Testing | `assets/projects/kalibrasi-chamber-real.jpg` |
| projects | AirGradien | `assets/projects/aqms-device.jpg` |
| projects | TrapGradien | `assets/projects/trapgradien-pcb.png` |
| projects | ROV | `assets/projects/armor-prototype.jpg` |
| projects | Effect of Motion | `assets/projects/motion-scatter-chamber.png` |
| projects | HAR | `assets/projects/har-aktivitas.png` |
| projects | Kost-In | `assets/projects/kostin-logo.png` |
| certificates | (semua) | `assets/certificates/*.jpg`, kecuali Basic Intensive English Program (belum ada gambar) |
| blog | (belum ada tulisan) | Halaman Blog menampilkan panel "Coming soon" dengan latar `assets/img/blog.jpg` |

Gambar di halaman detail (`work-*.html`, `project-*.html`) didata saat Tahap 10.
