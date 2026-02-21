import { NextResponse } from "next/server";

export async function POST(req) {
  try {
    const { messages, systemPrompt } = await req.json();

    if (!messages || !systemPrompt) {
      return NextResponse.json({ error: "Missing fields" }, { status: 400 });
    }

    var apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      return NextResponse.json(
        { error: "GEMINI_API_KEY not configured" },
        { status: 500 }
      );
    }

    var contents = [];
    for (var i = 0; i < messages.length; i++) {
      contents.push({
        role: messages[i].role === "user" ? "user" : "model",
        parts: [{ text: messages[i].text }],
      });
    }

    var url =
      "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=" +
      apiKey;

    var res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        system_instruction: {
          parts: [{ text: systemPrompt }],
        },
        contents: contents,
        generationConfig: {
          maxOutputTokens: 350,
          temperature: 0.9,
        },
      }),
    });

    if (!res.ok) {
      var errData = await res.json().catch(function () {
        return {};
      });
      console.error("Gemini chat error:", JSON.stringify(errData));
      return NextResponse.json(
        {
          error: errData?.error?.message || "Gemini API error " + res.status,
        },
        { status: res.status }
      );
    }

    var data = await res.json();

    var text = "";
    if (
      data &&
      data.candidates &&
      data.candidates[0] &&
      data.candidates[0].content &&
      data.candidates[0].content.parts
    ) {
      for (var j = 0; j < data.candidates[0].content.parts.length; j++) {
        if (data.candidates[0].content.parts[j].text) {
          text += data.candidates[0].content.parts[j].text;
        }
      }
    }

    if (!text) {
      return NextResponse.json(
        { error: "No response generated" },
        { status: 422 }
      );
    }

    return NextResponse.json({ text: text });
  } catch (e) {
    console.error("Chat route error:", e);
    return NextResponse.json({ error: "Server error" }, { status: 500 });
  }
}
