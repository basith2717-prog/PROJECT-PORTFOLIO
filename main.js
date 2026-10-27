/**
 * MOHAMMED BASITH — PORTFOLIO ENGINE & INTERACTIVE EXPERIENCES
 * Built with Japanese Editorial Zen aesthetics inspired by Kigo Studio.
 * Features:
 * - Magnetic Custom Cursor
 * - Falling Sakura Petals with Physics & Radial Click Bursts
 * - Kinetic Rotating Headline Slot Machine
 * - Cinema Developer Showcase with Web Audio Frequency Visualizer
 * - Postcard Airmail Project Gallery & Interactive Case Study Drawer
 * - Postcard Contact System with Realistic Hanko Ink Stamp Audio
 * - Bilingual Japanese / English Language Switcher
 */

// ==========================================================================
// 1. SOUND SYSTEM (WEB AUDIO API SYNTHETIC SOUNDS - ZERO EXTERNAL ASSETS)
// ==========================================================================
class SoundEngine {
  constructor() {
    this.enabled = true;
    this.ctx = null;
  }

  init() {
    if (!this.ctx && typeof window !== 'undefined') {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    return this.enabled;
  }

  playClick() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    if (this.ctx.state === 'suspended') this.ctx.resume();

    // Subtle gentle bamboo click sound
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(620, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(140, this.ctx.currentTime + 0.05);

    gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.05);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.05);
  }

  playZenChime() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    if (this.ctx.state === 'suspended') this.ctx.resume();

    // Japanese singing bowl / chime harmonic
    const freqs = [528, 792, 1056];
    freqs.forEach((f, idx) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(f, this.ctx.currentTime);

      const delay = idx * 0.03;
      gain.gain.setValueAtTime(0.06 / (idx + 1), this.ctx.currentTime + delay);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + delay + 1.2);

      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(this.ctx.currentTime + delay);
      osc.stop(this.ctx.currentTime + delay + 1.2);
    });
  }

  playStamp() {
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    if (this.ctx.state === 'suspended') this.ctx.resume();

    // Low resonant thud of a Japanese red ink hanko stamp hitting paper
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(180, this.ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(45, this.ctx.currentTime + 0.12);

    gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.14);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start();
    osc.stop(this.ctx.currentTime + 0.14);
  }
}

const sound = new SoundEngine();

// ==========================================================================
// 2. MAGNETIC CUSTOM CURSOR
// ==========================================================================
class MagneticCursor {
  constructor() {
    this.cursor = document.getElementById('customCursor');
    this.label = this.cursor?.querySelector('.cursor-label');
    this.pos = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
    this.mouse = { x: this.pos.x, y: this.pos.y };
    this.speed = 0.18;
    this.init();
  }

  init() {
    if (!this.cursor) return;

    window.addEventListener('mousemove', (e) => {
      this.mouse.x = e.clientX;
      this.mouse.y = e.clientY;
    });

    window.addEventListener('mousedown', () => {
      this.cursor.classList.add('is-active');
    });

    window.addEventListener('mouseup', () => {
      this.cursor.classList.remove('is-active');
    });

    this.attachHoverListeners();
    this.render();
  }

  attachHoverListeners() {
    const targets = document.querySelectorAll('[data-cursor], a, button, .work-postcard, .client-card, .faq-question');
    targets.forEach((target) => {
      target.addEventListener('mouseenter', () => {
        const customText = target.getAttribute('data-cursor') || '';
        this.cursor.classList.add('is-hovering');
        if (this.label) {
          this.label.textContent = customText;
        }
      });

      target.addEventListener('mouseleave', () => {
        this.cursor.classList.remove('is-hovering');
        if (this.label) {
          this.label.textContent = '';
        }
      });
    });
  }

  render() {
    this.pos.x += (this.mouse.x - this.pos.x) * this.speed;
    this.pos.y += (this.mouse.y - this.pos.y) * this.speed;

    if (this.cursor) {
      this.cursor.style.transform = `translate3d(${this.pos.x}px, ${this.pos.y}px, 0)`;
    }

    requestAnimationFrame(() => this.render());
  }
}

