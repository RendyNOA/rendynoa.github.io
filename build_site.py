import base64, os

with open('/home/claude/avatar.jpg','rb') as f:
    AVATAR_B64 = base64.b64encode(f.read()).decode()
with open('/home/claude/logo72.jpg','rb') as f:
    LOGO_B64 = base64.b64encode(f.read()).decode()

OUT = '/home/claude/site'
os.makedirs(OUT, exist_ok=True)

ICON_STROKE = "#D9AE6E"
_C = f'stroke="{ICON_STROKE}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"'

ICONS = {
"organisasi": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M5 20 L24 6 L43 20" {_C}/>
<line x1="4" y1="21" x2="44" y2="21" {_C}/>
<line x1="10" y1="24" x2="10" y2="37" {_C}/>
<line x1="18" y1="24" x2="18" y2="37" {_C}/>
<line x1="30" y1="24" x2="30" y2="37" {_C}/>
<line x1="38" y1="24" x2="38" y2="37" {_C}/>
<line x1="4" y1="41" x2="44" y2="41" stroke="{ICON_STROKE}" stroke-width="3" stroke-linecap="round"/>
</svg>''',
"lab": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<line x1="19" y1="6" x2="19" y2="17" {_C}/>
<line x1="29" y1="6" x2="29" y2="17" {_C}/>
<line x1="16" y1="6" x2="32" y2="6" {_C}/>
<path d="M19 17 L9 36 Q24 43 39 36 L29 17" {_C}/>
<line x1="13" y1="30" x2="35" y2="30" {_C}/>
<circle cx="21" cy="35" r="1.4" fill="{ICON_STROKE}" stroke="none"/>
<circle cx="27" cy="37" r="1" fill="{ICON_STROKE}" stroke="none"/>
</svg>''',
"wirausaha": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M18 18 v-4 a6 6 0 0 1 12 0 v4" {_C}/>
<rect x="7" y="18" width="34" height="21" rx="3" {_C}/>
<line x1="7" y1="28" x2="41" y2="28" {_C}/>
<rect x="20.5" y="25.5" width="7" height="5" rx="1" {_C}/>
</svg>''',
"bahasa": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<rect x="6" y="8" width="36" height="24" rx="7" {_C}/>
<path d="M14 32 L11 41 L22 32" {_C}/>
<line x1="13" y1="16" x2="35" y2="16" {_C}/>
<line x1="13" y1="22" x2="29" y2="22" {_C}/>
</svg>''',
"embedded": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="14" width="20" height="20" rx="3" {_C}/>
<rect x="20" y="20" width="8" height="8" {_C}/>
<line x1="20" y1="14" x2="20" y2="9" {_C}/>
<line x1="28" y1="14" x2="28" y2="9" {_C}/>
<line x1="20" y1="34" x2="20" y2="39" {_C}/>
<line x1="28" y1="34" x2="28" y2="39" {_C}/>
<line x1="14" y1="20" x2="9" y2="20" {_C}/>
<line x1="14" y1="28" x2="9" y2="28" {_C}/>
<line x1="34" y1="20" x2="39" y2="20" {_C}/>
<line x1="34" y1="28" x2="39" y2="28" {_C}/>
</svg>''',
"iot": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<circle cx="24" cy="37" r="2.6" fill="{ICON_STROKE}" stroke="none"/>
<line x1="24" y1="34" x2="24" y2="30" {_C}/>
<path d="M16,28 A11,11 0 0 1 32,28" {_C}/>
<path d="M10,20 A20,20 0 0 1 38,20" {_C}/>
</svg>''',
"instrumentation": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M9,33 A15,15 0 0 1 39,33" {_C}/>
<line x1="6" y1="33" x2="42" y2="33" {_C}/>
<line x1="24" y1="33" x2="17" y2="20" {_C}/>
<circle cx="24" cy="33" r="2.2" fill="{ICON_STROKE}" stroke="none"/>
<line x1="12" y1="24" x2="14.5" y2="26" {_C}/>
<line x1="36" y1="24" x2="33.5" y2="26" {_C}/>
</svg>''',
"data": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M14,6 L28,6 L34,12 L34,42 L14,42 Z" {_C}/>
<path d="M28,6 L28,12 L34,12" {_C}/>
<line x1="18" y1="20" x2="30" y2="20" {_C}/>
<line x1="18" y1="26" x2="30" y2="26" {_C}/>
<line x1="18" y1="32" x2="25" y2="32" {_C}/>
</svg>''',
"pelatihan": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M4,18 L24,9 L44,18 L24,27 Z" {_C}/>
<path d="M13,22 L13,31 Q24,37 35,31 L35,22" {_C}/>
<line x1="44" y1="18" x2="44" y2="29" {_C}/>
<circle cx="44" cy="31" r="2" fill="{ICON_STROKE}" stroke="none"/>
</svg>''',
"kalibrasi-banner": f'''<svg viewBox="0 0 200 140" xmlns="http://www.w3.org/2000/svg">
<rect x="8" y="14" width="184" height="112" rx="8" {_C}/>
<rect x="30" y="56" width="34" height="34" rx="4" {_C}/>
<line x1="38" y1="56" x2="38" y2="49" {_C}/>
<line x1="48" y1="56" x2="48" y2="49" {_C}/>
<line x1="56" y1="56" x2="56" y2="49" {_C}/>
<line x1="38" y1="90" x2="38" y2="97" {_C}/>
<line x1="48" y1="90" x2="48" y2="97" {_C}/>
<line x1="56" y1="90" x2="56" y2="97" {_C}/>
<line x1="70" y1="73" x2="126" y2="73" stroke="{ICON_STROKE}" stroke-width="2" stroke-dasharray="5 6" fill="none"/>
<path d="M120,67 L127,73 L120,79" fill="none" stroke="{ICON_STROKE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="160" cy="73" r="24" {_C}/>
<line x1="160" y1="73" x2="160" y2="58" {_C}/>
<line x1="160" y1="73" x2="171" y2="80" {_C}/>
<circle cx="160" cy="73" r="2.4" fill="{ICON_STROKE}" stroke="none"/>
<circle cx="98" cy="38" r="11" fill="none" stroke="{ICON_STROKE}" stroke-width="2"/>
<path d="M92,38 L96,43 L105,32" fill="none" stroke="{ICON_STROKE}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>''',
}

def write_icons():
    icon_dir = os.path.join(OUT, "assets", "icons")
    os.makedirs(icon_dir, exist_ok=True)
    for name, svg in ICONS.items():
        with open(os.path.join(icon_dir, f"{name}.svg"), "w") as f:
            f.write(svg)

write_icons()

