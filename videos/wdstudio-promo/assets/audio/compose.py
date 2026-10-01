# Procedural score for the WD Studio promo: warm pad + sparse piano + sync hooks. Deterministic.
import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt
SR=48000; DUR=50.5; N=int(SR*DUR)
rng=np.random.default_rng(7)
L=np.zeros(N); R=np.zeros(N)
def hz(m): return 440*2**((m-69)/12)
def add(sig,t,pan=0.0,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig)); s=sig[:j-i]*g
    L[i:j]+=s*np.sqrt(0.5*(1-pan)); R[i:j]+=s*np.sqrt(0.5*(1+pan))
def piano(m,dur=4.0,vel=0.5):
    t=np.arange(int(SR*dur))/SR; f=hz(m); s=np.zeros_like(t)
    for k,a in [(1,1),(2,.45),(3,.22),(4,.12),(5,.06),(6,.03)]:
        s+=a*np.sin(2*np.pi*f*k*t*(1+0.0004*k*k))*np.exp(-t*(1.1+0.55*k))
    atk=np.minimum(1,t/0.006); return s*atk*vel
def pad(ms,dur,vel=0.12):
    t=np.arange(int(SR*dur))/SR; s=np.zeros_like(t)
    for m in ms:
        for d in (-0.06,0,0.07):
            f=hz(m)*2**(d/12); s+=np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*2*f*t)
    env=np.minimum(1,t/2.2)*np.minimum(1,(dur-t)/2.0)
    sos=butter(2,1800,'lp',fs=SR,output='sos'); return sosfilt(sos,s*env)*vel/len(ms)
def bell(m,vel=.35,dur=5):
    t=np.arange(int(SR*dur))/SR; f=hz(m)
    s=np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*2)+.25*np.sin(2*np.pi*f*5.4*t)*np.exp(-t*4)
    return s*np.exp(-t*0.9)*np.minimum(1,t/0.003)*vel
def swell(dur=1.6,vel=.18,lo=600,hi=5000):
    n=int(SR*dur); t=np.arange(n)/SR; w=rng.standard_normal(n)
    sos=butter(2,[lo,hi],'bp',fs=SR,output='sos'); w=sosfilt(sos,w)
    env=np.sin(np.pi*np.clip(t/dur,0,1))**2; return w*env*vel
def thud(vel=.5):
    t=np.arange(int(SR*1.2))/SR; f=55*np.exp(-t*3)+40
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*5)*vel
def tick(vel=.12,f=2600):
    t=np.arange(int(SR*.05))/SR; return np.sin(2*np.pi*f*t)*np.exp(-t*90)*vel
def click(vel=.18):
    t=np.arange(int(SR*.06))/SR; w=rng.standard_normal(len(t)); sos=butter(2,[1500,6000],'bp',fs=SR,output='sos')
    return sosfilt(sos,w)*np.exp(-t*120)*vel
# --- keynote-style UI sounds ---
def ui_click(vel=.5):
    t=np.arange(int(SR*.09))/SR
    body=np.sin(2*np.pi*1800*t)*np.exp(-t*160)+.6*np.sin(2*np.pi*3600*t)*np.exp(-t*260)
    nz=sosfilt(butter(2,[3000,9000],'bp',fs=SR,output='sos'),rng.standard_normal(len(t)))*np.exp(-t*400)*.5
    return (body+nz)*vel
def whoosh(dur=.7,vel=.35,rise=True):
    n=int(SR*dur); t=np.arange(n)/SR; w=rng.standard_normal(n); out=np.zeros(n); seg=1024
    for k in range(0,n,seg):
        u=k/n; fc=(400+5600*u) if rise else (6000-5600*u)
        out[k:k+seg]=sosfilt(butter(2,[fc*.6,fc*1.4],'bp',fs=SR,output='sos'),w[k:k+seg])
    env=np.sin(np.pi*np.clip(t/dur,0,1))**1.5; return out*env*vel
