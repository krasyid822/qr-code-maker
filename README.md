# QR Code Maker - Pembuat Kode QR 🎯

Aplikasi Progressive Web App (PWA) untuk membuat kode QR dengan watermark kustom. **Berfungsi sepenuhnya offline** dan dapat diinstall sebagai aplikasi standalone.

## ✨ Fitur

### 🎨 Desain
- **Fluent Design System** - Mengikuti design language Microsoft Windows 11
- **Acrylic blur effects** - Material design modern dengan transparansi
- **Responsive layout** - Bekerja di desktop, tablet, dan mobile
- **Dark mode ready** - Siap untuk mode gelap (dapat ditambahkan)

### 🔧 Fungsionalitas
- ✅ Generate kode QR dari teks atau URL
- ✅ Ukuran QR dapat disesuaikan (64-1024 px)
- ✅ **Watermark kustom** dengan 2 mode:
  - **Overlay** - Teks transparan menimpa QR
  - **Embed** - Teks dalam box dengan background putih
- ✅ Posisi watermark: 5 pilihan (kanan bawah, kiri bawah, kanan atas, kiri atas, tengah)
- ✅ Ukuran font watermark: 8-72 px
- ✅ **Download sebagai PNG** dengan nama file otomatis + timestamp
- ✅ Preview real-time dengan Data URL

### 📱 PWA (Progressive Web App)
- ✅ **Installable** - Dapat diinstall sebagai aplikasi di desktop/mobile
- ✅ **Offline-first** - Berfungsi 100% tanpa internet setelah pertama kali dibuka
- ✅ **Service Worker** - Caching otomatis semua assets
- ✅ **App manifest** - Metadata lengkap untuk installation
- ✅ **Auto-update** - Notifikasi saat ada update baru

## 🚀 Cara Menggunakan

### Online (Pertama Kali)
1. Buka `index.html` di browser modern (Chrome, Edge, Firefox, Safari)
2. Aplikasi akan otomatis mengunduh semua assets ke cache
3. Setelah itu, aplikasi akan berfungsi offline

### Install sebagai PWA

#### Desktop (Chrome/Edge):
1. Buka aplikasi di browser
2. Klik ikon **Install** (⊕) di address bar
3. Atau: Menu → Install QR Maker
4. Aplikasi akan muncul sebagai app standalone

#### Mobile (Android):
1. Buka aplikasi di Chrome/Edge
2. Tap **Menu (⋮)** → **Add to Home screen**
3. Icon akan muncul di home screen
4. Tap icon untuk buka sebagai app

#### Mobile (iOS/Safari):
1. Buka aplikasi di Safari
2. Tap **Share button** (⬆️)
3. Scroll dan tap **Add to Home Screen**
4. Tap **Add**

### Offline Usage
Setelah aplikasi dibuka pertama kali dan di-cache:
- ✅ Buka aplikasi tanpa koneksi internet
- ✅ Semua fitur tetap berfungsi
- ✅ Generate QR, tambah watermark, download - semuanya offline

## 📂 Struktur File

```
qr-code-maker/
├── index.html              # Halaman utama aplikasi
├── manifest.json           # PWA manifest (metadata app)
├── service-worker.js       # Service worker untuk offline caching
├── qrious.min.js          # Library QRious (lokal, tidak perlu CDN)
├── icon-192.png           # Icon 192x192 untuk PWA
├── icon-512.png           # Icon 512x512 untuk PWA
├── generate-icons.html    # Tool untuk generate icon (opsional)
└── README.md              # Dokumentasi ini
```

## 🎯 Cara Generate Kode QR

1. **Input Teks/URL**
   - Ketik teks atau URL di textarea
   - Contoh: `https://example.com` atau `Hello World!`

2. **Atur Ukuran** (opsional)
   - Default: 300px
   - Range: 64-1024px

3. **Tambah Watermark** (opsional)
   - Ketik teks watermark (contoh: `© 2025 My Brand`)
   - Pilih **Tipe**: Overlay atau Embed
   - Pilih **Posisi**: 5 pilihan lokasi
   - Atur **Ukuran Font**: 8-72px

4. **Generate**
   - Klik tombol **Generate** (biru)
   - Preview akan muncul di kanan

5. **Download**
   - Klik tombol **Download PNG**
   - File akan tersimpan: `qr_<text>_<timestamp>.png`

6. **Reset** (jika perlu mulai ulang)
   - Klik tombol **Reset**

## 🛠️ Teknologi

- **HTML5 Canvas** - Rendering QR code dan watermark
- **QRious 4.0.2** - Library untuk generate QR code
- **Service Worker API** - Offline caching
- **Cache API** - Asset storage untuk offline
- **Web App Manifest** - PWA metadata
- **Fluent Design CSS** - Modern UI dengan acrylic effects
- **Vanilla JavaScript** - No framework, lightweight

## 🔧 Development

### Generate Icons
1. Buka `generate-icons.html` di browser
2. Icons akan otomatis terdownload
3. Simpan sebagai `icon-192.png` dan `icon-512.png`

Atau buat custom icons dengan tool:
- [PWA Asset Generator](https://github.com/elegantapp/pwa-asset-generator)
- [RealFaviconGenerator](https://realfavicongenerator.net/)
- Photoshop/Figma/Canva

### Update Cache Version
Jika ada perubahan file, update `CACHE_NAME` di `service-worker.js`:
```javascript
const CACHE_NAME = 'qr-maker-v2'; // Increment version
```

### Test Offline
1. Buka DevTools (F12)
2. Tab **Application** → **Service Workers**
3. Centang **Offline**
4. Refresh halaman - app tetap jalan

## 📋 Browser Support

| Browser | Version | PWA Install | Offline |
|---------|---------|-------------|---------|
| Chrome  | 67+     | ✅          | ✅      |
| Edge    | 79+     | ✅          | ✅      |
| Firefox | 44+     | ⚠️ (limited)| ✅      |
| Safari  | 11.1+   | ⚠️ (iOS)    | ✅      |
| Opera   | 54+     | ✅          | ✅      |

**Catatan**: 
- Firefox: Service Worker support, tapi tidak ada install prompt
- Safari: PWA support terbatas, gunakan "Add to Home Screen" manual

## 🐛 Troubleshooting

### Service Worker tidak register
- Pastikan menggunakan **HTTPS** atau **localhost**
- Cek Console untuk error messages
- Clear browser cache dan reload

### App tidak berfungsi offline
- Buka app minimal 1x saat online
- Tunggu hingga semua assets tercache
- Cek DevTools → Application → Cache Storage

### Icons tidak muncul
- Generate icons dengan `generate-icons.html`
- Atau buat manual 192x192 dan 512x512 PNG
- Update path di `manifest.json` jika diperlukan

### Update tidak muncul
- Hard refresh: `Ctrl+Shift+R` (Windows) atau `Cmd+Shift+R` (Mac)
- Clear cache: DevTools → Application → Clear storage
- Unregister SW dan reload

## 📝 License

MIT License - Bebas digunakan untuk project personal atau komersial.

## 🤝 Contributing

Kontribusi welcome! Beberapa ide enhancement:
- [ ] Dark mode toggle
- [ ] Custom color untuk watermark
- [ ] Export ke SVG/PDF
- [ ] QR code templates
- [ ] Batch processing
- [ ] Logo di tengah QR
- [ ] Analytics/tracking (opsional)

## 📧 Contact

Dibuat dengan ❤️ menggunakan GitHub Copilot

---

**Status**: ✅ Production Ready | 📱 PWA Enabled | 🔒 Offline-First | 🎨 Fluent Design