SHARED_CSS = """
:root{
  --bg:#1E1810; --panel:#2A2116; --panel-raised:#392D1E;
  --grid-line: rgba(214,178,120,0.14);
  --cyan:#D9AE6E; --amber:#C99A65; --danger:#C06A4E;
  --text:#EFE5D4; --muted:#AB9A7C;
}
*{margin:0;padding:0;box-sizing:border-box;}
body{
  background:
    radial-gradient(ellipse at 50% 0%, rgba(210,165,100,0.20), transparent 55%),
    radial-gradient(ellipse at 100% 100%, rgba(120,80,45,0.35), transparent 60%),
    radial-gradient(ellipse at 0% 100%, rgba(60,45,28,0.5), transparent 55%),
    var(--bg);
  color:var(--text); font-family:'IBM Plex Sans', sans-serif; min-height:100vh;
  position:relative;
}
body::before{
  content:"";
  position:fixed; inset:-100px; z-index:1; pointer-events:none;
  opacity:0.06; mix-blend-mode:overlay;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
body::after{
  content:"";
  position:fixed; inset:0; z-index:2; pointer-events:none;
  box-shadow:inset 0 0 180px 50px rgba(0,0,0,0.5);
}
.mono{font-family:'IBM Plex Mono', monospace;}
a{color:inherit;}
.corner{position:fixed;width:16px;height:16px;border-color:var(--muted);opacity:0.45;z-index:5;}
.corner.tl{top:14px;left:14px;border-top:2px solid;border-left:2px solid;}
.corner.tr{top:14px;right:14px;border-top:2px solid;border-right:2px solid;}
.corner.bl{bottom:14px;left:14px;border-bottom:2px solid;border-left:2px solid;}
.corner.br{bottom:14px;right:14px;border-bottom:2px solid;border-right:2px solid;}

.glow-orb{display:none;}

/* SITE NAV */
.site-nav{
  position:sticky; top:0; z-index:20;
  background:rgba(30,24,16,0.92); backdrop-filter:blur(8px);
  border-bottom:1px solid var(--grid-line);
  display:flex; align-items:center; justify-content:space-between;
  padding:12px 24px; flex-wrap:wrap; gap:12px;
}
.site-nav .brand{display:flex; align-items:center; gap:10px; text-decoration:none;}
.site-nav .brand img{width:34px; height:34px; border-radius:50%; border:1px solid var(--cyan); object-fit:cover;}
.site-nav .brand span{font-family:'IBM Plex Mono', monospace; font-size:0.85rem; font-weight:600; color:var(--text);}
.site-nav nav{display:flex; gap:4px; flex-wrap:wrap;}
.site-nav nav a{
  font-family:'IBM Plex Mono', monospace; font-size:0.72rem; letter-spacing:0.06em;
  color:var(--muted); text-decoration:none; padding:8px 14px; border:1px solid transparent;
  transition:all .15s ease;
}
.site-nav nav a:hover{color:var(--text);}
.site-nav nav a.active{color:var(--cyan); border-color:var(--cyan); background:rgba(201,168,118,0.08);}

main{max-width:960px; margin:0 auto; padding:0 20px 80px; position:relative; z-index:1;}

/* PAGE HEADER (non-home pages) */
.section-eyebrow{
  font-family:'IBM Plex Mono', monospace; font-size:0.72rem; letter-spacing:0.14em;
  color:var(--cyan); text-transform:uppercase; margin-bottom:10px;
}
.section-title{font-size:2rem; font-weight:700; margin-bottom:10px;}
.section-intro{color:var(--muted); max-width:600px; line-height:1.7; margin-bottom:10px;}

/* HERO (home only) */
.hero{text-align:center; padding:0 0 34px; position:relative; z-index:1;}
.hero-banner{
  position:relative; height:200px; margin:0 -20px 0; overflow:hidden;
  background:var(--panel-raised);
  border-bottom:1px solid var(--grid-line);
}
.hero-banner img{width:100%; height:100%; object-fit:cover; display:block;}
.hero-banner .banner-overlay{
  position:absolute; inset:0;
  background:linear-gradient(180deg, rgba(30,24,16,0.15), var(--bg) 92%);
}
.hero-banner .banner-placeholder{
  display:none; position:absolute; inset:0; flex-direction:column; align-items:center; justify-content:center;
  gap:8px; color:var(--muted);
  background:repeating-linear-gradient(135deg, rgba(214,178,120,0.05) 0 10px, transparent 10px 20px);
}
.hero-banner .banner-placeholder .ph-icon{font-size:1.8rem; opacity:0.6;}
.hero-banner .banner-placeholder .ph-text{font-size:0.75rem; font-family:'IBM Plex Mono', monospace;}
.hero-banner .banner-placeholder .ph-path{font-family:'IBM Plex Mono', monospace; font-size:0.7rem; color:var(--cyan);}
.avatar-wrap{position:relative; width:148px; height:148px; margin:-84px auto 24px;}
.avatar-ring{position:absolute; inset:0; border-radius:50%; border:1px solid var(--cyan); opacity:0.4; animation:pulseRing 2.6s ease-out infinite;}
@keyframes pulseRing{0%{transform:scale(0.92); opacity:0.5;} 70%{transform:scale(1.18); opacity:0;} 100%{transform:scale(1.18); opacity:0;}}
.avatar{width:132px; height:132px; border-radius:50%; position:absolute; top:8px; left:8px; object-fit:cover; border:2px solid var(--cyan); box-shadow:0 4px 16px rgba(0,0,0,0.35);}
.eyebrow-chip{display:inline-block; font-family:'IBM Plex Mono', monospace; font-size:0.7rem; letter-spacing:0.14em; color:var(--cyan); border:1px solid rgba(201,168,118,0.3); background:rgba(201,168,118,0.06); padding:5px 14px; margin-bottom:16px; text-transform:uppercase;}
.hero-name{font-size:clamp(2rem,4.4vw,2.8rem); font-weight:700; color:var(--text);}
.hero-role{color:var(--muted); font-size:1.02rem; margin-top:10px; max-width:540px; margin-left:auto; margin-right:auto; line-height:1.6;}
.social-row{display:flex; justify-content:center; gap:12px; margin-top:26px; flex-wrap:wrap;}
.social-btn{display:flex; align-items:center; gap:8px; font-family:'IBM Plex Mono', monospace; font-size:0.78rem; background:var(--panel); border:1px solid var(--grid-line); color:var(--text); text-decoration:none; padding:10px 16px; transition:all .15s ease;}
.social-btn:hover{border-color:var(--cyan); color:var(--cyan);}
.social-btn svg{width:15px; height:15px; fill:currentColor;}

.section{padding:44px 0 44px 28px; border-top:1px solid var(--grid-line); position:relative;}
.section::before{
  content:""; position:absolute; left:0; top:44px; bottom:44px; width:1px;
  background:linear-gradient(to bottom, var(--cyan), var(--grid-line) 70%, transparent);
}
.section::after{
  content:""; position:absolute; left:-3px; top:40px; width:7px; height:7px;
  border-radius:50%; background:var(--cyan);
}
.page-header{padding:50px 0 10px 28px; position:relative;}
.page-header::before{
  content:""; position:absolute; left:0; top:6px; bottom:14px; width:1px;
  background:linear-gradient(to bottom, var(--cyan), var(--grid-line) 70%, transparent);
}
.page-header::after{
  content:""; position:absolute; left:-3px; top:2px; width:7px; height:7px;
  border-radius:50%; background:var(--cyan);
}
.about-text{color:var(--text); opacity:0.85; line-height:1.85; font-size:1rem; max-width:760px;}
.stat-row{display:flex; gap:34px; margin-top:26px; flex-wrap:wrap;}
.stat{font-family:'IBM Plex Mono', monospace;}
.stat-num{font-size:1.5rem; color:var(--cyan); font-weight:700;}
.stat-label{font-size:0.72rem; color:var(--muted); letter-spacing:0.06em;}

.cta-row{display:flex; gap:12px; margin-top:30px; flex-wrap:wrap;}
.cta-btn{
  font-family:'IBM Plex Mono', monospace; font-size:0.78rem; letter-spacing:0.05em;
  text-decoration:none; padding:12px 20px; border:1px solid var(--cyan); color:var(--cyan);
  transition:all .15s ease;
}
.cta-btn:hover{background:var(--cyan); color:var(--bg);}
.cta-btn.ghost{border-color:var(--grid-line); color:var(--text);}
.cta-btn.ghost:hover{border-color:var(--muted); background:transparent; color:var(--text);}

/* WORK HISTORY PAGE */
.exp-item{display:grid; grid-template-columns:150px 1fr; gap:22px; padding:24px 0; border-bottom:1px solid var(--grid-line); text-decoration:none; color:inherit; transition:opacity .15s ease;}
.exp-item:last-child{border-bottom:none;}
.exp-item:hover{opacity:0.75;}
.exp-item:hover .exp-more{color:var(--cyan);}
.exp-more{font-family:'IBM Plex Mono', monospace; font-size:0.74rem; color:var(--muted); margin-top:10px; display:inline-block;}
.exp-date{font-family:'IBM Plex Mono', monospace; font-size:0.78rem; color:var(--cyan);}
.exp-role{font-weight:600; font-size:1.05rem; margin-bottom:3px;}
.exp-org{color:var(--muted); font-size:0.88rem; margin-bottom:10px;}
.exp-desc{color:var(--text); opacity:0.8; font-size:0.9rem; line-height:1.7;}
.exp-desc ul{margin:8px 0 0 18px;}
.exp-desc li{margin-bottom:4px;}
@media(max-width:640px){.exp-item{grid-template-columns:1fr; gap:6px;}}

/* SKILLS PAGE */
.skills-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(200px,1fr)); gap:16px;}
.skill-card{background:var(--panel); border:1px solid var(--grid-line); padding:26px 20px; text-align:center; transition:border-color .15s ease, transform .15s ease; box-shadow:0 6px 18px rgba(0,0,0,0.3); cursor:pointer;}
.skill-card:hover{border-color:var(--cyan); transform:translateY(-3px);}
.skill-icon{font-size:2rem; margin-bottom:14px;}
.skill-icon-img{width:44px; height:44px; margin:0 auto 14px; display:block;}
.skill-name{font-weight:600; font-size:1.02rem; margin-bottom:8px;}
.skill-desc{color:var(--muted); font-size:0.82rem; line-height:1.5; margin-bottom:14px;}
.tag-wrap{display:flex; flex-wrap:wrap; gap:6px; justify-content:center;}
.tag{font-family:'IBM Plex Mono', monospace; font-size:0.68rem; background:rgba(214,178,120,0.10); color:var(--text); padding:4px 10px;}

/* PROJECTS GRID (clickable -> new page) */
.project-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(260px,1fr)); gap:18px;}
.project-card{background:var(--panel); border:1px solid var(--grid-line); overflow:hidden; text-decoration:none; display:block; transition:border-color .15s ease, transform .15s ease; box-shadow:0 6px 18px rgba(0,0,0,0.3);}
.project-card:hover{border-color:var(--cyan); transform:translateY(-3px);}
.project-banner{height:90px; display:flex; align-items:center; justify-content:center; font-size:2rem; border-bottom:1px solid var(--grid-line);}
.project-card:nth-child(1) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(201,168,118,0.14));}
.project-card:nth-child(2) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(185,142,92,0.14));}
.project-card:nth-child(3) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(176,100,74,0.14));}
.project-card:nth-child(4) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(150,160,120,0.14));}
.project-card:nth-child(5) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(120,130,160,0.14));}
.project-card:nth-child(6) .project-banner{background:linear-gradient(135deg, var(--panel-raised), rgba(160,120,150,0.14));}
.project-body{padding:20px;}
.project-title{font-weight:600; font-size:1rem; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;}
.project-chevron{color:var(--cyan); font-family:'IBM Plex Mono', monospace; font-size:0.9rem;}
.project-summary{color:var(--muted); font-size:0.85rem; line-height:1.6;}
.tag-row{display:flex; gap:6px; flex-wrap:wrap; margin-top:12px;}
.tag-amber{font-family:'IBM Plex Mono', monospace; font-size:0.68rem; color:var(--amber); border:1px solid rgba(185,142,92,0.4); padding:3px 9px;}

/* PROJECT DETAIL PAGE */
.back-link{display:inline-flex; align-items:center; gap:6px; font-family:'IBM Plex Mono', monospace; font-size:0.78rem; color:var(--cyan); text-decoration:none; margin-bottom:22px;}
.back-link:hover{text-decoration:underline;}
.detail-banner{height:180px; display:flex; align-items:center; justify-content:center; font-size:4rem; border:1px solid var(--grid-line); background:linear-gradient(135deg, var(--panel-raised), rgba(201,168,118,0.12)); margin-bottom:28px; overflow:hidden;}
.detail-banner img{max-height:70%; max-width:60%; object-fit:contain;}
.detail-banner img.banner-photo{width:100%; height:100%; max-width:100%; max-height:100%; object-fit:cover; object-position:center 25%;}
.detail-meta{display:flex; gap:28px; flex-wrap:wrap; margin:22px 0 28px; padding:20px; background:var(--panel); border:1px solid var(--grid-line);}
.detail-meta div{font-family:'IBM Plex Mono', monospace;}
.detail-meta .k{font-size:0.68rem; color:var(--muted); letter-spacing:0.08em; margin-bottom:4px;}
.detail-meta .v{font-size:0.88rem; color:var(--text);}
.detail-body p{color:var(--text); opacity:0.85; line-height:1.85; margin-bottom:16px; max-width:760px;}
.other-projects{margin-top:50px; padding-top:30px; border-top:1px solid var(--grid-line);}
.other-projects .label{font-family:'IBM Plex Mono', monospace; font-size:0.72rem; color:var(--muted); letter-spacing:0.1em; margin-bottom:14px;}

.thesis-note{
  margin:24px 0; padding:16px 18px; background:rgba(201,168,118,0.06);
  border:1px solid rgba(201,168,118,0.25); font-size:0.85rem; color:var(--text); line-height:1.7;
}
.thesis-note b{color:var(--cyan);}
.thesis-note .tn-links{display:flex; gap:10px; flex-wrap:wrap; margin-top:10px;}
.thesis-note .tn-links a{
  font-family:'IBM Plex Mono', monospace; font-size:0.74rem; color:var(--cyan);
  text-decoration:none; border:1px solid rgba(201,168,118,0.35); padding:5px 12px;
}
.thesis-note .tn-links a:hover{background:rgba(201,168,118,0.1);}

.stat-mini-row{display:flex; gap:28px; flex-wrap:wrap; margin:20px 0;}
.stat-mini{font-family:'IBM Plex Mono', monospace;}
.stat-mini .sm-num{font-size:1.3rem; color:var(--cyan); font-weight:700;}
.stat-mini .sm-label{font-size:0.68rem; color:var(--muted); letter-spacing:0.05em;}
.data-table{width:100%; border-collapse:collapse; margin:18px 0 6px; font-size:0.88rem;}
.data-table th, .data-table td{padding:10px 14px; border:1px solid var(--grid-line); text-align:left;}
.data-table th{font-family:'IBM Plex Mono', monospace; font-size:0.72rem; letter-spacing:0.06em; color:var(--cyan); text-transform:uppercase; background:var(--panel-raised);}
.data-table td{color:var(--text); opacity:0.9;}
.data-table tr:nth-child(even) td{background:rgba(201,168,118,0.04);}

.narrative-section{margin:34px 0;}
.narrative-section:first-child{margin-top:0;}
.narrative-heading{font-size:1.25rem; font-weight:700; color:var(--text); margin-bottom:12px;}
.narrative-section p{color:var(--text); opacity:0.85; line-height:1.85; font-size:0.95rem; margin-bottom:0;}
.narrative-list{list-style:none; margin:14px 0 0; padding:0;}
.narrative-list li{
  color:var(--text); opacity:0.85; line-height:1.8; font-size:0.95rem;
  padding-left:18px; position:relative; margin-bottom:14px;
}
.narrative-list li:last-child{margin-bottom:0;}
.narrative-list li::before{content:"—"; position:absolute; left:0; color:var(--cyan);}
.narrative-list li b{color:var(--cyan); font-weight:600;}
.narrative-figure{margin:26px 0;}
.narrative-figure img{max-width:100%; max-height:380px; width:auto; height:auto; display:block; margin:0 auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;}
.narrative-figure figcaption{
  font-family:'IBM Plex Mono', monospace; font-size:0.76rem; color:var(--muted);
  margin-top:8px; text-align:center; line-height:1.5;
}

.chart-gallery{margin:28px 0;}
.chart-figure{margin-bottom:24px;}
.chart-figure:last-child{margin-bottom:0;}
.chart-figure img{width:100%; height:auto; display:block; border:1px solid var(--grid-line); background:#fff;}
.chart-figure figcaption{
  font-family:'IBM Mono', monospace; font-size:0.78rem; color:var(--muted);
  margin-top:8px; text-align:center; line-height:1.5;
}
.analysis-block{
  margin-top:36px; padding:26px; background:var(--panel);
  border:1px solid rgba(201,168,118,0.35); border-left:3px solid var(--cyan);
}
.analysis-item{margin-bottom:22px;}
.analysis-item:last-child{margin-bottom:0;}
.analysis-title{font-weight:700; font-size:0.98rem; margin-bottom:10px; color:var(--text);}
.analysis-item p{color:var(--text); opacity:0.85; line-height:1.8; font-size:0.9rem; margin:0;}
.analysis-item b{color:var(--cyan); font-weight:600;}

/* PROJECT PHOTO GALLERY */
.photo-gallery{display:grid; grid-template-columns:repeat(auto-fit, minmax(200px,1fr)); gap:14px; margin:24px 0 30px;}
.photo-slot{position:relative; aspect-ratio:4/3; border:1px solid var(--grid-line); overflow:hidden; background:var(--panel);}
.photo-slot img{width:100%; height:100%; object-fit:cover; display:block;}
.photo-placeholder{
  display:none; position:absolute; inset:0; flex-direction:column; align-items:center; justify-content:center;
  gap:8px; border:1px dashed var(--grid-line); color:var(--muted); text-align:center; padding:14px;
  background:repeating-linear-gradient(135deg, rgba(214,178,120,0.06) 0 10px, transparent 10px 20px);
}
.photo-placeholder .ph-icon{font-size:1.6rem; opacity:0.6;}
.photo-placeholder .ph-text{font-size:0.72rem; line-height:1.5;}
.photo-placeholder .ph-path{font-family:'IBM Plex Mono', monospace; font-size:0.68rem; color:var(--cyan); word-break:break-all;}

/* PHOTO CAROUSEL (work detail pages) */
.photo-carousel{margin:24px 0 30px;}
.carousel-viewport{position:relative; overflow:hidden; border:1px solid var(--grid-line); background:var(--panel); aspect-ratio:16/9;}
.carousel-track{display:flex; height:100%; transition:transform .35s ease;}
.carousel-slide{flex:0 0 100%; height:100%; position:relative;}
.carousel-slide img{width:100%; height:100%; object-fit:cover; display:block;}
.carousel-btn{
  position:absolute; top:50%; transform:translateY(-50%);
  width:36px; height:36px; border-radius:50%;
  background:rgba(20,15,10,0.5); border:1px solid var(--grid-line); color:var(--text);
  display:flex; align-items:center; justify-content:center; cursor:pointer; font-size:1.1rem;
  z-index:3; transition:background .15s ease; line-height:1;
}
.carousel-btn:hover{background:rgba(20,15,10,0.75);}
.carousel-btn.prev{left:10px;}
.carousel-btn.next{right:10px;}
.carousel-dots{display:flex; gap:8px; justify-content:center; margin-top:14px;}
.carousel-dot{width:7px; height:7px; border-radius:50%; background:var(--grid-line); cursor:pointer; border:none; padding:0;}
.carousel-dot.active{background:var(--cyan);}
.carousel-caption{margin-top:12px; font-size:0.86rem; color:var(--muted); text-align:center; min-height:1.4em; font-family:'IBM Plex Mono', monospace;}

/* SKILL MODAL POPUP */
.skill-modal-overlay{
  position:fixed; inset:0; z-index:90; background:rgba(10,7,4,0.65);
  display:none; align-items:center; justify-content:center; padding:20px;
}
.skill-modal-overlay.open{display:flex;}
.skill-modal{
  background:var(--panel-raised); border:1px solid var(--grid-line);
  max-width:420px; width:100%; padding:26px; position:relative;
  box-shadow:0 20px 50px rgba(0,0,0,0.5);
}
.skill-modal-close{
  position:absolute; top:14px; right:14px; width:28px; height:28px;
  border-radius:50%; border:1px solid var(--grid-line); background:transparent;
  color:var(--muted); cursor:pointer; font-size:0.9rem; display:flex; align-items:center; justify-content:center;
}
.skill-modal-close:hover{color:var(--text); border-color:var(--cyan);}
.skill-modal-title{font-weight:700; font-size:1.1rem; margin-bottom:6px;}
.skill-modal-label{font-family:'IBM Plex Mono', monospace; font-size:0.7rem; letter-spacing:0.1em; color:var(--muted); text-transform:uppercase; margin:16px 0 8px;}
.skill-modal-label:first-of-type{margin-top:0;}
.skill-modal-story{font-size:0.86rem; color:var(--text); opacity:0.85; line-height:1.6; margin-bottom:4px;}
.tool-level-row{display:flex; justify-content:space-between; align-items:center; padding:8px 0; border-bottom:1px solid var(--grid-line); font-size:0.85rem;}
.tool-level-row:last-child{border-bottom:none;}
.tool-level-row .t-name{color:var(--text);}
.tool-level-row .t-level{font-family:'IBM Plex Mono', monospace; font-size:0.72rem; color:var(--cyan); border:1px solid rgba(201,168,118,0.3); padding:2px 9px;}
.skill-modal-link{
  display:flex; align-items:center; justify-content:space-between; gap:10px;
  padding:14px 16px; background:var(--panel); border:1px solid var(--grid-line);
  text-decoration:none; color:var(--text); margin-bottom:10px; transition:border-color .15s ease;
}
.skill-modal-link:last-child{margin-bottom:0;}
.skill-modal-link:hover{border-color:var(--cyan);}
.skill-modal-link .l-title{font-size:0.9rem; font-weight:600;}
.skill-modal-link .l-arrow{color:var(--cyan); font-family:'IBM Plex Mono', monospace;}

/* CERTIFICATES PAGE - folder style */
.folder-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(220px,1fr)); gap:20px;}
.cert-folder{
  position:relative; background:var(--panel); border:1px solid var(--grid-line);
  padding:32px 20px 24px; text-align:center; cursor:pointer; overflow:hidden;
  transition:border-color .15s ease, transform .15s ease;
}
.cert-folder:hover{border-color:var(--cyan); transform:translateY(-4px);}
.cert-folder::before{
  content:""; position:absolute; top:0; left:20px; width:56px; height:6px;
  background:var(--cyan); opacity:0.55; border-radius:0 0 4px 4px;
}
.cert-folder-icon{font-size:2.6rem; margin-bottom:16px; opacity:0.9;}
.cert-folder-icon-img{width:48px; height:48px; margin:0 auto 16px; display:block;}
.cert-folder-name{font-weight:700; font-size:1.05rem; margin-bottom:6px;}
.cert-folder-count{
  font-family:'IBM Plex Mono', monospace; font-size:0.7rem; color:var(--muted);
  letter-spacing:0.08em; text-transform:uppercase;
}

.cert-modal-overlay{
  position:fixed; inset:0; z-index:90; background:rgba(10,7,4,0.65);
  display:none; align-items:center; justify-content:center; padding:20px;
}
.cert-modal-overlay.open{display:flex;}
.cert-modal{
  background:var(--panel-raised); border:1px solid var(--grid-line);
  max-width:520px; width:100%; max-height:80vh; padding:26px; position:relative;
  box-shadow:0 20px 50px rgba(0,0,0,0.5); display:flex; flex-direction:column;
}
.cert-modal-close{
  position:absolute; top:14px; right:14px; width:28px; height:28px;
  border-radius:50%; border:1px solid var(--grid-line); background:transparent;
  color:var(--muted); cursor:pointer; font-size:0.9rem; display:flex; align-items:center; justify-content:center;
}
.cert-modal-close:hover{color:var(--text); border-color:var(--cyan);}
.cert-modal-title{font-weight:700; font-size:1.1rem; margin-bottom:16px; flex:0 0 auto;}
.cert-modal-scroll{overflow-y:auto; flex:1 1 auto; margin:0 -6px; padding:0 6px;}
.cert-modal-item{display:flex; gap:14px; padding:14px 0; border-bottom:1px solid var(--grid-line); cursor:pointer; transition:opacity .15s ease;}
.cert-modal-item:hover{opacity:0.75;}
.cert-modal-item:last-child{border-bottom:none;}

.cert-lightbox-overlay{
  position:fixed; inset:0; z-index:95; background:rgba(5,3,2,0.85);
  display:none; align-items:center; justify-content:center; padding:30px;
}
.cert-lightbox-overlay.open{display:flex;}
.cert-lightbox-overlay img{max-width:90vw; max-height:90vh; object-fit:contain; box-shadow:0 20px 60px rgba(0,0,0,0.6);}
.cert-lightbox-close{
  position:fixed; top:24px; right:24px; width:40px; height:40px; border-radius:50%;
  border:1px solid var(--grid-line); background:rgba(20,15,10,0.6); color:var(--text);
  cursor:pointer; font-size:1.1rem; display:flex; align-items:center; justify-content:center; z-index:96;
}
.cert-lightbox-close:hover{border-color:var(--cyan); color:var(--cyan);}
.cert-lightbox-nav{
  position:fixed; top:50%; transform:translateY(-50%); width:44px; height:44px; border-radius:50%;
  border:1px solid var(--grid-line); background:rgba(20,15,10,0.6); color:var(--text);
  cursor:pointer; font-size:1.3rem; z-index:96; align-items:center; justify-content:center;
}
.cert-lightbox-nav:hover{border-color:var(--cyan); color:var(--cyan);}
.cert-lightbox-nav.prev{left:20px;}
.cert-lightbox-nav.next{right:20px;}
.cert-lightbox-counter{
  position:fixed; bottom:24px; left:50%; transform:translateX(-50%);
  font-family:'IBM Plex Mono', monospace; font-size:0.78rem; color:var(--text);
  background:rgba(20,15,10,0.6); border:1px solid var(--grid-line); padding:6px 14px; z-index:96;
}
.m-multi{
  font-family:'IBM Plex Mono', monospace; font-size:0.68rem; color:var(--cyan);
  border:1px solid rgba(201,168,118,0.3); padding:1px 7px; margin-left:6px; display:inline-block;
}
.cert-modal-thumb{width:64px; height:64px; flex:0 0 auto; background:var(--panel); border:1px solid var(--grid-line); position:relative; overflow:hidden;}
.cert-modal-thumb img{width:100%; height:100%; object-fit:cover; display:block;}
.cert-modal-thumb .photo-placeholder{gap:2px;}
.cert-modal-thumb .ph-icon{font-size:1.1rem;}
.cert-modal-thumb .ph-text, .cert-modal-thumb .ph-path{display:none;}
.cert-modal-info .m-title{font-weight:600; font-size:0.9rem; margin-bottom:3px;}
.cert-modal-info .m-issuer{color:var(--muted); font-size:0.78rem; margin-bottom:4px;}
.cert-modal-info .m-date{font-family:'IBM Plex Mono', monospace; font-size:0.7rem; color:var(--cyan);}

.cert-category{margin-bottom:36px;}
.cert-category:last-child{margin-bottom:0;}
.cert-category-label{
  font-size:0.74rem; letter-spacing:0.14em; color:var(--cyan); text-transform:uppercase;
  margin-bottom:14px; padding-bottom:8px; border-bottom:1px solid var(--grid-line);
}
.cert-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(240px,1fr)); gap:18px;}
.cert-card{background:var(--panel); border:1px solid var(--grid-line); overflow:hidden; transition:border-color .15s ease, transform .15s ease; box-shadow:0 6px 18px rgba(0,0,0,0.3);}
.cert-card:hover{border-color:var(--cyan); transform:translateY(-3px);}
.cert-thumb{position:relative; aspect-ratio:4/3; background:var(--panel-raised);}
.cert-thumb img{width:100%; height:100%; object-fit:cover; display:block;}
.cert-body{padding:18px;}
.cert-title{font-weight:600; font-size:0.95rem; margin-bottom:4px;}
.cert-issuer{color:var(--muted); font-size:0.8rem; margin-bottom:8px;}
.cert-date{font-family:'IBM Plex Mono', monospace; font-size:0.7rem; color:var(--cyan);}
.notice-box{
  background:rgba(201,154,101,0.10); border:1px solid rgba(201,154,101,0.3);
  padding:16px 18px; margin-bottom:26px; font-size:0.85rem; color:var(--text); line-height:1.6;
}
.notice-box b{color:var(--amber);}

/* LATEST ARTICLES MARQUEE */
.marquee-wrap{overflow:hidden; position:relative; margin-top:6px;}
.marquee-wrap::before, .marquee-wrap::after{
  content:""; position:absolute; top:0; bottom:0; width:60px; z-index:2; pointer-events:none;
}
.marquee-wrap::before{left:0; background:linear-gradient(90deg, var(--bg), transparent);}
.marquee-wrap::after{right:0; background:linear-gradient(270deg, var(--bg), transparent);}
.marquee-track{display:flex; gap:16px; width:max-content; animation:marqueeScroll 28s linear infinite;}
.marquee-wrap:hover .marquee-track{animation-play-state:paused;}
@keyframes marqueeScroll{from{transform:translateX(0);} to{transform:translateX(-50%);}}
.article-card{
  width:300px; flex:0 0 auto; background:var(--panel); border:1px solid var(--grid-line);
  padding:18px; transition:border-color .15s ease;
}
.article-card:hover{border-color:var(--cyan);}
.article-icon{font-size:1.6rem; margin-bottom:10px;}
.article-title{font-weight:600; font-size:0.92rem; margin-bottom:6px; line-height:1.4;}
.article-desc{color:var(--muted); font-size:0.8rem; line-height:1.55; margin-bottom:10px;}
.article-meta{font-family:'IBM Plex Mono', monospace; font-size:0.68rem; color:var(--muted); display:flex; gap:8px; align-items:center;}

/* SPLASH / LOADING SCREEN v2 */
#splash{
  position:fixed; inset:0; z-index:100;
  background:var(--bg);
  display:flex; flex-direction:column; justify-content:space-between;
  transition:opacity .7s ease, visibility .7s ease;
  overflow:hidden;
}
#splash.hide{opacity:0; visibility:hidden; pointer-events:none;}

.splash-marquee{
  overflow:hidden; white-space:nowrap; border-color:var(--grid-line); flex:0 0 auto;
}
.splash-marquee.top{border-bottom:1px solid var(--grid-line);}
.splash-marquee.bottom{border-top:1px solid var(--grid-line);}
.splash-marquee-track{
  display:inline-block; width:max-content;
  font-family:'IBM Plex Mono', monospace; font-size:0.85rem; letter-spacing:0.3em;
  color:var(--muted); padding:14px 0;
  animation:splashMarquee 14s linear infinite;
}
.splash-marquee-track span{padding:0 30px;}
@keyframes splashMarquee{from{transform:translateX(0);} to{transform:translateX(-50%);}}

.splash-center{
  flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:20px;
  position:relative;
}
.splash-pct{
  font-size:clamp(3.2rem,10vw,6rem); font-weight:700; line-height:1;
  color:transparent; -webkit-text-stroke:1.5px var(--text); font-family:'IBM Plex Sans', sans-serif;
  letter-spacing:0.02em;
}
.splash-bar-outer{width:min(70vw,340px); height:2px; background:rgba(214,178,120,0.16); overflow:hidden;}
.splash-bar-inner{height:100%; width:0%; background:var(--cyan);}

.splash-name-wrap{
  position:absolute; display:flex; flex-direction:column; align-items:center; gap:10px;
  opacity:0; transition:opacity .6s ease;
}
.splash-name-wrap.show{opacity:1;}
.splash-name{
  font-size:clamp(1.6rem,4.4vw,2.4rem); font-weight:700;
  color:var(--cyan);
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.splash-name-sub{
  font-family:'IBM Plex Mono', monospace; font-size:0.72rem; letter-spacing:0.24em;
  color:var(--muted); text-transform:uppercase;
}

footer{text-align:center; padding:26px; color:var(--muted); font-family:'IBM Plex Mono', monospace; font-size:0.75rem; border-top:1px solid var(--grid-line); position:relative; z-index:1;}
"""

