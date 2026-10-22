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

/* ---------- Fungsi bantu tampilan (dipakai beberapa halaman) ---------- */

// ["KiCad", "Python"] → <ul class="tags"><li>KiCad</li><li>Python</li></ul>
function tagList(items) {
  return `<ul class="tags">${items.map((item) => `<li>${item}</li>`).join("")}</ul>`;
}

// Gambar dengan opsi fit: "contain" untuk logo (lihat petunjuk di data.js)
function imageTag(item) {
  const fitClass = item.fit === "contain" ? ` class="fit-contain"` : "";
  return `<img src="${item.image}" alt=""${fitClass} loading="lazy">`;
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

/* ---------- Blog ----------
   Memakai gaya kartu Feeds. Kartu tanpa link = <div> berlabel "Coming soon". */
const blogGrid = document.getElementById("blog-grid");
if (blogGrid) {
  blogGrid.innerHTML = SITE.blog
    .map((post) => {
      const tag = post.link ? "a" : "div";
      const href = post.link ? ` href="${post.link}"` : "";
      const more = post.link ? "Read →" : "Coming soon";
      return `
        <${tag} class="feed-card"${href}>
          ${imageTag(post)}
          <div class="feed-card-body">
            <span class="feed-card-date mono">${formatDate(post.date)}</span>
            <h2>${post.title}</h2>
            <p>${post.text}</p>
            <span class="feed-card-more mono">${more}</span>
          </div>
        </${tag}>`;
    })
    .join("");
}

/* ---------- Timeline Experience ---------- */
const TYPE_LABEL = { work: "Work", org: "Organization" };

// Satu kartu. Kalau link = null, kartu dibuat sebagai <div> (tidak bisa diklik).
function timelineCard(item) {
  const tag = item.link ? "a" : "div";
  const href = item.link ? ` href="${item.link}"` : "";
  return `
    <${tag} class="tl-card"${href}>
      ${imageTag(item)}
      <div class="tl-card-body">
        <span class="tl-type mono">${TYPE_LABEL[item.type]}</span>
        <h4>${item.role}</h4>
        <p class="tl-place">${item.place}</p>
        <p class="tl-period mono">${formatPeriod(item.start, item.end)}</p>
        ${tagList(item.skills)}
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

/* ---------- Certificates ----------
   Urutan kategori mengikuti daftar ini. Kategori baru di data.js
   perlu ditambahkan juga di sini supaya tampil. */
const CERT_CATEGORIES = ["Work Experience", "Workshop", "Language", "Entrepreneurship", "Organization"];

// "Work Experience" → "work-experience" (dipakai sebagai id/alamat #pintas)
function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-");
}

function certCard(cert, index) {
  const date = `<span class="cert-date mono">${cert.date}</span>`;
  const text = `
    <span class="cert-title">${cert.title}</span>
    <span class="cert-issuer">${cert.issuer}</span>
    ${date}`;

  // Belum ada gambar: kartu biasa, tidak bisa diklik
  if (cert.images.length === 0) {
    return `
      <div class="cert-card">
        <span class="cert-thumb"><img src="${PLACEHOLDER}" alt=""></span>
        <span class="cert-body">${text}</span>
      </div>`;
  }

  // Lebih dari satu gambar: tampilkan penanda "+1", "+2", ...
  const extra = cert.images.length > 1
    ? `<span class="cert-more mono">+${cert.images.length - 1}</span>`
    : "";
  return `
    <button type="button" class="cert-card" data-cert="${index}">
      <span class="cert-thumb"><img src="${cert.images[0]}" alt="" loading="lazy">${extra}</span>
      <span class="cert-body">${text}</span>
    </button>`;
}

const certList = document.getElementById("certificate-list");
if (certList) {
  const jump = document.getElementById("cert-jump");

  // Tombol pintas di atas: "Workshop (2)" → lompat ke bagian #workshop
  jump.innerHTML = CERT_CATEGORIES
    .map((category) => {
      const count = SITE.certificates.filter((cert) => cert.category === category).length;
      return `<a href="#${slugify(category)}">${category} <span class="mono">${count}</span></a>`;
    })
    .join("");

  // Satu <section> per kategori. index = posisi sertifikat di SITE.certificates,
  // disimpan di data-cert supaya penampil tahu gambar mana yang dibuka.
  certList.innerHTML = CERT_CATEGORIES
    .map((category) => {
      const cards = SITE.certificates
        .map((cert, index) => (cert.category === category ? certCard(cert, index) : ""))
        .join("");
      return `
        <section class="cert-section" id="${slugify(category)}">
          <h2>${category}</h2>
          <div class="cert-grid">${cards}</div>
        </section>`;
    })
    .join("");

  /* --- Penampil gambar --- */
  const viewer = document.getElementById("cert-viewer");
  const viewerImg = document.getElementById("viewer-img");
  const viewerTitle = document.getElementById("viewer-title");
  const viewerCount = document.getElementById("viewer-count");
  let current = null;   // sertifikat yang sedang dibuka
  let page = 0;         // gambar ke berapa (0 = pertama)

  function showPage() {
    const total = current.images.length;
    viewerImg.src = current.images[page];
    viewerImg.alt = `${current.title} — image ${page + 1} of ${total}`;
    viewerCount.textContent = `${page + 1} / ${total}`;
    viewer.classList.toggle("single", total === 1);   // sembunyikan Prev/Next kalau hanya 1
  }

  function step(direction) {
    const total = current.images.length;
    page = (page + direction + total) % total;        // % = sisa bagi: setelah terakhir kembali ke awal
    showPage();
  }

  // Klik kartu → buka penampil
  certList.addEventListener("click", (event) => {
    const card = event.target.closest("[data-cert]");
    if (!card) return;
    current = SITE.certificates[Number(card.dataset.cert)];
    page = 0;
    viewerTitle.textContent = current.title;
    showPage();
    viewer.showModal();
  });

  // Tombol di dalam penampil, dan klik di area gelap di luar gambar
  viewer.addEventListener("click", (event) => {
    const action = event.target.closest("[data-viewer]")?.dataset.viewer;
    if (action === "close" || event.target === viewer) viewer.close();
    if (action === "prev") step(-1);
    if (action === "next") step(1);
  });

  // Panah kiri/kanan di keyboard saat penampil terbuka (Esc sudah otomatis menutup)
  viewer.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") step(-1);
    if (event.key === "ArrowRight") step(1);
  });
}

/* ---------- Daftar Projects ----------
   Urutan tampil = urutan di SITE.projects (paling relevan di atas). */
const projectList = document.getElementById("project-list");
if (projectList) {
  projectList.innerHTML = SITE.projects
    .map((project) => {
      // Periode hanya ditampilkan kalau tercantum (start bukan null)
      const period = project.start
        ? `<p class="project-period mono">${formatPeriod(project.start, project.end)}</p>`
        : "";
      return `
        <li>
          <a class="project-row" href="${project.link}">
            <div class="project-cat">
              <span class="brace" aria-hidden="true">{</span>
              <span class="project-cat-label mono">${project.category}</span>
            </div>
            ${imageTag(project)}
            <div class="project-info">
              <h2>${project.title}</h2>
              <p>${project.text}</p>
              ${period}
              ${tagList(project.tags)}
            </div>
            <span class="project-arrow" aria-hidden="true">→</span>
          </a>
        </li>`;
    })
    .join("");
}
