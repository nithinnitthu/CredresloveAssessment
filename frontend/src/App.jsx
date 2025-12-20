import React, { useState, useRef } from "react";

const BACKEND = import.meta.env.VITE_BACKEND_URL || "";

export default function App() {
  const [userId, setUserId] = useState("user1");
  const [sessionId, setSessionId] = useState("session1");
  const [recognized, setRecognized] = useState("");
  const [log, setLog] = useState("");
  const [recording, setRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const appendLog = (s) => setLog((l) => l + s + "\n");

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mr = new MediaRecorder(stream);
    mediaRecorderRef.current = mr;
    audioChunksRef.current = [];
    mr.ondataavailable = (e) => audioChunksRef.current.push(e.data);
    mr.start();
    setRecording(true);
    appendLog("Recording...");
  };

  const stopRecording = () => {
    mediaRecorderRef.current?.stop();
    setRecording(false);
    appendLog("Stopped.");
  };

  const sendToStt = async (mockText) => {
    const blob = new Blob(audioChunksRef.current, { type: "audio/webm" });
    const fd = new FormData();
    if (blob.size > 0) fd.append("audio", blob, "rec.webm");
    if (mockText) fd.append("mock_text", mockText);
    const resp = await fetch("/api/stt", { method: "POST", body: fd });
    const data = await resp.json();
    setRecognized(data.text);
    appendLog("STT => " + data.text);
    audioChunksRef.current = [];
  };

  const runAgent = async () => {
    const fd = new FormData();
    fd.append("user_id", userId);
    fd.append("session_id", sessionId);
    fd.append("text", recognized);
    const resp = await fetch("/api/agent", { method: "POST", body: fd });
    const res = await resp.json();
    appendLog("Agent reply:\n" + res.reply_text);
    // play TTS
    const ttsResp = await fetch("/api/tts?text=" + encodeURIComponent(res.tts_text));
    const mp3 = await ttsResp.blob();
    const url = URL.createObjectURL(mp3);
    const audio = new Audio(url);
    audio.play();
    appendLog("Played TTS audio.");
  };

  return (
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Telugu Voice Agent — React PoC</h1>
      <div>
        <label>
          User ID: <input value={userId} onChange={(e) => setUserId(e.target.value)} />
        </label>{" "}
        <label style={{ marginLeft: 10 }}>
          Session ID: <input value={sessionId} onChange={(e) => setSessionId(e.target.value)} />
        </label>
      </div>

      <div style={{ marginTop: 10 }}>
        <button onClick={startRecording} disabled={recording}>
          Start Recording
        </button>
        <button onClick={stopRecording} disabled={!recording}>
          Stop
        </button>
        <button
          onClick={() => sendToStt(prompt("Optional mock_text (for quick testing) or leave blank):"))}
        >
          Send to STT
        </button>
        <button onClick={runAgent} disabled={!recognized}>
          Confirm & Run Agent
        </button>
      </div>

      <div style={{ marginTop: 10 }}>
        <strong>Recognized text:</strong>
        <div style={{ border: "1px solid #ddd", padding: 8, minHeight: 24 }}>{recognized}</div>
      </div>

      <div style={{ marginTop: 10 }}>
        <strong>Log:</strong>
        <pre style={{ border: "1px solid #ddd", padding: 8, height: 240, overflow: "auto" }}>
          {log}
        </pre>
      </div>
    </div>
  );
}

