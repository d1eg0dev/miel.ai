# Procedural score for the WD Studio promo: warm pad + sparse piano + sync hooks. Deterministic.
import numpy as np
from scipy.io import wavfile
from scipy.signal import fftconvolve, butter, sosfilt
SR=48000; DUR=45.0; N=int(SR*DUR)
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
# --- harmonic bed: Fmaj9 | Dm9 | Bbmaj7 | C/E ... (F major, slow) ---
chords=[(0,[53,57,60,64,67]),(10,[50,53,57,60,64]),(17,[46,50,53,57,60]),(22,[53,57,60,64,67]),(31,[46,50,53,57,62]),(38,[53,57,60,64,69])]
for i,(t0,ms) in enumerate(chords):
    t1=chords[i+1][0]+1.5 if i+1<len(chords) else DUR
    add(pad(ms,t1-t0+.5),t0,0,1.0)
# --- sparse piano motif, landing on the reveals ---
for t,m,v in [(1.2,72,.32),(1.9,69,.22),(2.6,67,.2),(6.6,62,.3),(7.4,65,.22),(10.4,57,.25),(17.6,72,.28),(18.8,76,.3),(19.6,74,.2),
              (23.8,79,.18),(25.8,77,.18),(27.8,76,.2),(29.4,72,.18),(34.4,81,.25),(35.2,77,.2),(36.2,72,.2),
              (38.2,69,.25),(39.4,72,.28),(41.4,77,.3),(42.2,81,.22)]:
    add(piano(m,5,v),t,pan=(m-70)/30)
for m in (41,48): add(piano(m,6,.25),41.4,-.2)   # final low root
# --- sound hooks synced to animation ---
add(swell(1.6,.10),0.0)                 # f1 hairline draw
add(thud(.45),6.55)                     # f2 bold line lands
add(swell(1.2,.08,300,2000),10.0)        # seam into 16%
for k in range(16):                     # counter 0→16 (ease-out spacing)
    u=(k+1)/16; tt=10.6+2.2*(1-(1-u)**0.5)
    add(tick(.06+.04*u,2200+40*k),tt)
add(bell(64,.18),12.8)                  # count settles
add(swell(1.4,.09),17.0)                # into direct
add(bell(76,.16),18.75)                 # "on your site."
add(click(.16),23.8); add(click(.12),24.0)  # dates selected
add(click(.16),27.4)                    # extras step
add(swell(1.0,.07),31.0)
for k in range(10): add(tick(.05,3000+60*k),34.4+1.8*(1-(1-(k+1)/10)**0.5))
add(bell(69,.22),36.2); add(bell(76,.16),36.25)   # $530 lands
add(swell(1.4,.1),40.8)                 # signature hairline
add(bell(65,.18,7),41.5)                # wordmark
# --- reverb, master ---
ir_t=np.arange(int(SR*3.2))/SR
ir=rng.standard_normal((2,len(ir_t)))*np.exp(-ir_t*2.2); ir[:,0]=0
wetL=fftconvolve(L,ir[0])[:N]; wetR=fftconvolve(R,ir[1])[:N]
mixL=L+wetL*0.012; mixR=R+wetR*0.012
fade=np.ones(N); fi=int(SR*1.5); fo=int(SR*3)
fade[:fi]=np.linspace(0,1,fi); fade[-fo:]=np.linspace(1,0,fo)
st=np.stack([mixL*fade,mixR*fade],1)
st=np.tanh(st/np.max(np.abs(st))*1.2)*0.85
wavfile.write('score.wav',SR,(st*32767).astype(np.int16))
print('wrote score.wav')
