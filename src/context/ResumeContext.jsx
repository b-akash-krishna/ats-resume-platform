"use client"

import { createContext, useState } from "react"

export const ResumeContext = createContext()

export function ResumeProvider({ children }) {
  const [resumes, setResumes] = useState([])
  const [currentResume, setCurrentResume] = useState(null)

  const addResume = (resume) => {
    setResumes([...resumes, resume])
  }

  const updateResume = (id, updatedResume) => {
    setResumes(resumes.map((r) => (r.id === id ? updatedResume : r)))
  }

  return (
    <ResumeContext.Provider value={{ resumes, currentResume, setCurrentResume, addResume, updateResume }}>
      {children}
    </ResumeContext.Provider>
  )
}
