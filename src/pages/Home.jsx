import { Link } from "react-router-dom"
import { FileText, Mic, Zap } from "lucide-react"

export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl font-bold mb-4">ATS Resume Pro</h1>
          <p className="text-xl mb-8">AI-powered resume builder and mock interview platform</p>
          <div className="flex gap-4 justify-center">
            <Link
              to="/resume-builder"
              className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100"
            >
              Build Resume
            </Link>
            <Link
              to="/mock-interview"
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700"
            >
              Practice Interview
            </Link>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <FileText className="mx-auto mb-4 text-blue-600" size={48} />
              <h3 className="text-xl font-semibold mb-2">ATS-Optimized Resumes</h3>
              <p className="text-gray-600">Create resumes that pass ATS systems with AI-powered optimization</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <Mic className="mx-auto mb-4 text-blue-600" size={48} />
              <h3 className="text-xl font-semibold mb-2">Mock Interviews</h3>
              <p className="text-gray-600">Practice with AI-generated questions tailored to your target role</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <Zap className="mx-auto mb-4 text-blue-600" size={48} />
              <h3 className="text-xl font-semibold mb-2">Instant Feedback</h3>
              <p className="text-gray-600">Get detailed analysis and improvement suggestions</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Land Your Dream Job?</h2>
          <p className="text-xl mb-8">Start building your ATS-optimized resume today</p>
          <Link
            to="/resume-builder"
            className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 inline-block"
          >
            Get Started
          </Link>
        </div>
      </section>
    </div>
  )
}
