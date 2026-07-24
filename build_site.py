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
"code": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<path d="M17,14 L6,24 L17,34" {_C}/>
<path d="M31,14 L42,24 L31,34" {_C}/>
<line x1="27" y1="11" x2="21" y2="37" {_C}/>
</svg>''',
"leadership": f'''<svg viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
<circle cx="24" cy="10" r="6" {_C}/>
<circle cx="9" cy="35" r="5" {_C}/>
<circle cx="39" cy="35" r="5" {_C}/>
<line x1="24" y1="16" x2="10" y2="30" {_C}/>
<line x1="24" y1="16" x2="38" y2="30" {_C}/>
<line x1="24" y1="16" x2="24" y2="30" {_C}/>
<line x1="10" y1="30" x2="38" y2="30" {_C}/>
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
.exp-highlight-row{display:flex; gap:20px; flex-wrap:wrap; margin-top:12px; padding-top:12px; border-top:1px dashed var(--grid-line);}
.exp-highlight{font-family:'IBM Plex Mono', monospace;}
.exp-highlight .h-num{color:var(--cyan); font-weight:700; font-size:1.1rem;}
.exp-highlight .h-label{color:var(--muted); font-size:0.62rem; letter-spacing:0.05em; text-transform:uppercase;}
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
<html lang="en">
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
<footer>© 2026 RENDY RYAN RENALDI — BUILT WITH GITHUB PAGES</footer>
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
    ("🌫️","Calibrating Low-Cost Air Quality Sensors","Technical notes on PM2.5 sensor drift and how to correct it with simple regression.","2026-05","4 min read"),
    ("🔋","Dynamic Power Management on Wearable Devices","How DPM can extend battery life without sacrificing sensor accuracy.","2026-04","5 min read"),
    ("📡","Intro to Wireless Sensor Networks","A summary of the core WSN concepts I picked up during my research at IS-IoT.","2026-03","3 min read"),
    ("🧪","Testing an Air Filtration System with Real-Time Data","The data validation process behind the TrapGradien system, and the challenges along the way.","2026-02","6 min read"),
    ("🛠️","A Technical Documentation Checklist from the Aerospace World","Documentation habits I picked up during my internship in the defense industry.","2026-01","4 min read"),
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
      <div class="ph-text">Cover photo not added yet.</div>
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
  <div class="section-eyebrow">01 / ABOUT</div>
  <div class="section-title">About Me</div>
  <p class="about-text">
    Undergraduate Engineering Physics student focused on instrumentation, embedded systems, and the Internet
    of Things (IoT). Experienced as a Laboratory Teaching Assistant and researcher developing a wearable
    air quality monitoring system that integrates Human Activity Recognition (HAR) and Dynamic Power
    Management (DPM). Comfortable with sensor integration, microcontroller programming, data analysis,
    system validation, and technical documentation — with a strong interest in building engineering
    solutions that bridge research and real-world application.
  </p>
  <div class="stat-row">
    <div class="stat"><div class="stat-num">3.30</div><div class="stat-label mono">GPA / 4.00</div></div>
    <div class="stat"><div class="stat-num">6</div><div class="stat-label mono">WORK EXPERIENCES</div></div>
    <div class="stat"><div class="stat-num">11</div><div class="stat-label mono">ASSISTANTS LED</div></div>
    <div class="stat"><div class="stat-num">2026</div><div class="stat-label mono">EXPECTED GRADUATE</div></div>
  </div>
  <div class="cta-row">
    <a class="cta-btn" href="projects.html">View Featured Projects →</a>
    <a class="cta-btn ghost" href="work.html">Work History</a>
    <a class="cta-btn ghost" href="skills.html">Skills</a>
  </div>
</section>

<section class="section">
  <div class="section-eyebrow">02 / NOTES</div>
  <div class="section-title">Latest Articles</div>
  <p class="section-intro">Short notes on instrumentation, IoT, and other technical topics I've been learning.</p>
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
  <div class="section-eyebrow">HISTORY</div>
  <div class="section-title">Work History</div>
  <p class="section-intro">Work, research, and organizational experience throughout my studies. Click any entry to see the full details.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <a class="exp-item" href="work-mersi.html">
    <div class="exp-date mono">SEP 2025 —<br>JUN 2026</div>
    <div>
      <div class="exp-role">Head of Assistant</div>
      <div class="exp-org">Measurement and Instrumentation Systems Laboratory (MERSI), Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Led and coordinated a team of 11 lab assistants.</li>
        <li>Oversaw lab sessions for 190 students across 2 courses: Measurement Systems & Instrumentation Systems.</li>
        <li>Designed the practicum schedule and monitored the quality of each session.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">11</div><div class="h-label">Assistants Led</div></div>
        <div class="exp-highlight"><div class="h-num">190</div><div class="h-label">Total Students</div></div>
        <div class="exp-highlight"><div class="h-num">2</div><div class="h-label">Courses</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>

  <a class="exp-item" href="work-puiptiot.html">
    <div class="exp-date mono">SEP 2025 —<br>JAN 2026</div>
    <div>
      <div class="exp-role">Hardware Engineer</div>
      <div class="exp-org">PUI-PT Intelligent Sensing-IoT, Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Developed and tested an IoT-based sensor system to monitor the performance of the TrapGradien air filtration system.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">4</div><div class="h-label">Sensors Integrated</div></div>
        <div class="exp-highlight"><div class="h-num">1</div><div class="h-label">AIoT Product</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>

  <a class="exp-item" href="work-sasaero.html">
    <div class="exp-date mono">JUN 2025 —<br>AUG 2025</div>
    <div>
      <div class="exp-role">Intern — System Division</div>
      <div class="exp-org">PT SAS Aerosishan, Bandung</div>
      <div class="exp-desc"><ul>
        <li>Supported the engineering team with technical documentation and system development on the Moving Armor Target System project.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">MATS</div><div class="h-label">Main Project</div></div>
        <div class="exp-highlight"><div class="h-num">3</div><div class="h-label">Months Interned</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>

  <a class="exp-item" href="work-oversight.html">
    <div class="exp-date mono">AUG 2025 —<br>JAN 2026</div>
    <div>
      <div class="exp-role">Leader of Commission II</div>
      <div class="exp-org">Student Representative Council (MPM), Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Led a team of 2 to oversee HMTF's governance and performance across 5 departments, 3 bureaus, 2 BSO, and the core executive board.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">11</div><div class="h-label">Bodies Supervised</div></div>
        <div class="exp-highlight"><div class="h-num">2</div><div class="h-label">Team Members Led</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>

  <a class="exp-item" href="work-praktikum.html">
    <div class="exp-date mono">JUN 2024 —<br>JUL 2025</div>
    <div>
      <div class="exp-role">Practicum Assistant</div>
      <div class="exp-org">Instrumentation System Laboratory, Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Prepared Modules, Journals, Preliminary Assignments, and Technical Reports for 3 practicums: Electrical Circuits, Basic Electronics, and Digital Electronics.</li>
        <li>Taught and mentored students through the entire practicum series for the 2023 cohort.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">190</div><div class="h-label">Students Taught</div></div>
        <div class="exp-highlight"><div class="h-num">3</div><div class="h-label">Practicums Taught</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>

  <a class="exp-item" href="work-daskom.html">
    <div class="exp-date mono">JUN 2023 —<br>JUN 2024</div>
    <div>
      <div class="exp-role">Practicum Assistant</div>
      <div class="exp-org">Basic Computing Laboratory, Telkom University</div>
      <div class="exp-desc"><ul>
        <li>Taught basic algorithms and C programming across 11 practicum modules, working alongside 92 fellow assistants.</li>
        <li>Member of the Rules & Discipline Committee, leading practicum shifts.</li>
      </ul></div>
      <div class="exp-highlight-row">
        <div class="exp-highlight"><div class="h-num">240</div><div class="h-label">Students Taught</div></div>
        <div class="exp-highlight"><div class="h-num">92</div><div class="h-label">Fellow Assistants</div></div>
        <div class="exp-highlight"><div class="h-num">11</div><div class="h-label">Modules Taught</div></div>
      </div>
      <span class="exp-more">Read full details →</span>
    </div>
  </a>
