const {chromium}=require('playwright');
(async()=>{const [,,mode,...ts]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/anim_built.html');await p.waitForTimeout(1500);await p.evaluate(()=>document.fonts.ready);
if(mode==='preview'){for(const t of ts){await p.evaluate(t=>render(+t),t);await p.screenshot({path:'prev_'+t+'.jpg',type:'jpeg',quality:80})}}
else{const fps=+ts[0],total=+ts[1];const n=Math.ceil(total*fps);for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);
 await p.screenshot({path:'frames/f'+String(i).padStart(5,'0')+'.jpg',type:'jpeg',quality:92});if(i%150==0)console.log(i,'/',n)}}
await b.close()})();