// ==========================================================================
// 3. FALLING SAKURA PETALS SIMULATION WITH BURST DYNAMICS
// ==========================================================================
class SakuraSimulation {
  constructor() {
    this.canvas = document.getElementById('sakuraCanvas') || document.getElementById('petalCanvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.petals = [];
    this.maxPetals = 20;
    this.width = window.innerWidth;
    this.height = window.innerHeight;

    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', () => this.resize());

    // Spawn initial petal cloud
    for (let i = 0; i < this.maxPetals; i++) {
      this.petals.push(this.createPetal(true));
    }

    // Radial burst on user click
    window.addEventListener('click', (e) => {
      this.burst(e.clientX, e.clientY);
    });

    this.animate();
  }

  resize() {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.canvas.width = this.width;
    this.canvas.height = this.height;
  }

  createPetal(randomY = false) {
    return {
      x: Math.random() * this.width,
      y: randomY ? Math.random() * this.height : -20 - Math.random() * 40,
      size: 6 + Math.random() * 8,
      speedY: 1.2 + Math.random() * 1.8,
      speedX: -0.6 + Math.random() * 1.2,
      rotation: Math.random() * 360,
      rotationSpeed: (Math.random() - 0.5) * 2.2,
      sway: Math.random() * 100,
      swaySpeed: 0.02 + Math.random() * 0.02,
      opacity: 0.35 + Math.random() * 0.3,
      tint: Math.random() > 0.4 ? '#db5b7f' : '#f8adbc'
    };
  }

  burst(originX, originY) {
    const burstCount = 14;
    for (let i = 0; i < burstCount; i++) {
      const angle = (Math.PI * 2 / burstCount) * i + (Math.random() - 0.5);
      const force = 4 + Math.random() * 6;
      this.petals.push({
        x: originX,
        y: originY,
        size: 12 + Math.random() * 12,
        speedY: Math.sin(angle) * force + 0.8,
        speedX: Math.cos(angle) * force,
        rotation: Math.random() * 360,
        rotationSpeed: (Math.random() - 0.5) * 4,
        sway: 0,
        swaySpeed: 0.03,
        opacity: 0.95,
        tint: '#d62828'
      });
    }

    if (this.petals.length > this.maxPetals + 25) {
      this.petals.splice(0, 14);
    }
  }

  drawPetal(p) {
    this.ctx.save();
    this.ctx.translate(p.x, p.y);
    this.ctx.rotate((p.rotation * Math.PI) / 180);
    this.ctx.globalAlpha = p.opacity;

    // Organic sakura petal curve
    this.ctx.beginPath();
    this.ctx.moveTo(0, -p.size * 0.5);
    this.ctx.bezierCurveTo(p.size * 0.5, -p.size * 0.3, p.size * 0.6, p.size * 0.4, 0, p.size * 0.6);
    this.ctx.bezierCurveTo(-p.size * 0.6, p.size * 0.4, -p.size * 0.5, -p.size * 0.3, 0, -p.size * 0.5);
    this.ctx.closePath();

    this.ctx.fillStyle = p.tint;
    this.ctx.fill();
    this.ctx.restore();
  }

  animate() {
    this.ctx.clearRect(0, 0, this.width, this.height);

    for (let i = 0; i < this.petals.length; i++) {
      const p = this.petals[i];
      p.sway += p.swaySpeed;
      p.x += p.speedX + Math.sin(p.sway) * 0.8;
      p.y += p.speedY;
      p.rotation += p.rotationSpeed;

      this.drawPetal(p);

      if (p.y > this.height + 30 || p.x < -30 || p.x > this.width + 30) {
        this.petals[i] = this.createPetal(false);
      }
    }

    requestAnimationFrame(() => this.animate());
  }
}

// ==========================================================================
// 4. KINETIC ROTATING HEADLINE
// ==========================================================================
class KineticHeadline {
  constructor() {
    this.container = document.getElementById('heroHeadline') || document.getElementById('heroTitle');
    this.subjectEl = document.getElementById('rotatingSubject') || document.getElementById('rotatingWord');
    this.accentEl = document.getElementById('rotatingAccent');

    this.words = [
      { subject: 'FULL-STACK', accent: 'scalable', jpSubject: 'フルスタック', jpAccent: 'スケーラブル' },
      { subject: 'AI SYSTEMS', accent: 'intelligent', jpSubject: 'AI システム', jpAccent: 'インテリジェント' },
      { subject: 'WEB APPS', accent: 'seamless', jpSubject: 'Webアプリ', jpAccent: 'シームレス' },
      { subject: 'PYTHON', accent: 'robust', jpSubject: 'Python', jpAccent: '堅牢' }
    ];

    this.currentIndex = 0;
    this.isPaused = false;
    this.init();
  }

  init() {
    if (!this.subjectEl || !this.accentEl) return;

    this.container?.addEventListener('mouseenter', () => { this.isPaused = true; });
    this.container?.addEventListener('mouseleave', () => { this.isPaused = false; });

    setInterval(() => {
      if (!this.isPaused) {
        this.next();
      }
    }, 3200);
  }

  next() {
    this.currentIndex = (this.currentIndex + 1) % this.words.length;
    const currentLang = document.documentElement.getAttribute('lang') || 'en';
    const pair = this.words[this.currentIndex];

    const nextSubject = currentLang === 'jp' ? pair.jpSubject : pair.subject;
    const nextAccent = currentLang === 'jp' ? pair.jpAccent : pair.accent;

    // Slide out
    this.subjectEl.classList.add('is-sliding-out');
    this.accentEl.classList.add('is-sliding-out');

    setTimeout(() => {
      this.subjectEl.textContent = nextSubject;
      this.accentEl.textContent = nextAccent;

      this.subjectEl.classList.remove('is-sliding-out');
      this.accentEl.classList.remove('is-sliding-out');

      this.subjectEl.classList.add('is-sliding-in');
      this.accentEl.classList.add('is-sliding-in');

      void this.subjectEl.offsetWidth;

      this.subjectEl.classList.remove('is-sliding-in');
      this.accentEl.classList.remove('is-sliding-in');
    }, 450);
  }

  updateLanguage(lang) {
    const pair = this.words[this.currentIndex];
    this.subjectEl.textContent = lang === 'jp' ? pair.jpSubject : pair.subject;
    this.accentEl.textContent = lang === 'jp' ? pair.jpAccent : pair.accent;
  }
}

// ==========================================================================
// 5. CINEMA SHOWREEL VIDEO PLAYER STAGE
// ==========================================================================
class CinemaShowreel {
  constructor() {
    this.modal = document.getElementById('reelModal');
    this.openBtn = document.getElementById('reelPlayButton');
    this.closeBtn = document.getElementById('closeReelModal');
    this.playPauseBtn = document.getElementById('cinemaPlayPauseBtn');
    this.playIcon = document.getElementById('cinemaPlayIcon');
    this.pauseIcon = document.getElementById('cinemaPauseIcon');
    this.timecode = document.getElementById('cinemaTimecode');
    this.progressFill = document.getElementById('cinemaProgress');
    this.visualizer = document.getElementById('cinemaVisualizer');
    this.canvas = document.getElementById('cinemaCanvas');

    this.isPlaying = true;
    this.currentTime = 14;
    this.duration = 74;

    this.init();
  }

  init() {
    // In-page reel player (kigo-style home-reel)
    const inPagePoster = document.getElementById('reelPoster');
    const inPageStage = document.getElementById('reelStage');
    const inPageClose = document.getElementById('reelClose');

    if (inPagePoster && inPageStage) {
      inPagePoster.addEventListener('click', () => {
        sound.playZenChime();
        inPageStage.classList.add('is-active');
        if (!inPageStage.querySelector('iframe')) {
          const iframe = document.createElement('iframe');
          iframe.src = 'https://www.youtube-nocookie.com/embed/dQw4w9WgXcQ?autoplay=1&mute=1&controls=0&loop=1';
          iframe.title = 'Portfolio Showcase Reel';
          iframe.style.width = '100%';
          iframe.style.height = '100%';
          iframe.style.border = 'none';
          iframe.setAttribute('allow', 'autoplay; encrypted-media');
          inPageStage.appendChild(iframe);
        }
      });

      inPageClose?.addEventListener('click', (e) => {
        e.stopPropagation();
        sound.playClick();
        inPageStage.classList.remove('is-active');
        const iframe = inPageStage.querySelector('iframe');
        if (iframe) iframe.remove();
      });
    }

    if (!this.modal) return;

    if (this.visualizer) {
      for (let i = 0; i < 36; i++) {
        const bar = document.createElement('div');
        bar.className = 'visualizer-bar';
        this.visualizer.appendChild(bar);
      }
    }

    this.openBtn?.addEventListener('click', () => {
      sound.playZenChime();
      this.open();
    });

    this.closeBtn?.addEventListener('click', () => {
      sound.playClick();
      this.close();
    });

    this.modal.querySelector('.reel-modal__backdrop')?.addEventListener('click', () => {
      this.close();
    });

    this.playPauseBtn?.addEventListener('click', () => {
      sound.playClick();
      this.togglePlay();
    });

    this.renderCinemaCanvas();

    setInterval(() => {
      if (this.modal.classList.contains('is-active') && this.isPlaying) {
        this.currentTime += 0.5;
        if (this.currentTime >= this.duration) this.currentTime = 0;
        this.updateTimeDisplay();
      }
    }, 500);
  }

