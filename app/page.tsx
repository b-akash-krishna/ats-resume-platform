"use client"

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Navigation */}
      <nav className="bg-white shadow-md">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="text-2xl font-bold text-blue-600">ATS Resume Pro</div>
            <div className="hidden md:flex space-x-8">
              <a href="#" className="text-gray-700 hover:text-blue-600">
                Home
              </a>
              <a href="#" className="text-gray-700 hover:text-blue-600">
                Resume Builder
              </a>
              <a href="#" className="text-gray-700 hover:text-blue-600">
                Mock Interview
              </a>
              <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Login</button>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="bg-gradient-to-r from-blue-600 to-blue-800 text-white py-20">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-5xl font-bold mb-4">ATS Resume Pro</h1>
          <p className="text-xl mb-8">AI-powered resume builder and mock interview platform</p>
          <div className="flex gap-4 justify-center">
            <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">
              Build Resume
            </button>
            <button className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700">
              Practice Interview
            </button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Features</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="mx-auto mb-4 text-blue-600 text-5xl">📄</div>
              <h3 className="text-xl font-semibold mb-2">ATS-Optimized Resumes</h3>
              <p className="text-gray-600">Create resumes that pass ATS systems with AI-powered optimization</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="mx-auto mb-4 text-blue-600 text-5xl">🎤</div>
              <h3 className="text-xl font-semibold mb-2">Mock Interviews</h3>
              <p className="text-gray-600">Practice with AI-generated questions tailored to your target role</p>
            </div>
            <div className="bg-white p-6 rounded-lg shadow-md text-center">
              <div className="mx-auto mb-4 text-blue-600 text-5xl">⚡</div>
              <h3 className="text-xl font-semibold mb-2">Instant Feedback</h3>
              <p className="text-gray-600">Get detailed analysis and improvement suggestions</p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">How It Works</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-blue-600">1</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Upload Your Resume</h3>
              <p className="text-gray-600">Upload your existing resume or start from scratch with our templates</p>
            </div>
            <div className="text-center">
              <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-blue-600">2</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Optimize for ATS</h3>
              <p className="text-gray-600">Get AI-powered suggestions to improve your ATS compatibility score</p>
            </div>
            <div className="text-center">
              <div className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4">
                <span className="text-2xl font-bold text-blue-600">3</span>
              </div>
              <h3 className="text-xl font-semibold mb-2">Practice Interviews</h3>
              <p className="text-gray-600">Practice with AI-generated questions and get detailed feedback</p>
            </div>
          </div>
        </div>
      </section>

      {/* Pricing Section */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Simple Pricing</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-lg shadow-md">
              <h3 className="text-xl font-semibold mb-4">Free</h3>
              <p className="text-3xl font-bold text-blue-600 mb-6">$0</p>
              <ul className="space-y-3 mb-6">
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> 1 Resume
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Basic ATS Analysis
                </li>
                <li className="flex items-center">
                  <span className="text-gray-400 mr-2">✗</span> Mock Interviews
                </li>
              </ul>
              <button className="w-full bg-gray-200 text-gray-800 py-2 rounded hover:bg-gray-300">Get Started</button>
            </div>
            <div className="bg-white p-8 rounded-lg shadow-md border-2 border-blue-600">
              <h3 className="text-xl font-semibold mb-4">Pro</h3>
              <p className="text-3xl font-bold text-blue-600 mb-6">
                $9<span className="text-lg">/mo</span>
              </p>
              <ul className="space-y-3 mb-6">
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Unlimited Resumes
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Advanced ATS Analysis
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> 10 Mock Interviews
                </li>
              </ul>
              <button className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Start Free Trial</button>
            </div>
            <div className="bg-white p-8 rounded-lg shadow-md">
              <h3 className="text-xl font-semibold mb-4">Enterprise</h3>
              <p className="text-3xl font-bold text-blue-600 mb-6">Custom</p>
              <ul className="space-y-3 mb-6">
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Everything in Pro
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Unlimited Interviews
                </li>
                <li className="flex items-center">
                  <span className="text-green-600 mr-2">✓</span> Priority Support
                </li>
              </ul>
              <button className="w-full bg-gray-200 text-gray-800 py-2 rounded hover:bg-gray-300">Contact Sales</button>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 text-white py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl font-bold mb-4">Ready to Land Your Dream Job?</h2>
          <p className="text-xl mb-8">Start building your ATS-optimized resume today</p>
          <button className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100">
            Get Started Free
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <h3 className="text-lg font-bold mb-4">ATS Resume Pro</h3>
              <p className="text-gray-400">AI-powered resume builder and mock interview platform</p>
            </div>
            <div>
              <h4 className="text-lg font-bold mb-4">Product</h4>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <a href="#" className="hover:text-white">
                    Features
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Pricing
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Security
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-bold mb-4">Company</h4>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <a href="#" className="hover:text-white">
                    About
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Blog
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Contact
                  </a>
                </li>
              </ul>
            </div>
            <div>
              <h4 className="text-lg font-bold mb-4">Legal</h4>
              <ul className="space-y-2 text-gray-400">
                <li>
                  <a href="#" className="hover:text-white">
                    Privacy
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Terms
                  </a>
                </li>
                <li>
                  <a href="#" className="hover:text-white">
                    Cookies
                  </a>
                </li>
              </ul>
            </div>
          </div>
          <div className="border-t border-gray-700 pt-8 text-center text-gray-400">
            <p>&copy; 2025 ATS Resume Pro. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}
