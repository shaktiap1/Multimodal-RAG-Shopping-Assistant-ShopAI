import React, { useState, useRef } from "react";
import { transcribeAudio } from "../api";

function AudioRecorder() {
  const [text, setText] = useState("");
  const recorderRef = useRef(null);
  const [recording, setRecording] = useState(false);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    recorderRef.current = { mediaRecorder, chunks: [] };

    mediaRecorder.ondataavailable = (e) => {
      recorderRef.current.chunks.push(e.data);
    };
    mediaRecorder.onstop = async () => {
      const blob = new Blob(recorderRef.current.chunks, { type: "audio/webm" });
      const file = new File([blob], "audio.webm");
      const { data } = await transcribeAudio(file);
      setText(data.text);
    };

    mediaRecorder.start();
    setRecording(true);
  };

  const stopRecording = () => {
    recorderRef.current.mediaRecorder.stop();
    setRecording(false);
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow">
      <button
        onClick={recording ? stopRecording : startRecording}
        className="px-4 py-2 bg-blue-600 rounded text-white"
      >
        {recording ? "Stop" : "Record"}
      </button>
      {text && <p className="mt-2 text-blue-600">Transcript: {text}</p>}
    </div>
  );
}

export default AudioRecorder;
