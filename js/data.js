/*
  ============================================================
  data.js — SEMUA KONTEN DAFTAR DI SITUS INI
  ============================================================
  Halaman Experience, Projects, Certificates, Blog, dan kartu
  Feeds di beranda dibuat otomatis dari data di file ini.

  Cara mengedit:
  - Ubah teks di antara tanda kutip "...".
  - Tanggal ditulis "TAHUN-BULAN", contoh "2025-09" = Sep 2025.
    Kalau hanya tahun yang diketahui, tulis "2024".
    end: "present" berarti masih berlangsung.
  - image: path ke gambar. Ganti dengan foto Anda sendiri,
    contoh "assets/work/foto-baru.jpg". Daftar lengkapnya juga
    ada di assets/IMAGES.md.
  - fit: "contain" (opsional) untuk gambar berupa LOGO, supaya tampil
    utuh dan tidak terpotong. Tanpa fit, foto dipotong mengisi kotak.
  - link: halaman detail. null berarti kartu tidak bisa diklik.
  - Setiap item dipisah koma. Jangan hapus tanda { } [ ] ,

  Sumber konten: CV (assets/cv/CV_Rendy_Ryan_Renaldi.pdf).
  ============================================================
*/

const PLACEHOLDER = "assets/img/placeholder.svg";