</div>
"""
with open(f"{OUT}/work.html","w") as f:
    f.write(page_shell("Work History — Rendy Ryan Renaldi", "work.html", work_body))

# ==================== SKILLS.HTML ====================
skills_body = """
<div class="page-header">
  <div class="section-eyebrow">CAPABILITIES</div>
  <div class="section-title">Skills</div>
  <p class="section-intro">Technical areas I've built through coursework, research, and work experience. Click any card to see where it's been applied.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <div class="skills-grid">
    <div class="skill-card" data-skill-name="Embedded Systems"
      data-story="Started with instrumentation & embedded systems coursework, then deepened through the AQMS thesis project and my internship at PT SAS Aerosishan."
      data-tools='[{"name":"Arduino","level":"Advanced"},{"name":"Sensor Integration","level":"Advanced"},{"name":"Firmware","level":"Intermediate"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"Moving Armor Target System","url":"project-armor.html"}]'>
      <img class="skill-icon-img" src="assets/icons/embedded.svg" alt="">
      <div class="skill-name">Embedded Systems</div>
      <div class="skill-desc">Microcontroller programming &amp; sensor integration for embedded systems</div>
      <div class="tag-wrap"><span class="tag">Arduino</span><span class="tag">Sensor Integration</span><span class="tag">Firmware</span></div>
    </div>
    <div class="skill-card" data-skill-name="IoT &amp; Wireless Sensing"
      data-story="First picked up during research at PUI-PT Intelligent Sensing-IoT, digging into how sensors connect within real-time monitoring systems."
      data-tools='[{"name":"Wireless Sensor Network","level":"Intermediate"},{"name":"MQTT","level":"Basic"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"}]'>
      <img class="skill-icon-img" src="assets/icons/iot.svg" alt="">
      <div class="skill-name">IoT &amp; Wireless Sensing</div>
      <div class="skill-desc">IoT devices and sensor networks for monitoring systems</div>
      <div class="tag-wrap"><span class="tag">Wireless Sensor Network</span><span class="tag">MQTT</span></div>
    </div>
    <div class="skill-card" data-skill-name="Instrumentation"
      data-story="Sharpened while serving as Head of Assistant at MERSI Laboratory, guiding measurement & instrumentation systems practicums for hundreds of students."
      data-tools='[{"name":"DAQ","level":"Advanced"},{"name":"Signal Conditioning","level":"Intermediate"},{"name":"Calibration","level":"Advanced"}]'
      data-related='[{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"},{"title":"Head of Assistant — MERSI","url":"work-mersi.html"}]'>
      <img class="skill-icon-img" src="assets/icons/instrumentation.svg" alt="">
      <div class="skill-name">Instrumentation</div>
      <div class="skill-desc">Signal conditioning, data acquisition, and calibration of measurement systems</div>
      <div class="tag-wrap"><span class="tag">DAQ</span><span class="tag">Signal Conditioning</span><span class="tag">Calibration</span></div>
    </div>
    <div class="skill-card" data-skill-name="Data &amp; Documentation"
      data-story="Built from the habit of writing technical documentation at PT SAS Aerosishan and validating research data throughout my studies."
      data-tools='[{"name":"Data Analysis","level":"Advanced"},{"name":"System Validation","level":"Intermediate"},{"name":"Tech Docs","level":"Advanced"}]'
      data-related='[{"title":"Wearable AQMS + HAR &amp; DPM","url":"project-aqms.html"},{"title":"TrapGradien Air Filtration Monitor","url":"project-trapgradien.html"},{"title":"Moving Armor Target System","url":"project-armor.html"}]'>
      <img class="skill-icon-img" src="assets/icons/data.svg" alt="">
      <div class="skill-name">Data &amp; Documentation</div>
      <div class="skill-desc">Data analysis, system validation, and technical documentation</div>
      <div class="tag-wrap"><span class="tag">Data Analysis</span><span class="tag">System Validation</span><span class="tag">Tech Docs</span></div>
    </div>
    <div class="skill-card" data-skill-name="C Programming"
      data-story="Sharpened while serving as a Practicum Assistant at the Basic Computing Laboratory (Daskom), teaching basic algorithms & C programming to hundreds of students, then applied directly by building the Kost-In program."
      data-tools='[{"name":"C Programming","level":"Advanced"},{"name":"Struct & File Handling","level":"Advanced"},{"name":"Algorithms & Data Structures","level":"Advanced"}]'
      data-related='[{"title":"Practicum Assistant — Basic Computing Laboratory","url":"work-daskom.html"},{"title":"Kost-In: Room Rental Management System","url":"project-kostin.html"}]'>
      <img class="skill-icon-img" src="assets/icons/code.svg" alt="">
      <div class="skill-name">C Programming</div>
      <div class="skill-desc">From basic algorithms to full programs built on struct & file handling</div>
      <div class="tag-wrap"><span class="tag">C Programming</span><span class="tag">Struct</span><span class="tag">File Handling</span></div>
    </div>
    <div class="skill-card" data-skill-name="Leadership &amp; Organizational Management"
      data-story="Shaped by two distinct leadership roles: leading Commission II at MPM overseeing HMTF's governance, and serving as Assistant Coordinator at MERSI Laboratory leading 11 assistants."
      data-tools='[{"name":"Team Leadership","level":"Advanced"},{"name":"Organizational Governance","level":"Advanced"},{"name":"Strategic Evaluation","level":"Intermediate"}]'
      data-related='[{"title":"Leader of Commission II — MPM","url":"work-oversight.html"},{"title":"Head of Assistant — MERSI","url":"work-mersi.html"}]'>
      <img class="skill-icon-img" src="assets/icons/leadership.svg" alt="">
      <div class="skill-name">Leadership &amp; Organizational Management</div>
      <div class="skill-desc">Leading teams, overseeing organizational governance, and strategic performance evaluation</div>
      <div class="tag-wrap"><span class="tag">Team Leadership</span><span class="tag">Governance</span><span class="tag">Evaluation</span></div>
    </div>
  </div>
</div>

<div class="skill-modal-overlay" id="skillModalOverlay">
  <div class="skill-modal">
    <button class="skill-modal-close" id="skillModalClose">✕</button>
    <div class="skill-modal-title" id="skillModalTitle"></div>
    <div class="skill-modal-label">THE STORY</div>
    <div class="skill-modal-story" id="skillModalStory"></div>
    <div class="skill-modal-label">PROFICIENCY LEVEL</div>
    <div id="skillModalTools"></div>
    <div class="skill-modal-label">APPLIED IN</div>
    <div id="skillModalList"></div>
  </div>
</div>
"""
with open(f"{OUT}/skills.html","w") as f:
    f.write(page_shell("Skills — Rendy Ryan Renaldi", "skills.html", skills_body))

# ==================== PROJECTS.HTML (grid -> links to detail pages) ====================
projects_body = """
<div class="page-header">
  <div class="section-eyebrow">WORKS</div>
  <div class="section-title">Featured Projects</div>
  <p class="section-intro">Click any project to see its full detail page. The first 3 projects come from the same undergraduate thesis, split out to highlight different skills.</p>
</div>

