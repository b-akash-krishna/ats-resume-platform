"use client"

import { Link } from "react-router-dom"
import { Menu, X } from "lucide-react"
import { useState } from "react"

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="bg-white shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="text-2xl font-bold text-blue-600">
            ATS Resume Pro
          </Link>

          <div className="hidden md:flex space-x-8">
            <Link to="/" className="text-gray-700 hover:text-blue-600">
              Home
            </Link>
            <Link to="/resume-builder" className="text-gray-700 hover:text-blue-600">
              Resume Builder
            </Link>
            <Link to="/mock-interview" className="text-gray-700 hover:text-blue-600">
              Mock Interview
            </Link>
            <Link to="/dashboard" className="text-gray-700 hover:text-blue-600">
              Dashboard
            </Link>
            <Link to="/login" className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
              Login
            </Link>
          </div>

          <button className="md:hidden" onClick={() => setIsOpen(!isOpen)}>
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {isOpen && (
          <div className="md:hidden pb-4 space-y-2">
            <Link to="/" className="block text-gray-700 hover:text-blue-600 py-2">
              Home
            </Link>
            <Link to="/resume-builder" className="block text-gray-700 hover:text-blue-600 py-2">
              Resume Builder
            </Link>
            <Link to="/mock-interview" className="block text-gray-700 hover:text-blue-600 py-2">
              Mock Interview
            </Link>
            <Link to="/dashboard" className="block text-gray-700 hover:text-blue-600 py-2">
              Dashboard
            </Link>
            <Link to="/login" className="block bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
              Login
            </Link>
          </div>
        )}
      </div>
    </nav>
  )
}