  open() {
    this.modal.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.modal.classList.remove('is-active');
    document.body.style.overflow = '';
  }

  togglePlay() {
    this.isPlaying = !this.isPlaying;
    if (this.isPlaying) {
      this.playIcon.style.display = 'none';
      this.pauseIcon.style.display = 'block';
    } else {
      this.playIcon.style.display = 'block';
      this.pauseIcon.style.display = 'none';
    }
  }

  updateTimeDisplay() {
    const mins = Math.floor(this.currentTime / 60).toString().padStart(2, '0');
    const secs = Math.floor(this.currentTime % 60).toString().padStart(2, '0');
    if (this.timecode) {
      this.timecode.textContent = `${mins}:${secs} / 01:14`;
    }
    if (this.progressFill) {
      this.progressFill.style.width = `${(this.currentTime / this.duration) * 100}%`;
    }

    const bars = this.visualizer?.querySelectorAll('.visualizer-bar');
    bars?.forEach((b) => {
      const h = 10 + Math.random() * 90;
      b.style.height = `${h}%`;
    });
  }

  renderCinemaCanvas() {
    if (!this.canvas) return;
    const ctx = this.canvas.getContext('2d');
    let t = 0;

    const draw = () => {
      if (this.canvas.offsetWidth) {
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
      }

      const w = this.canvas.width;
      const h = this.canvas.height;

      ctx.fillStyle = '#0a0a0a';
      ctx.fillRect(0, 0, w, h);

      ctx.save();
      ctx.translate(w / 2, h / 2);

      for (let wave = 0; wave < 3; wave++) {
        ctx.beginPath();
        ctx.strokeStyle = wave === 0 ? 'rgba(219, 91, 127, 0.8)' : wave === 1 ? 'rgba(214, 40, 40, 0.6)' : 'rgba(255, 255, 255, 0.3)';
        ctx.lineWidth = 2;
        for (let x = -w / 2; x < w / 2; x += 10) {
          const y = Math.sin((x * 0.015) + (t * 0.05) + wave) * (40 + wave * 25);
          if (x === -w / 2) ctx.moveTo(x, y);
          else ctx.lineTo(x, y);
        }
        ctx.stroke();
      }

      ctx.font = '800 36px Kanit';
      ctx.textAlign = 'center';
      ctx.fillStyle = 'rgba(255, 255, 255, 0.9)';
      ctx.fillText('MOHAMMED BASITH • 2026', 0, -20);

      ctx.font = '600 15px Poppins';
      ctx.fillStyle = '#db5b7f';
      ctx.fillText('PYTHON • DJANGO • REACT • TYPESCRIPT • SQL • AI DISPATCH', 0, 20);

      ctx.restore();

      if (this.isPlaying) t++;
      requestAnimationFrame(draw);
    };
    draw();
  }
}

// ==========================================================================
// 6. CASE STUDY DRAWER DATABASE & MODAL (TAILORED FROM RESUME)
// ==========================================================================
const PROJECT_DATA = {
  civiccare: {
    title: 'CivicCare: AI-Powered Public Complaint System',
    client: 'Municipal Governance & Citizen Welfare',
    category: 'AI Integration & Real-Time Full-Stack Web Platform',
    metric: 'Real-Time Dispatch & Issue Resolution',
    accentColor: '#d62828',
    summary: 'An AI-powered public complaint registration and service dispatch web platform designed to streamline municipal grievance resolution and provide real-time issue tracking for citizens.',
    challenge: 'Civic complaints often suffer from bureaucratic bottlenecks, slow manual categorization, and zero visibility for the submitting citizens.',
    solution: 'Engineered an interactive React web interface featuring automated complaint categorization, priority routing, real-time status dispatch, and transparent administrative dashboards.',
    stack: ['JavaScript (ES6+)', 'React.js', 'AI Classification Pipelines', 'Real-Time Webhooks', 'CSS Grid & Flexbox']
  },
  city360: {
    title: 'CITY-360: Web-Based Service Provider Platform',
    client: 'Local Service Ecosystems & Providers',
    category: 'Python Backend & Structured SQL Database System',
    metric: 'Normalized Database & Secure Auth',
    accentColor: '#21464b',
    summary: 'A web-based service provider platform featuring structured backend solutions for managing service listings, booking schedules, and user interactions with strict data integrity.',
    challenge: 'Handling diverse service provider categories, dynamic availability schedules, and secure user data coordination without database bottlenecks.',
    solution: 'Designed database-driven functionalities using Python and Django with relational SQL/MySQL schemas, enforcing secure authentication, search filtering, and service booking workflows.',
    stack: ['Python', 'Django Framework', 'SQL / MySQL', 'RESTful API Views', 'Bootstrap / CSS3']
  },
  growy: {
    title: 'Growy: AI-Driven Language Immersion & Coach',
    client: 'Mobile Language Learners & Communication Practice',
    category: 'React Native & Mobile Full-Stack Architecture',
    metric: 'Conversational Immersion Flow',
    accentColor: '#94e669',
    summary: 'An interactive cross-platform mobile application focused on real-time conversational practice, speech immersion, and personalized feedback powered by full-stack AI integrations.',
    challenge: 'Creating a low-latency, engaging conversational immersion environment on mobile devices that keeps language learners motivated and tracks learning progress.',
    solution: 'Architected the React Native mobile codebase with TypeScript, integrating modern conversational prompts, speech evaluation feedback, and responsive state persistence.',
    stack: ['React Native', 'TypeScript', 'Conversational AI APIs', 'AsyncStorage', 'Modern Mobile UX']
  },
  basithlabs: {
    title: 'Basith Interactive Studio & Labs',
    client: 'Personal Creative Portfolio & Experiments',
    category: 'Creative Frontend & Web Audio Architecture',
    metric: '60 FPS Physics Simulation',
    accentColor: '#db5b7f',
    summary: 'An ultra-refined Japanese editorial digital portfolio combining brutalist typography, magnetic physics cursors, procedural sakura petal canvas animations, and Web Audio API synthesized feedback.',
    challenge: 'Delivering cutting-edge micro-interactions and audio-visual feedback with zero external sound asset dependencies and instant page load speeds.',
    solution: 'Crafted bespoke vanilla CSS and ES modules with Canvas 2D physics, procedural audio oscillators, and custom slot-machine kinetic typography.',
    stack: ['Vanilla CSS3', 'JavaScript ES6+', 'HTML5 Canvas', 'Web Audio API', 'Vite']
  },
  lccwork: {
    title: 'Python Engineering & Development Workflows',
    client: 'LCC Computer Education Internship',
    category: 'Backend Optimization & Software Architecture',
    metric: '2-Month Production Internship',
    accentColor: '#fcbf49',
    summary: 'Professional software development internship focused on engineering and optimizing Python backend workflows, clean modular architecture, and automated test suites.',
    challenge: 'Refactoring legacy scripts to meet modern modular standards while maintaining clean readability and test coverage.',
    solution: 'Engineered clean Python modules, assisted peers in standard adherence, and conducted systematic debugging and unit testing across application components.',
    stack: ['Python', 'Object-Oriented Programming (OOP)', 'Software Testing', 'Git & Linux', 'Clean Architecture']
  },
  analyticslab: {
    title: 'Data Analytics & GenAI Systems Lab',
    client: 'Google & TATA Industry Simulation',
    category: 'Data Analytics, SQL Aggregations & GenAI',
    metric: 'Google Certified Professional',
    accentColor: '#a13d27',
    summary: 'Data-driven analytical simulations including the Google Data Analytics Professional Certificate (Coursera), GenAI Powered Data Analytics (TATA), and Claude AI productivity workflows.',
    challenge: 'Transforming messy relational datasets into high-signal executive dashboards and generative AI insights.',
    solution: 'Applied SQL querying, data cleaning pipelines, exploratory data analysis (EDA), and automated prompt chains for data synthesis.',
    stack: ['SQL / MySQL', 'Google Data Analytics', 'GenAI Tools', 'Data Visualization', 'Claude AI']
  }
};

class CaseStudyDrawer {
  constructor() {
    this.drawer = document.getElementById('caseStudyDrawer');
    this.drawerBody = document.getElementById('caseDrawerBody');
    this.closeBtn = document.getElementById('closeCaseDrawer');
    this.cards = document.querySelectorAll('.work-postcard');

    this.init();
  }

