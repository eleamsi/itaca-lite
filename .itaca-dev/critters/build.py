import json, os
D = os.path.dirname(os.path.abspath(__file__))
sp = json.load(open(os.path.join(D, 'sprites.json')))
css = open(os.path.join(D, 'critters.css')).read().replace('CAT_PNG', sp['cat']).replace('CAT_DARK_PNG', sp['catDark']).replace('BOAT_PNG', sp['boat']).replace('SEA_DARK_PNG', sp['seaDark']).replace('SEA_PNG', sp['sea']).replace('SLEIGH_PNG', sp['sleigh']).replace('SNOW_DARK_PNG', sp['snowDark']).replace('SNOW_PNG', sp['snow'])
js = open(os.path.join(D, 'critters.js')).read()
markup = ('<div class="critters" id="critters" aria-hidden="true" hidden>'
          '<div class="sea" hidden></div><div class="boat" hidden><div class="sprite"><i class="sheet"></i></div></div><div class="sea front" hidden></div>'
          '<div class="snow" hidden></div><div class="sleigh" hidden><div class="sprite"><i class="sheet"></i></div></div>'
          '<div class="cat" hidden><div class="cat-flip"><div class="sprite"><i class="sheet"></i></div></div></div></div>')
open(os.path.join(D, 'out.css'), 'w').write(css)
open(os.path.join(D, 'out.html'), 'w').write(markup)
preview = f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Anteprima gatto e barca</title>
<style>
:root {{ --paper:#fff; --muted:#5e6a77; --line-soft:#e6ebef; color-scheme: light; }}
:root[data-theme=dark] {{ --paper:#171f27; --muted:#9aa7b3; --line-soft:#26313b; color-scheme: dark; }}
body {{ margin:0; font:14px system-ui; background:var(--paper); color:var(--muted); height:100vh; display:flex; flex-direction:column; }}
.area {{ position:relative; flex:1; overflow:hidden; }}
.area p {{ max-width:600px; margin:40px auto; line-height:1.7 }}
.status {{ height:38px; border-top:1px solid var(--line-soft); display:flex; gap:10px; align-items:center; padding:0 10px }}
#log {{ font:12px ui-monospace; }}
{css}
</style></head><body>
<div class="area"><p>Anteprima. Lo stato del gatto è indicato in basso.</p>{markup}</div>
<div class="status"><button onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">Tema</button>
<button onclick="toggle('off')">Off</button><button onclick="toggle('cat')">Gatto</button><button onclick="toggle('boat')">Barca</button><button onclick="toggle('sleigh')">Slitta</button><button onclick="toggle(window.mode, window.size = window.size === 'double' ? 'normal' : 'double')">×2</button><span id="log"></span></div>
<script>{js.replace("return { start, stop,", "window.catGo = go; window.sail = sail; return { start, stop,")}
window.mode = new URLSearchParams(location.search).get('m') || 'boat';
const set = setupCritters(window.mode, new URLSearchParams(location.search).get('s') || 'normal');
const toggle = (m, s) => {{ window.mode = m; set(m, s || window.size || 'normal'); }};
setInterval(() => log.textContent = document.getElementById('critters').dataset.cat, 200);
</script></body></html>'''
open(os.path.join(D, 'preview.html'), 'w').write(preview)
print(len(css) + len(js) + len(markup))