FONT_LINK = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">"""

def nav(active):
    items = [("index.html","HOME"), ("work.html","WORK HISTORY"), ("skills.html","SKILLS"), ("projects.html","PROJECTS"), ("certificates.html","CERTIFICATES")]
    links = ""
    for href, label in items:
        cls = "active" if href == active else ""
        links += f'<a class="{cls}" href="{href}">{label}</a>\n      '
    return f"""<div class="site-nav">
  <a class="brand" href="index.html">
    <img src="data:image/jpeg;base64,{LOGO_B64}" alt="RR">
    <span>RENDY RYAN RENALDI</span>
  </a>
  <nav>
      {links}
  </nav>
</div>"""

def corners():
    return '<div class="corner tl"></div><div class="corner tr"></div><div class="corner bl"></div><div class="corner br"></div>'

def page_shell(title, active, body, extra_script=""):
    carousel_script = """
<script>
  document.querySelectorAll('.photo-carousel').forEach(function(car){
    var track = car.querySelector('.carousel-track');
    var slides = car.querySelectorAll('.carousel-slide');
    var dots = car.querySelectorAll('.carousel-dot');
    var caption = car.querySelector('.carousel-caption');
    var captions = JSON.parse(car.dataset.captions || '[]');
    var idx = 0;
    function update(){
      track.style.transform = 'translateX(-' + (idx*100) + '%)';
      dots.forEach(function(d,i){ d.classList.toggle('active', i===idx); });
      caption.textContent = captions[idx] || '';
    }
    var prevBtn = car.querySelector('.carousel-btn.prev');
    var nextBtn = car.querySelector('.carousel-btn.next');
    if(prevBtn) prevBtn.addEventListener('click', function(){ idx = (idx-1+slides.length)%slides.length; update(); });
    if(nextBtn) nextBtn.addEventListener('click', function(){ idx = (idx+1)%slides.length; update(); });
    dots.forEach(function(d,i){ d.addEventListener('click', function(){ idx=i; update(); }); });
    update();
  });

  document.querySelectorAll('.skill-card').forEach(function(card){
    card.addEventListener('click', function(){
      var related = JSON.parse(card.dataset.related || '[]');
      var tools = JSON.parse(card.dataset.tools || '[]');
      var story = card.dataset.story || '';
      var overlay = document.getElementById('skillModalOverlay');
      if(!overlay) return;
      document.getElementById('skillModalTitle').textContent = card.dataset.skillName || '';
      document.getElementById('skillModalStory').textContent = story;

      var toolList = document.getElementById('skillModalTools');
      toolList.innerHTML = '';
      tools.forEach(function(t){
        var row = document.createElement('div');
        row.className = 'tool-level-row';
        row.innerHTML = '<span class="t-name">' + t.name + '</span><span class="t-level">' + t.level + '</span>';
        toolList.appendChild(row);
      });

      var list = document.getElementById('skillModalList');
      list.innerHTML = '';
      related.forEach(function(item){
        var a = document.createElement('a');
        a.className = 'skill-modal-link';
        a.href = item.url;
        a.innerHTML = '<span class="l-title">' + item.title + '</span><span class="l-arrow">→</span>';
        list.appendChild(a);
      });
      overlay.classList.add('open');
    });
  });
  var overlayEl = document.getElementById('skillModalOverlay');
  if(overlayEl){
    overlayEl.addEventListener('click', function(e){
      if(e.target === overlayEl) overlayEl.classList.remove('open');
    });
    var closeBtn = document.getElementById('skillModalClose');
    if(closeBtn) closeBtn.addEventListener('click', function(){ overlayEl.classList.remove('open'); });
  }

  document.querySelectorAll('.cert-folder').forEach(function(folder){
    folder.addEventListener('click', function(){
      var items = JSON.parse(folder.dataset.items || '[]');
      var overlay = document.getElementById('certModalOverlay');
      if(!overlay) return;
      document.getElementById('certModalTitle').textContent = folder.dataset.folderName || '';
      var list = document.getElementById('certModalScroll');
      list.innerHTML = '';
      items.forEach(function(item){
        var row = document.createElement('div');
        row.className = 'cert-modal-item';
        var firstImg = item.images[0];
        var extraBadge = item.images.length > 1 ? ' <span class="m-multi">+' + (item.images.length-1) + '</span>' : '';
        row.innerHTML =
          '<div class="cert-modal-thumb">' +
            '<img src="assets/certificates/' + firstImg + '.jpg" alt="" onerror="this.style.display=\\'none\\'; this.nextElementSibling.style.display=\\'flex\\';">' +
            '<div class="photo-placeholder"><div class="ph-icon">📄</div></div>' +
          '</div>' +
          '<div class="cert-modal-info">' +
            '<div class="m-title">' + item.title + extraBadge + '</div>' +
            '<div class="m-issuer">' + item.issuer + '</div>' +
            '<div class="m-date">' + item.date + '</div>' +
          '</div>';
        row.addEventListener('click', function(){
          openLightbox(item.images, 0);
        });
        list.appendChild(row);
      });
      overlay.classList.add('open');
    });
  });
  var certOverlay = document.getElementById('certModalOverlay');
  if(certOverlay){
    certOverlay.addEventListener('click', function(e){
      if(e.target === certOverlay) certOverlay.classList.remove('open');
    });
    var certClose = document.getElementById('certModalClose');
    if(certClose) certClose.addEventListener('click', function(){ certOverlay.classList.remove('open'); });
  }

  var lbImages = [];
  var lbIndex = 0;
  function renderLightbox(){
    var lbImg = document.getElementById('certLightboxImg');
    var counter = document.getElementById('certLightboxCounter');
    lbImg.src = 'assets/certificates/' + lbImages[lbIndex] + '.jpg';
    var navShow = lbImages.length > 1 ? 'flex' : 'none';
    document.getElementById('certLightboxPrev').style.display = navShow;
    document.getElementById('certLightboxNext').style.display = navShow;
    counter.style.display = lbImages.length > 1 ? 'block' : 'none';
    counter.textContent = (lbIndex+1) + ' / ' + lbImages.length;
  }
  function openLightbox(images, startIndex){
    lbImages = images; lbIndex = startIndex;
    renderLightbox();
    document.getElementById('certLightboxOverlay').classList.add('open');
  }
  var lightbox = document.getElementById('certLightboxOverlay');
  if(lightbox){
    lightbox.addEventListener('click', function(e){
      if(e.target === lightbox) lightbox.classList.remove('open');
    });
    var lbClose = document.getElementById('certLightboxClose');
    if(lbClose) lbClose.addEventListener('click', function(e){ e.stopPropagation(); lightbox.classList.remove('open'); });
    var lbPrev = document.getElementById('certLightboxPrev');
    var lbNext = document.getElementById('certLightboxNext');
    if(lbPrev) lbPrev.addEventListener('click', function(e){ e.stopPropagation(); lbIndex = (lbIndex-1+lbImages.length)%lbImages.length; renderLightbox(); });
    if(lbNext) lbNext.addEventListener('click', function(e){ e.stopPropagation(); lbIndex = (lbIndex+1)%lbImages.length; renderLightbox(); });
  }
</script>"""
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{FONT_LINK}
<style>{SHARED_CSS}</style>
</head>
<body>
{corners()}
{nav(active)}
<div class="glow-orb one"></div>
<div class="glow-orb two"></div>
<main>
{body}
</main>
<footer>© 2026 RENDY RYAN RENALDI — DIBANGUN DENGAN GITHUB PAGES</footer>
{extra_script}
{carousel_script}
</body>
</html>"""

# ---------------- SOCIAL ROW (reused) ----------------
SOCIAL_ROW = """
<div class="social-row">
  <a class="social-btn" href="https://github.com/RendyNOA" target="_blank">
    <svg viewBox="0 0 24 24"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/></svg>
    GitHub
  </a>
  <a class="social-btn" href="https://www.linkedin.com/in/rendyryanr" target="_blank">
    <svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.58c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.68H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 110-4.13 2.07 2.07 0 010 4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>
    LinkedIn
  </a>
  <a class="social-btn" href="https://mail.google.com/mail/?view=cm&fs=1&to=rendyrr3nd@gmail.com&su=Halo%20Rendy" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
    Email
  </a>
  <a class="social-btn" href="https://instagram.com/rendy_ryanr" target="_blank">
    <svg viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.85.07s-3.58-.01-4.85-.07c-3.26-.15-4.77-1.7-4.92-4.92-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85C2.35 3.86 3.87 2.33 7.12 2.18 8.39 2.12 8.77 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07c-4.35.2-6.78 2.62-6.98 6.98C.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.2 4.36 2.62 6.78 6.98 6.98C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c4.35-.2 6.78-2.62 6.98-6.98.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.2-4.35-2.62-6.78-6.98-6.98C15.67.01 15.26 0 12 0zm0 5.84A6.16 6.16 0 1012 18.16 6.16 6.16 0 0012 5.84zm0 10.16a4 4 0 110-8 4 4 0 010 8zm6.41-10.41a1.44 1.44 0 11-2.88 0 1.44 1.44 0 012.88 0z"/></svg>
    Instagram
  </a>