  init() {
    if (!this.drawer) return;

    this.cards.forEach((card) => {
      card.addEventListener('click', () => {
        sound.playZenChime();
        const pKey = card.getAttribute('data-project');
        if (pKey && PROJECT_DATA[pKey]) {
          this.renderCase(PROJECT_DATA[pKey]);
          this.open();
        }
      });
    });

    this.closeBtn?.addEventListener('click', () => {
      sound.playClick();
      this.close();
    });

    this.drawer.querySelector('.case-drawer__backdrop')?.addEventListener('click', () => {
      this.close();
    });
  }

  open() {
    this.drawer.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.drawer.classList.remove('is-active');
    document.body.style.overflow = '';
  }

  renderCase(data) {
    if (!this.drawerBody) return;
    this.drawerBody.innerHTML = `
      <div class="case-header">
        <span class="section-tag" style="color:${data.accentColor};">${data.category}</span>
        <h2 style="font-family:var(--font-title); font-size:2.2rem; font-weight:800; text-transform:uppercase; margin-top:0.4rem; letter-spacing:-0.03em;">
          ${data.title}
        </h2>
        <span style="font-size:0.9rem; color:#888888;">Focus: ${data.client}</span>
      </div>

      <div class="case-hero-visual" style="background: radial-gradient(circle at center, ${data.accentColor}33, #111111 80%); border: 1px solid rgba(255,255,255,0.15);">
        <div style="font-family:var(--font-kanji); font-size:64px; color:${data.accentColor}; font-weight:700;">創</div>
      </div>

      <div class="case-metric-box">
        <div class="metric-card">
          <span class="metric-card__number">${data.metric}</span>
          <span class="metric-card__label">Project Highlight</span>
        </div>
        <div class="metric-card">
          <span class="metric-card__number">100%</span>
          <span class="metric-card__label">Clean Architecture &amp; OOP</span>
        </div>
      </div>

      <div style="margin-bottom: 2rem;">
        <h3 style="font-family:var(--font-title); font-size:1.2rem; font-weight:700; text-transform:uppercase; margin-bottom:0.6rem;">Overview</h3>
        <p style="color:#c0c0c0; line-height:1.7;">${data.summary}</p>
      </div>

      <div style="margin-bottom: 2rem;">
        <h3 style="font-family:var(--font-title); font-size:1.2rem; font-weight:700; text-transform:uppercase; margin-bottom:0.6rem;">The Challenge</h3>
        <p style="color:#c0c0c0; line-height:1.7;">${data.challenge}</p>
      </div>

      <div style="margin-bottom: 2rem;">
        <h3 style="font-family:var(--font-title); font-size:1.2rem; font-weight:700; text-transform:uppercase; margin-bottom:0.6rem;">Architectural Solution</h3>
        <p style="color:#c0c0c0; line-height:1.7;">${data.solution}</p>
      </div>

      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family:var(--font-title); font-size:1.2rem; font-weight:700; text-transform:uppercase; margin-bottom:0.8rem;">Technologies Applied</h3>
        <div class="case-tag-list">
          ${data.stack.map(st => `<span class="case-tag-item">${st}</span>`).join('')}
        </div>
      </div>

      <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:1.8rem; display:flex; justify-content:space-between; align-items:center;">
        <span style="font-size:0.85rem; color:#888888;">Interested in discussing this build?</span>
        <button id="caseDrawerCta" class="btn btn--primary" style="padding:0.6rem 1.4rem;">
          <span>Contact Mohammed</span>
          <span class="btn__stamp">押</span>
        </button>
      </div>
    `;

    document.getElementById('caseDrawerCta')?.addEventListener('click', () => {
      this.close();
      const postcard = document.getElementById('postcardModal');
      postcard?.classList.add('is-active');
      document.body.style.overflow = 'hidden';
    });
  }
}

// ==========================================================================
// 7. POSTCARD CONTACT MODAL & FORM ENGINE
// ==========================================================================
class PostcardContact {
  constructor() {
    this.modal = document.getElementById('postcardModal');
    this.closeBtn = document.getElementById('closePostcardModal');
    this.form = document.getElementById('postcardForm');
    this.success = document.getElementById('postcardSuccess');
    this.resetBtn = document.getElementById('resetPostcardBtn');
    this.chips = document.querySelectorAll('.chip');

    this.triggers = [
      document.getElementById('headerPostcardBtn'),
      document.getElementById('mobilePostcardBtn'),
      document.getElementById('heroPostcardTrigger'),
      document.getElementById('footerPostcardBtn')
    ];

    this.serviceButtons = document.querySelectorAll('.open-contact-with-service');
    this.init();
  }

