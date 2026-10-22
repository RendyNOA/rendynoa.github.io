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

/* ---------- Fungsi bantu tanggal ----------
   "2025-09" → "Sep 2025", "2024" → "2024", "present" → "Present" */
const MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

function formatDate(value) {
  if (value === "present") return "Present";
  const [year, month] = value.split("-");          // "2025-09" → year "2025", month "09"
  return month ? `${MONTHS[Number(month) - 1]} ${year}` : year;
}

function formatPeriod(start, end) {
  if (start === end) return formatDate(start);      // contoh: "2024" saja
  return `${formatDate(start)} – ${formatDate(end)}`;
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

/* ---------- Timeline Experience ---------- */
const TYPE_LABEL = { work: "Work", org: "Organization" };

// Satu kartu. Kalau link = null, kartu dibuat sebagai <div> (tidak bisa diklik).
function timelineCard(item) {
  const tag = item.link ? "a" : "div";
  const href = item.link ? ` href="${item.link}"` : "";
  const skills = item.skills.map((skill) => `<li>${skill}</li>`).join("");
  const fitClass = item.fit === "contain" ? ` class="fit-contain"` : "";
  return `
    <${tag} class="tl-card"${href}>
      <img src="${item.image}" alt=""${fitClass} loading="lazy">
      <div class="tl-card-body">
        <span class="tl-type mono">${TYPE_LABEL[item.type]}</span>
        <h4>${item.role}</h4>
        <p class="tl-place">${item.place}</p>
        <p class="tl-period mono">${formatPeriod(item.start, item.end)}</p>
        <ul class="tags">${skills}</ul>
      </div>
    </${tag}>`;
}

const timelineEl = document.getElementById("timeline");
if (timelineEl) {
  // 1. Gabungkan dua daftar, beri tiap item penanda jenisnya.
  //    "...item" = salin semua isi item, lalu tambahkan type.
  const items = [
    ...SITE.work.map((item) => ({ ...item, type: "work" })),
    ...SITE.organizations.map((item) => ({ ...item, type: "org" })),
  ];

  // 2. Kumpulkan tahun mulai yang ada (tanpa duplikat), urutkan terbaru dulu.
  const years = [...new Set(items.map((item) => item.start.slice(0, 4)))].sort().reverse();

  // 3. Untuk tiap tahun: pilih item yang mulai di tahun itu, pisah kiri/kanan.
  timelineEl.innerHTML = years
    .map((year) => {
      const inYear = items
        .filter((item) => item.start.startsWith(year))
        .sort((a, b) => b.start.localeCompare(a.start));     // terbaru di atas
      const work = inYear.filter((item) => item.type === "work");
      const org = inYear.filter((item) => item.type === "org");
      return `
        <section class="tl-year" aria-label="Started in ${year}">
          <h3 class="tl-year-label mono">${year}</h3>
          <div class="tl-col tl-work">${work.map(timelineCard).join("")}</div>
          <div class="tl-col tl-org">${org.map(timelineCard).join("")}</div>
        </section>`;
    })
    .join("");
}
