"use client"

import { useState } from "react"
import { Mic, MicOff, Volume2 } from "lucide-react"

export default function InterviewSession({ question, onAnswer }) {
  const [isRecording, setIsRecording] = useState(false)
  const [answer, setAnswer] = useState("")

  const handleSubmit = () => {
    onAnswer(answer)
    setAnswer("")
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-2xl mx-auto">
      <div className="mb-6">
        <h3 className="text-lg font-semibold text-gray-700 mb-4">Question</h3>
        <p className="text-xl text-gray-900">{question}</p>
        <button className="mt-4 flex items-center gap-2 text-blue-600 hover:text-blue-700">
          <Volume2 size={20} />
          Play Audio
        </button>
      </div>

      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Your Answer</label>
          <textarea
            value={answer}
            onChange={(e) => setAnswer(e.target.value)}
            placeholder="Type or speak your answer..."
            rows="6"
            className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600 focus:border-transparent"
          />
        </div>

        <div className="flex gap-4">
          <button
            onClick={() => setIsRecording(!isRecording)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg font-semibold ${
              isRecording ? "bg-red-600 text-white hover:bg-red-700" : "bg-gray-200 text-gray-800 hover:bg-gray-300"
            }`}
          >
            {isRecording ? <MicOff size={20} /> : <Mic size={20} />}
            {isRecording ? "Stop Recording" : "Start Recording"}
          </button>
          <button
            onClick={handleSubmit}
            className="flex-grow bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 font-semibold"
          >
            Submit Answer
          </button>
        </div>
      </div>
    </div>
  )
}