  init() {
    if (!this.modal) return;

    this.triggers.forEach((btn) => {
      btn?.addEventListener('click', () => {
        sound.playStamp();
        this.open();
      });
    });

    this.serviceButtons.forEach((btn) => {
      btn?.addEventListener('click', () => {
        sound.playZenChime();
        const serviceName = btn.getAttribute('data-service-preset');
        if (serviceName) {
          this.chips.forEach(c => {
            if (c.getAttribute('data-value')?.toLowerCase().includes(serviceName.toLowerCase())) {
              c.classList.add('active');
            } else {
              c.classList.remove('active');
            }
          });
        }
        this.open();
      });
    });

    this.closeBtn?.addEventListener('click', () => {
      sound.playClick();
      this.close();
    });

    this.modal.querySelector('.postcard-modal__backdrop')?.addEventListener('click', () => {
      this.close();
    });

    this.chips.forEach((chip) => {
      chip.addEventListener('click', () => {
        sound.playClick();
        this.chips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
      });
    });

    this.form?.addEventListener('submit', (e) => {
      e.preventDefault();
      this.handleSubmit();
    });

    this.resetBtn?.addEventListener('click', () => {
      sound.playClick();
      this.resetForm();
    });
  }

  open() {
    this.modal.classList.add('is-active');
    document.body.style.overflow = 'hidden';
  }

  close() {
    this.modal.classList.remove('is-active');
    document.body.style.overflow = '';
  }

  handleSubmit() {
    const name = document.getElementById('senderName')?.value;
    const email = document.getElementById('senderEmail')?.value;
    const msg = document.getElementById('senderMessage')?.value;

    if (!name || !email || !msg) {
      alert('Please fill in your name, email, and inquiry details.');
      return;
    }

    sound.playStamp();
    this.form.style.display = 'none';
    this.success.style.display = 'block';
  }

