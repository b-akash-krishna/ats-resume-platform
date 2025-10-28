"use client"

import { useState, useCallback, useEffect } from "react"
import { apiClient } from "@/lib/api"

interface User {
  id: number
  email: string
  full_name: string
  is_active: boolean
}

interface AuthState {
  user: User | null
  isLoading: boolean
  error: string | null
  isAuthenticated: boolean
}

export function useAuth() {
  const [state, setState] = useState<AuthState>({
    user: null,
    isLoading: false,
    error: null,
    isAuthenticated: false,
  })

  // Check if user is already logged in
  useEffect(() => {
    const checkAuth = async () => {
      if (apiClient.getToken()) {
        setState((prev) => ({ ...prev, isLoading: true }))
        const { data, error } = await apiClient.getCurrentUser()
        if (data) {
          setState({
            user: data as User,
            isLoading: false,
            error: null,
            isAuthenticated: true,
          })
        } else {
          setState({
            user: null,
            isLoading: false,
            error: null,
            isAuthenticated: false,
          })
          apiClient.clearToken()
        }
      }
    }

    checkAuth()
  }, [])

  const signup = useCallback(async (email: string, password: string, fullName: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }))
    const { data, error } = await apiClient.signup(email, password, fullName)

    if (error) {
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error,
        isAuthenticated: false,
      }))
      return { success: false, error }
    }

    if (data) {
      apiClient.setToken(data.access_token)
      setState({
        user: {
          id: data.user_id,
          email: data.email,
          full_name: data.full_name,
          is_active: true,
        },
        isLoading: false,
        error: null,
        isAuthenticated: true,
      })
      return { success: true }
    }
  }, [])

  const login = useCallback(async (email: string, password: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }))
    const { data, error } = await apiClient.login(email, password)

    if (error) {
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error,
        isAuthenticated: false,
      }))
      return { success: false, error }
    }

    if (data) {
      apiClient.setToken(data.access_token)
      setState({
        user: {
          id: data.user_id,
          email: data.email,
          full_name: data.full_name,
          is_active: true,
        },
        isLoading: false,
        error: null,
        isAuthenticated: true,
      })
      return { success: true }
    }
  }, [])

  const logout = useCallback(async () => {
    await apiClient.logout()
    setState({
      user: null,
      isLoading: false,
      error: null,
      isAuthenticated: false,
    })
  }, [])

  return {
    ...state,
    signup,
    login,
    logout,
  }
}