</div>"""

# ---------------- ARTICLES MARQUEE ----------------
ARTICLES = [
    ("🌫️","Kalibrasi Sensor Kualitas Udara Low-Cost","Catatan teknis soal drift sensor PM2.5 dan cara mengoreksinya dengan regresi sederhana.","2026-05","4 min read"),
    ("🔋","Dynamic Power Management di Perangkat Wearable","Bagaimana DPM bisa memperpanjang usia baterai tanpa mengorbankan akurasi sensor.","2026-04","5 min read"),
    ("📡","Pengantar Wireless Sensor Network untuk Pemula","Ringkasan konsep dasar WSN yang saya pelajari selama riset di IS-IoT.","2026-03","3 min read"),
    ("🧪","Menguji Sistem Filtrasi Udara dengan Data Real-Time","Proses validasi data dari sistem TrapGradien, lengkap dengan tantangannya.","2026-02","6 min read"),
    ("🛠️","Checklist Dokumentasi Teknis ala Tim Aerospace","Kebiasaan dokumentasi yang saya bawa dari pengalaman magang di industri pertahanan.","2026-01","4 min read"),
]

def articles_marquee():
    cards = ""
    for icon, title, desc, date, read in ARTICLES * 2:  # duplicate for seamless loop
        cards += f"""<div class="article-card">
      <div class="article-icon">{icon}</div>
      <div class="article-title">{title}</div>
      <div class="article-desc">{desc}</div>
      <div class="article-meta"><span>{date}</span><span>•</span><span>{read}</span></div>
    </div>
    """
    return f"""<div class="marquee-wrap">
    <div class="marquee-track">
    {cards}
    </div>
  </div>"""

# ==================== INDEX.HTML (HOME = hero + About Me + Articles) ====================
index_body = f"""
<section class="hero">
  <div class="hero-banner">
    <img src="assets/banner.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.nextElementSibling.style.display='flex';">
    <div class="banner-overlay"></div>
    <div class="banner-placeholder">
      <div class="ph-icon">🖼️</div>
      <div class="ph-text">Foto cover belum ditambahkan.</div>
      <div class="ph-path">assets/banner.jpg</div>
    </div>
  </div>
  <div class="avatar-wrap">
    <div class="avatar-ring"></div>
    <img class="avatar" src="data:image/jpeg;base64,{AVATAR_B64}" alt="Rendy Ryan Renaldi">
  </div>
  <div class="eyebrow-chip">◈ Available for Opportunities</div>
  <div class="hero-name">Rendy Ryan Renaldi</div>
  <div class="hero-role">Engineering Physics Undergraduate — Instrumentation, Embedded Systems &amp; IoT</div>
  {SOCIAL_ROW}
</section>

<section class="section">
  <div class="section-eyebrow">01 / TENTANG</div>
  <div class="section-title">About Me</div>
  <p class="about-text">
    Mahasiswa S1 Teknik Fisika yang fokus pada instrumentasi, embedded system, dan Internet of Things (IoT).
    Berpengalaman sebagai Laboratory Teaching Assistant dan peneliti dalam pengembangan sistem wearable
    air quality monitoring yang mengintegrasikan Human Activity Recognition (HAR) dan Dynamic Power
    Management (DPM). Terbiasa dengan integrasi sensor, pemrograman mikrokontroler, analisis data, validasi
    sistem, dan dokumentasi teknis — dengan minat besar membangun solusi rekayasa yang menjembatani riset
    dan aplikasi nyata.
  </p>
  <div class="stat-row">
    <div class="stat"><div class="stat-num">3.30</div><div class="stat-label mono">IPK / 4.00</div></div>
    <div class="stat"><div class="stat-num">3</div><div class="stat-label mono">PENGALAMAN KERJA</div></div>
    <div class="stat"><div class="stat-num">11</div><div class="stat-label mono">ASISTEN DIBIMBING</div></div>
    <div class="stat"><div class="stat-num">2026</div><div class="stat-label mono">EXPECTED GRADUATE</div></div>
  </div>
  <div class="cta-row">
    <a class="cta-btn" href="projects.html">Lihat Featured Projects →</a>
    <a class="cta-btn ghost" href="work.html">Work History</a>
    <a class="cta-btn ghost" href="skills.html">Skills</a>
  </div>
</section>

<section class="section">
  <div class="section-eyebrow">02 / CATATAN</div>
  <div class="section-title">Latest Articles</div>
  <p class="section-intro">Catatan singkat seputar instrumentasi, IoT, dan hal teknis lain yang saya pelajari.</p>
  {articles_marquee()}
</section>
"""
def marquee_line(word, count=14):
    spans = "".join(f"<span>{word}</span>" for _ in range(count))
    return f'<div class="splash-marquee-track">{spans}{spans}</div>'

index_splash = f"""
<div id="splash">
  <div class="splash-marquee top">{marquee_line("LOADING")}</div>

  <div class="splash-center">
    <div class="splash-pct" id="splashPct">0%</div>
    <div class="splash-bar-outer"><div class="splash-bar-inner" id="splashBar"></div></div>
    <div class="splash-name-wrap" id="splashName">
      <div class="splash-name">Rendy Ryan Renaldi</div>
      <div class="splash-name-sub">Engineering Physics Portfolio</div>
    </div>
  </div>

  <div class="splash-marquee bottom">{marquee_line("LOADING")}</div>
</div>
"""

index_script = """
<script>
  window.addEventListener('load', () => {
    const seen = sessionStorage.getItem('introShown');
    const splash = document.getElementById('splash');
    if (seen) { splash.remove(); return; }

    const pctEl = document.getElementById('splashPct');
    const barEl = document.getElementById('splashBar');
    const nameEl = document.getElementById('splashName');

    let pct = 0;
    const countUp = setInterval(() => {
      pct += 2;
      if (pct >= 100) { pct = 100; clearInterval(countUp); }
      pctEl.textContent = pct + '%';
      barEl.style.width = pct + '%';
      if (pct === 100) {
        pctEl.style.transition = 'opacity .4s ease';
        pctEl.style.opacity = '0';
        barEl.parentElement.style.transition = 'opacity .4s ease';
        barEl.parentElement.style.opacity = '0';
        setTimeout(() => nameEl.classList.add('show'), 200);
      }
    }, 22);

    setTimeout(() => {
      splash.classList.add('hide');
      sessionStorage.setItem('introShown', '1');
      setTimeout(() => splash.remove(), 800);
    }, 3200);
  });
</script>
"""

with open(f"{OUT}/index.html","w") as f:
    html = page_shell("Rendy Ryan Renaldi — Portfolio", "index.html", index_body, extra_script=index_script)
    html = html.replace('<div class="glow-orb one"></div>', index_splash + '<div class="glow-orb one"></div>', 1)
    f.write(html)

# ==================== WORK.HTML ====================
work_body = """
<div class="page-header">
  <div class="section-eyebrow">RIWAYAT</div>
  <div class="section-title">Work History</div>
  <p class="section-intro">Pengalaman kerja, riset, dan organisasi selama masa studi. Klik salah satu untuk lihat detailnya.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <a class="exp-item" href="work-mersi.html">
    <div class="exp-date mono">SEP 2025 —<br>JUN 2026</div>
    <div>
      <div class="exp-role">Head of Assistant</div>
      <div class="exp-org">Measurement and Instrumentation Systems Laboratory (MERSI), Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Memimpin dan mengoordinasikan tim 11 asisten laboratorium.</li>
        <li>Mengawasi sesi laboratorium untuk 100+ mahasiswa S1 di bidang Measurement &amp; Instrumentation Systems.</li>
        <li>Merancang jadwal praktikum dan memantau kualitas sesi praktik.</li>
      </ul></div>
      <span class="exp-more">Baca detail lengkap →</span>
    </div>
  </a>

  <a class="exp-item" href="work-puiptiot.html">
    <div class="exp-date mono">SEP 2025 —<br>JAN 2026</div>
    <div>
      <div class="exp-role">Hardware Engineer</div>
      <div class="exp-org">PUI-PT Intelligent Sensing-IoT, Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Mengembangkan dan menguji sistem sensor berbasis IoT untuk monitoring performa sistem filtrasi udara TrapGradien.</li>
      </ul></div>
      <span class="exp-more">Baca detail lengkap →</span>
    </div>
  </a>

  <a class="exp-item" href="work-sasaero.html">
    <div class="exp-date mono">JUN 2025 —<br>AGU 2025</div>
    <div>
      <div class="exp-role">Intern — System Division</div>
      <div class="exp-org">PT SAS Aerosishan, Bandung</div>
      <div class="exp-desc"><ul>
        <li>Membantu tim engineering dalam dokumentasi teknis dan pengembangan sistem pada proyek Moving Armor Target System.</li>
      </ul></div>
      <span class="exp-more">Baca detail lengkap →</span>
    </div>
  </a>

  <a class="exp-item" href="work-oversight.html">
    <div class="exp-date mono">AUG 2025 —<br>JAN 2026</div>
    <div>
      <div class="exp-role">Head of the Oversight Commission</div>
      <div class="exp-org">Engineering Physics Representative Council, Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Memimpin komisi pengawasan dalam evaluasi kinerja organisasi eksekutif mahasiswa.</li>
      </ul></div>
      <span class="exp-more">Baca detail lengkap →</span>
    </div>
  </a>
</div>
"""
with open(f"{OUT}/work.html","w") as f:
    f.write(page_shell("Work History — Rendy Ryan Renaldi", "work.html", work_body))

# ==================== SKILLS.HTML ====================
skills_body = """
<div class="page-header">
  <div class="section-eyebrow">KEMAMPUAN</div>
  <div class="section-title">Skills</div>
  <p class="section-intro">Bidang teknis yang saya kuasai dari kuliah, riset, dan pengalaman kerja. Klik salah satu untuk lihat penerapannya.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <div class="skills-grid">
    <div class="skill-card" data-skill-name="Embedded Systems"
      data-story="Berawal dari mata kuliah instrumentasi & sistem tertanam, lalu diperdalam lewat proyek skripsi AQMS dan magang di PT SAS Aerosishan."
      data-tools='[{"name":"Arduino","level":"Mahir"},{"name":"Sensor Integration","level":"Mahir"},{"name":"Firmware","level":"Menengah"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"Moving Armor Target System","url":"project-armor.html"}]'>
      <img class="skill-icon-img" src="assets/icons/embedded.svg" alt="">
      <div class="skill-name">Embedded Systems</div>
      <div class="skill-desc">Pemrograman mikrokontroler &amp; integrasi sensor untuk sistem tertanam</div>
      <div class="tag-wrap"><span class="tag">Arduino</span><span class="tag">Sensor Integration</span><span class="tag">Firmware</span></div>
    </div>
    <div class="skill-card" data-skill-name="IoT &amp; Wireless Sensing"
      data-story="Mulai dikenal saat riset di PUI-PT Intelligent Sensing-IoT, mendalami cara sensor saling terhubung dalam sistem monitoring real-time."
      data-tools='[{"name":"Wireless Sensor Network","level":"Menengah"},{"name":"MQTT","level":"Dasar"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"}]'>
      <img class="skill-icon-img" src="assets/icons/iot.svg" alt="">
      <div class="skill-name">IoT &amp; Wireless Sensing</div>
      <div class="skill-desc">Perangkat IoT dan jaringan sensor untuk sistem monitoring</div>
      <div class="tag-wrap"><span class="tag">Wireless Sensor Network</span><span class="tag">MQTT</span></div>
    </div>
    <div class="skill-card" data-skill-name="Instrumentation"
      data-story="Terasah selama menjadi Head of Assistant di Laboratorium MERSI, membimbing praktikum sistem pengukuran & instrumentasi untuk ratusan mahasiswa."
      data-tools='[{"name":"DAQ","level":"Mahir"},{"name":"Signal Conditioning","level":"Menengah"},{"name":"Kalibrasi","level":"Mahir"}]'
      data-related='[{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"},{"title":"Head of Assistant — MERSI","url":"work-mersi.html"}]'>
      <img class="skill-icon-img" src="assets/icons/instrumentation.svg" alt="">
      <div class="skill-name">Instrumentation</div>
      <div class="skill-desc">Signal conditioning, data acquisition, dan kalibrasi sistem pengukuran</div>
      <div class="tag-wrap"><span class="tag">DAQ</span><span class="tag">Signal Conditioning</span><span class="tag">Kalibrasi</span></div>
    </div>
    <div class="skill-card" data-skill-name="Data &amp; Dokumentasi"
      data-story="Terbentuk dari kebiasaan menyusun dokumentasi teknis di PT SAS Aerosishan dan validasi data riset selama masa kuliah."
      data-tools='[{"name":"Data Analysis","level":"Mahir"},{"name":"System Validation","level":"Menengah"},{"name":"Tech Docs","level":"Mahir"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"},{"title":"Moving Armor Target System","url":"project-armor.html"}]'>
      <img class="skill-icon-img" src="assets/icons/data.svg" alt="">
      <div class="skill-name">Data &amp; Dokumentasi</div>
      <div class="skill-desc">Analisis data, validasi sistem, dan dokumentasi teknis</div>
      <div class="tag-wrap"><span class="tag">Data Analysis</span><span class="tag">System Validation</span><span class="tag">Tech Docs</span></div>
    </div>
  </div>
