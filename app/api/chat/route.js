import { NextResponse } from "next/server";

export async function POST(req) {
  try {
    const { messages, systemPrompt } = await req.json();

    if (!messages || !systemPrompt) {
      return NextResponse.json({ error: "Missing fields" }, { status: 400 });
    }

    const apiKey = process.env.ANTHROPIC_API_KEY;
    if (!apiKey) {
      return NextResponse.json(
        { error: "ANTHROPIC_API_KEY not configured" },
        { status: 500 }
      );
    }

    const res = await fetch("https://api.anthropic.com/v1/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": apiKey,
        "anthropic-version": "2023-06-01",
      },
      body: JSON.stringify({
        model: "claude-sonnet-4-20250514",
        max_tokens: 350,
        system: systemPrompt,
        messages: messages.map(function (m) {
          return {
            role: m.role === "user" ? "user" : "assistant",
            content: m.text,
          };
        }),
      }),
    });

    if (!res.ok) {
      const err = await res.json().catch(function () {
        return {};
      });
      console.error("Anthropic error:", err);
      return NextResponse.json(
        { error: err?.error?.message || "Claude API error " + res.status },
        { status: res.status }
      );
    }

    const data = await res.json();
    const text = data.content
      .map(function (b) {
        return b.text || "";
      })
      .join("");

    return NextResponse.json({ text: text });
  } catch (e) {
    console.error("Chat route error:", e);
    return NextResponse.json({ error: "Server error" }, { status: 500 });
  }
}
