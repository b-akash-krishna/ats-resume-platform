"use client"

import { useEffect } from "react"
import { X } from "lucide-react"

export default function Toast({ message, type = "info", onClose }) {
  useEffect(() => {
    const timer = setTimeout(onClose, 3000)
    return () => clearTimeout(timer)
  }, [onClose])

  const bgColor = {
    success: "bg-green-500",
    error: "bg-red-500",
    info: "bg-blue-500",
    warning: "bg-yellow-500",
  }[type]

  return (
    <div className={`${bgColor} text-white px-6 py-4 rounded shadow-lg flex justify-between items-center`}>
      <span>{message}</span>
      <button onClick={onClose} className="ml-4">
        <X size={20} />
      </button>
    </div>
  )
}
