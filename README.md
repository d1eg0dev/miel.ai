# 🍯 Miel AI — Tu compañía perfecta

AI companion app para el mercado mexicano. Chat con personalidades en español mexicano + generación de selfies con IA.

## Stack

- **Frontend:** Next.js 14 (App Router)
- **Chat AI:** Claude Sonnet (Anthropic API)
- **Image AI:** Gemini Nano Banana (Google AI — gratis hasta 500 imgs/día)
- **Deploy:** Vercel (gratis)

## Setup rápido

### 1. Clona el repo

```bash
git clone https://github.com/TU-USUARIO/miel-ai.git
cd miel-ai
npm install
```

### 2. Configura tus API keys

Crea un archivo `.env.local` en la raíz:

```env
ANTHROPIC_API_KEY=sk-ant-tu-key-aqui
GEMINI_API_KEY=tu-gemini-key-aqui
```

**¿Dónde conseguir las keys?**

- **Anthropic:** https://console.anthropic.com → API Keys (tiene free credits al registrarte)
- **Google Gemini:** https://aistudio.google.com/apikey → Crear API Key (gratis, 500 imágenes/día)

### 3. Corre en local

```bash
npm run dev
```

Abre http://localhost:3000

### 4. Deploy a Vercel

```bash
# Instala Vercel CLI (una vez)
npm i -g vercel

# Despliega
vercel

# O conecta tu repo de GitHub en vercel.com:
# 1. Ve a vercel.com/new
# 2. Importa tu repo de GitHub
# 3. Agrega las variables de entorno (ANTHROPIC_API_KEY, GEMINI_API_KEY)
# 4. Deploy
```

## Arquitectura

```
miel-ai/
├── app/
│   ├── layout.js          # Root layout + metadata SEO
│   ├── globals.css         # Dark theme premium
│   ├── page.js             # UI principal (selección + chat)
│   └── api/
│       ├── chat/route.js   # Proxy a Claude (key segura en server)
│       └── image/route.js  # Proxy a Gemini Nano Banana (key segura)
├── lib/
│   └── companions.js       # Configuración de personalidades
├── .env.example
└── package.json
```

**Las API keys NUNCA se exponen al usuario.** Las llamadas van:

```
Usuario → Vercel (tu server) → Anthropic/Google APIs
```

## Costos estimados

| Concepto | Costo |
|---|---|
| Hosting (Vercel) | $0 (free tier) |
| Chat (Claude Sonnet) | ~$0.003/mensaje |
| Selfies (Gemini) | $0 (hasta 500/día gratis) |
| **100 usuarios activos/día** | **~$3-5 USD/día** |

## Roadmap MVP → Producto

- [ ] Auth con email/Google (NextAuth)
- [ ] Base de datos para guardar chats (Supabase free tier)
- [ ] Rate limiting por usuario
- [ ] Pagos con Stripe o MercadoPago
- [ ] Más companions
- [ ] Voz (text-to-speech con Gemini)
- [ ] PWA para instalar en celular
- [ ] Analytics (Vercel Analytics / Posthog free)

## License

MIT
