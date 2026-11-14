// node render.js <id> still|video   -> out/<id>.png | out/<id>.mp4 (Einzelbilder in frames/<id>/)
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),{execFileSync}=require('child_process');
(async()=>{const [,,id,mode]=process.argv;const dir=__dirname,meta=JSON.parse(fs.readFileSync(dir+'/build/meta.json'));const END=meta[id];
fs.mkdirSync(dir+'/out',{recursive:true});const b=await chromium.launch();
const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:mode==='still'?2:1});
await p.goto('file://'+dir+'/build/'+id+'.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);
if(mode==='still'){await p.evaluate(t=>render(t),END+1.4);await p.screenshot({path:dir+'/out/'+id+'.png'})}
else{const fd=dir+'/frames/'+id;fs.mkdirSync(fd,{recursive:true});const fps=30,n=Math.round((END+2.5)*fps);
 for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:fd+'/f'+String(i).padStart(5,'0')+'.jpg',type:'jpeg',quality:93})}
 execFileSync('ffmpeg',['-hide_banner','-loglevel','error','-y','-framerate','30','-i',fd+'/f%05d.jpg','-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-shortest','-c:v','libx264','-preset','slow','-crf','18','-pix_fmt','yuv420p','-c:a','aac','-b:a','64k','-movflags','+faststart',dir+'/out/'+id+'.mp4']);
 fs.rmSync(fd,{recursive:true,force:true})}
await b.close();console.log('ok',id,mode)})();