</div>

<div class="skill-modal-overlay" id="skillModalOverlay">
  <div class="skill-modal">
    <button class="skill-modal-close" id="skillModalClose">✕</button>
    <div class="skill-modal-title" id="skillModalTitle"></div>
    <div class="skill-modal-label">CERITA SINGKAT</div>
    <div class="skill-modal-story" id="skillModalStory"></div>
    <div class="skill-modal-label">LEVEL PENGUASAAN</div>
    <div id="skillModalTools"></div>
    <div class="skill-modal-label">DITERAPKAN DI</div>
    <div id="skillModalList"></div>
  </div>
</div>
"""
with open(f"{OUT}/skills.html","w") as f:
    f.write(page_shell("Skills — Rendy Ryan Renaldi", "skills.html", skills_body))

# ==================== PROJECTS.HTML (grid -> links to detail pages) ====================
projects_body = """
<div class="page-header">
  <div class="section-eyebrow">KARYA</div>
  <div class="section-title">Featured Projects</div>
  <p class="section-intro">Klik salah satu proyek untuk melihat halaman detailnya. 3 proyek pertama berasal dari Tugas Akhir yang sama, dipecah untuk menonjolkan skill yang berbeda-beda.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <div class="project-grid">
    <a class="project-card" href="project-aqms.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(201,168,118,0.14));"><img src="assets/projects/aqms-device.jpg" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Wearable AQMS (Perangkat) <span class="project-chevron">→</span></div>
        <div class="project-summary">Skripsi: perangkat wearable pemantau kualitas udara berbasis IoT.</div>
        <div class="tag-row"><span class="tag-amber">IoT</span><span class="tag-amber">Wearable</span><span class="tag-amber">Embedded</span></div>
      </div>
    </a>

    <a class="project-card" href="project-kalibrasi.html">
      <div class="project-banner" style="padding:0;"><img src="assets/projects/kalibrasi-banner.jpg" alt="" style="width:100%; height:100%; object-fit:cover;"></div>
      <div class="project-body">
        <div class="project-title">Kalibrasi Sensor & Pemrosesan Data <span class="project-chevron">→</span></div>
        <div class="project-summary">Skripsi: kalibrasi 6 parameter sensor terhadap instrumen referensi.</div>
        <div class="tag-row"><span class="tag-amber">Data Analysis</span><span class="tag-amber">Statistik</span></div>
      </div>
    </a>

    <a class="project-card" href="project-har.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(176,100,74,0.14));"><img src="assets/projects/har-aktivitas.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Pengembangan Model HAR <span class="project-chevron">→</span></div>
        <div class="project-summary">Skripsi: model klasifikasi aktivitas dari data IMU (96.33% akurasi).</div>
        <div class="tag-row"><span class="tag-amber">Machine Learning</span><span class="tag-amber">Python</span></div>
      </div>
    </a>

    <a class="project-card" href="project-motion-effect.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(150,160,120,0.14));"><img src="assets/projects/motion-icon.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Pengaruh Gerakan terhadap Pengukuran Partikulat <span class="project-chevron">→</span></div>
        <div class="project-summary">Skripsi: temuan utama — analisis deviasi PM2.5/PM10 akibat kondisi dinamis.</div>
        <div class="tag-row"><span class="tag-amber">Data Analysis</span><span class="tag-amber">Statistik</span></div>
      </div>
    </a>

    <a class="project-card" href="project-trapgradien.html">
      <div class="project-banner" style="padding:0; background:#fff;"><img src="assets/projects/trapgradien-icon.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:12px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">TrapGradien Air Filtration Monitor <span class="project-chevron">→</span></div>
        <div class="project-summary">Sistem sensor IoT untuk memantau performa filtrasi udara.</div>
        <div class="tag-row"><span class="tag-amber">IoT</span><span class="tag-amber">Sensor Testing</span></div>
      </div>
    </a>

    <a class="project-card" href="project-armor.html">
      <div class="project-banner" style="padding:0;"><img src="assets/projects/armor-icon.jpg" alt="" style="width:100%; height:100%; object-fit:cover;"></div>
      <div class="project-body">
        <div class="project-title">Moving Armor Target System <span class="project-chevron">→</span></div>
        <div class="project-summary">Dukungan teknis untuk proyek sistem pertahanan di PT SAS Aerosishan.</div>
        <div class="tag-row"><span class="tag-amber">Defense Tech</span><span class="tag-amber">System Dev</span></div>
      </div>
    </a>
  </div>
</div>
"""
with open(f"{OUT}/projects.html","w") as f:
    f.write(page_shell("Projects — Rendy Ryan Renaldi", "projects.html", projects_body))

def photo_slot(path):
    return f"""<div class="photo-slot">
      <img src="{path}" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
      <div class="photo-placeholder">
        <div class="ph-icon">🖼️</div>
        <div class="ph-text">Foto belum ditambahkan.<br>Taruh file gambar di:</div>
        <div class="ph-path">{path}</div>
      </div>
    </div>"""

def photo_carousel(folder, slug, captions):
    import json as _json
    slides = ""
    for i in range(1, len(captions)+1):
        slides += f"""<div class="carousel-slide">
      <img src="assets/{folder}/{slug}-{i}.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
      <div class="photo-placeholder">
        <div class="ph-icon">🖼️</div>
        <div class="ph-text">Foto belum ditambahkan.<br>Taruh file gambar di:</div>
        <div class="ph-path">assets/{folder}/{slug}-{i}.jpg</div>
      </div>
    </div>"""
    dots = "".join(f'<button class="carousel-dot{" active" if i==0 else ""}"></button>' for i in range(len(captions)))
    captions_attr = _json.dumps(captions).replace('"', "&quot;")
    return f"""<div class="photo-carousel" data-captions="{captions_attr}">
  <div class="carousel-viewport">
    <div class="carousel-track">{slides}</div>
    <button class="carousel-btn prev" aria-label="Sebelumnya">‹</button>
    <button class="carousel-btn next" aria-label="Selanjutnya">›</button>
  </div>
  <div class="carousel-dots">{dots}</div>
  <div class="carousel-caption"></div>
</div>"""

def photo_gallery(slug):
    slots = "".join(photo_slot(f"assets/projects/{slug}-{i}.jpg") for i in (1,2,3))
    return f"""<div class="photo-gallery">{slots}</div>"""

# ==================== PROJECT DETAIL PAGES ====================
def image_carousel(images, aspect_ratio="16/9", fit="cover"):
    import json as _json
    slides = "".join(f'<div class="carousel-slide"><img src="{src}" alt="" style="object-fit:{fit};"></div>' for src, cap in images)
    dots = "".join(f'<button class="carousel-dot{" active" if i==0 else ""}"></button>' for i in range(len(images)))
    captions = [cap for _, cap in images]
    captions_attr = _json.dumps(captions).replace('"', "&quot;")
    return f"""<div class="photo-carousel" data-captions="{captions_attr}">
  <div class="carousel-viewport" style="aspect-ratio:{aspect_ratio};">
    <div class="carousel-track">{slides}</div>
    <button class="carousel-btn prev" aria-label="Sebelumnya">‹</button>
    <button class="carousel-btn next" aria-label="Selanjutnya">›</button>
  </div>
  <div class="carousel-dots">{dots}</div>
  <div class="carousel-caption"></div>
</div>"""

def project_detail(filename, icon, title, role, org, duration, tools, paragraphs, tags, other, slug, extra_html="", thesis_note="", photo_captions=None, override_content=None, banner_img=None, banner_carousel_images=None, show_banner=True):
    others_html = ""
    for href, oicon, otitle in other:
        others_html += f'<a class="project-card" href="{href}" style="margin-bottom:10px;"><div class="project-body" style="display:flex; align-items:center; gap:12px; padding:14px 18px;"><span style="font-size:1.3rem;">{oicon}</span><span style="font-size:0.88rem; font-weight:600;">{otitle}</span></div></a>\n    '
    tags_html = "".join(f'<span class="tag-amber">{t}</span>' for t in tags)
    if not show_banner:
        banner_block = ""
    elif banner_carousel_images:
        banner_block = image_carousel(banner_carousel_images, aspect_ratio="16/9", fit="contain")
    elif banner_img:
        img_class = "banner-photo" if banner_img.lower().endswith((".jpg",".jpeg",".png")) else ""
        banner_block = f'<div class="detail-banner"><img class="{img_class}" src="{banner_img}" alt=""></div>'
    else:
        banner_block = f'<div class="detail-banner">{icon}</div>'
    if photo_captions is None:
        photo_captions = [f"Dokumentasi {title} — foto 1", f"Dokumentasi {title} — foto 2", f"Dokumentasi {title} — foto 3"]

    if override_content is not None:
        main_content = f"""{override_content}
<div class="tag-row" style="margin-top:20px;">{tags_html}</div>"""
    else:
        paras_html = "".join(f"<p>{p}</p>\n  " for p in paragraphs)
        main_content = f"""<div class="section-eyebrow" style="margin-top:6px;">GALERI FOTO</div>
{photo_carousel("projects", slug, photo_captions)}

<div class="detail-body">
  {paras_html}
  <div class="tag-row">{tags_html}</div>
</div>

{extra_html}"""

    body = f"""
<div class="page-header">
  <a class="back-link" href="projects.html">← Kembali ke Projects</a>
  {banner_block}
  <div class="section-title">{title}</div>
</div>

<div class="detail-meta">
  <div><div class="k">ROLE</div><div class="v">{role}</div></div>
  <div><div class="k">ORGANISASI</div><div class="v">{org}</div></div>
  <div><div class="k">DURASI</div><div class="v">{duration}</div></div>
  <div><div class="k">TOOLS</div><div class="v">{tools}</div></div>
</div>

{thesis_note}

{main_content}

<div class="other-projects">
  <div class="label">PROYEK LAINNYA</div>
  {others_html}
</div>
"""
    with open(f"{OUT}/{filename}","w") as f:
        f.write(page_shell(f"{title} — Rendy Ryan Renaldi", "projects.html", body))

def chart_gallery(charts):
    figs = ""
    for src, caption in charts:
        figs += f"""<figure class="chart-figure">
    <img src="{src}" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
    <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
      <div class="ph-icon">📊</div>
      <div class="ph-text">Grafik belum ditambahkan.<br>Taruh file gambar di:</div>
      <div class="ph-path">{src}</div>
    </div>
    <figcaption>{caption}</figcaption>
  </figure>"""
    return f'<div class="chart-gallery">{figs}</div>'

def thesis_note(current_label, links):
    links_html = "".join(f'<a href="{href}">{label}</a>' for href, label in links)
    return f"""<div class="thesis-note">
  <b>📖 Bagian dari Tugas Akhir yang sama:</b> "Pengembangan Wearable Air Quality Monitoring System
  dengan Integrasi Human Activity Recognition untuk Analisis Pengaruh Gerakan terhadap Pengukuran
  Partikulat" — halaman ini fokus ke bagian <b>{current_label}</b>. Bagian lain dari riset yang sama:
  <div class="tn-links">{links_html}</div>
