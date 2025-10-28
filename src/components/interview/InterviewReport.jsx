export default function InterviewReport({ report = {} }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-6">Interview Report</h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div className="bg-blue-50 p-4 rounded-lg">
          <p className="text-gray-600 text-sm">Overall Score</p>
          <p className="text-3xl font-bold text-blue-600">78%</p>
        </div>
        <div className="bg-green-50 p-4 rounded-lg">
          <p className="text-gray-600 text-sm">Communication</p>
          <p className="text-3xl font-bold text-green-600">85%</p>
        </div>
        <div className="bg-yellow-50 p-4 rounded-lg">
          <p className="text-gray-600 text-sm">Technical Knowledge</p>
          <p className="text-3xl font-bold text-yellow-600">72%</p>
        </div>
      </div>

      <div className="space-y-4">
        <div>
          <h3 className="font-semibold text-gray-900 mb-2">Strengths</h3>
          <ul className="list-disc list-inside text-gray-700 space-y-1">
            <li>Clear communication and articulation</li>
            <li>Good problem-solving approach</li>
          </ul>
        </div>

        <div>
          <h3 className="font-semibold text-gray-900 mb-2">Areas for Improvement</h3>
          <ul className="list-disc list-inside text-gray-700 space-y-1">
            <li>Provide more specific examples</li>
            <li>Improve technical depth in explanations</li>
          </ul>
        </div>
      </div>

      <button className="w-full mt-6 bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 font-semibold">
        Download Report
      </button>
    </div>
  )
}
