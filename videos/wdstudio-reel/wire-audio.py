# Re-run after assemble-index: mounts the locally composed score (assets/audio/score.m4a) on the root.
p='index.html';s=open(p).read()
if 'id="score"' not in s:
    s=s.replace('data-height="1920"\n    >','data-height="1920"\n    >\n      <audio id="score" src="assets/audio/score.m4a" data-start="0" data-duration="50.5" data-track-index="11" data-volume="1"></audio>',1)
open(p,'w').write(s); print('score' in s)
