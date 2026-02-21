"use client";

import { useState, useRef, useEffect, useCallback } from "react";
import { COMPANIONS } from "@/lib/companions";

// ═══════════════════════════════════════════
// API helpers (call OUR server, not external)
// ═══════════════════════════════════════════

async function sendChat(messages, systemPrompt) {
  const res = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ messages, systemPrompt }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || "Chat error");
  return data.text;
}

async function generateImage(prompt) {
  const res = await fetch("/api/image", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || "Image error");
  return data.imageUrl;
}

// ═══════════════════════════════════════════
// Selection Screen
// ═══════════════════════════════════════════

function SelectionScreen({ onSelect }) {
  return (
    <div style={styles.selectionScreen}>
      {/* Ambient bg */}
      <div style={styles.ambientBg} />

      <div style={styles.logoSection}>
        <span style={styles.logoIcon}>🍯</span>
        <h1 style={styles.logoTitle}>Miel AI</h1>
        <p style={styles.logoSubtitle}>Tu compañía perfecta</p>
      </div>

      <p style={styles.chooseLabel}>Elige con quién quieres platicar</p>

      <div style={styles.grid}>
        {COMPANIONS.map((c) => (
          <CompanionCard key={c.id} companion={c} onSelect={onSelect} />
        ))}
      </div>

      <p style={styles.disclaimer}>
        Powered by AI — Las conversaciones no se guardan. Proyecto en beta.
      </p>
    </div>
  );
}

function CompanionCard({ companion, onSelect }) {
  const [hovered, setHovered] = useState(false);

  return (
    <div
      style={{
        ...styles.card,
        borderColor: hovered ? companion.accent : "var(--border)",
        boxShadow: hovered ? `0 8px 40px ${companion.accent}22` : "none",
        transform: hovered ? "translateY(-6px) scale(1.02)" : "none",
      }}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      onClick={() => onSelect(companion)}
    >
      <span style={styles.cardEmoji}>{companion.emoji}</span>
      <div style={styles.cardName}>{companion.name}</div>
      <div style={styles.cardTagline}>{companion.tagline}</div>
    </div>
  );
}

// ═══════════════════════════════════════════
// Chat Screen
// ═══════════════════════════════════════════

function ChatScreen({ companion, onBack }) {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const [error, setError] = useState(null);
  const bottomRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = useCallback(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping, scrollToBottom]);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleImageGen = async (msgIndex, contextHint) => {
    setMessages((prev) => {
      const u = [...prev];
      u[msgIndex] = { ...u[msgIndex], imageLoading: true };
      return u;
    });

    try {
      const prompt = `${companion.imagePrompt}, ${contextHint || "casual selfie, smiling at camera"}. Ultra realistic, natural, warm.`;
      const url = await generateImage(prompt);
      setMessages((prev) => {
        const u = [...prev];
        u[msgIndex] = { ...u[msgIndex], imageLoading: false, imageUrl: url };
        return u;
      });
    } catch (err) {
      console.error("Image gen error:", err);
      setMessages((prev) => {
        const u = [...prev];
        u[msgIndex] = {
          ...u[msgIndex],
          imageLoading: false,
          text: u[msgIndex].text + "\n\n(No pude generar la foto esta vez 😅)",
        };
        return u;
      });
    }
  };

  const send = async (overrideText) => {
    const text = (overrideText || input).trim();
    if (!text || isTyping) return;

    setError(null);
    const userMsg = { role: "user", text };
    const newMsgs = [...messages, userMsg];
    setMessages(newMsgs);
    if (!overrideText) setInput("");
    setIsTyping(true);

    try {
      const reply = await sendChat(newMsgs, companion.personality);
      const hasPhoto = reply.includes("[PHOTO_REQUEST]");
      const clean = reply.replace(/\[PHOTO_REQUEST\]/g, "").trim();
      const aiMsg = { role: "ai", text: clean };
      const updated = [...newMsgs, aiMsg];
      setMessages(updated);
      setIsTyping(false);

      if (hasPhoto) {
        handleImageGen(updated.length - 1, text);
      }
    } catch (err) {
      setIsTyping(false);
      setError(err.message);
    }
  };

  const requestSelfie = () => send("¡Mándame una selfie tuya!");

  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      send();
    }
  };

  return (
    <div style={styles.chatScreen}>
      {/* Header */}
      <div style={styles.header}>
        <button style={styles.backBtn} onClick={onBack}>
          ←
        </button>
        <div
          style={{ ...styles.headerAvatar, background: companion.gradient }}
        >
          {companion.emoji}
        </div>
        <div style={{ flex: 1 }}>
          <div style={styles.headerName}>{companion.name}</div>
          <div style={styles.headerStatus}>
            <span style={styles.statusDot} />
            En línea
          </div>
        </div>
        <button style={styles.photoBtn} onClick={requestSelfie}>
          📸 Selfie
        </button>
      </div>

      {/* Error */}
      {error && <div style={styles.errorBanner}>⚠️ {error}</div>}

      {/* Messages */}
      <div style={styles.messagesArea}>
        {messages.length === 0 && (
          <div style={styles.welcome}>
            <span style={{ fontSize: 48, display: "block", marginBottom: 12 }}>
              {companion.emoji}
            </span>
            <p style={{ maxWidth: 300, margin: "0 auto", lineHeight: 1.6 }}>
              ¡Hola! Soy {companion.name}. Escríbeme lo que quieras, estoy
              aquí para platicar contigo ✨
            </p>
          </div>
        )}

        {messages.map((msg, i) => (
          <div
            key={i}
            style={{
              ...styles.msgRow,
              justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
              animation: "msgIn 0.35s ease-out",
            }}
          >
            <div
              style={
                msg.role === "user" ? styles.userBubble : styles.aiBubble
              }
            >
              {msg.text}
              {msg.imageLoading && (
                <div style={styles.imgLoading}>📸 Generando selfie...</div>
              )}
              {msg.imageUrl && (
                <img src={msg.imageUrl} alt="selfie" style={styles.msgImage} />
              )}
            </div>
          </div>
        ))}

        {isTyping && (
          <div style={styles.typingRow}>
            <div style={styles.typingDots}>
              {[0, 1, 2].map((i) => (
                <span
                  key={i}
                  style={{
                    ...styles.dot,
                    animationDelay: `${i * 0.2}s`,
                  }}
                />
              ))}
            </div>
          </div>
        )}

        <div ref={bottomRef} />
      </div>

      {/* Input */}
      <div style={styles.inputArea}>
        <div style={styles.inputRow}>
          <textarea
            ref={inputRef}
            style={styles.textarea}
            placeholder={`Escríbele a ${companion.name}...`}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            rows={1}
          />
          <button
            style={{
              ...styles.sendBtn,
              background: companion.gradient,
              opacity: !input.trim() || isTyping ? 0.4 : 1,
            }}
            onClick={() => send()}
            disabled={!input.trim() || isTyping}
          >
            ↑
          </button>
        </div>
      </div>
    </div>
  );
}

