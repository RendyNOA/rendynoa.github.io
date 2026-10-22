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
            '<img src="assets/certificates/' + firstImg + '.jpg" alt="" onerror="this.style.display=\'none\'; this.nextElementSibling.style.display=\'flex\';">' +
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
