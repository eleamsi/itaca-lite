// Gatto, barchetta o slitta (in alternativa): macchina a stati con temporizzatori sospendibili.
// I fotogrammi li anima il CSS (steps); qui si scelgono solo stato, durata e spostamenti.
function createCritters(stage) {
  // misure in pixel dello schermo: un pixel d'arte vale --px (2 px, 4 px con la dimensione doppia)
  let PX = 2, CAT_W, BOAT_W, SLEIGH_W, CAT_SPEED, BOAT_SPEED, SLEIGH_SPEED;   // velocità in px al secondo
  function measure() {
    PX = parseFloat(getComputedStyle(stage).getPropertyValue('--px')) || 2;
    const k = PX / 2;
    [CAT_W, BOAT_W, SLEIGH_W] = [22 * PX, 30 * PX, 66 * PX];
    [CAT_SPEED, BOAT_SPEED, SLEIGH_SPEED] = [20 * k, 11 * k, 26 * k];
  }
  // riga nel foglio, fotogrammi, durata di un giro; once = una volta sola, back = al contrario
  const ANIMS = {
    walk:  { row: 0, n: 4, t: 560 },
    stand: { row: 1, n: 1, t: 1000 },
    idle:  { row: 2, n: 8, t: 2600 },
    lick:  { row: 3, n: 8, t: 1500 },
    sleep: { row: 4, n: 4, t: 3600 },
    sit:   { row: 5, n: 3, t: 420, once: true },
    unsit: { row: 5, n: 3, t: 420, once: true, back: true },
    lie:   { row: 6, n: 3, t: 800, once: true },
    wake:  { row: 6, n: 3, t: 700, once: true, back: true },
  };
  const cat = stage.querySelector('.cat'), flip = cat.querySelector('.cat-flip');
  const catSprite = cat.querySelector('.sprite'), catSheet = cat.querySelector('.sheet');
  const boat = stage.querySelector('.boat'), seas = stage.querySelectorAll('.sea');
  const sleigh = stage.querySelector('.sleigh'), snow = stage.querySelector('.snow');
  const rand = (a, b) => a + Math.random() * (b - a);
  const snap = x => Math.round(x / PX) * PX;
  const pick = weights => {
    const entries = Object.entries(weights).filter(([, w]) => w > 0);
    let r = Math.random() * entries.reduce((sum, [, w]) => sum + w, 0);
    for (const [key, w] of entries) if ((r -= w) < 0) return key;
    return entries[0][0];
  };

  // --- temporizzatori che si fermano quando la pagina non è visibile
  const timers = new Set();
  let running = false, paused = false, generation = 0;   // generation: ignora i callback di un avvio precedente
  const arm = t => { t.at = performance.now(); t.id = setTimeout(() => { timers.delete(t); t.fn(); }, t.left); };
  const after = (ms, fn) => { const t = { fn, left: ms }; timers.add(t); if (!paused) arm(t); };
  const moves = () => stage.getAnimations({ subtree: true });
  function pause() {
    if (paused) return;
    paused = true;
    for (const t of timers) { clearTimeout(t.id); t.left = Math.max(0, t.left - (performance.now() - t.at)); }
    moves().forEach(a => a.pause());
  }
  function resume() {
    if (!paused) return;
    paused = false;
    timers.forEach(arm);
    moves().forEach(a => a.play());
  }

  // spostamento orizzontale a scatti di un pixel d'arte (niente sfocature)
  function slide(el, from, to, speed, done) {
    const distance = Math.abs(to - from);
    el.style.transform = `translateX(${to}px)`;
    if (!distance) return after(0, done);
    const move = el.animate([{ transform: `translateX(${from}px)` }, { transform: `translateX(${to}px)` }],
      { duration: distance / speed * 1000, easing: `steps(${Math.max(1, Math.round(distance / PX))})` });
    if (paused) move.pause();
    const current = generation;
    move.onfinish = () => { if (current === generation) done(); };
  }

  // --- gatto
  const C = { x: 0, dir: 1, state: '', prev: '' };
  function play(name) {
    const a = ANIMS[name];
    catSprite.className = 'sprite' + (a.once ? ' once' : '') + (a.back ? ' back' : '');
    catSprite.style.cssText = `--row:${a.row};--n:${a.n};--t:${a.t}ms`;
    catSheet.classList.toggle('alt');           // cambia nome all'animazione → riparte dal primo fotogramma
    return a.t;
  }
  const face = dir => { C.dir = dir; flip.classList.toggle('left', dir < 0); };
  let lastWidth = 600;   // la striscia può essere nascosta (larghezza 0): vale l'ultima misura
  const width = () => (lastWidth = stage.clientWidth || lastWidth);

  function walkTo(target, next) {
    play('walk');
    const from = C.x;
    C.x = target;
    slide(cat, from, target, CAT_SPEED, () => go(next));
  }
  // si ferma, si gira, poi riparte: niente inversioni a metà passo
  function turnThen(dir, then) {
    if (dir === C.dir) return then();
    play('stand');
    after(rand(250, 600), () => { face(dir); after(rand(200, 450), then); });
  }

  const CAT = {
    stand() { play('stand'); after(rand(700, 2600), () => go(pick({ walk: 5, sit: C.prev === 'unsit' ? 0 : 3, exit: .6 }))); },
    walk() {
      const max = width() - CAT_W;
      let target = C.x;
      for (let i = 0; i < 6 && Math.abs(target - C.x) < 60; i++) {
        // di solito prosegue nella stessa direzione
        const ahead = Math.random() < .65;
        target = snap(ahead ? (C.dir > 0 ? rand(C.x, max) : rand(0, C.x)) : rand(0, max));
      }
      target = Math.min(Math.max(target, 0), Math.max(0, max));
      if (Math.abs(target - C.x) < 24) return go('sit');
      turnThen(Math.sign(target - C.x), () => walkTo(target, 'stand'));
    },
    sit() { after(play('sit') + 120, () => go('idle')); },
    idle() {
      play('idle');
      after(rand(2600, 8000), () => go(pick({ lick: 2, lie: C.prev === 'wake' ? 0 : 1.4, unsit: 2.2 })));
    },
    lick() { after(play('lick') * Math.ceil(rand(1, 3.99)), () => go('idle')); },
    lie() { after(play('lie') + 200, () => go('sleep')); },
    sleep() { play('sleep'); after(rand(12000, 40000), () => go('wake')); },
    wake() { after(play('wake') + 300, () => go('idle')); },
    unsit() { after(play('unsit') + 150, () => go('stand')); },
    exit() {
      const dir = Math.random() < .7 ? C.dir : -C.dir;
      turnThen(dir, () => walkTo(dir > 0 ? snap(width()) + PX : -CAT_W - PX, 'away'));
    },
    away() { cat.hidden = true; after(rand(6000, 30000), () => go('enter')); },
    enter() {
      const w = width(), fromLeft = Math.random() < .5;
      C.x = fromLeft ? -CAT_W : snap(w);
      cat.style.transform = `translateX(${C.x}px)`;
      face(fromLeft ? 1 : -1);
      cat.hidden = false;
      walkTo(snap(rand(w * .15, w * .85 - CAT_W)), 'stand');
    },
  };
  function go(state) {
    if (!running) return;
    C.prev = C.state;
    C.state = state;
    stage.dataset.cat = state;
    CAT[state]();
  }

  // --- barchetta e slitta: attraversano da sinistra a destra, spariscono, ritornano
  function cross(el, w, speed, first) {
    el.hidden = true;
    after(first ? rand(1000, 4000) : rand(8000, 35000), () => {
      el.hidden = false;
      slide(el, -w, snap(width()) + PX, speed, () => cross(el, w, speed, false));
    });
  }

  function stop() {
    running = paused = false;
    generation++;
    timers.forEach(t => clearTimeout(t.id));
    timers.clear();
    moves().forEach(a => { if (!(a instanceof CSSAnimation)) a.cancel(); });
    stage.hidden = true;
  }
  // mode: 'cat' | 'boat' | 'sleigh'; size: 'normal' | 'double'; still = movimento ridotto (tutto fermo)
  function start(mode, still = false, size = 'normal') {
    stop();
    stage.hidden = false;
    stage.classList.toggle('still', still);
    stage.dataset.mode = mode;
    stage.dataset.size = size;
    measure();
    running = !still;
    paused = document.hidden;
    const w = width(), isCat = mode === 'cat';
    cat.hidden = !isCat;
    boat.hidden = mode !== 'boat';
    seas.forEach(sea => { sea.hidden = mode !== 'boat'; });
    sleigh.hidden = mode !== 'sleigh';
    snow.hidden = mode !== 'sleigh';
    if (!isCat) {
      const [el, itemWidth, speed] = mode === 'boat' ? [boat, BOAT_W, BOAT_SPEED] : [sleigh, SLEIGH_W, SLEIGH_SPEED];
      if (still) el.style.transform = `translateX(${snap(w * .4)}px)`;   // ferma a metà
      else cross(el, itemWidth, speed, true);
      return;
    }
    C.x = snap(rand(w * .2, w * .8 - CAT_W));
    cat.style.transform = `translateX(${C.x}px)`;
    face(Math.random() < .5 ? 1 : -1);
    if (still) return void play('sleep');   // un gatto che dorme, fermo
    C.state = '';
    go(Math.random() < .5 ? 'idle' : 'stand');
  }
  document.addEventListener('visibilitychange', () => {
    if (!running) return;
    document.hidden ? pause() : resume();
  });
  return { start, stop, get state() { return C.state; } };
}

// accensione: mode 'off' | 'cat' | 'boat' | 'sleigh' (impostazione critters), size 'normal' | 'double'
// (crittersSize); rispetta prefers-reduced-motion
function setupCritters(mode, size = 'normal') {
  const stage = document.getElementById('critters');
  if (!stage) return () => {};
  const critters = createCritters(stage);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const apply = () => mode === 'off' ? critters.stop() : critters.start(mode, reduce.matches, size);
  reduce.addEventListener('change', apply);
  apply();
  return (value, nextSize = size) => { if (value !== mode || nextSize !== size) { mode = value; size = nextSize; apply(); } };
}