<div class="section" style="border-top:none; padding-top:10px;">
  <div class="project-grid">
    <a class="project-card" href="project-aqms.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(201,168,118,0.14));"><img src="assets/projects/aqms-device.jpg" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Wearable AQMS (Device) <span class="project-chevron">→</span></div>
        <div class="project-summary">Thesis: an IoT-based wearable air quality monitoring device.</div>
        <div class="tag-row"><span class="tag-amber">IoT</span><span class="tag-amber">Wearable</span><span class="tag-amber">Embedded</span></div>
      </div>
    </a>

    <a class="project-card" href="project-kalibrasi.html">
      <div class="project-banner" style="padding:0;"><img src="assets/projects/kalibrasi-banner.jpg" alt="" style="width:100%; height:100%; object-fit:cover;"></div>
      <div class="project-body">
        <div class="project-title">Sensor Calibration & Data Processing <span class="project-chevron">→</span></div>
        <div class="project-summary">Thesis: calibrating 6 sensor parameters against reference instruments.</div>
        <div class="tag-row"><span class="tag-amber">Data Analysis</span><span class="tag-amber">Statistics</span></div>
      </div>
    </a>

    <a class="project-card" href="project-har.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(176,100,74,0.14));"><img src="assets/projects/har-aktivitas.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">HAR Model Development <span class="project-chevron">→</span></div>
        <div class="project-summary">Thesis: an activity classification model from IMU data (96.33% accuracy).</div>
        <div class="tag-row"><span class="tag-amber">Machine Learning</span><span class="tag-amber">Python</span></div>
      </div>
    </a>

    <a class="project-card" href="project-motion-effect.html">
      <div class="project-banner" style="padding:0; background:linear-gradient(135deg, var(--panel-raised), rgba(150,160,120,0.14));"><img src="assets/projects/motion-icon.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:8px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Effect of Motion on Particulate Measurement <span class="project-chevron">→</span></div>
        <div class="project-summary">Thesis: the core finding — deviation analysis of PM2.5/PM10 under dynamic conditions.</div>
        <div class="tag-row"><span class="tag-amber">Data Analysis</span><span class="tag-amber">Statistics</span></div>
      </div>
    </a>

    <a class="project-card" href="project-trapgradien.html">
      <div class="project-banner" style="padding:0; background:#fff;"><img src="assets/projects/trapgradien-icon.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:12px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">TrapGradien Air Filtration Monitor <span class="project-chevron">→</span></div>
        <div class="project-summary">An IoT sensor system for monitoring air filtration performance.</div>
        <div class="tag-row"><span class="tag-amber">IoT</span><span class="tag-amber">Sensor Testing</span></div>
      </div>
    </a>

    <a class="project-card" href="project-armor.html">
      <div class="project-banner" style="padding:0;"><img src="assets/projects/armor-icon.jpg" alt="" style="width:100%; height:100%; object-fit:cover;"></div>
      <div class="project-body">
        <div class="project-title">Moving Armor Target System <span class="project-chevron">→</span></div>
        <div class="project-summary">Technical support for a defense systems project at PT SAS Aerosishan.</div>
        <div class="tag-row"><span class="tag-amber">Defense Tech</span><span class="tag-amber">System Dev</span></div>
      </div>
    </a>

    <a class="project-card" href="project-kostin.html">
      <div class="project-banner" style="padding:0; background:#fff;"><img src="assets/projects/kostin-logo.png" alt="" style="width:100%; height:100%; object-fit:contain; padding:14px; box-sizing:border-box;"></div>
      <div class="project-body">
        <div class="project-title">Kost-In: Room Rental Management System <span class="project-chevron">→</span></div>
        <div class="project-summary">A C program for kos (boarding house) management — from both the admin (owner) and user (tenant) side.</div>
        <div class="tag-row"><span class="tag-amber">C Programming</span><span class="tag-amber">Struct</span></div>
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
        <div class="ph-text">Photo not added yet.<br>Place the image file at:</div>
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
        <div class="ph-text">Photo not added yet.<br>Place the image file at:</div>
        <div class="ph-path">assets/{folder}/{slug}-{i}.jpg</div>
      </div>
    </div>"""
    dots = "".join(f'<button class="carousel-dot{" active" if i==0 else ""}"></button>' for i in range(len(captions)))
    captions_attr = _json.dumps(captions).replace('"', "&quot;")
    return f"""<div class="photo-carousel" data-captions="{captions_attr}">
  <div class="carousel-viewport">
    <div class="carousel-track">{slides}</div>
    <button class="carousel-btn prev" aria-label="Previous">‹</button>
    <button class="carousel-btn next" aria-label="Next">›</button>
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
    <button class="carousel-btn prev" aria-label="Previous">‹</button>
    <button class="carousel-btn next" aria-label="Next">›</button>
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
        photo_captions = [f"{title} documentation — photo 1", f"{title} documentation — photo 2", f"{title} documentation — photo 3"]

    if override_content is not None:
        main_content = f"""{override_content}
<div class="tag-row" style="margin-top:20px;">{tags_html}</div>"""
    else:
        paras_html = "".join(f"<p>{p}</p>\n  " for p in paragraphs)
        main_content = f"""<div class="section-eyebrow" style="margin-top:6px;">PHOTO GALLERY</div>
{photo_carousel("projects", slug, photo_captions)}

<div class="detail-body">
  {paras_html}
  <div class="tag-row">{tags_html}</div>
</div>

{extra_html}"""

    body = f"""
<div class="page-header">
  <a class="back-link" href="projects.html">← Back to Projects</a>
  {banner_block}
  <div class="section-title">{title}</div>
</div>

<div class="detail-meta">
  <div><div class="k">ROLE</div><div class="v">{role}</div></div>
  <div><div class="k">ORGANIZATION</div><div class="v">{org}</div></div>
  <div><div class="k">DURATION</div><div class="v">{duration}</div></div>
  <div><div class="k">TOOLS</div><div class="v">{tools}</div></div>
</div>

{thesis_note}

{main_content}

<div class="other-projects">
  <div class="label">OTHER PROJECTS</div>
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
      <div class="ph-text">Chart not added yet.<br>Place the image file at:</div>
      <div class="ph-path">{src}</div>
    </div>
    <figcaption>{caption}</figcaption>
  </figure>"""
    return f'<div class="chart-gallery">{figs}</div>'

def thesis_note(current_label, links):
    links_html = "".join(f'<a href="{href}">{label}</a>' for href, label in links)
    return f"""<div class="thesis-note">
  <b>📖 Part of the same undergraduate thesis:</b> "Development of a Wearable Air Quality Monitoring
  System with Human Activity Recognition Integration for Analyzing the Effect of Motion on
  Particulate Measurement" — this page focuses on the <b>{current_label}</b> section. Other parts of the same research:
  <div class="tn-links">{links_html}</div>
</div>"""

