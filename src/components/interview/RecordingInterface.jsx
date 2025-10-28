"use client"

import { useState } from "react"
import { Mic, Square } from "lucide-react"

export default function RecordingInterface() {
  const [isRecording, setIsRecording] = useState(false)
  const [duration, setDuration] = useState(0)

  return (
    <div className="bg-white rounded-lg shadow-md p-6 text-center">
      <div className="mb-6">
        <div
          className={`inline-flex items-center justify-center w-24 h-24 rounded-full ${
            isRecording ? "bg-red-100" : "bg-gray-100"
          }`}
        >
          {isRecording ? <Square className="text-red-600" size={40} /> : <Mic className="text-gray-600" size={40} />}
        </div>
      </div>

      <p className="text-2xl font-bold text-gray-900 mb-4">
        {Math.floor(duration / 60)}:{String(duration % 60).padStart(2, "0")}
      </p>

      <button
        onClick={() => setIsRecording(!isRecording)}
        className={`px-8 py-3 rounded-lg font-semibold text-white ${
          isRecording ? "bg-red-600 hover:bg-red-700" : "bg-blue-600 hover:bg-blue-700"
        }`}
      >
        {isRecording ? "Stop Recording" : "Start Recording"}
      </button>
    </div>
  )
}
