import { NextResponse } from "next/server";

export async function POST(req) {
  try {
    const { prompt } = await req.json();

    if (!prompt) {
      return NextResponse.json({ error: "Missing prompt" }, { status: 400 });
    }

    var apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      return NextResponse.json(
        { error: "GEMINI_API_KEY not configured" },
        { status: 500 }
      );
    }

    var url =
      "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent?key=" +
      apiKey;

    var res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [
          {
            parts: [
              {
                text:
                  "Generate a single photorealistic image: " +
                  prompt +
                  ". Do not include any text in the image. High quality, natural lighting, iPhone photo style.",
              },
            ],
          },
        ],
        generationConfig: {
          responseModalities: ["IMAGE", "TEXT"],
        },
      }),
    });

    if (!res.ok) {
      var errData = await res.json().catch(function () {
        return {};
      });
      console.error("Gemini image error:", JSON.stringify(errData));
      return NextResponse.json(
        {
          error: errData?.error?.message || "Gemini API error " + res.status,
        },
        { status: res.status }
      );
    }

    var data = await res.json();
    var parts = [];
    if (
      data &&
      data.candidates &&
      data.candidates[0] &&
      data.candidates[0].content &&
      data.candidates[0].content.parts
    ) {
      parts = data.candidates[0].content.parts;
    }

    for (var i = 0; i < parts.length; i++) {
      if (parts[i].inlineData) {
        var mimeType = parts[i].inlineData.mimeType;
        var b64 = parts[i].inlineData.data;
        var dataUrl = "data:" + mimeType + ";base64," + b64;
        return NextResponse.json({ imageUrl: dataUrl });
      }
    }

    return NextResponse.json(
      { error: "No image generated. Try a different prompt." },
      { status: 422 }
    );
  } catch (e) {
    console.error("Image route error:", e.message);

    if (
      (e.message && e.message.indexOf("SAFETY") !== -1) ||
      (e.message && e.message.indexOf("blocked") !== -1)
    ) {
      return NextResponse.json(
        { error: "Content filter triggered. Try again!" },
        { status: 422 }
      );
    }

    return NextResponse.json(
      { error: "Image generation failed: " + e.message },
      { status: 500 }
    );
  }
}
