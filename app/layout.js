import "./globals.css";

export const metadata = {
  title: "Miel AI — Tu compañía perfecta",
  description: "Compañeros virtuales con IA para platicar, conectar y pasarla bien.",
  openGraph: {
    title: "Miel AI — Tu compañía perfecta",
    description: "Compañeros virtuales con IA. Chat, selfies y más.",
    type: "website",
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