def pop(f=880,vel=.4):
    t=np.arange(int(SR*.35))/SR; fr=f*(1+.5*np.exp(-t*60))
    s=np.sin(2*np.pi*np.cumsum(fr)/SR)*np.exp(-t*14)+.4*np.sin(2*np.pi*f/2*t)*np.exp(-t*20)
    return s*np.minimum(1,t/.002)*vel
def dtick(f=3200,vel=.22):
    t=np.arange(int(SR*.03))/SR; return (np.sin(2*np.pi*f*t)+.3*np.sign(np.sin(2*np.pi*f*t)))*np.exp(-t*220)*vel
def shimmer(ms,vel=.3,dur=3):
    out=None
    for k,m in enumerate(ms):
        b=bell(m,vel,dur); b=np.pad(b,(int(SR*.035*k),0))[:int(SR*dur)]
        out=b if out is None else out+b
    return out
# --- harmonic bed (quiet) ---
chords=[(0,[53,57,60,64,67]),(10,[50,53,57,60,64]),(17,[46,50,53,57,60]),(22,[53,57,60,64,67]),(31,[46,50,53,57,62]),(38,[53,57,60,64,69]),(47,[53,60,65,69,72])]
for i,(t0,ms) in enumerate(chords):
    t1=chords[i+1][0]+1.5 if i+1<len(chords) else DUR
    add(pad(ms,t1-t0+.5,.09),t0,0,1.0)
for t,m,v in [(1.2,72,.2),(6.6,62,.2),(17.6,72,.18),(18.8,76,.2),(38.3,69,.18),(39.5,72,.2),(43.6,77,.18)]:
    add(piano(m,5,v),t,pan=(m-70)/30)
# --- transitions: whooshes on every seam ---
for t in (9.75,16.75,21.75,30.75,37.75,42.75,46.75): add(whoosh(.7,.30),t)
# --- reveals ---
add(whoosh(1.0,.18),0.15); add(pop(1320,.28),1.3)          # hairline, line
add(pop(660,.42),6.6); add(thud(.35),6.6)                   # bold line
add(pop(1100,.3),10.05)                                     # label
for k in range(16):
    u=(k+1)/16; add(dtick(2600+60*k,.16+.08*u),10.6+2.2*(1-(1-u)**0.5))
add(shimmer([72,76,79],.22),12.8)                           # 16% lands
for k,t in enumerate((13.0,13.6,14.2)): add(pop(1200+k*120,.2),t)
add(pop(1320,.28),17.5); add(pop(880,.36),18.7); add(shimmer([76,79,84],.16),18.75)
add(whoosh(.5,.18),22.0)                                    # card rises
add(ui_click(.5),23.8); add(ui_click(.35),24.05)            # pick dates
for t in (24.0,25.8,27.8): add(pop(1250,.22),t)
add(ui_click(.45),27.4)                                     # extras step
add(whoosh(.5,.15),31.0); add(ui_click(.3),33.0)            # highlight
for k in range(14): add(dtick(3000+70*k,.14+.08*(k+1)/14),34.4+1.8*(1-(1-(k+1)/14)**0.5))
add(shimmer([69,76,81],.3),36.2)                            # $530 USD
add(pop(1320,.26),38.2); add(pop(660,.4),39.4)             # rules
add(whoosh(.8,.16),43.1); add(pop(1100,.22),43.6)           # identity
add(shimmer([65,72,77,81],.3,4),47.0); add(thud(.3),47.0)   # logo
# --- reverb, master ---
ir_t=np.arange(int(SR*3.2))/SR
ir=rng.standard_normal((2,len(ir_t)))*np.exp(-ir_t*2.2); ir[:,0]=0
wetL=fftconvolve(L,ir[0])[:N]; wetR=fftconvolve(R,ir[1])[:N]
mixL=L+wetL*0.012; mixR=R+wetR*0.012
fade=np.ones(N); fi=int(SR*.3); fo=int(SR*2)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
st=np.stack([mixL*fade,mixR*fade],1)
st=np.tanh(st/np.max(np.abs(st))*1.2)*0.85
wavfile.write('score.wav',SR,(st*32767).astype(np.int16))
print('wrote score.wav')
