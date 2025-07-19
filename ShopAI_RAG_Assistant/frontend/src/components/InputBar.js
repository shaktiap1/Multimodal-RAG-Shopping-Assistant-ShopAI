import React, { useState } from 'react';

function InputBar({ onSend }) {
  const [input, setInput] = useState('');

  const handleSubmit = e => {
    e.preventDefault();
    if (input.trim()) {
      onSend(input);
      setInput('');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={input} 
        onChange={e => setInput(e.target.value)} 
        placeholder="Ask something..." />
      <button type="submit">Send</button>
    </form>
  );
}

export default InputBar;
