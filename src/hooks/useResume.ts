"use client"

import { useState, useCallback } from "react"
import { apiClient } from "@/lib/api"

interface Resume {
  id: number
  title: string
  full_name: string
  email: string
  phone?: string
  skills: string[]
  ats_score: number
  created_at: string
}

export function useResume() {
  const [resumes, setResumes] = useState<Resume[]>([])
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const uploadResume = useCallback(async (file: File) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.uploadResume(file)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const listResumes = useCallback(async () => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.listResumes()

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return
    }

    if (data) {
      setResumes(data as Resume[])
    }
    setIsLoading(false)
  }, [])

  const getResume = useCallback(async (resumeId: number) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.getResume(resumeId)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const analyzeATS = useCallback(async (resumeId: number, jobDescription: string) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.analyzeATS(resumeId, jobDescription)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const deleteResume = useCallback(async (resumeId: number) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.deleteResume(resumeId)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  return {
    resumes,
    isLoading,
    error,
    uploadResume,
    listResumes,
    getResume,
    analyzeATS,
    deleteResume,
  }
}
