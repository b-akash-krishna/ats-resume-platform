"use client"

import { useState, useCallback } from "react"
import { apiClient } from "@/lib/api"

interface InterviewQuestion {
  id: number
  question_number: number
  question: string
  category: string
}

export function useInterview() {
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const setupInterview = useCallback(async (jobTitle: string, jobDescription: string, difficulty: string) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.setupInterview(jobTitle, jobDescription, difficulty)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const getQuestions = useCallback(async (interviewId: number) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.getInterviewQuestions(interviewId)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data: data as InterviewQuestion[] }
  }, [])

  const submitResponse = useCallback(
    async (interviewId: number, questionId: number, answer: string, duration: number) => {
      setIsLoading(true)
      setError(null)
      const { data, error: apiError } = await apiClient.submitResponse(interviewId, questionId, answer, duration)

      if (apiError) {
        setError(apiError)
        setIsLoading(false)
        return { success: false, error: apiError }
      }

      setIsLoading(false)
      return { success: true, data }
    },
    [],
  )

  const completeInterview = useCallback(async (interviewId: number) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.completeInterview(interviewId)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const getReport = useCallback(async (interviewId: number) => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.getInterviewReport(interviewId)

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  const listInterviews = useCallback(async () => {
    setIsLoading(true)
    setError(null)
    const { data, error: apiError } = await apiClient.listInterviews()

    if (apiError) {
      setError(apiError)
      setIsLoading(false)
      return { success: false, error: apiError }
    }

    setIsLoading(false)
    return { success: true, data }
  }, [])

  return {
    isLoading,
    error,
    setupInterview,
    getQuestions,
    submitResponse,
    completeInterview,
    getReport,
    listInterviews,
  }
}