const SITE = {

  /* ---------- Kartu Feeds di beranda ---------- */
  feeds: [
    { title: "Work Experience", text: "Internships, laboratory roles and organizations.",
      image: "assets/work/mersi-praktikum.jpg", link: "experience.html" },
    { title: "Projects", text: "Instrumentation, calibration and monitoring projects.",
      image: "assets/projects/aqms-device.jpg", link: "projects.html" },
    { title: "Certificates", text: "Work, workshop, language and organization certificates.",
      image: PLACEHOLDER, link: "certificates.html" },
    { title: "Blog", text: "Notes and write-ups.",
      image: PLACEHOLDER, link: "blog.html" },
  ],

  /* ---------- Experience: kolom kiri ---------- */
  work: [
    { place: "Measurement and Instrumentation Laboratory, Telkom University",
      role: "Head of Laboratory Assistants",
      start: "2025-09", end: "2026-07",
      skills: ["Oscilloscope", "DC Power Supply", "Function Generator", "Arduino Uno", "Team Coordination"],
      image: "assets/work/mersi-praktikum.jpg", link: "work-mersi.html" },

    { place: "PUI-PT Intelligent Sensing-IoT, Telkom University",
      role: "Research Intern — MBKM Programme",
      start: "2025-09", end: "2025-12",
      skills: ["Sensor Integration", "Calibration Chamber", "Mass Flow Controller", "Multiplexer", "3D Printing"],
      image: "assets/work/puiptiot-logo.png", fit: "contain", link: "work-puiptiot.html" },

    { place: "PT SAS Aero Sishan",
      role: "Systems Division Intern — MATS Project",
      start: "2025-06", end: "2025-08",
      skills: ["Pixhawk 6C", "Wiring Architecture", "Power Distribution", "QGroundControl", "Autodesk Inventor"],
      image: "assets/work/sasaero-banner.jpg", link: "work-sasaero.html" },

    { place: "Instrumentation System Laboratory, Telkom University",
      role: "Teaching Assistant — Electrical Circuits and Electronics",
      start: "2024-06", end: "2025-07",
      skills: ["Circuit Analysis", "Troubleshooting", "Oscilloscope", "Digital Electronics"],
      image: "assets/work/praktikum-kegiatan.jpg", link: "work-praktikum.html" },

    { place: "Instrumentation System Laboratory, Telkom University",
      role: "Assistant Recruitment Committee Chair — SILO",
      start: "2025-02", end: "2025-06",
      skills: ["Recruitment", "Assessment", "Coordination"],
      image: PLACEHOLDER, link: null },

    { place: "Basic Computing Laboratory, Telkom University",
      role: "Teaching Assistant — C Programming",
      start: "2023-06", end: "2024-06",
      skills: ["C Programming", "Debugging", "Teaching"],
      image: "assets/work/daskom-praktikan.jpg", link: "work-daskom.html" },
  ],

  /* ---------- Experience: kolom kanan ---------- */
  organizations: [
    { place: "Engineering Physics Student Council",
      role: "Supervisory Commission Chair",
      start: "2025-08", end: "2026-01",
      skills: ["Oversight", "Performance Evaluation"],
      image: "assets/work/oversight-council.jpg", link: "work-oversight.html" },

    { place: "Engineering Service Community",
      role: "Human Resources Staff",
      start: "2025-04", end: "2026-01",
      skills: ["Recruitment", "Onboarding", "Member Development"],
      image: PLACEHOLDER, link: "org-esc.html" },

    { place: "HMTF Unitel",
      role: "Cadre Development Department Staff",
      start: "2024-09", end: "2025-05",
      skills: ["Member Development", "Program Leadership"],
      image: PLACEHOLDER, link: "org-hmtf.html" },

    { place: "Kalibrasi 2024 Organizing Committee",
      role: "Mentor",
      start: "2024", end: "2024",
      skills: ["Mentoring", "Leadership"],
      image: PLACEHOLDER, link: "org-kalibrasi.html" },

    { place: "Student English Society",
      role: "Member",
      start: "2022-09", end: "2023-09",
      skills: ["English Communication", "Public Speaking"],
      image: PLACEHOLDER, link: "org-ses.html" },
  ],

  /* ---------- Projects (urutan = urutan tampil, paling relevan di atas) ----------
     category: label di dalam penanda "{" di sisi kiri.
     start/end: null kalau periodenya tidak tercantum di CV. */
  projects: [
    { title: "Pump RPM Monitoring",
      category: "Equipment Monitoring",
      start: "2025-09", end: "2026-01",
      text: "TCRT5000 optical-sensor RPM monitoring for a centrifugal pump, with readings sent to Firebase and a live Kodular display.",
      tags: ["TCRT5000", "Firebase", "Kodular", "Machine Learning"],
      image: "assets/projects/pump-field.jpg", link: "project-pump.html" },

    { title: "Environmental Sensor Calibration and Data Processing",
      category: "Calibration",
      start: "2026-02", end: "2026-06",
      text: "Six parameters across seven wearable units calibrated against reference instruments; quadratic PM and linear TVOC, temperature and humidity corrections.",
      tags: ["Calibration", "Python", "Excel", "Data Analysis"],
      image: "assets/projects/kalibrasi-chamber-real.jpg", link: "project-kalibrasi.html" },

    { title: "AirGradien — Sensor Assembly, Testing and Calibration",
      category: "Instrumentation",
      start: "2026-02", end: "2026-06",
      text: "Seven wearable sensor units built on ESP32/ESP8266 with SPS30, ENS160 and AHT21, with C/C++ firmware and Wi-Fi connectivity.",
      tags: ["ESP32", "SPS30", "ENS160", "AHT21", "C/C++"],
      image: "assets/projects/aqms-device.jpg", link: "project-aqms.html" },

    { title: "TrapGradien — Sensor Integration and IoT Air Quality Monitoring",
      category: "Instrumentation",
      start: "2025-09", end: "2025-12",
      text: "Sensor selection, a Wemos D1 mini PCB in KiCad, and a calibration chamber with a Mass Flow Controller over Modbus RTU/RS-485.",
      tags: ["KiCad", "Modbus RTU", "RS-485", "Wemos D1 mini"],
      image: "assets/projects/trapgradien-pcb.png", link: "project-trapgradien.html" },

    { title: "ROV — Electrical Schematics, Power Distribution and Enclosure",
      category: "Electrical",
      start: "2025-06", end: "2025-08",
      text: "Pixhawk 6C electrical block architecture and power-distribution documentation, plus enclosures designed in Autodesk Inventor.",
      tags: ["Pixhawk 6C", "Power Distribution", "Autodesk Inventor", "Qt Creator"],
      image: "assets/projects/armor-prototype.jpg", link: "project-armor.html" },

    { title: "Sensor Testing — Effect of Motion on Particulate Measurement",
      category: "Measurement Analysis",
      start: "2026-02", end: "2026-06",
      text: "Chamber, rotation-platform and field tests comparing two dynamic units with three static controls to examine motion-related deviation.",
      tags: ["PM2.5", "PM10", "Python", "Data Analysis"],
      image: "assets/projects/motion-scatter-chamber.png", link: "project-motion-effect.html" },

    { title: "Human Activity Recognition (HAR)",
      category: "Machine Learning",
      start: "2025-09", end: "2026-07",
      text: "Activity recognition integrated into the IoT wearable air-quality monitoring final project.",
      tags: ["Machine Learning"],
      image: "assets/projects/har-aktivitas.png", link: "project-har.html" },

    { title: "Kost-In",
      category: "Software",
      start: "2023-04", end: "2023-04",
      text: "A C application project, through which I was selected as a C Programming teaching assistant.",
      tags: ["C Programming"],
      image: "assets/projects/kostin-logo.png", fit: "contain", link: "project-kostin.html" },
  ],

  /* ---------- Certificates ----------
     images: satu atau lebih gambar (depan/belakang). [] = belum ada gambar. */
  certificates: [
    { category: "Work Experience", title: "Measurement Laboratory Coordinator & Teaching Assistant",
      issuer: "Instrumentation System Laboratory, Telkom University", date: "2026",
      images: ["assets/certificates/teach-1a.jpg", "assets/certificates/teach-1b.jpg"] },
    { category: "Work Experience", title: "MBKM Research Internship",
      issuer: "PUI-PT Intelligent Sensing-IoT, Telkom University", date: "2026",
      images: ["assets/certificates/pelatihan-3.jpg"] },
    { category: "Work Experience", title: "Internship Certificate",
      issuer: "PT SAS Aero Sishan", date: "2026",
      images: ["assets/certificates/pelatihan-2.jpg"] },
    { category: "Work Experience", title: "Electrical Circuits Teaching Assistant & Practicum Division Member",
      issuer: "Instrumentation System Laboratory, Telkom University", date: "2025",
      images: ["assets/certificates/teach-2a.jpg", "assets/certificates/teach-2b.jpg"] },
    { category: "Work Experience", title: "Electronics Teaching Assistant & Practicum Division Member",
      issuer: "Instrumentation System Laboratory, Telkom University", date: "2025",
      images: ["assets/certificates/teach-3a.jpg", "assets/certificates/teach-3b.jpg"] },
    { category: "Work Experience", title: "Programming Laboratory Teaching Assistant & Rules and Discipline Committee Member",
      issuer: "Basic Computing Laboratory, Telkom University", date: "2024",
      images: ["assets/certificates/teach-4a.jpg", "assets/certificates/teach-4b.jpg"] },

    { category: "Workshop", title: "Digital Learning Study Group",
      issuer: "MBC Lab, Telkom University", date: "2024",
      images: ["assets/certificates/pelatihan-1.jpg"] },
    { category: "Workshop", title: "Using the Terminal/CMD for Development",
      issuer: "Codepolitan", date: "2024",
      images: ["assets/certificates/pelatihan-4.jpg"] },

    { category: "Language", title: "English Proficiency Test (EPrT) — 570/677, CEFR B2",
      issuer: "Telkom University Language Center", date: "2026",
      images: ["assets/certificates/bahasa-1a.jpg", "assets/certificates/bahasa-1b.jpg"] },
    { category: "Language", title: "Basic Intensive English Program",
      issuer: "Language Center (LC), Kampung Inggris Pare", date: "2022",
      images: [] },

    { category: "Entrepreneurship", title: "UMKM Semut Corner — FKS Business Fair x Api Karya 2024",
      issuer: "BEM FKS, Telkom University", date: "Nov 2024",
      images: ["assets/certificates/wirausaha-1a.jpg", "assets/certificates/wirausaha-1b.jpg"] },

    { category: "Organization", title: "Certificate of Appreciation — Mentor Division, Kalibrasi 2024 Organizing Committee",
      issuer: "HMTF, Telkom University", date: "2025",
      images: ["assets/certificates/org-1a.jpg", "assets/certificates/org-1b.jpg"] },
    { category: "Organization", title: "Cadre Development Department Staff — HMTF Unitel, 2024/2025 Board Term",
      issuer: "HMTF, Telkom University", date: "2025",
      images: ["assets/certificates/org-2a.jpg", "assets/certificates/org-2b.jpg"] },
  ],

  /* ---------- Blog (CONTOH — ganti dengan tulisan Anda) ---------- */
  blog: [
    { title: "Sample post — replace this title", date: "2026-10",
      text: "This is a sample card. Replace the title, summary, date and image with your own post.",
      image: PLACEHOLDER, link: null },
    { title: "Sample post — second example", date: "2026-10",
      text: "Blog cards are generated from the blog list in js/data.js.",
      image: PLACEHOLDER, link: null },
    { title: "Sample post — third example", date: "2026-10",
      text: "Set link to a page such as \"blog-my-post.html\" once the post exists.",
      image: PLACEHOLDER, link: null },
  ],
};
