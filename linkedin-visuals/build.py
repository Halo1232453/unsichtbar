# Baut aus engine.html + scenes.py je Beitrag eine HTML-Datei (build/<id>.html).
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from scenes import SCENES
import scenes_kw46  # noqa: F401  (registriert weitere Motive)
import scenes_workspace  # noqa: F401
import scenes_workspace_en  # noqa: F401
eng = open(os.path.join(here, "engine.html")).read()
os.makedirs(os.path.join(here, "build"), exist_ok=True)
meta = {}
for pid, s in SCENES.items():
    h = (eng.replace("__THEME__", s["theme"]).replace("__GRID__", '<div class="grid"></div>' if s["grid"] else "")
            .replace("__BODY__", s["body"]).replace("__END__", str(s["end"])).replace("__SCENE__", s["scene"]))
    open(os.path.join(here, "build", pid + ".html"), "w").write(h.replace('src="logo.png"', 'src="../logo.png"'))
    meta[pid] = s["end"]
json.dump(meta, open(os.path.join(here, "build", "meta.json"), "w"))
print(meta)
