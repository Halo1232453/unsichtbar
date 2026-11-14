import json, wave, sys
from piper import PiperVoice
from piper.config import SynthesisConfig
v = PiperVoice.load(sys.argv[1])
segs = json.load(open(sys.argv[2]))
cfg = SynthesisConfig(length_scale=1.08, noise_scale=0.6, noise_w_scale=0.7)
out=[]
for i,s in enumerate(segs):
    fn=f"seg{i:02d}.wav"
    with wave.open(fn,"wb") as wf:
        v.synthesize_wav(s["say"], wf, syn_config=cfg)
    with wave.open(fn) as wf: d=wf.getnframes()/wf.getframerate()
    out.append({**s,"file":fn,"dur":round(d,3)})
json.dump(out,open("segs_out.json","w"),ensure_ascii=False,indent=1)
for o in out: print(o["id"], o["dur"])
