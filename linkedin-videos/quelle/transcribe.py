import sys, wave, json, numpy as np, sherpa_onnx
d=sys.argv[1]; wav=sys.argv[2]
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f"{d}/sherpa-onnx-whisper-small/small-encoder.int8.onnx",
  decoder=f"{d}/sherpa-onnx-whisper-small/small-decoder.int8.onnx",tokens=f"{d}/sherpa-onnx-whisper-small/small-tokens.txt",
  language="de",task="transcribe",num_threads=4)
cfg=sherpa_onnx.VadModelConfig(); cfg.silero_vad.model=f"{d}/silero_vad.onnx"; cfg.silero_vad.min_silence_duration=0.25
cfg.silero_vad.min_speech_duration=0.2; cfg.sample_rate=16000
vad=sherpa_onnx.VoiceActivityDetector(cfg,buffer_size_in_seconds=120)
with wave.open(wav) as w: x=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
ws=cfg.silero_vad.window_size; out=[]
def drain():
  while not vad.empty():
    s=vad.front; st=s.start/16000; samp=np.array(s.samples,dtype=np.float32)
    o=rec.create_stream(); o.accept_waveform(16000,samp); rec.decode_stream(o)
    out.append({"start":round(st,2),"end":round(st+len(samp)/16000,2),"text":o.result.text.strip()}); vad.pop()
for i in range(0,len(x),ws): vad.accept_waveform(x[i:i+ws]); drain()
vad.flush(); drain()
json.dump(out,open(f"{d}/segments.json","w"),ensure_ascii=False,indent=1)
for s in out: print(f'{s["start"]:6.2f}-{s["end"]:6.2f}  {s["text"]}')