// ═══════════════════════════════════════════
// Main App
// ═══════════════════════════════════════════

export default function Home() {
  const [companion, setCompanion] = useState(null);

  if (!companion) {
    return <SelectionScreen onSelect={setCompanion} />;
  }

  return <ChatScreen companion={companion} onBack={() => setCompanion(null)} />;
}

// ═══════════════════════════════════════════
// Inline Styles
// ═══════════════════════════════════════════

const styles = {
  // Selection
  selectionScreen: {
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    padding: 24,
    position: "relative",
    zIndex: 1,
    animation: "fadeUp 0.8s ease-out",
  },
  ambientBg: {
    position: "fixed",
    top: "-50%",
    left: "-50%",
    width: "200%",
    height: "200%",
    background:
      "radial-gradient(ellipse at 30% 20%, rgba(255,107,157,0.05) 0%, transparent 50%), radial-gradient(ellipse at 70% 80%, rgba(78,205,196,0.04) 0%, transparent 50%)",
    pointerEvents: "none",
    zIndex: 0,
  },
  logoSection: { textAlign: "center", marginBottom: 48 },
  logoIcon: {
    fontSize: 56,
    display: "block",
    marginBottom: 16,
    filter: "drop-shadow(0 0 30px rgba(255,107,157,0.3))",
    animation: "float 3s ease-in-out infinite",
  },
  logoTitle: {
    fontSize: 42,
    fontWeight: 800,
    letterSpacing: -1.5,
    background: "linear-gradient(135deg, #FF6B9D, #C44569, #A78BFA)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
    lineHeight: 1.1,
  },
  logoSubtitle: {
    fontSize: 15,
    color: "var(--text-secondary)",
    marginTop: 8,
    fontWeight: 300,
    letterSpacing: 2,
    textTransform: "uppercase",
  },
  chooseLabel: {
    color: "var(--text-secondary)",
    marginBottom: 20,
    fontSize: 14,
    fontWeight: 500,
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, 1fr)",
    gap: 16,
    width: "100%",
    maxWidth: 540,
  },
  card: {
    background: "var(--bg-card)",
    border: "1.5px solid var(--border)",
    borderRadius: 20,
    padding: "28px 16px",
    textAlign: "center",
    cursor: "pointer",
    transition: "all 0.4s cubic-bezier(0.16,1,0.3,1)",
    backdropFilter: "blur(10px)",
  },
  cardEmoji: { fontSize: 44, marginBottom: 14, display: "block" },
  cardName: { fontWeight: 700, fontSize: 18, marginBottom: 4, letterSpacing: -0.3 },
  cardTagline: { fontSize: 12, color: "var(--text-secondary)", fontWeight: 300 },
  disclaimer: {
    color: "var(--text-muted)",
    marginTop: 32,
    fontSize: 12,
    textAlign: "center",
    maxWidth: 400,
    lineHeight: 1.6,
  },

  // Chat
  chatScreen: {
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    position: "relative",
  },
  header: {
    padding: "16px 20px",
    display: "flex",
    alignItems: "center",
    gap: 14,
    borderBottom: "1px solid var(--border)",
    backdropFilter: "blur(20px)",
    background: "rgba(10,10,15,0.85)",
    flexShrink: 0,
  },
  backBtn: {
    background: "none",
    border: "none",
    color: "var(--text-secondary)",
    fontSize: 22,
    cursor: "pointer",
    padding: "4px 8px",
    borderRadius: 8,
  },
  headerAvatar: {
    width: 42,
    height: 42,
    borderRadius: "50%",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    fontSize: 22,
    flexShrink: 0,
  },
  headerName: { fontWeight: 600, fontSize: 16, letterSpacing: -0.3 },
  headerStatus: {
    fontSize: 12,
    color: "#4ADE80",
    fontWeight: 400,
    display: "flex",
    alignItems: "center",
    gap: 5,
  },
  statusDot: {
    width: 7,
    height: 7,
    background: "#4ADE80",
    borderRadius: "50%",
    display: "inline-block",
    animation: "pulse-dot 2s infinite",
  },
  photoBtn: {
    background: "var(--bg-tertiary)",
    border: "1px solid var(--border)",
    color: "var(--text-secondary)",
    padding: "8px 14px",
    borderRadius: 10,
    fontSize: 13,
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    gap: 6,
  },

  // Messages
  messagesArea: {
    flex: 1,
    overflowY: "auto",
    padding: 20,
    display: "flex",
    flexDirection: "column",
    gap: 6,
  },
  welcome: {
    textAlign: "center",
    padding: "40px 20px",
    color: "var(--text-muted)",
    fontSize: 14,
  },
  msgRow: { display: "flex" },
  userBubble: {
    maxWidth: "78%",
    padding: "12px 16px",
    borderRadius: "18px 18px 6px 18px",
    fontSize: 15,
    lineHeight: 1.5,
    background: "var(--bg-tertiary)",
    border: "1px solid var(--border)",
    color: "var(--text-primary)",
    wordWrap: "break-word",
    whiteSpace: "pre-wrap",
  },
  aiBubble: {
    maxWidth: "78%",
    padding: "12px 16px",
    borderRadius: "18px 18px 18px 6px",
    fontSize: 15,
    lineHeight: 1.5,
    background: "var(--bg-card)",
    backdropFilter: "blur(10px)",
    border: "1px solid rgba(255,255,255,0.05)",
    color: "var(--text-primary)",
    wordWrap: "break-word",
    whiteSpace: "pre-wrap",
  },
  msgImage: {
    maxWidth: 260,
    borderRadius: 14,
    marginTop: 8,
    display: "block",
    border: "1px solid var(--border)",
  },
  imgLoading: {
    width: 260,
    height: 200,
    borderRadius: 14,
    marginTop: 8,
    background: "var(--bg-tertiary)",
    border: "1px solid var(--border)",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    color: "var(--text-muted)",
    fontSize: 13,
    animation: "shimmer 1.8s infinite",
  },
  typingRow: {
    display: "flex",
    justifyContent: "flex-start",
    padding: "8px 0",
  },
  typingDots: { display: "flex", gap: 5, padding: "12px 16px" },
  dot: {
    width: 8,
    height: 8,
    background: "var(--text-muted)",
    borderRadius: "50%",
    animation: "typing-bounce 1.4s infinite",
  },
  errorBanner: {
    background: "rgba(220,38,38,0.1)",
    border: "1px solid rgba(220,38,38,0.3)",
    color: "#FCA5A5",
    padding: "10px 16px",
    borderRadius: 10,
    fontSize: 13,
    margin: "8px 20px",
    textAlign: "center",
  },

  // Input
  inputArea: {
    padding: "16px 20px",
    borderTop: "1px solid var(--border)",
    backdropFilter: "blur(20px)",
    background: "rgba(10,10,15,0.85)",
    flexShrink: 0,
  },
  inputRow: {
    display: "flex",
    gap: 10,
    alignItems: "flex-end",
    maxWidth: 800,
    margin: "0 auto",
  },
  textarea: {
    flex: 1,
    padding: "14px 18px",
    background: "var(--bg-tertiary)",
    border: "1px solid var(--border)",
    borderRadius: 14,
    color: "var(--text-primary)",
    fontSize: 15,
    outline: "none",
    resize: "none",
    minHeight: 48,
    maxHeight: 120,
    lineHeight: 1.4,
  },
  sendBtn: {
    width: 48,
    height: 48,
    borderRadius: 14,
    border: "none",
    color: "white",
    fontSize: 20,
    cursor: "pointer",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexShrink: 0,
    transition: "all 0.3s",
  },
};
