"use client"

import { useState } from "react"
import { Upload } from "lucide-react"

export default function UploadResume({ onUpload }) {
  const [isDragging, setIsDragging] = useState(false)

  const handleDragOver = (e) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = () => {
    setIsDragging(false)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setIsDragging(false)
    const files = e.dataTransfer.files
    if (files.length > 0) {
      onUpload(files[0])
    }
  }

  const handleFileSelect = (e) => {
    if (e.target.files.length > 0) {
      onUpload(e.target.files[0])
    }
  }

  return (
    <div
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
      className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition ${
        isDragging ? "border-blue-600 bg-blue-50" : "border-gray-300"
      }`}
    >
      <Upload className="mx-auto mb-4 text-gray-400" size={48} />
      <p className="text-lg font-semibold mb-2">Drag and drop your resume</p>
      <p className="text-gray-600 mb-4">or</p>
      <label className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 cursor-pointer inline-block">
        Browse Files
        <input type="file" accept=".pdf,.docx,.doc" onChange={handleFileSelect} className="hidden" />
      </label>
      <p className="text-sm text-gray-500 mt-4">Supported formats: PDF, DOCX, DOC</p>
    </div>
  )
}