  resetForm() {
    this.form.reset();
    this.form.style.display = 'block';
    this.success.style.display = 'none';
  }
}

// ==========================================================================
// 8. BILINGUAL TRANSLATION DICTIONARY (EN / JP)
// ==========================================================================
const TRANSLATIONS = {
  en: {
    navServices: 'Capabilities',
    navTools: 'Projects',
    navStack: 'Tech Stack',
    navAbout: 'Education & Exp',
    navHome: 'Home',
    navFaq: 'FAQ',
    ctaContact: 'HIRE ME',
    servicesEyebrow: 'CORE DISCIPLINES & ARCHITECTURES',
    service1Title: 'Frontend & React',
    service1Preview: 'Ultra-fluid React, TypeScript & Tailwind web interfaces engineered with micro-interactions and 60fps physics.',
    service2Title: 'Backend & Python',
    service2Preview: 'Structured Django, PHP, and SQL database engines designed for security, scalability, and high performance.',
    service3Title: 'Mobile & React Native',
    service3Preview: 'Cross-platform mobile apps like Growy, built with React Native, TypeScript, and interactive immersion flows.',
    service4Title: 'AI & Data Analytics',
    service4Preview: 'Intelligent systems like CivicCare, combining Google Certified analytics, LLM pipelines, and automated civic dispatch.',
    heroMakeYour: 'I ENGINEER',
    heroSubtitle: 'Detail-oriented Computer Applications postgraduate candidate & full-stack developer with a passion for web application design, AI integration, and robust database systems using Python, React, Django, and SQL.',
    heroCtaPrimary: 'Start a Conversation',
    heroCtaSecondary: 'Interactive Reel',
    haikuText: '"Code crafted with conviction, purpose, and mathematical precision."',
    reelCaption: 'Click to play audio-visual developer experience (01:14)',
    clientsTag: 'TECHNICAL PROFICIENCY',
    clientsTitle: 'Skills & Tooling',
    clientsSubtitle: 'Modern programming languages, web frameworks, database engines, and developer environments mastered across academics and projects.',
    clientsAndMore: 'LCC Intern • MCA \'27',
    servicesTag: 'DISCIPLINES',
    servicesHeadline: 'End-to-end software engineering, from concept to deployment.',
    service1Full: 'Building responsive, intuitive user interfaces with React, JavaScript, TypeScript, and modern CSS. Focused on component modularity, fluid animations, and strict semantic HTML.',
    service2Full: 'Engineering secure, relational backend systems with Python and Django. Designing normalized database schemas in SQL and MySQL with clean ORM mappings and authentication.',
    service3Full: 'Architecting cross-platform applications focused on interactive immersion, high responsiveness, and seamless offline-ready usability across iOS and Android ecosystems.',
    service4Full: 'Integrating intelligent machine learning and LLM pipelines into everyday workflows. Certified by Google in Data Analytics, TATA GenAI, and ATAL in Cybersecurity.',
    serviceInquire: 'Discuss Opportunity',
    workTag: 'PORTFOLIO CASE STUDIES',
    workTitle: 'Selected Projects',
    filterAll: 'All',
    filterAi: 'AI Systems',
    filterFullstack: 'Full-Stack',
    filterPython: 'Python / Django',
    filterMobile: 'Mobile',
    viewCaseStudy: 'Read Postcard',
    teamTag: 'ACADEMIC & INDUSTRY BACKGROUND',
    teamTitle: 'Education & Experience',
    teamSubtitle: 'Academic credentials, internship contributions, and industry certifications backing Mohammed Basith\'s software foundation.',
    role1: 'Postgraduate & Graduate',
    role2: 'Python Development Intern',
    bio2: 'Engineered modular Python scripts, automated backend workflows, assisted in testing and debugging components to enhance system performance.',
    role3: 'Industry Verified',
    faqTag: 'CANDIDATE CLARITY',
    faqTitle: 'Frequently asked questions',
    q1: 'What roles is Mohammed Basith currently seeking?',
    a1: 'I am actively seeking Full-Stack Developer, Python Backend Engineer, and Frontend React developer roles and high-impact internships. I am open to on-site opportunities in Kochi/Ernakulam/Kerala, Bangalore, or remote software engineering positions globally.',
    q2: 'What is your core technology stack and primary strength?',
    a2: 'My core foundation revolves around Python, Django, React, TypeScript, and SQL/MySQL databases. My key strength is architecting structured, maintainable solutions from database design to fluid, accessible user interfaces with clean modular code.',
    q3: 'How did you engineer the CivicCare AI Complaint System?',
    a3: 'CivicCare was designed to eliminate bottlenecks in municipal governance. I built real-time public complaint dispatch using React and modern JavaScript on the frontend, integrated automated categorization and tracking algorithms, and structured database records for instant transparency.',
    q4: 'What experience did you gain at LCC Computer Education?',
    a4: 'During my 2-month Python internship at LCC, I engineered backend scripts, collaborated on modular code structures adhering to clean architecture standards, and conducted rigorous debugging and unit testing to ensure system stability.',
    q5: 'Are you available for freelance projects or contract work?',
    a5: 'Yes. I frequently collaborate on custom web applications, responsive portfolio websites, RESTful backend APIs, and automation scripts. Reach out via the postcard modal below or email me directly at basith2717@gmail.com.',
    q6: 'What is your academic timeline and MCA status?',
    a6: 'I completed my BSc in Computer Science (2023–2025) at KMM College of Arts and Science and am currently pursuing my Master of Computer Applications (MCA) at MES AIMAT, MG University (Expected 2027), with flexibility for internships and technical roles.',
    footerHeading: 'Ready to build something extraordinary?',
    footerSub: 'Drop me a postcard. Whether you are hiring for an engineering role, seeking a freelance collaborator, or want to discuss a project, I reply promptly.',
    ctaOpenPostcard: 'Open Postcard',
    footerMotto: 'Full-Stack Craft • AI Systems • Ernakulam, Kerala',
    postcardHeader: 'Postcard to Mohammed Basith',
    postcardSubtitle: 'Select your inquiry, pen your vision or job opportunity, and press the red stamp to dispatch.',
    formServicesLabel: 'WHAT BRINGS YOU HERE?',
    formName: 'YOUR NAME',
    formEmail: 'EMAIL ADDRESS',
    formMessage: 'PROJECT DETAILS / ROLE SPECIFICATION',
    formSubmit: 'Stamp & Send Postcard',
    formReassurance: '🔒 Direct message to basith2717@gmail.com. Replied promptly.',
    successTitle: 'Postcard Received!',
    successMsg: 'Arigatou! Your postcard has landed on Mohammed Basith\'s desk. I will review your note and respond shortly.'
  },
  jp: {
    navServices: '専門領域',
    navTools: 'プロジェクト',
    navStack: '技術スタック',
    navAbout: '学歴・経歴',
    navHome: 'ホーム',
    navFaq: 'よくある質問',
    ctaContact: '採用・相談',
    servicesEyebrow: 'コア技術とアーキテクチャ',
    service1Title: 'フロントエンド & React',
    service1Preview: '60fpsの物理アニメーションと直感的なUIを備えたReact/TypeScriptウェブインターフェース。',
    service2Title: 'バックエンド & Python',
    service2Preview: '堅牢なDjango、PHP、SQLリレーショナルデータベースによるセキュアなシステム構築。',
    service3Title: 'モバイル & React Native',
    service3Preview: 'GrowyをはじめとするReact NativeとTypeScriptによる没入型クロスプラットフォームアプリ。',
    service4Title: 'AI & データ分析',
    service4Preview: 'CivicCareによるAIディスパッチ、Google認定データ分析、LLMパイプラインの統合。',
    heroMakeYour: 'エンジニアリング',
    heroSubtitle: 'エルナクラム（ケーララ州）を拠点とするMCA候補生＆フルスタック開発者。Python、React、Django、SQLを用いた堅牢なシステム開発とAI統合を追求。',
    heroCtaPrimary: 'コンタクト [押]',
    heroCtaSecondary: 'リール再生',
    haikuText: '"技術と情熱、限界を超えて — 魂を込めたコードと設計"',
    reelCaption: 'クリックしてショーケースを体験 (01:14)',
    clientsTag: '技術力・ツール',
    clientsTitle: '技術スタック',
    clientsSubtitle: '学術研究および実務プロジェクトで習得したプログラミング言語、フレームワーク、データベース。',
    clientsAndMore: 'LCC修了 • MCA \'27',
    servicesTag: '開発領域',
    servicesHeadline: 'コンセプト立案から本番展開まで、一貫したソフトウェア開発。',
    service1Full: 'React、JavaScript、TypeScriptを用いた高パフォーマンスUI開発。モジュール設計とアクセシビリティを徹底。',
    service2Full: 'PythonとDjangoを用いた安全なバックエンド開発。SQL/MySQLによる正規化データベース設計と認証基盤。',
    service3Full: 'iOS・Android両対応のReact Nativeアプリ設計。オフライン耐性とスムーズな操作感を実現。',
    service4Full: 'Google認定データ分析と生成AIを活用した業務効率化およびCivicCareディスパッチシステムの構築。',
    serviceInquire: '相談する',
    workTag: 'ポートフォリオ事例',
    workTitle: '代表的なプロジェクト',
    filterAll: 'すべて',
    filterAi: 'AIシステム',
    filterFullstack: 'フルスタック',
    filterPython: 'Python / Django',
    filterMobile: 'モバイル',
    viewCaseStudy: '詳細を見る',
    teamTag: '学歴と実務経験',
    teamTitle: '学歴・職歴',
    teamSubtitle: 'コンピュータサイエンスの確かな基礎と実務インターンシップ、業界認定資格。',
    role1: '大学院・学部',
    role2: 'Python開発インターン',
    bio2: 'LCC Computer EducationにてPythonスクリプト開発、モジュール設計、デバッグおよびテスト業務を担当。',
    role3: '公式認定資格',
    faqTag: '採用担当者様へ',
    faqTitle: 'よくあるご質問',
    q1: '現在募集しているポジションは？',
    a1: 'フルスタックエンジニア、Pythonバックエンドエンジニア、Reactフロントエンドエンジニアのポジションおよびインターンシップを積極的に歓迎しています。リモートワークまたはオンサイト勤務に対応可能です。',
    q2: 'コア技術と強みは何ですか？',
    a2: 'Python、Django、React、TypeScript、SQL/MySQLを核とし、クリーンなモジュール構造と保守性の高いアーキテクチャ設計を得意としています。',
    q3: 'CivicCare AIシステムの仕組みは？',
    a3: '自治体の苦情受付と対応を自動化するため、Reactによる直感的なフロントエンドとAIによる自動分類・リアルタイム追跡を構築しました。',
    q4: 'LCCでのインターン経験について',
    a4: '2ヶ月のPythonインターンシップで、実務スクリプトの最適化やチームでのコード設計、テスト自動化に貢献しました。',
    q5: 'フリーランス案件の相談は可能ですか？',
    a5: 'はい、ウェブアプリ開発やAPI構築、ポートフォリオ制作など柔軟に対応可能です。お気軽にポストカードよりご連絡ください。',
    q6: '学業のスケジュールと修了予定は？',
    a6: 'BSc Computer Scienceを修了（2023–2025）、現在MES AIMATにてMCA課程を専攻中（2027年修了見込み）です。',
    footerHeading: '共に優れた製品を創り上げましょう',
    footerSub: '採用のお声がけ、プロジェクトのご相談、技術的な意見交換など、いつでもお気軽にポストカードをお送りください。',
    ctaOpenPostcard: 'ポストカードを開く',
    footerMotto: 'フルスタック開発 • AIシステム • インド・ケーララ州',
    postcardHeader: 'ムハンマド・バシットへのメッセージ',
    postcardSubtitle: 'お問い合わせ項目を選択し、内容をご記入の上、赤い印鑑を押してください。',
    formServicesLabel: 'お問い合わせの種類',
    formName: 'お名前',
    formEmail: 'メールアドレス',
    formMessage: 'メッセージ / 募集要件',
    formSubmit: '印鑑を押して送信',
    formReassurance: '🔒 basith2717@gmail.com へ直接送信されます。',
    successTitle: 'ポストカードが送信されました！',
    successMsg: 'ありがとうございます！メッセージを受け取りました。確認後、速やかにご返信いたします。'
  }
};

class LanguageSwitcher {
  constructor(headlineCycler) {
    this.headlineCycler = headlineCycler;
    this.buttons = document.querySelectorAll('.lang-btn, .language__locale');
    this.currentLang = 'en';
    this.init();
  }

