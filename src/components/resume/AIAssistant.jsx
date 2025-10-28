"use client"

import { useState } from "react"
import { Send } from "lucide-react"

export default function AIAssistant() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState("")

  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, { role: "user", content: input }])
      // TODO: Call AI service to generate response
      setInput("")
    }
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 h-96 flex flex-col">
      <h3 className="text-lg font-semibold mb-4">AI Resume Assistant</h3>

      <div className="flex-grow overflow-y-auto mb-4 space-y-4">
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>
            <div
              className={`max-w-xs px-4 py-2 rounded-lg ${
                msg.role === "user" ? "bg-blue-600 text-white" : "bg-gray-200 text-gray-800"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
          placeholder="Ask for resume suggestions..."
          className="flex-grow px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:border-transparent"
        />
        <button onClick={handleSend} className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700">
          <Send size={20} />
        </button>
      </div>
    </div>
  )
}
