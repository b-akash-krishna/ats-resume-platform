"use client"

import { useState } from "react"
import InterviewSetup from "../components/interview/InterviewSetup"
import InterviewSession from "../components/interview/InterviewSession"
import InterviewReport from "../components/interview/InterviewReport"

export default function MockInterview() {
  const [stage, setStage] = useState("setup")
  const [currentQuestion, setCurrentQuestion] = useState(0)
  const [answers, setAnswers] = useState([])

  const mockQuestions = [
    "Tell me about yourself",
    "What are your strengths?",
    "Describe a challenging project you worked on",
  ]

  const handleStartInterview = (config) => {
    console.log("Interview started with config:", config)
    setStage("session")
  }

  const handleAnswer = (answer) => {
    setAnswers([...answers, answer])
    if (currentQuestion < mockQuestions.length - 1) {
      setCurrentQuestion(currentQuestion + 1)
    } else {
      setStage("report")
    }
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-4xl font-bold mb-8">Mock Interview</h1>

      {stage === "setup" && <InterviewSetup onStart={handleStartInterview} />}

      {stage === "session" && <InterviewSession question={mockQuestions[currentQuestion]} onAnswer={handleAnswer} />}

      {stage === "report" && <InterviewReport />}
    </div>
  )
}
