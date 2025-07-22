import React, { useState } from "react";
import ImageUpload from "./components/ImageUpload";
import AudioRecorder from "./components/AudioRecorder";
import ChatWindow from "./components/ChatWindow";

function App() {
  const [messages, setMessages] = useState([]);

  return (
    <div className="max-w-5xl mx-auto p-4 space-y-6">
      <h1 className="text-3xl font-bold text-center">ShopAI</h1>
      <ImageUpload />
      <AudioRecorder />
      <ChatWindow messages={messages} setMessages={setMessages} />
    </div>
  );
}

export default App;
