import os
D='/home/user/miel.ai/videos/wdstudio-promo/compositions/frames'
FONT='assets/fonts/captured-UcC73FwrK3iLTeHuS_nVMrMxCp50SjIa1ZL7W0Q5nw.woff2'
def frame(fid,dur,css,html,js):
    bg='#FFFFFF' if fid=='09-logo' else '#FBFAF8'
    p='f'+fid.replace('-','')
    return f'''<template>
<div id="root" data-composition-id="{fid}" data-start="0" data-duration="{dur}" data-width="1920" data-height="1080">
<style>
@font-face{{font-family:'Inter';font-style:normal;font-weight:100 900;src:url("{FONT}") format('woff2');}}
#root{{position:relative;width:1920px;height:1080px;overflow:hidden;font-family:'Inter',sans-serif;color:#141412}}
.{p}-bg{{position:absolute;inset:0;background:{bg}}}
.{p}-wm{{position:absolute;left:64px;top:52px;font-size:13px;letter-spacing:5px;color:#75736E;font-weight:500}}
.{p}-lab{{font-size:15px;letter-spacing:5px;text-transform:uppercase;color:#8A7040;font-weight:500}}
.{p}-hair{{height:1px;background:#B69455;transform-origin:left center}}
.{p}-l{{font-weight:200}} .{p}-b{{font-weight:600}}
{css}
</style>
<div id="{p}-ground" class="clip {p}-bg" data-start="0" data-duration="{dur}" data-track-index="0"></div>
<div id="{p}-content" class="clip" data-start="0" data-duration="{dur}" data-track-index="1" style="position:absolute;inset:0">
{html}
</div>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
(function(){{
window.__timelines=window.__timelines||{{}};
const tl=gsap.timeline({{paused:true}});
{js}
window.__timelines["{fid}"]=tl;
}})();
</script>
</div>
</template>
'''
F={}
# 01
F['01-open']=(5,'''
#f01-wrap{position:absolute;left:230px;top:470px}
#f01-hair{width:115px}
#f01-l1{font-size:88px;letter-spacing:-2px;margin-top:40px;font-weight:200}
''','''<div class="f01open-wm">WD STUDIO</div>
<div id="f01-wrap"><div id="f01-hair" class="f01open-hair"></div><div id="f01-l1">A guest finds your house.</div></div>''','''
tl.fromTo("#f01-hair",{scaleX:0},{scaleX:1,duration:1.2,ease:"power2.inOut"},0.2);
tl.fromTo("#f01-l1",{opacity:0,y:16},{opacity:1,y:0,duration:1.4,ease:"power3.out"},1.2);
tl.fromTo("#f01-wrap",{y:0},{y:-8,duration:5,ease:"none"},0);
tl.fromTo(".f01open-wm",{opacity:0},{opacity:1,duration:1.5,ease:"power1.out"},0);
''')
F['02-platform']=(5,'''
#f02-wrap{position:absolute;left:230px;top:462px}
#f02-hair{width:115px}
#f02-l1{font-size:88px;letter-spacing:-2px;margin-top:40px;font-weight:200}
#f02-l2{font-size:88px;letter-spacing:-2px;margin-top:8px;font-weight:600}
''','''<div class="f02platform-wm">WD STUDIO</div>
<div id="f02-wrap"><div id="f02-hair" class="f02platform-hair"></div><div id="f02-l1">A guest finds your house.</div><div id="f02-l2">Then pays a platform to book it.</div></div>''','''
tl.fromTo("#f02-wrap",{y:0},{y:-60,duration:1.4,ease:"power2.inOut"},0.5);
tl.fromTo("#f02-l1",{color:"#141412"},{color:"#75736E",duration:1.0,ease:"power1.inOut"},0.6);
tl.fromTo("#f02-l2",{opacity:0,y:20},{opacity:1,y:0,duration:1.2,ease:"power3.out"},1.6);
''')
F['03-fee']=(7,'''
#f03-left{position:absolute;left:230px;top:300px}
#f03-num{font-size:320px;line-height:1.2;font-weight:200;letter-spacing:-14px;margin-top:20px}
#f03-of{font-size:44px;color:#75736E;font-weight:200}
#f03-right{position:absolute;left:1110px;top:520px;width:560px;font-size:30px;line-height:1.7;color:#4F4C47;font-weight:300}
#f03-right b{color:#141412;font-weight:600}
#f03-foot{position:absolute;left:230px;top:880px;font-size:16px;color:#75736E;letter-spacing:.5px}
''','''<div class="f03fee-wm">WD STUDIO</div>
<div id="f03-left"><div class="f03fee-lab" id="f03-lab">The platform fee</div><div id="f03-num"><span id="f03-n">0</span>%<sup style="font-size:60px;vertical-align:top;position:relative;top:40px;color:#8A7040">*</sup></div><div id="f03-of">of every booking.</div></div>
<div id="f03-right"><div id="f03-r1">On 50,000 USD a year —</div><div id="f03-r2"><b>8,000 USD.</b></div><div id="f03-r3">Every year.</div></div>
<div id="f03-foot">* Platform fees vary by country.</div>''','''
const c={v:0};const el=document.getElementById("f03-n");
tl.fromTo("#f03-lab",{opacity:0},{opacity:1,duration:0.8,ease:"power1.out"},0);
tl.fromTo("#f03-num",{opacity:0,scale:0.98,transformOrigin:"left bottom"},{opacity:1,scale:1,duration:1.2,ease:"power2.out"},0.4);
tl.fromTo(c,{v:0},{v:16,duration:2.2,ease:"power2.out",onUpdate:()=>{el.textContent=Math.round(c.v)}},0.6);
tl.fromTo("#f03-of",{opacity:0,y:10},{opacity:1,y:0,duration:1,ease:"power2.out"},2.2);
["#f03-r1","#f03-r2","#f03-r3"].forEach((s,i)=>tl.fromTo(s,{opacity:0,y:12},{opacity:1,y:0,duration:0.9,ease:"power2.out"},3+i*0.6));
tl.fromTo("#f03-foot",{opacity:0},{opacity:1,duration:1,ease:"power1.out"},5);
''')
F['04-direct']=(5,'''
#f04-wrap{position:absolute;left:230px;top:330px}
.f04-big{font-size:118px;line-height:1.05;letter-spacing:-3px}
#f04-sub{font-size:30px;color:#4F4C47;margin-top:40px;font-weight:300}
''','''<div class="f04direct-wm">WD STUDIO</div>
<div id="f04-wrap"><div class="f04direct-lab" id="f04-lab">Direct booking</div>
<div class="f04-big f04direct-l" id="f04-a" style="margin-top:30px">Your guest books</div>
<div class="f04-big f04direct-b" id="f04-b">on your site.</div>
<div id="f04-sub">No platform in between. No commission per reservation.</div></div>''','''
tl.fromTo("#f04-lab",{opacity:0},{opacity:1,duration:0.8},0);
tl.fromTo("#f04-a",{opacity:0,y:20},{opacity:1,y:0,duration:1.3,ease:"power3.out"},0.5);
tl.fromTo("#f04-b",{opacity:0,y:20},{opacity:1,y:0,duration:1.3,ease:"power3.out"},1.7);
tl.fromTo("#f04-sub",{opacity:0},{opacity:1,duration:1.2,ease:"power1.out"},3.0);
tl.fromTo("#f04-wrap",{y:0},{y:-6,duration:5,ease:"none"},0);
''')
F['05-booking']=(9,'''
#f05-card{position:absolute;left:170px;top:168px;width:840px;height:744px;background:#fff;box-shadow:0 40px 100px rgba(20,20,18,.09);overflow:hidden}
#f05-card img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}
#f05-side{position:absolute;left:1150px;top:380px;font-size:44px;line-height:1.9}
''','''<div class="f05booking-wm">WD STUDIO</div>
<div id="f05-card"><img id="f05-i1" src="assets/ui-calendar-empty.png"><img id="f05-i2" src="assets/ui-calendar-selected.png"><img id="f05-i3" src="assets/ui-extras.png"></div>
<div id="f05-side"><div class="f05booking-lab" id="f05-lab" style="line-height:1;margin-bottom:24px">The system</div>
<div class="f05booking-l" id="f05-s1">Live availability.</div><div class="f05booking-l" id="f05-s2">Your rates, your seasons.</div><div class="f05booking-b" id="f05-s3">Extras you define.</div></div>''','''
tl.fromTo("#f05-card",{opacity:0,y:40},{opacity:1,y:0,duration:1.4,ease:"power3.out"},0);
tl.fromTo("#f05-card",{scale:1},{scale:1.03,duration:9,ease:"none",immediateRender:false},0);
tl.fromTo("#f05-i2",{opacity:0},{opacity:1,duration:1.0,ease:"power1.inOut"},1.8);
tl.fromTo("#f05-i3",{opacity:0},{opacity:1,duration:1.2,ease:"power1.inOut"},5.4);
tl.fromTo("#f05-lab",{opacity:0},{opacity:1,duration:0.8},0.8);
tl.fromTo("#f05-s1",{opacity:0,y:14},{opacity:1,y:0,duration:1,ease:"power2.out"},2.0);
tl.fromTo("#f05-s2",{opacity:0,y:14},{opacity:1,y:0,duration:1,ease:"power2.out"},3.8);
tl.fromTo("#f05-s3",{opacity:0,y:14},{opacity:1,y:0,duration:1,ease:"power2.out"},5.8);
''')
F['06-kept']=(7,'''
#f06-card{position:absolute;left:170px;top:296px;width:820px;background:#fff;box-shadow:0 40px 100px rgba(20,20,18,.09);overflow:hidden}
#f06-card img{display:block;width:100%}
#f06-glow{position:absolute;left:0;right:0;bottom:0;height:19%;box-shadow:inset 0 0 0 1px rgba(45,95,86,.3);background:rgba(45,95,86,.04)}
#f06-right{position:absolute;left:1140px;top:340px}
#f06-num{font-size:200px;line-height:1;color:#2D5F56;font-weight:200;letter-spacing:-8px;margin-top:16px}
#f06-usd{font-size:56px;letter-spacing:2px;font-weight:300;margin-left:8px}
#f06-hair{width:115px;margin:36px 0 28px}
#f06-cap{font-size:38px;color:#4F4C47;font-weight:200}
''','''<div class="f06kept-wm">WD STUDIO</div>
<div id="f06-card"><img src="assets/ui-summary.png"><div id="f06-glow"></div></div>
<div id="f06-right"><div class="f06kept-lab" id="f06-lab">Booked direct</div><div id="f06-num">$<span id="f06-n">0</span><span id="f06-usd"> USD</span></div><div class="f06kept-hair" id="f06-hair"></div><div id="f06-cap">kept, on a single stay.</div></div>''','''
const c={v:0};const el=document.getElementById("f06-n");
tl.fromTo("#f06-card",{opacity:0,y:24},{opacity:1,y:0,duration:1.4,ease:"power3.out"},0);
tl.fromTo("#f06-glow",{opacity:0},{opacity:1,duration:1.2,ease:"power1.inOut"},2.0);
tl.fromTo("#f06-lab",{opacity:0},{opacity:1,duration:0.8},3.2);
tl.fromTo("#f06-num",{opacity:0},{opacity:1,duration:0.6},3.4);
tl.fromTo(c,{v:0},{v:530,duration:1.8,ease:"power2.out",onUpdate:()=>{el.textContent=Math.round(c.v)}},3.4);
tl.fromTo("#f06-hair",{scaleX:0},{scaleX:1,duration:1,ease:"power2.inOut"},5.0);
tl.fromTo("#f06-cap",{opacity:0,y:10},{opacity:1,y:0,duration:1,ease:"power2.out"},5.4);
''')
F['07-rules']=(5,'''
#f07-wrap{position:absolute;left:0;right:0;top:410px;text-align:center}
.f07-big{font-size:110px;letter-spacing:-3px;line-height:1.12}
''','''<div id="f07-wrap"><div class="f07-big f07rules-l" id="f07-a">Your house. Your rules.</div><div class="f07-big f07rules-b" id="f07-b">No platform.</div></div>''','''
tl.fromTo("#f07-a",{opacity:0,y:18},{opacity:1,y:0,duration:1.3,ease:"power3.out"},0.2);
tl.fromTo("#f07-b",{opacity:0,y:18},{opacity:1,y:0,duration:1.2,ease:"power3.out"},1.4);
tl.fromTo("#f07-wrap",{y:0},{y:-6,duration:5,ease:"none",immediateRender:false},0);
''')
F['08-identity']=(4,'''
#f08-wrap{position:absolute;left:0;right:0;top:420px;text-align:center}
#f08-hair{width:115px;margin:0 auto 52px;transform-origin:center}
#f08-desc{font-size:52px;font-weight:200;letter-spacing:-1px;line-height:1.25}
#f08-url{margin-top:52px;font-size:20px}
''','''<div id="f08-wrap"><div class="f08identity-hair" id="f08-hair"></div><div id="f08-desc">Digital identity for the world's<br>most beautiful properties.</div><div class="f08identity-lab" id="f08-url">wdstudio.agency</div></div>''','''
tl.fromTo("#f08-hair",{scaleX:0},{scaleX:1,duration:0.9,ease:"power2.inOut"},0.1);
tl.fromTo("#f08-desc",{opacity:0,y:16},{opacity:1,y:0,duration:1.2,ease:"power3.out"},0.5);
tl.fromTo("#f08-url",{opacity:0},{opacity:1,duration:0.9,ease:"power1.out"},1.7);
''')
F['09-logo']=(3.5,'''
#f09-end{position:absolute;left:0;top:0;width:1920px;height:1080px}
''','''<video id="f09-video" data-frame-video="approved" src="assets/logo-anim.mp4" muted playsinline data-start="0" data-duration="1.23" data-track-index="3" data-frame-video-x="0" data-frame-video-y="0" data-frame-video-width="1920" data-frame-video-height="1080" data-frame-video-fit="cover"></video>
<img id="f09-end" class="clip" src="assets/logo-end.png" data-start="1.2" data-duration="2.3" data-track-index="2" alt="WD Studio">''','''
tl.set("#f09-end",{opacity:1},0);
''')
for fid,(dur,css,html,js) in F.items():
    open(os.path.join(D,fid+'.html'),'w').write(frame(fid,dur,css,html,js))
print('ok',len(F))