AQMS_LINKS = [
    ("project-aqms.html", "🌫️", "Wearable AQMS (Device)"),
    ("project-kalibrasi.html", "🧪", "Sensor Calibration & Data Processing"),
    ("project-har.html", "🏃", "HAR Model Development"),
    ("project-motion-effect.html", "📉", "Effect of Motion on Particulate Measurement"),
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
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Ergonomic use of the Wearable AQMS on the chest area</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Why Build a Wearable AQMS?</div>
  <p>Conventional air quality monitoring systems (AQMS) are typically stationary, which limits their ability to capture micro-scale pollution variation. This low spatial resolution means the actual pollutant exposure an individual breathes in during daily activity often goes undetected. To address this, a wearable-based AQMS was developed, ergonomically designed to sit on the user's chest — the ideal position to represent breathing-zone air exposure while also capturing the body's mechanical vibration during movement.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-wiring.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/10; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Wiring diagram for integrating the microcontroller with multiple sensors and the power system</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Hardware Integration & IoT Architecture</div>
  <p>This device isn't just a simple sensor reader — it's a fully integrated IoT system that acquires multivariable data simultaneously. The central compute unit is a Wemos microcontroller (ESP32/ESP8266), wired into an integrated scheme connecting several components:</p>
  <ul class="narrative-list">
    <li><b>SPS30:</b> Precisely measures PM2.5 and PM10 particulates.</li>
    <li><b>ENS160 & AHT2x:</b> Measures volatile gases (TVOC), estimated CO2, ambient temperature, and humidity.</li>
    <li><b>Bosch IMU (Nicla Sense ME):</b> Acquires accelerometer and gyroscope data to detect the user's body movement patterns.</li>
    <li><b>Power Management:</b> A 3.7V 2000mAh Li-Po battery with an integrated charger/boost module to power the system independently (portable).</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-device.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:3/4; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>The Wearable AQMS's compact, portable form-factor</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Device Fabrication & Edge Computing</div>
  <p>On the physical design side, all components were assembled and fabricated into a sturdy, lightweight, pocket-sized casing (form-factor). Its compact size keeps airflow into the sensor inlet optimal without weighing down the user's movement.</p>
  <p style="margin-top:16px;">One of the key engineering innovations in this system is data transmission efficiency. Instead of sending hundreds of raw IMU data points per second — which would drain the battery — the device performs edge computing (local computation) to calculate the Motion Index in real time. The system only extracts and transmits a summary movement value alongside the air quality data, significantly saving on communication bandwidth.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/aqms-dashboard.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Real-time Cloud Gradien air quality monitoring dashboard</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Real-Time Data Monitoring (IoT Dashboard)</div>
  <p>Data acquired by the device is transmitted to a cloud interface (Cloud Gradien) for visual monitoring. This dashboard displays all critical metrics in real time — from the Air Quality Index (AQI), PM2.5 levels, and TVOC, to temperature status, humidity, and remaining battery percentage (Battery Criticality).</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion & Project Impact</div>
  <p>This project demonstrates the successful development of an end-to-end IoT architecture — from hardware design and power management wiring, to cloud transmission and interface visualization. By moving the IMU computation load directly onto the device (edge computing), this Wearable AQMS is able to operate efficiently, portably, and stably when used by people in the field, enabling a more personal measurement of air pollution exposure.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Documentation</div>
</div>
""" + image_carousel([
    ("assets/projects/aqms-solder.jpg", "Soldering and assembling the device's electronic components"),
    ("assets/projects/aqms-users.jpg", "Documentation of users wearing the Wearable AQMS during field testing"),
], aspect_ratio="16/9", fit="contain")

project_detail(
    "project-aqms.html", "🌫️",
    "Wearable AQMS (Device)",
    "Principal Researcher (Thesis)", "Telkom University", "Feb 2026 — Mar 2026",
    "ESP32, ESP8266, SPS30, ENS160, AHT21, Nicla Sense ME (Bosch IMU)",
    [],
    ["IoT","Wearable","Embedded Systems","Thesis"],
    [("project-trapgradien.html","🧪","TrapGradien Air Filtration Monitor"),
     ("project-armor.html","🛡️","Moving Armor Target System")],
    "aqms",
    override_content=AQMS_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Wearable AQMS (Device)", thesis_note_links("project-aqms.html"))
)

# ---- 2. KALIBRASI SENSOR LINGKUNGAN ----
KALIBRASI_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-diagram-sistem.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>Calibration chamber setup / calibration system block diagram</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Why Do Sensors Need Calibration?</div>
  <p>Building a wearable air quality monitoring system means using low-cost sensors to keep the form factor compact (like the SPS30 and ENS160). However, this class of sensor often carries factory-inherent reading bias. Without calibration, it would be very hard to tell whether a change in readings is purely due to environmental conditions, motion disturbance, or just sensor noise. That's why 6 environmental parameters across 7 device units had to be tested and aligned against industry-standard reference instruments (OPC-N3, DT-900A, and SHT20).</p>
  <table class="data-table">
    <tr><th>Parameter</th><th>Sensor on the Wearable AQMS</th><th>Reference Instrument</th></tr>
    <tr><td>PM2.5</td><td>SPS30</td><td>OPC-N3</td></tr>
    <tr><td>PM10</td><td>SPS30</td><td>OPC-N3</td></tr>
    <tr><td>TVOC</td><td>ENS160</td><td>DT-900A</td></tr>
    <tr><td>eCO2</td><td>ENS160</td><td>RS485 CO2 Sensor</td></tr>
    <tr><td>Temperature</td><td>AHT21</td><td>SHT20</td></tr>
    <tr><td>Humidity</td><td>AHT21</td><td>SHT20</td></tr>
  </table>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-ts-pm25.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>PM2.5 calibration time series (decay method) — Mobile-1 through Mobile-7</figcaption>
</div>
<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-ts-suhu.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>Temperature calibration time series (heating phase) — Mobile-1 through Mobile-7</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Data Collection Method (Sensor Acquisition)</div>
  <p>To build an accurate model, data was collected through calibration chamber experiments, each with a tailored approach per parameter:</p>
  <ul class="narrative-list">
    <li><b>Particulates (PM2.5 & PM10):</b> Used the decay method. Pollutants were pumped in until concentrated, then allowed to gradually decrease using clean air. This trains the sensor to recognize the pollution range from high to low naturally.</li>
    <li><b>Temperature & Humidity:</b> Testing was focused purely on the heating (rising) phase. The cooling (decay) phase was intentionally excluded from the modeling to avoid data distortion from residual heat or internal heat generated by the microcontroller's own electronic components.</li>
  </ul>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">0.9978</div><div class="sm-label">R² PM2.5 (QUADRATIC)</div></div>
  <div class="stat-mini"><div class="sm-num">0.9797</div><div class="sm-label">R² PM10 (QUADRATIC)</div></div>
  <div class="stat-mini"><div class="sm-num">&lt;0.7%</div><div class="sm-label">TEMP & HUMIDITY MAPE</div></div>
  <div class="stat-mini"><div class="sm-num">6</div><div class="sm-label">PARAMETERS CALIBRATED</div></div>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Behind the Numbers: Data Cleansing & Model Evaluation</div>
  <p>The high accuracy figures above weren't obtained instantly. This process involved a rigorous data pipeline and preprocessing:</p>
  <ul class="narrative-list">
    <li><b>Handling Large Datasets:</b> Processing, time-syncing/cropping, and consolidating 22,297 rows of raw time-series data pulled simultaneously from all IoT devices.</li>
    <li><b>Data Cleansing & Transformation:</b> Filtering out roughly 800 anomalous data points (outliers) using statistical approaches (Interquartile Range / IQR and Rolling MAD) to preserve data integrity. This process produced 12,225 clean data points ready for model training.</li>
    <li><b>Model Error Analysis:</b> Iteratively evaluating prediction algorithms using error metrics such as RMSE, MAE, and MAPE.</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-scatter.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>Scatter plot of the corrected sensor readings (post-calibration), tightly clustered along the ideal line</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Modeling Results & Conclusion</div>
  <p>Comparing the modeling approaches (Linear vs. Quadratic), the Quadratic model proved most effective at correcting the non-linear bias in the particulate sensors, significantly reducing the error (RMSE). Conversely, for temperature, humidity, and TVOC gas, the Linear model was chosen since it was already highly accurate and much lighter (more efficient) to implement directly in microcontroller computation (on-device).</p>
  <p style="margin-top:16px;">Through this data processing pipeline, the system successfully turned low-cost sensors into high-accuracy instruments (R² values up to 0.99). With this valid, clean data baseline in place, the more complex analysis in the next stage — detecting metric disturbances caused by running/walking motion (Human Activity Recognition) — could be carried out with a very high level of confidence.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/kalibrasi-rekap-slide.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>Calibration results summary: MAPE heatmap across all units & parameters, along with the final correction model chosen</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Documentation</div>
</div>
""" + image_carousel([
    ("assets/projects/kalibrasi-banner.jpg", "HMI panel monitoring real-time PM2.5, PM10, temperature, and CO2 during calibration"),
    ("assets/projects/kalibrasi-1.jpg", "Documentation of the sensor calibration process inside the chamber"),
    ("assets/projects/kalibrasi-chamber-real.jpg", "The actual calibration chamber setup, including the pump, filter, and airflow control systems"),
], aspect_ratio="16/9", fit="contain")

project_detail(
    "project-kalibrasi.html", "🧪",
    "Environmental Sensor Calibration & Data Processing",
    "Principal Researcher (Thesis)", "Telkom University", "Feb 2026 — Mar 2026",
    "Python (pandas, NumPy, SciPy), Microsoft Excel, Matplotlib, Calibration Chamber",
    [],
    ["Data Analysis","Statistics","Regression","Sensor Calibration","Python"],
    other_aqms_links("project-kalibrasi.html"),
    "kalibrasi",
    override_content=KALIBRASI_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Environmental Sensor Calibration & Data Processing", thesis_note_links("project-kalibrasi.html"))
)

# ---- 3. PENGEMBANGAN MODEL HAR ----
HAR_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/har-aktivitas.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/12; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>The four main user activities classified by the system: Sitting, Walking, Running, and Riding/Beam</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Context & Modeling Goal</div>
  <p>In wearable-based air quality monitoring, sensor accuracy is highly vulnerable to motion artifacts. To study how much body movement affects pollution readings, the system needs to automatically recognize what the user is doing at any given moment. That's why a Machine Learning model based on Human Activity Recognition (HAR) was developed to classify 4 main user activities: Sitting, Walking, Running, and Riding (Beam).</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/har-windowing.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>Visualization of the Windowing technique on raw sensor signals, using a 2-second window with 50% overlap</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Data Acquisition & Windowing</div>
  <p>Data was collected from an Inertial Measurement Unit (IMU) — a 6-axis accelerometer and gyroscope — tested on 10 different subjects. Raw time-series data (over 101,000 samples) can't be fed directly into an ML model; analyzing human movement requires time segmentation. The data was sliced using a Windowing technique (2 seconds, 50% overlap), turning the raw 20Hz signal into 5,039 rows of structured dataset ready for extraction.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Feature Engineering & Motion Index</div>
  <p>To turn waveform signals into data an algorithm can learn from, 73 statistical features (such as Mean, Standard Deviation, Variance, RMS, Skewness, and Kurtosis) were extracted from every window.</p>
  <p style="margin-top:16px;">Beyond the standard features, one crucial metric was also extracted — the Motion Index — calculated from the standard deviation of acceleration magnitude. This value numerically measures movement intensity (Sitting = ~0.10, Running = ~19.54), which is later correlated directly with the air quality sensor's reading error rate.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/har-akurasi.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">📊</div>
    <div class="ph-text">Chart not added yet.</div>
  </div>
  <figcaption>Classification algorithm accuracy comparison (Random Forest, Decision Tree, KNN) at the evaluation stage</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Model Training: Balancing Accuracy & Computational Efficiency</div>
  <p>Model training used several classification algorithms: Random Forest, Decision Tree, and K-Nearest Neighbors. Random Forest produced the highest accuracy (98.51%), but for an IoT device (edge computing), that model was too complex and memory-hungry. System efficiency was the priority, so Decision Tree (DT) was ultimately chosen as the final algorithm. Although its accuracy is slightly below RF's, DT still delivered outstanding performance at 96.33%, with the advantage of a far lighter model structure that's easy to convert into if-else logic within the microcontroller's C/C++ code.</p>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">96.33%</div><div class="sm-label">DECISION TREE ACCURACY</div></div>
  <div class="stat-mini"><div class="sm-num">73</div><div class="sm-label">FEATURES PER WINDOW</div></div>
  <div class="stat-mini"><div class="sm-num">5,039</div><div class="sm-label">DATASET WINDOWS</div></div>
  <div class="stat-mini"><div class="sm-num">0.96</div><div class="sm-label">AVERAGE F1-SCORE</div></div>
</div>

<div class="narrative-figure">
  <div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
    <img src="assets/projects/har-confusion.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:360px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/har-feature-importance.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:360px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
  </div>
  <figcaption>Confusion Matrix for the Decision Tree model (left) and the Feature Importance chart showing the most influential features (right)</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Metric Evaluation & Feature Importance</div>
  <p>A rigorous evaluation was carried out using a Classification Report (Precision, Recall, F1-Score averaging 0.96) and Confusion Matrix analysis. The model proved highly robust at distinguishing contrasting activities (Sitting vs Running), though there was some prediction overlap (false positives) between Walking and Riding due to similar mechanical vibration at certain moments.</p>
  <p style="margin-top:16px;">Feature Importance analysis confirmed that the acc_mag_var feature (Accelerometer Magnitude Variance) carried the greatest weight in the algorithm's decision-making, proving that acceleration fluctuation is the best predictor for recognizing human movement patterns.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion</div>
  <p>This HAR model development successfully transformed raw movement data into activity context (Movement Category) and motion intensity (Motion Index) in real time. Successfully deploying a lightweight Machine Learning model onto the microcontroller proves that artificial intelligence can run smoothly on a wearable device, while also paving the way to validate air sensor data quality in the final analysis stage.</p>
</div>
"""

project_detail(
    "project-har.html", "🏃",
    "HAR Model Development",
    "Principal Researcher (Thesis)", "Telkom University", "Sep 2025 — Jul 2026 (Expected)",
    "Python, scikit-learn, pandas, numpy",
    [],
    ["Machine Learning","Data Analysis","Python","Feature Engineering","Classification"],
    other_aqms_links("project-har.html"),
    "har",
    override_content=HAR_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("HAR Model Development", thesis_note_links("project-har.html"))
)

# ---- 4. EFFECT OF MOTION ON PARTICULATE MEASUREMENT ANALYSIS ----
MOTION_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">Experiment Background: Why Motion Matters</div>
  <p>The Wearable AQMS system is designed to be worn on the body, meaning the device is constantly moving along with daily activity. This movement triggers orientation changes, mechanical vibration, and airflow turbulence around the particulate sensor inlet (SPS30), which relies on the laser light-scattering principle. This experiment was designed to answer one critical, data-driven question: <b>"Does the user's body motion distort pollution level readings (PM<sub>2.5</sub> and PM<sub>10</sub>), and how large is that deviation?"</b></p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/motion-diagram.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>Illustration of the A/B Testing methodology: dynamic device on the user vs. 3 static devices as an environmental control</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Testing Methodology: Static vs. Dynamic Approach</div>
  <p>To isolate the effect of motion from actual air pollution fluctuation, a direct A/B Testing methodology was applied. Devices were split into two groups:</p>
  <ul class="narrative-list">
    <li><b>Dynamic Group (Mobile 1 & 5):</b> Devices worn on the user's chest or mounted on a mechanical rotating rig.</li>
    <li><b>Control / Static Group (Mobile 3, 4, 6):</b> Three devices kept stationary at a fixed position to represent actual ambient particulate conditions.</li>
  </ul>
  <p style="margin-top:16px;">Testing was carried out across three tiered scenarios: (1) an enclosed chamber, (2) a controlled outdoor setting, and (3) real field testing covering Sitting, Walking, Running, and Riding (Beam) activities.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Data Analysis: Baseline Correction</div>
  <p>In low-cost sensor analysis, comparing raw value differences (ΔPM = PM<sub>dynamic</sub> − PM<sub>static</sub>) can be misleading due to inherent bias between sensor units that remains even after calibration.</p>
  <p style="margin-top:16px;">As the data analyst, this anomaly was addressed by applying Baseline Correction (E = ΔPM − B). Before and after each test, all devices were left together (co-located) to determine their baseline offset (B). Only by subtracting this baseline from the raw difference (ΔPM) could the pure effect of motion be extracted with precision.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/motion-formula.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>Analytical formula for neutralizing inter-sensor bias using Baseline Correction</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Analysis Results & Metric Correlation</div>
  <p>The post-correction data computation revealed a very interesting pattern: dynamic conditions (movement) consistently tended to make the device read lower particulate concentrations (negative deviation) compared to the static control.</p>
  <p style="margin-top:16px;">Further, a linear correlation analysis (Pearson's r) was performed between movement intensity (represented by the Mean Motion Index metric from the HAR algorithm) and the magnitude of the sensor's absolute deviation |E| in µg/m³:</p>
  <ul class="narrative-list">
    <li><b>Chamber Scenario:</b> A strong positive correlation was found (r = 0.863 for PM<sub>2.5</sub> and r = 0.580 for PM<sub>10</sub>) across all P1–P4 test schemes.</li>
    <li><b>Field Scenario:</b> This positive correlation grew even stronger as activity variation increased — from r = 0.804 (PM<sub>2.5</sub>) in Field 1, sharpening to r = 0.992 (PM<sub>2.5</sub>) in Field 2. The more extreme the motion (such as running), the greater the deviation in the device's readings.</li>
    <li>The <b>maximum deviation</b> recorded while running reached a range of ~1 to nearly 3 µg/m³ — a statistically significant figure, though still within the sensor's error tolerance margin.</li>
  </ul>
</div>

<div class="narrative-figure">
  <div style="display:flex; gap:14px; flex-wrap:wrap; justify-content:center;">
    <img src="assets/projects/motion-scatter-chamber.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/motion-scatter-lapangan1.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
    <img src="assets/projects/motion-scatter-lapangan2.png" alt="" onerror="this.style.display='none';" style="max-width:100%; width:320px; height:auto; border:1px solid var(--grid-line); background:#fff; object-fit:contain;">
  </div>
  <figcaption>Scatter plots of the correlation between Mean Motion Index and average absolute deviation |E| — Chamber Test grouped by trial scheme P1–P4 (left), Field Test 1 (middle) and Field Test 2 (right) grouped by activity (Walking, Running, Beam)</figcaption>
</div>

<div class="stat-mini-row">
  <div class="stat-mini"><div class="sm-num">0.992</div><div class="sm-label">HIGHEST r PM2.5 (FIELD 2)</div></div>
  <div class="stat-mini"><div class="sm-num">0.863</div><div class="sm-label">r PM2.5 (CHAMBER)</div></div>
  <div class="stat-mini"><div class="sm-num">~1—3 µg/m³</div><div class="sm-label">MAX DEVIATION WHILE RUNNING</div></div>
  <div class="stat-mini"><div class="sm-num">3</div><div class="sm-label">TEST SCENARIOS</div></div>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Final Project Conclusion</div>
  <p>This research successfully mapped a blind spot in wearable air quality instruments. By combining hardware integration (IoT), Machine Learning feature extraction (HAR), and statistical data wrangling, this project demonstrates that personal air quality data isn't valid if taken at face value without accounting for the mechanical context of the wearer's body. These findings lay the fundamental groundwork for designing automatic compensation algorithms (adaptive filtering) for future smart wearable hardware.</p>
</div>
"""

project_detail(
    "project-motion-effect.html", "📉",
    "Effect of Motion on Particulate Measurement",
    "Principal Researcher (Thesis)", "Telkom University", "Sep 2025 — Jul 2026 (Expected)",
    "Python, Statistical Analysis, Wearable Sensors",
    [],
    ["Data Analysis","Statistics","Python","Wearable Sensor","Thesis"],
    other_aqms_links("project-motion-effect.html"),
    "motion",
    override_content=MOTION_CONTENT,
    show_banner=False,
    thesis_note=thesis_note("Effect of Motion on Particulate Measurement", thesis_note_links("project-motion-effect.html"))
)

TRAPGRADIEN_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">About TrapGradien: An AIoT-Based Smart Air Purifier</div>
  <p>TrapGradien is a smart air purification system that combines electrostatic precipitator technology with Artificial Intelligent-Internet of Things (AIoT) monitoring. It works by using positive and negative ions to charge airborne pollutant particles, then trapping them in a dust collector before releasing clean air back out — complete with an auto-clean mechanism on the collector.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-design.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>TrapGradien design, air purification mechanism, and AIoT air quality monitoring implementation</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Sensor Measurement Subsystem</div>
  <p>In this project, I served as Hardware Engineer, responsible for the sensor measurement subsystem — the part tasked with reading air conditions in real time on both the upstream (before purification) and downstream (after purification) side. Monitored parameters include PM (particulates), temperature (T), humidity (RH), VOC, and CO2, with the data then processed by the microcontroller as the foundation of the AIoT system.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Sensor Board Design</div>
  <p>I designed a dedicated PCB to integrate 4 sensor units into a single board connected to a D1 mini (ESP8266) microcontroller. This design was built using KiCad, covering signal routing, inter-sensor communication interfacing, and antenna placement for WiFi connectivity.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-pcb.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/10; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>TrapGradien sensor board PCB layout (KiCad) — integrating 4 sensors with the D1 mini microcontroller</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">AIoT Architecture: From Sensor to Dashboard</div>
  <p>Data read from the sensor board is sent over WiFi to a router/modem, forwarded to a cloud server via HTTP, and then displayed on a user interface (app/dashboard) accessible in real time.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-dashboard.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>Real-time TrapGradien monitoring dashboard — Lab P320</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Development Methodology: 2-Year V-Model</div>
  <p>TrapGradien's development follows a V-Model framework across two years of research. The first year (2025) focused on design-build and validation in a laboratory environment — from system requirements, design, and sub-system construction, through to integration (reaching TRL 4). The second year (2026) focuses on system validation and demonstration in a relevant environment, up to reaching TRL 6.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/trapgradien-vdiagram.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>V-diagram flowchart of TrapGradien's 2-year research and development</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion</div>
  <p>The sensor measurement subsystem I developed was successfully run and fully integrated into the TrapGradien system — from sensor readings on the board and data transmission over WiFi, to real-time display on the monitoring dashboard.</p>
</div>
"""

project_detail(
    "project-trapgradien.html", "🧪",
    "TrapGradien Air Filtration Monitor",
    "Hardware Engineer", "PUI-PT Intelligent Sensing-IoT, Telkom University", "Sep 2025 — Jan 2026",
    "KiCad, ESP8266 (D1 mini), IoT Sensors (PM/RH/T/VOC/CO2), AIoT Dashboard",
    [],
    ["IoT","Hardware","PCB Design","Air Filtration"],
    [("project-aqms.html","🌫️","Wearable AQMS (Device)"),
     ("project-armor.html","🛡️","Moving Armor Target System")],
    "trapgradien",
    override_content=TRAPGRADIEN_CONTENT,
    show_banner=False
)

ARMOR_CONTENT = """
<div class="narrative-section">
  <div class="narrative-heading">About the Moving Armor Target System</div>
  <p>The Moving Armor Target System is a collaborative project between Telkom University and PT SAS Aerosishan (SAS Defense) — a moving target based on a tracked robot vehicle, designed for military live-fire training needs, simulating a dynamic target on the shooting range.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-icon.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>The Moving Armor Target System, developed jointly by Telkom University & SAS Defense, tested at the Cipatat shooting range</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Contributing to the System Architecture</div>
  <p>As an Intern in the System Division, I contributed to developing the high-level system architecture for this project — making sure every hardware and software component designed by the team integrated well together.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Prototype Casing Design</div>
  <p>I designed the prototype casing for the hardware implementation using Autodesk Inventor and SOLIDWORKS, balancing functional feasibility (so the electronic components stayed protected and accessible) with structural feasibility (so it could withstand field conditions).</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-prototype.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>The Moving Armor Target System robot prototype that was developed</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Firmware & Interface Support</div>
  <p>Beyond hardware, I also helped with firmware development and configuring the system's interface display — working with the engineering team to integrate the hardware and embedded system components into a single functioning whole.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Field Testing</div>
  <p>The system was tested directly on the shooting range, witnessed by the Indonesian Armed Forces (TNI) and the related team, to validate the moving target's performance in a real training scenario.</p>
</div>

<div class="narrative-figure">
  <img src="assets/projects/armor-test.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Image not added yet.</div>
  </div>
  <figcaption>Field testing at the shooting range, witnessed by the TNI and the related team</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion</div>
  <p>The Moving Armor Target System was successfully run and demonstrated live on the shooting range — proving the success of cross-team collaboration in integrating mechanical design, hardware, firmware, and control systems into a single, fully functional target robot.</p>
</div>
"""

project_detail(
    "project-armor.html", "🛡️",
    "Moving Armor Target System",
    "Intern — System Division", "PT SAS Aerosishan, Bandung", "Jun 2025 — Aug 2025",
    "Autodesk Inventor, SOLIDWORKS, Firmware Development, System Architecture",
    [],
    ["Defense Tech","System Dev","Prototyping"],
    [("project-aqms.html","🌫️","Wearable AQMS (Device)"),
     ("project-trapgradien.html","🧪","TrapGradien Air Filtration Monitor")],
    "armor",
    override_content=ARMOR_CONTENT,
    show_banner=False
)

KOSTIN_CONTENT = """
<div class="narrative-figure">
  <img src="assets/projects/kostin-logo.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:200px; background:#fff;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>Kost-In — Room Rental Management System</figcaption>
</div>
<div class="narrative-section">
  <div class="narrative-heading">Background: An Assistant Recruitment Project</div>
  <p>Kost-In is a C-based kos (boarding house) rental management program I built as part of the recruitment process to become a Practicum Assistant at the Basic Computing Laboratory (Daskom). The program simulates a kos management system from two sides at once: the kos owner (admin) and the tenant (user), complete with a flow from booking through to payment.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Admin-Side Features: Kos Management</div>
  <p>As the admin (kos owner), a user can:</p>
  <ul class="narrative-list">
    <li><b>View Registered Accounts</b> — monitor every user who has registered on the system.</li>
    <li><b>View Room Bookings</b> — see the list of booked rooms along with their availability status.</li>
    <li><b>Set Payment Reminder Timing</b> — configure a reminder for the rent payment due date.</li>
    <li><b>Set Prices</b> — determine the rental price for each room type.</li>
  </ul>
</div>

<div class="narrative-section">
  <div class="narrative-heading">User-Side Features: Search & Book a Room</div>
  <p>As the user (tenant), a person can register or log in, then:</p>
  <ul class="narrative-list">
    <li><b>Choose a room type</b> — Premium or Standard, with an optional laundry subscription.</li>
    <li><b>Choose a kos type</b> — Mixed, Male-only, or Female-only.</li>
    <li><b>Check the total cost</b> and choose a payment option — BCA, BRI, or QRIS.</li>
    <li><b>Leave a review</b> after renting, which other prospective tenants can see before booking.</li>
  </ul>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Technology & Implementation</div>
  <p>This program is built entirely in C, using <b>struct</b> to store account and room data, and <b>file handling</b> to persist data across sessions. The entire interaction flow is menu-driven (a menu-driven console interface) with a layered login system for admin and user.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion</div>
  <p>Kost-In successfully demonstrated my thorough understanding of C programming concepts — from struct and file handling, to designing complex program logic with multiple roles and user scenarios. This project became one of the key portfolio pieces that helped me get accepted as a Practicum Assistant at the Basic Computing Laboratory.</p>
</div>
"""

project_detail(
    "project-kostin.html", "🏠",
    "Kost-In: Room Rental Management System",
    "Developer (Recruitment Project)", "Basic Computing Laboratory, Telkom University", "Apr 2023",
    "C, Struct, File Handling",
    [],
    ["C Programming","Struct","File Handling","Console App"],
    [("work-daskom.html","💻","Practicum Assistant — Basic Computing Laboratory"),
     ("project-trapgradien.html","🧪","TrapGradien Air Filtration Monitor")],
    "kostin",
    override_content=KOSTIN_CONTENT,
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
        main_content = f"""<div class="section-eyebrow" style="margin-top:6px;">PHOTO GALLERY</div>
{photo_carousel("work", slug, captions)}

<div class="detail-body">
  {paras_html}
  <div class="tag-row">{tags_html}</div>
</div>"""
    body = f"""
<div class="page-header">
  <a class="back-link" href="work.html">← Back to Work History</a>
  <div class="section-title">{role}</div>
</div>

<div class="detail-meta">
  <div><div class="k">ORGANIZATION</div><div class="v">{org}</div></div>
  <div><div class="k">LOKASI</div><div class="v">{location}</div></div>
  <div><div class="k">DURATION</div><div class="v">{duration}</div></div>
</div>

{main_content}

<div class="other-projects">
  <div class="label">OTHER EXPERIENCE</div>
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
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>MERSI Laboratory logo, Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About MERSI Laboratory</div>
  <p>MERSI is an academic laboratory at Telkom University focused on education and research in measurement systems, sensors, instrumentation, signal conditioning, and data acquisition. The laboratory provides hands-on training and research opportunities to develop students' technical and analytical skills in instrumentation engineering.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Assistant Coordinator</div>
  <p>As Assistant Coordinator, I led and coordinated a team of <b>11 lab assistants</b> — from dividing tasks per module and scheduling practicum sessions, to making sure every assistant was ready to guide students to the lab's standard.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-asisten.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>MERSI Laboratory assistant team</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Practicum Scope: 2 Courses, 95 Students per Class</div>
  <p>I coordinated two practicum courses at once — <b>Measurement Systems</b> and <b>Instrumentation Systems</b> — each attended by <b>95 students</b> per course.</p>
  <p style="margin-top:16px;">The <b>Measurement Systems</b> practicum modules covered:</p>
  <ul class="narrative-list">
    <li>Module 1 — Measurement Systems and Data Analysis</li>
    <li>Module 2 — Position Sensors</li>
    <li>Module 3 — Angle Sensors</li>
    <li>Module 4 — Temperature Sensors</li>
    <li>Module 5 — Flow Sensors</li>
    <li>Module 6 — Light Sensors</li>
  </ul>
  <p style="margin-top:16px;">The <b>Instrumentation Systems</b> practicum modules covered:</p>
  <ul class="narrative-list">
    <li>Module 1 — Signal Conditioning</li>
    <li>Module 2 — Voltage to Current Converter</li>
    <li>Module 3 — Analog to Digital Converter</li>
    <li>Module 4 — Digital to Analog Converter</li>
    <li>Module 5 — Sensors and Actuators</li>
    <li>Module 6 — Introduction to Arduino Uno</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-modul.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Running a practicum module session</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Training of Trainers (ToT) & Evaluation</div>
  <p>Before each practicum session, I led a <b>Training of Trainers (ToT)</b> to make sure every assistant understood the material and module mechanics consistently. After each practicum wrapped up, I also led an <b>evaluation</b> session to assess teaching quality and gather feedback for improving the next session.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/mersi-praktikum.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Practicum session in progress</figcaption>
</div>

<div class="thesis-note">
  <b>📄 Related certificate:</b> Koordinator Asisten Sistem Pengukuran — see the Certificates page, under "Teaching & Laboratory".
  <div class="tn-links">
    <a href="certificates.html">📜 View Certificate →</a>
  </div>
</div>
"""

work_detail(
    "work-mersi.html",
    "Head of Assistant",
    "Measurement and Instrumentation Systems Laboratory (MERSI), Telkom University",
    "Sep 2025 — Jun 2026", "Bandung, Indonesia",
    [],
    ["Leadership", "Instrumentation", "Teaching Assistant"],
    [("work-puiptiot.html","Hardware Engineer — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-oversight.html","Leader of Commission II"),
     ("work-praktikum.html","Practicum Assistant — Instrumentation System Laboratory"),
     ("work-daskom.html","Practicum Assistant — Basic Computing Laboratory")],
    "mersi",
    ["Practicum mentoring session at MERSI Laboratory",
     "Briefing and coordination with the lab assistant team",
     "Instrumentation measurement tools used by students"],
    override_content=MERSI_CONTENT
)

PUIPTIOT_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/puiptiot-logo.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:160px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/6; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>Pusat Unggulan IPTEK Perguruan Tinggi — Intelligent Sensing-IoT (IS-IoT), Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About PUI-PT Intelligent Sensing-IoT</div>
  <p>PUI-PT Intelligent Sensing-IoT (IS-IoT) is a Telkom University research center focused on Intelligent Sensing, the Internet of Things (IoT), Wireless Sensor Networks (WSN), and Artificial Intelligence (AI). The center develops innovative sensing technologies for smart, connected, and sustainable solutions through collaboration with academia and industry.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Hardware Engineer</div>
  <p>As Hardware Engineer here, I was responsible for developing the sensor measurement subsystem for TrapGradien — an AIoT-based smart air purifier. My work covered designing the sensor PCB, integrating it with the microcontroller, and making sure sensor data streamed to the monitoring dashboard in real time.</p>
</div>

<div class="thesis-note">
  <b>🔗 Project I worked on here:</b> TrapGradien Air Filtration Monitor — see the full detail on the PCB design, AIoT architecture, and my work on the project page.
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
     ("work-oversight.html","Leader of Commission II"),
     ("work-praktikum.html","Practicum Assistant — Instrumentation System Laboratory"),
     ("work-daskom.html","Practicum Assistant — Basic Computing Laboratory")],
    "puiptiot",
    ["Sensor installation on the TrapGradien filtration unit",
     "Real-time sensor data collection",
     "Discussing research results with the IS-IoT team"],
    override_content=PUIPTIOT_CONTENT
)

SASAERO_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/sasaero-banner.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/5; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Banner not added yet.</div>
  </div>
  <figcaption>PT SAS Aero Sishan — Aerospace & Defense Systems Engineering</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About PT SAS Aero Sishan</div>
  <p>PT SAS Aero Sishan is a defense and aerospace engineering company based in Bandung, focused on developing advanced defense systems, aerospace technology, automation, fabrication, precision machining, and unmanned aerial vehicle solutions.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Intern — System Division</div>
  <p>During my internship in the System Division, I worked in a professional engineering environment that emphasized innovation, technical precision, and national defense technology development. My main contribution was working on the Moving Armor Target System (MATS) project — from system architecture support and prototype casing design, to hardware and firmware integration.</p>
</div>

<div class="thesis-note">
  <b>🔗 Project I worked on here:</b> Moving Armor Target System — see the full detail on the casing design, firmware, and field test results.
  <div class="tn-links">
    <a href="project-armor.html">🛡️ Moving Armor Target System →</a>
  </div>
</div>
"""

work_detail(
    "work-sasaero.html",
    "Intern — System Division",
    "PT SAS Aerosishan",
    "Jun 2025 — Aug 2025", "Bandung, Indonesia",
    [],
    ["Defense Tech", "System Development", "Prototyping"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Hardware Engineer — PUI-PT Intelligent Sensing-IoT"),
     ("work-oversight.html","Leader of Commission II"),
     ("work-praktikum.html","Practicum Assistant — Instrumentation System Laboratory"),
     ("work-daskom.html","Practicum Assistant — Basic Computing Laboratory")],
    "sasaero",
    ["The working environment in the System Division",
     "Technical documentation for the Moving Armor Target System project",
     "PT SAS Aerosishan's work environment"],
    override_content=SASAERO_CONTENT
)

OVERSIGHT_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/mpm-logo.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:160px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>Majelis Perwakilan Mahasiswa (Student Representative Council), HMTF Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About the Student Representative Council (MPM)</div>
  <p>The Student Representative Council (MPM) is the legislative body of Himpunan Mahasiswa Teknik Fisika (HMTF) at Telkom University, responsible for representing students, overseeing student organizations, evaluating organizational performance, and upholding transparent and accountable student governance.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/oversight-profile.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:3/4; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Rendy Ryan Renaldi — Leader of Commission II, MPM Unitel 2025/2026</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Leader of Commission II</div>
  <p>I served as Leader of Commission II under the Student Representative Council (MPM), leading a team of 2 members to oversee the governance and performance of HMTF.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Scope of Supervision</div>
  <p>Commission II's oversight covered the full structure of HMTF's organization:</p>
  <ul class="narrative-list">
    <li><b>5 departments</b></li>
    <li><b>3 bureaus</b></li>
    <li><b>2 semi-autonomous bodies (BSO)</b></li>
    <li><b>The core executive board</b></li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/work/oversight-council.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:3/4; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Full team of the Student Representative Council (MPM), School of Electrical Engineering, Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Periodic Evaluation & Strategic Recommendations</div>
  <p>I conducted periodic evaluations, ensured accountability, and provided strategic recommendations to improve organizational effectiveness and compliance across all supervised bodies.</p>
</div>
"""

work_detail(
    "work-oversight.html",
    "Leader of Commission II",
    "Student Representative Council (MPM), Telkom University",
    "Aug 2025 — Jan 2026", "Bandung, Indonesia",
    [],
    ["Leadership", "Governance", "Organizational Oversight"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Hardware Engineer — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-praktikum.html","Practicum Assistant — Instrumentation System Laboratory"),
     ("work-daskom.html","Practicum Assistant — Basic Computing Laboratory")],
    "oversight",
    ["Rapat komisi pengawasan MPM",
     "Evaluasi kinerja organisasi mahasiswa",
     "Kegiatan Engineering Physics Representative Council"],
    override_content=OVERSIGHT_CONTENT
)

PRAKTIKUM_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/lab-sismen-logo.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:140px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>Instrumentation System Laboratory (Lab Sismen) logo, Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About the Instrumentation System Laboratory</div>
  <p>The Instrumentation System Laboratory is a laboratory at Telkom University where basic electrical and electronics practicums are held for Engineering Physics students and related programs.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Practicum Division Assistant</div>
  <p>As a Practicum Division Assistant, I was responsible for preparing all the supporting material for practicum activities — from putting together <b>Modules</b>, <b>Journals</b>, and <b>Preliminary Assignments</b>, to writing the <b>Technical Report</b> for every practicum session.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/praktikum-tim.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>The full team of practicum assistants</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Practicum Scope: 190 Students</div>
  <p>I taught three practicums at once — <b>Electrical Circuits</b>, <b>Basic Electronics</b>, and <b>Digital Electronics</b> — mentoring a total of <b>190 students</b> over a 1 year 2 month contract (Jun 2024 – Jul 2025).</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/praktikum-kegiatan.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Documentation after a practicum session</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Training of Trainers (ToT)</div>
  <p>Before every practicum session started, I took part in Training of Trainers (ToT) — a rehearsal session for assistants to make sure the material was delivered to students consistently and to a high standard.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/praktikum-tot.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>A Training of Trainers (ToT) session before practicum begins</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Conclusion</div>
  <p>Over the course of my contract, I successfully helped complete the entire practicum series for the 2023 cohort — making sure all 190 students received consistent guidance, from the very first module and preliminary assignments, through the practicum journal, to writing the final technical report.</p>
</div>

<div class="thesis-note">
  <b>📄 Related certificates:</b> Asisten Praktikum Rangkaian Listrik & Asisten Praktikum Elektronika — see the Certificates page, under "Teaching & Laboratory".
  <div class="tn-links">
    <a href="certificates.html">📜 View Certificates →</a>
  </div>
</div>
"""

work_detail(
    "work-praktikum.html",
    "Practicum Assistant",
    "Instrumentation System Laboratory, Telkom University",
    "Jun 2024 — Jul 2025", "Bandung, Indonesia",
    [],
    ["Teaching", "Electronics", "Practicum Division"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Hardware Engineer — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-oversight.html","Leader of Commission II"),
     ("work-daskom.html","Practicum Assistant — Basic Computing Laboratory")],
    "praktikum",
    ["Documentation after a practicum session",
     "The full team of practicum assistants",
     "Training of Trainers (ToT) activity"],
    override_content=PRAKTIKUM_CONTENT
)

DASKOM_CONTENT = """
<div class="narrative-figure">
  <img src="assets/work/daskom-logo.png" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';" style="max-height:160px;">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:1/1; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Logo not added yet.</div>
  </div>
  <figcaption>Basic Computing Laboratory (Daskom) logo, Telkom University</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">About Basic Computing Laboratory</div>
  <p>Basic Computing Laboratory (Laboratorium Dasar Komputer) is a practicum laboratory under the School of Electrical Engineering, Telkom University. It provides basic algorithm and C programming practicums for students in Electrical Engineering, Engineering Physics, Telecommunication Engineering, and Biomedical Engineering.</p>
</div>

<div class="narrative-section">
  <div class="narrative-heading">My Role: Practicum Assistant</div>
  <p>As a Practicum Assistant, I worked alongside <b>92 fellow assistants</b> to teach and mentor a total of <b>240 students</b> in the algorithm and C programming practicum.</p>
  <p style="margin-top:16px;">The material I taught spanned 11 modules:</p>
  <ul class="narrative-list">
    <li>Module 1 — IDE Installation and Introduction to Algorithms</li>
    <li>Module 2 — Data Types and Algorithm Components</li>
    <li>Module 3 — Branching</li>
    <li>Module 4 — Looping</li>
    <li>Module 5 — Functions</li>
    <li>Module 6 — Arrays</li>
    <li>Module 7 — Sorting</li>
    <li>Module 8 — Searching</li>
    <li>Module 9 — Recursive Algorithms</li>
    <li>Module 10 — File Handling</li>
    <li>Module 11 — Basic Technical Report Writing</li>
  </ul>
</div>

<div class="narrative-figure">
  <img src="assets/work/daskom-praktikan.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:16/9; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>Group photo with students after completing all practicum modules</figcaption>
</div>

<div class="narrative-section">
  <div class="narrative-heading">Special Division: Rules & Discipline Committee</div>
  <p>Beyond teaching, I was also part of the <b>Rules & Discipline Committee</b> — responsible for enforcing rules during the practicum and leading each practicum shift to keep it orderly and up to lab standards.</p>
</div>

<div class="narrative-figure">
  <img src="assets/work/daskom-divisi.jpg" alt="" onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
  <div class="photo-placeholder" style="position:relative; aspect-ratio:4/3; display:none;">
    <div class="ph-icon">🖼️</div>
    <div class="ph-text">Photo not added yet.</div>
  </div>
  <figcaption>The Rules & Discipline Committee team</figcaption>
</div>

<div class="thesis-note">
  <b>🔗 Related project:</b> Kost-In — a C-based kos (boarding house) rental management program I built as part of the recruitment process to become an assistant here.
  <div class="tn-links">
    <a href="project-kostin.html">🏠 Kost-In: Room Rental Management System →</a>
  </div>
</div>
"""

work_detail(
    "work-daskom.html",
    "Practicum Assistant",
    "Basic Computing Laboratory, Telkom University",
    "Jun 2023 — Jun 2024", "Bandung, Indonesia",
    [],
    ["Teaching", "C Programming", "Algorithm"],
    [("work-mersi.html","Head of Assistant — MERSI"),
     ("work-puiptiot.html","Hardware Engineer — PUI-PT Intelligent Sensing-IoT"),
     ("work-sasaero.html","Intern — PT SAS Aerosishan"),
     ("work-oversight.html","Leader of Commission II"),
     ("work-praktikum.html","Practicum Assistant — Instrumentation System Laboratory")],
    "daskom",
    ["Group photo with students",
     "Rules & Discipline Committee team",
     "Daskom practicum activity"],
    override_content=DASKOM_CONTENT
)

# ==================== CERTIFICATES.HTML ====================
def cert_folder(icon_slug, label, items):
    import json as _json
    items_data = [{"images": images, "title": title, "issuer": issuer, "date": date} for title, issuer, date, images in items]
    items_attr = _json.dumps(items_data).replace('"', "&quot;")
    count = len(items)
    count_label = f"{count} CERTIFICATES" if count != 1 else "1 CERTIFICATE"
    return f"""<div class="cert-folder" data-folder-name="{label}" data-items='{items_attr}'>
  <img class="cert-folder-icon-img" src="assets/icons/{icon_slug}.svg" alt="">
  <div class="cert-folder-name">{label}</div>
  <div class="cert-folder-count">{count_label}</div>
</div>"""

CERT_CATEGORIES = [
    ("organisasi", "Organization", [
        ("Sertifikat Apresiasi — Anggota Divisi Mentor, OC/Panitia Kalibrasi 2024", "HMTF (Himpunan Mahasiswa Teknik Fisika), Universitas Telkom", "Jan 2025", ["org-1a", "org-1b"]),
        ("Staff Departemen Kaderisasi — Badan Pengurus Harian HMTF 2024/2025", "Himpunan Mahasiswa Teknik Fisika (HMTF), Universitas Telkom", "Jan 2025", ["org-2a", "org-2b"]),
    ]),
    ("lab", "Teaching & Laboratory", [
        ("Koordinator Asisten Sistem Pengukuran", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2026", ["teach-1a", "teach-1b"]),
        ("Asisten Praktikum Rangkaian Listrik", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2025", ["teach-2a", "teach-2b"]),
        ("Asisten Praktikum Elektronika", "Instrumentation System Laboratory, Universitas Telkom", "Jan 2025", ["teach-3a", "teach-3b"]),
        ("Asisten Praktikum Algoritma dan Pemrograman", "Laboratorium Dasar Komputer, Universitas Telkom", "Jan 2024", ["teach-4a", "teach-4b"]),
    ]),
    ("wirausaha", "Entrepreneurship", [
        ("UMKM Semut Corner — FKS Business Fair x Api Karya 2024", "BEM FKS, Universitas Telkom", "Nov 2024", ["wirausaha-1a", "wirausaha-1b"]),
    ]),
    ("bahasa", "Language", [
        ("EPrT (English Proficiency Test) — Skor 570", "Telkom University Language Center", "Jun 2026", ["bahasa-1a", "bahasa-1b"]),
    ]),
    ("pelatihan", "Training & Internship", [
        ("Digital Learning — Study Group", "MBC Lab, Telkom University", "May–Jun 2024", ["pelatihan-1"]),
        ("Certificate of Internship", "PT SAS Aero Sishan", "Jun–Aug 2025", ["pelatihan-2"]),
        ("Program MBKM — Intelligent Sensing-IoT", "PUI-PT Intelligent Sensing-IoT, Telkom University", "Sep–Dec 2025", ["pelatihan-3"]),
        ("Terminal / CMD untuk Development", "CODEPOLITAN", "Apr 2024", ["pelatihan-4"]),
    ]),
]

folders_html = "".join(cert_folder(icon_slug, label, items) for icon_slug, label, items in CERT_CATEGORIES)

certificates_body = f"""
<div class="page-header">
  <div class="section-eyebrow">AWARDS</div>
  <div class="section-title">Certificates</div>
  <p class="section-intro">Certificates are grouped by category. Click any folder to see what's inside.</p>
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
