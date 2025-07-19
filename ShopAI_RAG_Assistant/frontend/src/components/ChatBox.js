import React, { useState } from 'react';
import InputBar from './InputBar';

function ChatBox() {
  const [messages, setMessages] = useState([]);

  const sendMessage = async (msg) => {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({message: msg, user_id: 'test_user'})
    });
    const data = await res.json();
    setMessages([...messages, {user: msg, bot: data.response}]);
  };

  return (
    <div>
      <div>
        {messages.map((m, i) => (
          <div key={i}>
            <b>You:</b> {m.user}<br/>
            <b>ShopAI:</b> {m.bot}
          </div>
        ))}
      </div>
      <InputBar onSend={sendMessage} />
    </div>
  );
}

export default ChatBox;