</div>"""

AQMS_LINKS = [
    ("project-aqms.html", "🌫️", "Wearable AQMS (Perangkat)"),
    ("project-kalibrasi.html", "🧪", "Kalibrasi Sensor & Pemrosesan Data"),
    ("project-har.html", "🏃", "Pengembangan Model HAR"),
    ("project-motion-effect.html", "📉", "Pengaruh Gerakan terhadap Pengukuran Partikulat"),
]

def other_aqms_links(exclude):
    return [(h, i, l) for h, i, l in AQMS_LINKS if h != exclude]

def thesis_note_links(exclude):
    return [(h, f"{i} {l}") for h, i, l in AQMS_LINKS if h != exclude]

# ---- 1. WEARABLE AQMS (perangkat/hardware) ----
AQMS_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/aqms-wear.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:9/16; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Penggunaan Wearable AQMS secara ergonomis pada area dada</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Mengapa Membangun Wearable AQMS?</div>
  <p>Sistem pemantau kualitas udara (AQMS) konvensional umumnya bersifat stasioner, sehingga memiliki keterbatasan dalam merekam variasi polusi berskala mikro. Resolusi spasial yang rendah ini menyebabkan eksposur polutan aktual yang dihirup individu saat beraktivitas sering kali tidak terdeteksi. Untuk menjawab tantangan tersebut, dikembangkanlah sistem AQMS berbasis wearable yang dirancang ergonomis untuk ditempatkan pada area dada pengguna — posisi ideal yang paling merepresentasikan eksposur udara pernapasan sekaligus mampu menangkap getaran mekanis tubuh saat bergerak.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-wiring.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/10; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Diagram wiring integrasi mikrokontroler dengan multi-sensor dan sistem daya</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Integrasi Hardware & Arsitektur IoT</div>
  <p>Perangkat ini bukanlah sekadar pembaca sensor biasa, melainkan sistem IoT terintegrasi yang mengakuisisi data multivariabel secara serentak. Otak komputasi sentral menggunakan mikrokontroler Wemos (ESP32/ESP8266) yang dihubungkan dengan skema wiring terpadu ke berbagai komponen:</p>
  <ul class="narrative-list">
    <li><b>SPS30:</b> Mengukur partikulat PM2.5 dan PM10 secara presisi.</li>
    <li><b>ENS160 & AHT2x:</b> Mengukur gas volatil (TVOC), estimasi CO2, suhu, dan kelembapan lingkungan.</li>
    <li><b>Bosch IMU (Nicla Sense ME):</b> Mengakuisisi data akselerometer dan giroskop untuk deteksi pola gerakan tubuh pengguna.</li>
    <li><b>Power Management:</b> Menggunakan baterai Li-Po 3.7V 2000mAh yang dilengkapi modul charger/boost terintegrasi untuk menyuplai daya sistem secara mandiri (portabel).</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-device.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:3/4; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Form-factor perangkat Wearable AQMS yang ringkas dan portabel</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Fabrikasi Perangkat & Edge Computing</div>
  <p>Dari segi desain fisik, seluruh komponen dirakit dan difabrikasi ke dalam casing (form-factor) berukuran saku yang kokoh dan ringan. Ukurannya yang compact memastikan aliran udara tetap optimal masuk ke inlet sensor tanpa membebani pergerakan pengguna.</p>
  <p style="margin-top:16px;">Salah satu inovasi engineering pada sistem ini adalah efisiensi transmisi data. Alih-alih mengirimkan ratusan data mentah IMU per detik yang menguras baterai, perangkat melakukan edge computing (komputasi lokal) untuk menghitung Motion Index secara real-time. Sistem hanya mengekstraksi dan mengirimkan nilai ringkasan pergerakan bersamaan dengan data kualitas udara, menghemat bandwidth komunikasi secara signifikan.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-dashboard.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Dashboard pemantauan kualitas udara Cloud Gradien secara real-time</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Pemantauan Data Real-Time (IoT Dashboard)</div>
  <p>Data yang berhasil diakuisisi oleh perangkat kemudian ditransmisikan menuju antarmuka cloud (Cloud Gradien) untuk pemantauan visual. Dashboard ini menampilkan seluruh metrik krusial secara real-time — mulai dari Air Quality Index (AQI), tingkat PM2.5, TVOC, hingga status suhu, kelembapan, dan persentase sisa baterai (Battery Criticality).</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Kesimpulan & Dampak Proyek</div>
  <p>Proyek ini membuktikan keberhasilan pembangunan arsitektur IoT end-to-end — mulai dari perancangan hardware, skema kelistrikan (power management), transmisi cloud, hingga visualisasi antarmuka. Dengan memindahkan beban komputasi IMU langsung ke dalam perangkat (edge computing), Wearable AQMS ini mampu beroperasi secara efisien, portabel, dan stabil saat digunakan oleh pengguna di lapangan, sehingga dapat melakukan pengukuran paparan polusi udara yang lebih personal.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Dokumentasi</div>
</div>
""" + image_carousel([
    ("assets/projects/aqms-solder.jpg", "Proses soldering dan perakitan komponen elektronik perangkat"),
    ("assets/projects/aqms-users.jpg", "Dokumentasi pengguna yang telah memakai Wearable AQMS saat pengujian lapangan"),
], aspect_ratio="16/9", fit="contain")

project_detail(
    "project-aqms.html", "🌫️",
    "Wearable AQMS (Perangkat)",
    "Peneliti Utama (Skripsi)", "Telkom University", "Feb 2026 — Mar 2026",
    "ESP32, ESP8266, SPS30, ENS160, AHT21, Nicla Sense ME (Bosch IMU)",
    [],
    ["IoT","Wearable","Embedded Systems","Skripsi"],
    [("project-trapgradien.html","🧪","TrapGradien Air Filtration Monitor"),
     ("project-armor.html","🛡️","Moving Armor Target System")],
    "aqms",
    override_content=AQMS_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Wearable AQMS (Perangkat)", thesis_note_links("project-aqms.html"))
)

# ---- 2. KALIBRASI SENSOR LINGKUNGAN ----
KALIBRASI_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-diagram-sistem.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Setup calibration chamber / diagram blok sistem kalibrasi</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Mengapa Sensor Perlu Dikalibrasi?</div>
  <p>Membangun sistem pemantau kualitas udara wearable berarti kita harus menggunakan sensor berbiaya rendah agar bentuknya ringkas (seperti SPS30 dan ENS160). Namun, sensor jenis ini sering kali memiliki bias pembacaan bawaan pabrik. Jika tidak dikalibrasi, akan sangat sulit untuk membedakan apakah perubahan angka yang muncul itu murni karena kondisi lingkungan, gangguan gerakan pengguna, atau sekadar noise dari sensor. Oleh karena itu, 6 parameter lingkungan dari 7 unit perangkat harus diuji dan disamakan terlebih dahulu dengan instrumen referensi berstandar industri (OPC-N3, DT-900A, dan SHT20).</p>
  <table class="data-table">
    <tr><th>Parameter</th><th>Sensor pada Wearable AQMS</th><th>Instrumen Referensi</th></tr>
    <tr><td>PM2.5</td><td>SPS30</td><td>OPC-N3</td></tr>
    <tr><td>PM10</td><td>SPS30</td><td>OPC-N3</td></tr>
    <tr><td>TVOC</td><td>ENS160</td><td>DT-900A</td></tr>
    <tr><td>eCO2</td><td>ENS160</td><td>Sensor CO2 RS485</td></tr>
    <tr><td>Suhu</td><td>AHT21</td><td>SHT20</td></tr>
    <tr><td>Kelembapan</td><td>AHT21</td><td>SHT20</td></tr>
  </table>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-ts-pm25.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Time series kalibrasi PM2.5 (metode decay) — Mobile-1 sampai Mobile-7</figcaption>
</div>
<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-ts-suhu.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Time series kalibrasi suhu (fase pemanasan) — Mobile-1 sampai Mobile-7</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Metode Pengambilan Data (Akuisisi Sensor)</div>
  <p>Untuk mendapatkan model yang akurat, data dikumpulkan melalui eksperimen ruang uji (calibration chamber) dengan pendekatan khusus untuk tiap parameter:</p>
  <ul class="narrative-list">
    <li><b>Partikulat (PM2.5 & PM10):</b> Menggunakan metode decay. Polutan dipompa hingga pekat, lalu dibiarkan menurun perlahan menggunakan udara bersih. Ini melatih sensor mengenali rentang polusi dari tinggi ke rendah secara natural.</li>
    <li><b>Suhu & Kelembapan:</b> Pengujian difokuskan murni pada fase pemanasan (naik). Fase pendinginan (decay) sengaja tidak dilibatkan dalam pemodelan untuk menghindari distorsi data akibat panas sisa atau panas internal dari komponen elektronik mikrokontroler itu sendiri.</li>
  </ul>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">0.9978</div><div class="sm-label">R² PM2.5 (KUADRATIK)</div></div>
  <div class="stat-mini"><div class="sm-num">0.9797</div><div class="sm-label">R² PM10 (KUADRATIK)</div></div>
  <div class="stat-mini"><div class="sm-num">&lt;0.7%</div><div class="sm-label">MAPE SUHU & KELEMBAPAN</div></div>
  <div class="stat-mini"><div class="sm-num">6</div><div class="sm-label">PARAMETER DIKALIBRASI</div></div>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Di Balik Angka: Data Cleansing & Evaluasi Model</div>
  <p>Angka akurasi tinggi di atas bukanlah hasil yang didapat secara instan. Proses ini murni melibatkan data pipeline dan preprocessing yang ketat:</p>
  <ul class="narrative-list">
    <li><b>Handling Large Datasets:</b> Memproses, menyelaraskan waktu (time-sync/crop), dan mengonsolidasi 22.297 baris data mentah (time-series) yang ditarik secara serentak dari seluruh perangkat IoT.</li>
    <li><b>Data Cleansing & Transformation:</b> Memfilter sekitar 800 titik data anomali (outliers) menggunakan pendekatan statistik (Interquartile Range / IQR dan Rolling MAD) untuk menjaga integritas data. Proses ini menghasilkan 12.225 data super bersih (clean dataset) yang siap digunakan untuk training model.</li>
    <li><b>Model Error Analysis:</b> Mengevaluasi algoritma prediksi secara iteratif menggunakan metrik error seperti RMSE, MAE, dan MAPE.</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-scatter.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Scatter plot hasil koreksi sensor (sesudah kalibrasi) yang rapat di garis ideal</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Hasil Pemodelan & Kesimpulan</div>
  <p>Dari hasil komparasi pemodelan (Linear vs. Kuadratik), Model Kuadratik terbukti paling optimal untuk mengoreksi bias non-linear pada sensor partikulat, sukses menekan angka error (RMSE) secara signifikan. Sebaliknya, untuk suhu, kelembapan, dan gas TVOC, algoritma Model Linear dipilih karena terbukti sudah sangat akurat dan jauh lebih ringan (efisien) untuk diimplementasikan langsung ke dalam komputasi mikrokontroler (on-device).</p>
  <p style="margin-top:16px;">Melalui rangkaian proses data ini, sistem berhasil mengubah sensor berbiaya rendah menjadi instrumen dengan akurasi tinggi (nilai R² hingga 0.99). Dengan memiliki baseline data yang sangat valid dan bersih ini, analisis kompleks di tahap selanjutnya — yaitu mendeteksi gangguan metrik akibat guncangan dari lari/jalan (Human Activity Recognition) — dapat dieksekusi dengan tingkat kepercayaan yang sangat tinggi.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-rekap-slide.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Rekapan hasil kalibrasi: heatmap MAPE seluruh unit & parameter, beserta model koreksi final yang dipilih</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Dokumentasi</div>
</div>
""" + image_carousel([
    ("assets/projects/kalibrasi-banner.jpg", "Panel HMI monitoring real-time PM2.5, PM10, suhu, dan CO2 saat proses kalibrasi"),
    ("assets/projects/kalibrasi-1.jpg", "Dokumentasi proses kalibrasi sensor di dalam chamber"),
    ("assets/projects/kalibrasi-chamber-real.jpg", "Setup asli chamber kalibrasi beserta sistem pompa, filter, dan pengatur aliran udara"),
], aspect_ratio="16/9", fit="contain")

project_detail(
    "project-kalibrasi.html", "🧪",
    "Kalibrasi Sensor & Pemrosesan Data Lingkungan",
    "Peneliti Utama (Skripsi)", "Telkom University", "Feb 2026 — Mar 2026",
    "Python (pandas, NumPy, SciPy), Microsoft Excel, Matplotlib, Calibration Chamber",
    [],
    ["Data Analysis","Statistik","Regresi","Sensor Calibration","Python"],
    other_aqms_links("project-kalibrasi.html"),
    "kalibrasi",
    override_content=KALIBRASI_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Kalibrasi Sensor & Pemrosesan Data Lingkungan", thesis_note_links("project-kalibrasi.html"))
)

# ---- 3. PENGEMBANGAN MODEL HAR ----
HAR_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/har-aktivitas.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/12; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Empat aktivitas utama pengguna yang diklasifikasikan oleh sistem: Duduk, Berjalan, Berlari, dan Berkendara/Beam</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Konteks & Tujuan Pemodelan</div>
  <p>Dalam pemantauan kualitas udara berbasis wearable, akurasi sensor sangat rentan terhadap gangguan pergerakan (motion artifact). Untuk meneliti seberapa besar guncangan tubuh memengaruhi pembacaan polusi, sistem harus bisa mengenali sedang apa pengguna saat itu secara otomatis. Oleh karena itu, dikembangkanlah model Machine Learning berbasis Human Activity Recognition (HAR) untuk mengklasifikasikan 4 aktivitas utama pengguna: Duduk, Berjalan, Berlari, dan Berkendara (Beam).</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/har-windowing.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Visualisasi teknik Windowing pada sinyal sensor mentah, dengan ukuran window 2 detik dan overlap 50%</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Akuisisi Data & Windowing</div>
  <p>Data dikumpulkan dari sensor Inertial Measurement Unit (IMU) — akselerometer dan giroskop 6-sumbu — yang diuji coba pada 10 subjek berbeda. Pemrosesan data mentah time-series (lebih dari 101.000 sampel) tidak bisa langsung diumpankan ke model ML; analisis gerakan manusia membutuhkan segmentasi waktu. Data dipotong menggunakan teknik Windowing (2 detik, overlap 50%), mengubah sinyal mentah berfrekuensi 20Hz menjadi 5.039 baris dataset terstruktur yang siap diekstraksi.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Feature Engineering & Motion Index</div>
  <p>Untuk mengubah sinyal gelombang menjadi data yang bisa dipelajari algoritma, dilakukan ekstraksi 73 fitur statistik (seperti Mean, Standar Deviasi, Variance, RMS, Skewness, dan Kurtosis) dari setiap window.</p>
  <p style="margin-top:16px;">Selain fitur standar, diekstraksi pula satu metrik krusial bernama Motion Index — dihitung dari standar deviasi magnitudo akselerometer (acceleration magnitude). Nilai ini berfungsi mengukur intensitas gerakan secara numerik (Duduk = ~0.10, Berlari = ~19.54), yang nantinya dikorelasikan langsung dengan tingkat error pembacaan sensor kualitas udara.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/har-akurasi.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Grafik belum ditambahkan.</div>
  </div>
  <figcaption>Perbandingan akurasi algoritma klasifikasi (Random Forest, Decision Tree, KNN) pada tahap evaluasi</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Pelatihan Model: Mencari Titik Temu Akurasi & Efisiensi Komputasi</div>
  <p>Pelatihan model dilakukan menggunakan beberapa algoritma klasifikasi: Random Forest, Decision Tree, dan K-Nearest Neighbors. Random Forest menghasilkan akurasi tertinggi (98.51%), namun untuk perangkat IoT (edge computing), model tersebut terlalu kompleks dan memakan banyak memori. Efisiensi sistem menjadi prioritas, sehingga Decision Tree (DT) akhirnya dipilih sebagai algoritma final. Meskipun akurasinya sedikit di bawah RF, DT masih mencatat performa luar biasa di angka 96.33% dengan keunggulan struktur model yang jauh lebih ringan dan mudah dikonversi menjadi logika if-else di dalam bahasa C/C++ mikrokontroler.</p>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">96.33%</div><div class="sm-label">AKURASI DECISION TREE</div></div>
  <div class="stat-mini"><div class="sm-num">73</div><div class="sm-label">FITUR PER WINDOW</div></div>
  <div class="stat-mini"><div class="sm-num">5.039</div><div class="sm-label">WINDOW DATASET</div></div>
  <div class="stat-mini"><div class="sm-num">0.96</div><div class="sm-label">RATA-RATA F1-SCORE</div></div>
</div>

<div class="narrative-figure">
  <div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
    <img src="assets/projects/har-confusion.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:360px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/har-feature-importance.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:360px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
  </div>
  <figcaption>Confusion Matrix dari model Decision Tree (kiri) dan Grafik Feature Importance yang menunjukkan fitur paling berpengaruh (kanan)</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Evaluasi Metrik & Feature Importance</div>
  <p>Evaluasi ketat dilakukan menggunakan Classification Report (Precision, Recall, F1-Score rata-rata di angka 0.96) dan analisis Confusion Matrix. Model terbukti sangat tangguh membedakan aktivitas kontras (Duduk vs Lari), meskipun terdapat sedikit irisan prediksi (false positive) antara aktivitas Jalan dan Berkendara karena kemiripan getaran mekanis pada beberapa momen.</p>
  <p style="margin-top:16px;">Melalui analisis Feature Importance, tervalidasi bahwa fitur acc_mag_var (Variansi Magnitudo Akselerometer) memegang bobot terbesar dalam pengambilan keputusan algoritma, membuktikan bahwa fluktuasi percepatan adalah prediktor terbaik untuk mengenali pola manusia.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Kesimpulan</div>
  <p>Pengembangan model HAR ini sukses mentransformasi data pergerakan kasar menjadi konteks aktivitas (Movement Category) dan intensitas gerak (Motion Index) secara real-time. Keberhasilan deploy model Machine Learning yang ringan ke dalam mikrokontroler membuktikan bahwa kecerdasan buatan dapat berjalan mulus di perangkat wearable, sekaligus membuka jalan untuk memvalidasi kualitas data sensor udara di tahap analisis akhir.</p>
</div>
"""

