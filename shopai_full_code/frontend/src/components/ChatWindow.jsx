import React, { useState } from "react";
import { askRAG, getRecommendations } from "../api";
import ProductCard from "./ProductCard";

function ChatWindow({ messages, setMessages }) {
  const [input, setInput] = useState("");
  const [products, setProducts] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;
    setMessages([...messages, { role: "user", content: input }]);
    const { data } = await askRAG(input);
    setMessages((msgs) => [...msgs, { role: "assistant", content: data.answer }]);

    // Also fetch product suggestions
    const rec = await getRecommendations(input);
    setProducts(rec.data.products);
    setInput("");
  };

  return (
    <div className="p-4 bg-white rounded-lg shadow space-y-2">
      <div className="h-64 overflow-y-auto border p-2">
        {messages.map((msg, idx) => (
          <p key={idx} className={msg.role === "user" ? "text-right" : "text-left"}>
            <span className={msg.role === "user" ? "font-semibold" : "text-green-700"}>
              {msg.role === "user" ? "You" : "ShopAI"}:
            </span>{" "}
            {msg.content}
          </p>
        ))}
      </div>
      <div className="flex space-x-2">
        <input
          className="flex-1 border rounded p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask me anything..."
        />
        <button onClick={handleSend} className="px-4 py-2 bg-green-600 rounded text-white">
          Send
        </button>
      </div>

      {products.length > 0 && (
        <div className="grid grid-cols-2 gap-4 mt-4">
          {products.map((p) => (
            <ProductCard key={p.id} product={p} />
          ))}
        </div>
      )}
    </div>
  );
}

export default ChatWindow;
