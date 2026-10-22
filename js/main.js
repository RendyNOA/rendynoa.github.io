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

/* ---------- Feeds (beranda) ----------
   Ambil daftar SITE.feeds dari data.js, ubah tiap item menjadi
   potongan HTML kartu, lalu masukkan ke <div id="feeds-grid">. */
const feedsGrid = document.getElementById("feeds-grid");
if (feedsGrid) {
  feedsGrid.innerHTML = SITE.feeds
    .map((feed) => `
      <a class="feed-card" href="${feed.link}">
        <img src="${feed.image}" alt="" loading="lazy">
        <div class="feed-card-body">
          <h3>${feed.title}</h3>
          <p>${feed.text}</p>
          <span class="feed-card-more mono">View →</span>
        </div>
      </a>`)
    .join("");
}
