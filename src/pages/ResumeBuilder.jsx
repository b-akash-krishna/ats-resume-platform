"use client"

import { useState } from "react"
import UploadResume from "../components/resume/UploadResume"
import ResumeEditor from "../components/resume/ResumeEditor"
import ATSScoreMeter from "../components/resume/ATSScoreMeter"
import TemplatePicker from "../components/resume/TemplatePicker"
import ResumePreview from "../components/resume/ResumePreview"
import AIAssistant from "../components/resume/AIAssistant"

export default function ResumeBuilder() {
  const [step, setStep] = useState("upload")
  const [resumeData, setResumeData] = useState({})

  const handleUpload = (file) => {
    // TODO: Parse resume file and extract data
    console.log("File uploaded:", file)
    setStep("edit")
  }

  const handleTemplateSelect = (templateId) => {
    console.log("Template selected:", templateId)
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <h1 className="text-4xl font-bold mb-8">Resume Builder</h1>

      {step === "upload" && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <UploadResume onUpload={handleUpload} />
          </div>
          <div>
            <TemplatePicker onSelect={handleTemplateSelect} />
          </div>
        </div>
      )}

      {step === "edit" && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 space-y-6">
            <ResumeEditor initialData={resumeData} />
            <AIAssistant />
          </div>
          <div className="space-y-6">
            <ATSScoreMeter score={75} />
            <ResumePreview data={resumeData} />
          </div>
        </div>
      )}
    </div>
  )
}