  init() {
    this.buttons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const lang = btn.getAttribute('data-lang') || 'en';
        if (lang !== this.currentLang) {
          sound.playClick();
          this.switchLanguage(lang);
        }
      });
    });
  }

  switchLanguage(lang) {
    this.currentLang = lang;
    document.documentElement.setAttribute('lang', lang);

    this.buttons.forEach((b) => {
      if (b.getAttribute('data-lang') === lang) {
        b.classList.add('active', 'current');
        b.setAttribute('aria-current', 'true');
      } else {
        b.classList.remove('active', 'current');
        b.removeAttribute('aria-current');
      }
    });

    const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;

    document.querySelectorAll('[data-i18n]').forEach((el) => {
      const key = el.getAttribute('data-i18n');
      if (key && dict[key]) {
        el.textContent = dict[key];
      }
    });

    this.headlineCycler?.updateLanguage(lang);
  }
}

// ==========================================================================
// 9. DANCER ALTERNATING POSE INTERVAL
// ==========================================================================
class DancerMascot {
  constructor() {
    this.pose1 = document.getElementById('dancerPose1') || document.querySelectorAll('.client-dancer__pose')[0];
    this.pose2 = document.getElementById('dancerPose2') || document.querySelectorAll('.client-dancer__pose')[1];
    this.stage = document.querySelector('.clients-dancer-stage, .client-dancer');
    this.isPose1 = true;
    this.init();
  }

  init() {
    if (!this.pose1 || !this.pose2) return;

    setInterval(() => {
      this.togglePose();
    }, 2800);

    this.stage?.addEventListener('mouseenter', () => {
      this.togglePose();
    });
  }

  togglePose() {
    this.isPose1 = !this.isPose1;
    if (this.pose1 && this.pose2) {
      this.pose1.style.opacity = this.isPose1 ? '1' : '0';
      this.pose2.style.opacity = this.isPose1 ? '0' : '1';
      this.pose1.classList.toggle('dancer-pose--active', this.isPose1);
      this.pose2.classList.toggle('dancer-pose--active', !this.isPose1);
    }
  }
}

// ==========================================================================
// 10. PROJECT CATEGORY FILTERS
// ==========================================================================
class ProjectFilters {
  constructor() {
    this.buttons = document.querySelectorAll('.filter-btn, .work-filter');
    this.cards = document.querySelectorAll('.work-postcard, .work-card');
    this.init();
  }

  init() {
    this.buttons.forEach((btn) => {
      btn.addEventListener('click', () => {
        sound.playClick();
        this.buttons.forEach(b => {
          b.classList.remove('active', 'work-filter--active');
          b.setAttribute('aria-selected', 'false');
        });
        btn.classList.add('active', 'work-filter--active');
        btn.setAttribute('aria-selected', 'true');

        const filter = btn.getAttribute('data-filter') || 'all';
        this.filter(filter);
      });
    });
  }

