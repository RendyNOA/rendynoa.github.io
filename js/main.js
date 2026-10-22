/* ============================================================
   main.js — perilaku yang dipakai semua halaman
   ============================================================
   Nanti di sini: loading screen (Tahap 4) dan fungsi yang
   membuat kartu dari js/data.js (Tahap 5–9).
*/

// Isi tahun di footer otomatis, supaya tidak perlu diubah tiap tahun.
const yearEl = document.getElementById("year");
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}