project_detail(
    "project-har.html", "🏃",
    "Pengembangan Model HAR",
    "Peneliti Utama (Skripsi)", "Telkom University", "Sep 2025 — Jul 2026 (Expected)",
    "Python, scikit-learn, pandas, numpy",
    [],
    ["Machine Learning","Data Analysis","Python","Feature Engineering","Classification"],
    other_aqms_links("project-har.html"),
    "har",
    override_content=HAR_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Pengembangan Model HAR", thesis_note_links("project-har.html"))
)

# ---- 4. ANALISIS PENGARUH GERAKAN TERHADAP PENGUKURAN PARTIKULAT ----
MOTION_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">Latar Belakang Eksperimen: Mengapa Gerakan Berpengaruh?</div>
  <p>Sistem Wearable AQMS dirancang untuk dipakai di tubuh pengguna, yang berarti perangkat akan terus bergerak seiring aktivitas harian. Pergerakan ini memicu perubahan orientasi, getaran mekanis, dan turbulensi aliran udara di sekitar inlet sensor partikulat (SPS30) yang mengandalkan prinsip hamburan cahaya laser. Eksperimen ini dirancang untuk menjawab satu pertanyaan kritis secara data: <b>"Apakah guncangan dari tubuh pengguna mendistorsi pembacaan tingkat polusi (PM<sub>2.5</sub> dan PM<sub>10</sub>), dan seberapa besar deviasinya?"</b></p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/motion-diagram.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Ilustrasi metodologi A/B Testing: Perangkat dinamis pada pengguna vs 3 perangkat statis sebagai kontrol lingkungan</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Metodologi Pengujian: Pendekatan Statis vs. Dinamis</div>
  <p>Untuk mengisolasi efek gerakan dari fluktuasi polusi udara yang sebenarnya, diterapkan metode komparasi langsung (A/B Testing methodology). Perangkat dibagi menjadi dua grup:</p>
  <ul class="narrative-list">
    <li><b>Grup Dinamis (Mobile 1 & 5):</b> Perangkat yang dikenakan di dada pengguna atau diletakkan pada alat pemutar mekanis.</li>
    <li><b>Grup Kontrol / Statis (Mobile 3, 4, 6):</b> Tiga perangkat yang diletakkan diam pada posisi tetap untuk merepresentasikan kondisi partikulat lingkungan aktual.</li>
  </ul>
  <p style="margin-top:16px;">Pengujian dilakukan melalui tiga skenario berjenjang: (1) Chamber tertutup, (2) Luar Ruangan (terkontrol), dan (3) Uji Lapangan Nyata yang melibatkan aktivitas Duduk, Berjalan, Berlari, dan Berkendara (Beam).</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Analisis Data: Koreksi Baseline (Baseline Correction)</div>
  <p>Dalam analisis sensor berbiaya rendah, membandingkan selisih nilai secara mentah (ΔPM = PM<sub>dinamis</sub> − PM<sub>statis</sub>) bisa menyesatkan akibat bias bawaan antar-unit sensor yang tersisa pasca-kalibrasi.</p>
  <p style="margin-top:16px;">Sebagai analis data, anomali ini diatasi dengan menerapkan Koreksi Baseline (E = ΔPM − B). Sebelum dan sesudah pengujian, seluruh perangkat didiamkan bersama (kolokasi) untuk mencari selisih dasarnya (B). Hanya dengan memotong selisih kotor (ΔPM) dengan baseline ini, efek murni dari pergerakan dapat diekstraksi secara presisi.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/motion-formula.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Formula analitik untuk menetralkan bias antar-sensor menggunakan Koreksi Baseline</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Hasil Analisis & Korelasi Metrik</div>
  <p>Hasil komputasi data pasca-koreksi menunjukkan pola yang sangat menarik: kondisi dinamis (pergerakan) secara konsisten cenderung membuat perangkat membaca konsentrasi partikulat lebih rendah (deviasi negatif) dibandingkan kontrol statis.</p>
  <p style="margin-top:16px;">Lebih lanjut, dilakukan analisis korelasi linear (Pearson's r) antara intensitas gerakan (diwakili metrik Mean Motion Index dari algoritma HAR) terhadap besaran deviasi absolut sensor |E| dalam µg/m³:</p>
  <ul class="narrative-list">
    <li><b>Skenario Chamber:</b> Ditemukan korelasi positif yang kuat (r = 0.863 untuk PM<sub>2.5</sub> dan r = 0.580 untuk PM<sub>10</sub>) di seluruh skema percobaan P1–P4.</li>
    <li><b>Skenario Lapangan:</b> Korelasi positif ini tervalidasi semakin kuat seiring bertambahnya variasi aktivitas — dari r = 0.804 (PM<sub>2.5</sub>) pada Lapangan 1, hingga menguat tajam menjadi r = 0.992 (PM<sub>2.5</sub>) pada Lapangan 2. Semakin ekstrem guncangannya (seperti aktivitas Berlari), semakin besar pula penyimpangan pembacaan alat.</li>
    <li><b>Deviasi maksimum</b> yang tercatat saat berlari mencapai rentang ~1 hingga nyaris 3 µg/m³ — angka yang cukup signifikan secara statistik meskipun masih berada di dalam margin toleransi error sensor.</li>
  </ul>
</div>

<div class="narrative-figure">
  <div style="display:flex; gap:14px; flex-wrap:wrap; justify-content:center;">
    <img src="assets/projects/motion-scatter-chamber.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/motion-scatter-lapangan1.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/motion-scatter-lapangan2.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
  </div>
  <figcaption>Scatter plot korelasi antara Mean Motion Index dengan rata-rata deviasi absolut |E| — Uji Chamber dikelompokkan per skema percobaan P1–P4 (kiri), Uji Lapangan 1 (tengah) dan Uji Lapangan 2 (kanan) dikelompokkan per aktivitas (Jalan, Lari, Beam)</figcaption>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">0.992</div><div class="sm-label">r TERTINGGI PM2.5 (LAPANGAN 2)</div></div>
  <div class="stat-mini"><div class="sm-num">0.863</div><div class="sm-label">r PM2.5 (CHAMBER)</div></div>
  <div class="stat-mini"><div class="sm-num">~1—3 µg/m³</div><div class="sm-label">DEVIASI MAKS SAAT LARI</div></div>
  <div class="stat-mini"><div class="sm-num">3</div><div class="sm-label">SKENARIO PENGUJIAN</div></div>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Kesimpulan Akhir Proyek</div>
  <p>Riset ini sukses memetakan blind-spot pada instrumen wearable kualitas udara. Melalui perpaduan ilmu integrasi hardware (IoT), ekstraksi fitur Machine Learning (HAR), hingga data wrangling statistik, proyek ini membuktikan bahwa data kualitas udara personal tidak valid jika ditelan mentah-mentah tanpa memperhitungkan konteks mekanis tubuh penggunanya. Temuan data ini menjadi fondasi fundamental bagi perancangan algoritma kompensasi otomatis (adaptive filtering) untuk perangkat keras pintar di masa depan.</p>
</div>
"""

project_detail(
    "project-motion-effect.html", "📉",
    "Pengaruh Gerakan terhadap Pengukuran Partikulat",
    "Peneliti Utama (Skripsi)", "Telkom University", "Sep 2025 — Jul 2026 (Expected)",
    "Python, Analisis Statistik, Sensor Wearable",
    [],
    ["Data Analysis","Statistik","Python","Sensor Wearable","Skripsi"],
    other_aqms_links("project-motion-effect.html"),
    "motion",
    override_content=MOTION_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Pengaruh Gerakan terhadap Pengukuran Partikulat", thesis_note_links("project-motion-effect.html"))
)

TRAPGRADIEN_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">Tentang TrapGradien: Air Purifier Cerdas Berbasis AIoT</div>
  <p>TrapGradien adalah sistem purifikasi udara cerdas yang mengombinasikan teknologi presipitator elektrostatik dengan pemantauan berbasis Artificial Intelligent-Internet of Things (AIoT). Prinsip kerjanya memanfaatkan ion positif dan negatif untuk memuati partikel polutan di udara, lalu menjebaknya dalam kolektor debu sebelum dilepaskan kembali sebagai udara bersih — dilengkapi mekanisme auto-clean pada kolektornya.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-design.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Rancangan TrapGradien, mekanisme pemurnian udara, serta implementasi pemantauan kualitas udara dengan AIoT</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Peran Saya: Subsistem Sensor Pengukuran</div>
  <p>Dalam proyek ini, saya berperan sebagai Hardware Engineer yang bertanggung jawab pada subsistem sensor pengukuran — bagian yang bertugas membaca kondisi udara secara real-time baik di sisi upstream (sebelum dimurnikan) maupun downstream (setelah dimurnikan). Parameter yang dipantau mencakup PM (partikulat), suhu (T), kelembapan (RH), VOC, dan CO2, yang datanya kemudian diproses oleh mikrokontroler sebagai dasar sistem AIoT.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Desain Board Sensor</div>
  <p>Saya merancang PCB khusus untuk mengintegrasikan 4 unit sensor ke dalam satu board yang terhubung ke mikrokontroler D1 mini (ESP8266). Desain ini dibuat menggunakan KiCad, mencakup pengaturan jalur sinyal, antarmuka komunikasi antar-sensor, serta penempatan antena untuk konektivitas WiFi.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-pcb.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/10; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Layout PCB board sensor TrapGradien (KiCad) — integrasi 4 sensor dengan mikrokontroler D1 mini</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Arsitektur AIoT: Dari Sensor ke Dashboard</div>
  <p>Data yang terbaca dari board sensor dikirim melalui WiFi ke router/modem, diteruskan ke cloud server via HTTP, lalu ditampilkan pada antarmuka pengguna (aplikasi/dashboard) yang bisa diakses secara real-time.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-dashboard.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Dashboard monitoring TrapGradien secara real-time — Lab P320</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Metodologi Pengembangan: Diagram-V 2 Tahun</div>
  <p>Pengembangan TrapGradien mengikuti kerangka Diagram-V selama dua tahun penelitian. Tahun pertama (2025) difokuskan pada rancang-bangun dan validasi di lingkungan laboratorium — mulai dari kebutuhan sistem, desain, pembangunan sub-sistem, hingga integrasi (mencapai TKT 4). Tahun kedua (2026) berfokus pada validasi dan demonstrasi sistem di lingkungan yang relevan, hingga mencapai TKT 6.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-vdiagram.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Diagram alir (diagram V) penelitian dan pengembangan TrapGradien selama 2 tahun</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Kesimpulan</div>
  <p>Subsistem sensor pengukuran yang saya kembangkan berhasil dijalankan dan terintegrasi penuh ke dalam sistem TrapGradien — mulai dari pembacaan sensor di board, pengiriman data melalui WiFi, hingga tampil secara real-time di dashboard monitoring.</p>
</div>
"""

project_detail(
    "project-trapgradien.html", "🧪",
    "TrapGradien Air Filtration Monitor",
    "Hardware Engineer", "PUI-PT Intelligent Sensing-IoT, Telkom University", "Sep 2025 — Jan 2026",
    "KiCad, ESP8266 (D1 mini), Sensor IoT (PM/RH/T/VOC/CO2), AIoT Dashboard",
    [],
    ["IoT","Hardware","PCB Design","Air Filtration"],
    [("project-aqms.html","🌫️","Wearable AQMS (Perangkat)"),
     ("project-armor.html","🛡️","Moving Armor Target System")],
    "trapgradien",
    override_content=TRAPGRADIEN_CONTENT,
    show_banner=False
)

ARMOR_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">Tentang Moving Armor Target System</div>
  <p>Moving Armor Target System adalah proyek kolaborasi antara Telkom University dan PT SAS Aerosishan (SAS Defense) — sebuah target bergerak berbasis robot beroda rantai (tracked vehicle) yang dirancang untuk kebutuhan latihan tembak militer, mensimulasikan sasaran dinamis di lapangan tembak.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-icon.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Moving Armor Target System hasil pengembangan bersama Telkom University & SAS Defense, diuji di lapangan tembak Cipatat</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Peran Saya: Kontribusi pada Arsitektur Sistem</div>
  <p>Sebagai Intern di divisi System, saya berkontribusi dalam pengembangan arsitektur sistem tingkat tinggi (system-level architecture) untuk proyek ini — memastikan setiap komponen hardware dan software yang dirancang tim saling terintegrasi dengan baik.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Desain Casing Prototipe</div>
  <p>Saya merancang casing prototipe untuk implementasi hardware menggunakan Autodesk Inventor dan SOLIDWORKS, dengan mempertimbangkan kelayakan fungsional (agar komponen elektronik terlindungi dan mudah diakses) sekaligus kelayakan struktural (agar tahan terhadap kondisi lapangan).</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-prototype.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Prototipe robot Moving Armor Target System yang dikembangkan</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Dukungan Firmware & Antarmuka</div>
  <p>Selain hardware, saya turut membantu dalam pengembangan firmware serta konfigurasi tampilan antarmuka (interface display) sistem — bekerja sama dengan tim engineering untuk mengintegrasikan komponen hardware dan embedded system menjadi satu kesatuan yang berfungsi.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Uji Coba Lapangan</div>
  <p>Sistem ini diuji langsung di lapangan tembak, disaksikan oleh pihak TNI dan tim terkait untuk memvalidasi performa target bergerak dalam skenario latihan nyata.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-test.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Gambar belum ditambahkan.</div>
  </div>
  <figcaption>Uji coba sistem di lapangan tembak, disaksikan oleh pihak TNI dan tim terkait</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Kesimpulan</div>
  <p>Moving Armor Target System berhasil dijalankan dan didemonstrasikan langsung di lapangan tembak — membuktikan keberhasilan kolaborasi lintas tim dalam mengintegrasikan desain mekanik, hardware, firmware, dan sistem kendali menjadi satu robot target yang berfungsi penuh.</p>
</div>
"""

project_detail(
    "project-armor.html", "🛡️",
    "Moving Armor Target System",
    "Intern — System Division", "PT SAS Aerosishan, Bandung", "Jun 2025 — Agu 2025",
    "Autodesk Inventor, SOLIDWORKS, Firmware Development, System Architecture",
    [],
    ["Defense Tech","System Dev","Prototyping"],
    [("project-aqms.html","🌫️","Wearable AQMS (Perangkat)"),
     ("project-trapgradien.html","🧪","TrapGradien Air Filtration Monitor")],
    "armor",
    override_content=ARMOR_CONTENT,
    show_banner=False
)

# ==================== WORK DETAIL PAGES ====================
def work_detail(filename, role, org, duration, location, paragraphs, tags, other, slug, captions, override_content=None):
    others_html = ""
    for href, otitle in other:
        others_html += f'<a class="project-card" href="{href}" style="margin-bottom:10px;"><div class="project-body" style="display:flex; align-items:center; gap:12px; padding:14px 18px;"><span style="font-size:0.88rem; font-weight:600;">{otitle}</span></div></a>\n    '
    tags_html = "".join(f'<span class="tag-amber">{t}</span>' for t in tags)
    if override_content is not None:
        main_content = f"""{override_content}
<div class="tag-row" style="margin-top:20px;">{tags_html}</div>"""
    else:
        paras_html = "".join(f"<p>{p}</p>\n  " for p in paragraphs)
        main_content = f"""<div class="section-eyebrow" style="margin-top:6px;">GALERI FOTO</div>
{photo_carousel("work", slug, captions)}

<div class="detail-body">
  {paras_html}
  <div class="tag-row">{tags_html}</div>
</div>"""
    body = f"""
<div class="page-header">
  <a class="back-link" href="work.html">← Kembali ke Work History</a>
  <div class="section-title">{role}</div>
</div>

<div class="detail-meta">
  <div><div class="k">ORGANISASI</div><div class="v">{org}</div></div>
  <div><div class="k">LOKASI</div><div class="v">{location}</div></div>
  <div><div class="k">DURASI</div><div class="v">{duration}</div></div>
</div>

{main_content}

<div class="other-projects">
  <div class="label">PENGALAMAN LAINNYA</div>
  {others_html}
</div>
"""
    with open(f"{OUT}/{filename}","w") as f:
        f.write(page_shell(f"{role} — Rendy Ryan Renaldi", "work.html", body))

MERSI_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/mersi-logo.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:140px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo belum ditambahkan.</div>
  </div>
  <figcaption>Logo Laboratorium MERSI, Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Tentang Laboratorium MERSI</div>
  <p>MERSI adalah laboratorium akademik Telkom University yang fokus pada pendidikan dan riset di bidang sistem pengukuran, sensor, instrumentasi, signal conditioning, dan data acquisition. Laboratorium ini memberikan pelatihan praktik dan kesempatan riset untuk mengembangkan kemampuan teknis dan analitis mahasiswa di bidang instrumentation engineering.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Peran Saya: Koordinator Asisten</div>
  <p>Sebagai Koordinator Asisten, saya memimpin dan mengoordinasikan tim yang terdiri dari <b>11 asisten laboratorium</b>, mulai dari pembagian tugas per modul, penjadwalan sesi praktikum, hingga memastikan setiap asisten siap membimbing praktikan sesuai standar yang ditetapkan lab.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-asisten.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Tim asisten Laboratorium MERSI</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Cakupan Praktikum: 2 Mata Kuliah, 95 Praktikan per Kelas</div>
  <p>Saya mengoordinasikan dua mata kuliah praktikum sekaligus — <b>Sistem Pengukuran</b> dan <b>Sistem Instrumentasi</b> — masing-masing diikuti oleh <b>95 mahasiswa praktikan</b> per mata kuliah.</p>
  <p style="margin-top:16px;">Modul praktikum <b>Sistem Pengukuran</b> mencakup:</p>
  <ul class="narrative-list">
    <li>Modul 1 — Sistem Pengukuran dan Analisis Data</li>
    <li>Modul 2 — Sensor Posisi</li>
    <li>Modul 3 — Sensor Sudut</li>
    <li>Modul 4 — Sensor Suhu</li>
    <li>Modul 5 — Sensor Aliran</li>
    <li>Modul 6 — Sensor Cahaya</li>
  </ul>
  <p style="margin-top:16px;">Modul praktikum <b>Sistem Instrumentasi</b> mencakup:</p>
  <ul class="narrative-list">
    <li>Modul 1 — Pengkondisian Sinyal</li>
    <li>Modul 2 — Voltage to Current Converter</li>
    <li>Modul 3 — Analog to Digital Converter</li>
    <li>Modul 4 — Digital to Analog Converter</li>
    <li>Modul 5 — Sensor dan Aktuator</li>
    <li>Modul 6 — Pengenalan Arduino Uno</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-modul.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Kegiatan running modul praktikum</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Training of Trainers (ToT) & Evaluasi</div>
  <p>Sebelum setiap sesi praktikum berjalan, saya memimpin <b>Training of Trainers (ToT)</b> untuk memastikan seluruh asisten memahami materi dan teknis modul secara seragam. Setelah praktikum selesai, saya juga memimpin sesi <b>evaluasi</b> untuk menilai kualitas penyampaian materi dan mengumpulkan masukan perbaikan untuk sesi berikutnya.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-praktikum.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Foto belum ditambahkan.</div>
  </div>
  <figcaption>Kondisi ketika praktikum berlangsung</figcaption>
</div>
"""

work_detail(
    "work-mersi.html",
    "Head of Assistant",
    "Measurement and Instrumentation Systems Laboratory (MERSI), Telkom University",
    "Sep 2025 — Jun 2026", "Bandung, Indonesia",
    [],
    ["Leadership", "Instrumentation", "Teaching Assistant"],
    [("work-puiptiot.html","Research Intern — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-oversight.html","Head of the Oversight Commission")],
    "mersi",
    ["Sesi pendampingan praktikum di Laboratorium MERSI",
     "Briefing dan koordinasi tim asisten laboratorium",
     "Alat ukur instrumentasi yang digunakan mahasiswa"],
    override_content=MERSI_CONTENT
)

PUIPTIOT_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/puiptiot-logo.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:160px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo belum ditambahkan.</div>
  </div>
  <figcaption>Pusat Unggulan IPTEK Perguruan Tinggi — Intelligent Sensing-IoT (IS-IoT), Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Tentang PUI-PT Intelligent Sensing-IoT</div>
  <p>PUI-PT Intelligent Sensing-IoT (IS-IoT) adalah pusat riset Telkom University yang berfokus pada Intelligent Sensing, Internet of Things (IoT), Wireless Sensor Networks (WSN), dan Artificial Intelligence (AI). Pusat riset ini mengembangkan teknologi sensing inovatif untuk solusi yang cerdas, terhubung, dan berkelanjutan melalui kolaborasi dengan akademisi dan industri.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Peran Saya: Hardware Engineer</div>
  <p>Selama menjadi Hardware Engineer di sini, saya bertanggung jawab mengembangkan subsistem sensor pengukuran untuk TrapGradien — air purifier cerdas berbasis AIoT. Pekerjaan saya mencakup perancangan PCB board sensor, integrasi dengan mikrokontroler, hingga memastikan data sensor tersalur real-time ke dashboard monitoring.</p>
</div>

<div class="thesis-note">
  <b>🔗 Proyek yang saya kerjakan di sini:</b> TrapGradien Air Filtration Monitor — lihat detail lengkap desain PCB, arsitektur AIoT, dan hasil kerja saya di halaman proyek.
  <div class="tn-links">
    <a href="project-trapgradien.html">🧪 TrapGradien Air Filtration Monitor →</a>
  </div>
</div>
"""

work_detail(
    "work-puiptiot.html",
    "Hardware Engineer",
    "PUI-PT Intelligent Sensing-IoT, Telkom University",
    "Sep 2025 — Jan 2026", "Bandung, Indonesia",
    [],
    ["Hardware", "IoT", "PCB Design"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-oversight.html","Head of the Oversight Commission")],
    "puiptiot",
    ["Instalasi sensor pada unit filtrasi TrapGradien",
     "Pengambilan data sensor secara real-time",
     "Diskusi hasil riset bersama tim IS-IoT"],
    override_content=PUIPTIOT_CONTENT
)

work_detail(
    "work-sasaero.html",
    "Intern — System Division",
    "PT SAS Aerosishan",
    "Jun 2025 — Agu 2025", "Bandung, Indonesia",
    [
        "PT SAS Aerosishan adalah perusahaan rekayasa pertahanan dan kedirgantaraan berbasis di Bandung, yang fokus pada pengembangan sistem pertahanan canggih, teknologi aerospace, otomasi, fabrikasi, precision machining, dan solusi terkait unmanned aerial vehicle.",
        "Selama magang di divisi System, saya berkesempatan terlibat dalam lingkungan engineering profesional yang menekankan inovasi, presisi teknis, dan pengembangan teknologi pertahanan nasional.",
        "Kontribusi utama saya adalah membantu tim engineering dalam dokumentasi teknis, dukungan proyek, dan aktivitas pengembangan sistem pada proyek Moving Armor Target System — memastikan setiap tahap pengembangan terdokumentasi dengan presisi tinggi sesuai standar industri pertahanan."
    ],
    ["Defense Tech", "System Development", "Dokumentasi Teknis"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Research Intern — PUI-PT Intelligent Sensing-IoT"),
     ("work-oversight.html","Head of the Oversight Commission")],
    "sasaero",
    ["Suasana kerja di divisi System",
     "Dokumentasi teknis proyek Moving Armor Target System",
     "Lingkungan kerja PT SAS Aerosishan"]
)

work_detail(
    "work-oversight.html",
    "Head of the Oversight Commission",
    "Engineering Physics Representative Council (MPM), Telkom University",
    "Aug 2025 — Jan 2026", "Bandung, Indonesia",
    [
        "Student Representative Council (MPM) adalah badan legislatif mahasiswa di Telkom University, bertanggung jawab mewakili mahasiswa, mengawasi organisasi mahasiswa, mengevaluasi kinerja organisasi, dan mendukung tata kelola mahasiswa yang transparan dan akuntabel.",
        "Sebagai Head of the Oversight Commission, saya memimpin komisi pengawasan dalam mengevaluasi kinerja organisasi eksekutif mahasiswa, serta mengoordinasikan anggota komisi untuk melakukan monitoring organisasi dan peninjauan kinerja secara berkala.",
        "Peran ini mengasah kemampuan saya dalam kepemimpinan, tata kelola organisasi, dan komunikasi lintas divisi — di luar konteks teknis, tapi tetap relevan sebagai bekal kerja tim di lingkungan profesional."
    ],
    ["Leadership", "Governance", "Organisasi"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Research Intern — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan")],
    "oversight",
    ["Rapat komisi pengawasan MPM",
     "Evaluasi kinerja organisasi mahasiswa",
     "Kegiatan Engineering Physics Representative Council"]
)

# ==================== CERTIFICATES.HTML ====================
def cert_folder(icon_slug, label, items):
    import json as _json
    items_data = [{"images": images, "title": title, "issuer": issuer, "date": date} for title, issuer, date, images in items]
    items_attr = _json.dumps(items_data).replace('"', "&quot;")
    count = len(items)
    count_label = f"{count} SERTIFIKAT" if count != 1 else "1 SERTIFIKAT"
    return f"""<div class="cert-folder" data-folder-name="{label}" data-items='{items_attr}'>
  <img class="cert-folder-icon-img" src="assets/icons/{icon_slug}.svg" alt="">
  <div class="cert-folder-name">{label}</div>
  <div class="cert-folder-count">{count_label}</div>
</div>"""

CERT_CATEGORIES = [
    ("organisasi", "Organisasi", [
        ("Sertifikat Apresiasi — Anggota Divisi Mentor, OC/Panitia Kalibrasi 2024", "HMTF (Himpunan Mahasiswa Teknik Fisika), Universitas Telkom", "Jan 2025", ["org-1a", "org-1b"]),
        ("Staff Departemen Kaderisasi — Badan Pengurus Harian HMTF 2024/2025", "Himpunan Mahasiswa Teknik Fisika (HMTF), Universitas Telkom", "Jan 2025", ["org-2a", "org-2b"]),
    ]),
    ("lab", "Mengajar & Laboratorium", [
        ("Kordinator Asisten & Asisten Praktikum Sistem Pengukuran", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2026", ["teach-1a", "teach-1b"]),
        ("Asisten Praktikum Rangkaian Listrik", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2025", ["teach-2a", "teach-2b"]),
        ("Asisten Praktikum Elektronika", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2025", ["teach-3a", "teach-3b"]),
        ("Asisten Praktikum Algoritma dan Pemrograman", "Laboratorium Dasar Komputer, Universitas Telkom", "Jan 2024", ["teach-4a", "teach-4b"]),
    ]),
    ("wirausaha", "Kewirausahaan", [
        ("UMKM Semut Corner — FKS Business Fair x Api Karya 2024", "BEM FKS, Universitas Telkom", "Nov 2024", ["wirausaha-1a", "wirausaha-1b"]),
    ]),
    ("bahasa", "Bahasa", [
        ("EPrT (English Proficiency Test) — Skor 570", "Telkom University Language Center", "Jun 2026", ["bahasa-1a", "bahasa-1b"]),
    ]),
    ("pelatihan", "Pelatihan & Magang", [
        ("Digital Learning — Study Group", "MBC Lab, Telkom University", "Mei–Jun 2024", ["pelatihan-1"]),
        ("Certificate of Internship", "PT SAS Aero Sishan", "Jun–Agu 2025", ["pelatihan-2"]),
        ("Program MBKM — Intelligent Sensing-IoT", "PUI-PT Intelligent Sensing-IoT, Telkom University", "Sep–Des 2025", ["pelatihan-3"]),
        ("Terminal / CMD untuk Development", "CODEPOLITAN", "Apr 2024", ["pelatihan-4"]),
    ]),
]

folders_html = "".join(cert_folder(icon_slug, label, items) for icon_slug, label, items in CERT_CATEGORIES)

certificates_body = f"""
<div class="page-header">
  <div class="section-eyebrow">PENGHARGAAN</div>
  <div class="section-title">Certificates</div>
  <p class="section-intro">Sertifikat dikelompokkan per kategori. Klik salah satu folder untuk lihat isinya.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <div class="folder-grid">
    {folders_html}
  </div>
</div>

<div class="cert-modal-overlay" id="certModalOverlay">
  <div class="cert-modal">
    <button class="cert-modal-close" id="certModalClose">✕</button>
    <div class="cert-modal-title" id="certModalTitle"></div>
    <div class="cert-modal-scroll" id="certModalScroll"></div>
  </div>
</div>

<div class="cert-lightbox-overlay" id="certLightboxOverlay">
  <button class="cert-lightbox-close" id="certLightboxClose">✕</button>
  <button class="cert-lightbox-nav prev" id="certLightboxPrev">‹</button>
  <img id="certLightboxImg" src="" alt="">
  <button class="cert-lightbox-nav next" id="certLightboxNext">›</button>
  <div class="cert-lightbox-counter" id="certLightboxCounter"></div>
</div>
"""
with open(f"{OUT}/certificates.html","w") as f:
    f.write(page_shell("Certificates — Rendy Ryan Renaldi", "certificates.html", certificates_body))

# ---- Regenerate all pages so nav includes Certificates link everywhere ----
print("All files generated:", os.listdir(OUT))