  filter(cat) {
    this.cards.forEach((card) => {
      const cardCats = (card.getAttribute('data-category') || card.getAttribute('data-tags') || '').split(/[\s,]+/);
      if (cat === 'all' || cardCats.includes(cat)) {
        card.style.display = 'block';
        card.style.opacity = '0';
        card.style.transform = 'translateY(12px)';
        setTimeout(() => {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
        }, 50);
      } else {
        card.style.display = 'none';
      }
    });
  }
}

// ==========================================================================
// 11. FAQ ACCORDION ENGINE
// ==========================================================================
class FaqAccordion {
  constructor() {
    this.items = document.querySelectorAll('.faq-item, .faq__item');
    this.init();
  }

  init() {
    this.items.forEach((item) => {
      const btn = item.querySelector('.faq-question, .faq__question');
      btn?.addEventListener('click', () => {
        sound.playClick();
        const isOpen = item.classList.contains('is-open');

        // Close other items
        this.items.forEach(other => {
          if (other !== item) {
            other.classList.remove('is-open');
            const otherBtn = other.querySelector('.faq-question, .faq__question');
            otherBtn?.setAttribute('aria-expanded', 'false');
          }
        });

        if (isOpen) {
          item.classList.remove('is-open');
          btn.setAttribute('aria-expanded', 'false');
        } else {
          item.classList.add('is-open');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
    });
  }
}

// ==========================================================================
// 12. SOUND TOGGLE BUTTON
// ==========================================================================
class SoundToggleUI {
  constructor() {
    this.btn = document.getElementById('soundToggle');
    this.iconOn = this.btn?.querySelector('.sound-icon--on');
    this.iconOff = this.btn?.querySelector('.sound-icon--off');
    this.init();
  }

  init() {
    if (!this.btn) return;
    this.btn.addEventListener('click', () => {
      const isEnabled = sound.toggle();
      if (isEnabled) {
        if (this.iconOn) this.iconOn.style.display = 'block';
        if (this.iconOff) this.iconOff.style.display = 'none';
        sound.playClick();
      } else {
        if (this.iconOn) this.iconOn.style.display = 'none';
        if (this.iconOff) this.iconOff.style.display = 'block';
      }
    });
  }
}

// ==========================================================================
// 13. MEGA MENU DROPDOWN & MOBILE DRAWER
// ==========================================================================
class NavigationMenu {
  constructor() {
    this.servicesTrigger = document.getElementById('servicesDropdownTrigger');
    this.megaMenu = document.getElementById('servicesMegaMenu') || document.getElementById('servicesMenu');
    this.closeMegaBtn = document.getElementById('closeMegaMenu');

    this.mobileToggle = document.getElementById('mobileMenuToggle');
    this.mobileDrawer = document.getElementById('mobileDrawer') || document.getElementById('mobileMenu');
    this.mobileLinks = document.querySelectorAll('.mobile-nav-link, .mobile-link');
    this.mobilePostcard = document.getElementById('mobilePostcardBtn') || document.querySelector('.mobile-cta');
    this.mobileServicesToggle = document.getElementById('mobileServicesToggle');

    this.init();
  }

  init() {
    // Mega Menu Trigger
    this.servicesTrigger?.addEventListener('click', (e) => {
      e.stopPropagation();
      sound.playClick();
      const isOpen = this.megaMenu?.classList.toggle('is-open');
      this.servicesTrigger?.classList.toggle('is-active', isOpen);
      const btn = this.servicesTrigger?.querySelector('button');
      btn?.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    this.closeMegaBtn?.addEventListener('click', () => {
      sound.playClick();
      this.megaMenu?.classList.remove('is-open');
      this.servicesTrigger?.classList.remove('is-active');
      this.servicesTrigger?.querySelector('button')?.setAttribute('aria-expanded', 'false');
    });

    document.addEventListener('click', (e) => {
      if (this.megaMenu && !this.megaMenu.contains(e.target) && !this.servicesTrigger?.contains(e.target)) {
        this.megaMenu.classList.remove('is-open');
        this.servicesTrigger?.classList.remove('is-active');
        this.servicesTrigger?.querySelector('button')?.setAttribute('aria-expanded', 'false');
      }
    });

    // Mobile Hamburger
    this.mobileToggle?.addEventListener('click', () => {
      sound.playClick();
      const isOpen = this.mobileDrawer?.classList.toggle('is-open');
      this.mobileToggle?.classList.toggle('is-active', isOpen);
      this.mobileToggle?.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    this.mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        this.mobileDrawer?.classList.remove('is-open');
        this.mobileToggle?.classList.remove('is-active');
        this.mobileToggle?.setAttribute('aria-expanded', 'false');
      });
    });

    this.mobilePostcard?.addEventListener('click', () => {
      this.mobileDrawer?.classList.remove('is-open');
      this.mobileToggle?.classList.remove('is-active');
      this.mobileToggle?.setAttribute('aria-expanded', 'false');
    });

    // Mobile services sub-menu toggle
    this.mobileServicesToggle?.addEventListener('click', (e) => {
      e.stopPropagation();
      sound.playClick();
      const panel = this.mobileServicesToggle?.nextElementSibling;
      const isOpen = panel?.classList.toggle('is-open');
      this.mobileServicesToggle?.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }
}

// ==========================================================================
// 14. VERTICAL SCROLLBAR INDICATOR
// ==========================================================================
class ScrollbarIndicator {
  constructor() {
    this.thumb = document.getElementById('scrollbar-thumb');
    this.container = document.getElementById('scrollbar-container');
    this.init();
  }

  init() {
    if (!this.thumb || !this.container) return;

    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (docHeight <= 0) return;
      const percent = (scrollTop / docHeight) * 100;
      this.thumb.style.height = `${Math.max(percent, 8)}%`;
    }, { passive: true });
  }
}

// ==========================================================================
// BOOTSTRAP APPLICATION
// ==========================================================================
document.addEventListener('DOMContentLoaded', () => {
  new MagneticCursor();
  new SakuraSimulation();
  const headline = new KineticHeadline();
  new CinemaShowreel();
  new CaseStudyDrawer();
  new PostcardContact();
  new LanguageSwitcher(headline);
  new DancerMascot();
  new ProjectFilters();
  new FaqAccordion();
  new SoundToggleUI();
  new NavigationMenu();
  new ScrollbarIndicator();
});
