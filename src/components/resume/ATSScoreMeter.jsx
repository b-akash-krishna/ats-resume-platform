export default function ATSScoreMeter({ score = 75 }) {
  const getScoreColor = (score) => {
    if (score >= 80) return "text-green-600"
    if (score >= 60) return "text-yellow-600"
    return "text-red-600"
  }

  const getProgressColor = (score) => {
    if (score >= 80) return "bg-green-600"
    if (score >= 60) return "bg-yellow-600"
    return "bg-red-600"
  }

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold mb-4">ATS Score</h3>
      <div className="flex items-center justify-between mb-4">
        <div className={`text-4xl font-bold ${getScoreColor(score)}`}>{score}%</div>
        <div className="text-right">
          <p className="text-sm text-gray-600">ATS Compatibility</p>
          <p className="text-xs text-gray-500">Based on keyword analysis</p>
        </div>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-3">
        <div className={`h-3 rounded-full transition-all ${getProgressColor(score)}`} style={{ width: `${score}%` }} />
      </div>
      <div className="mt-4 space-y-2 text-sm">
        <p className="text-gray-700">
          <span className="font-semibold">Strengths:</span> Good keyword usage
        </p>
        <p className="text-gray-700">
          <span className="font-semibold">Improvements:</span> Add more technical skills
        </p>
      </div>
    </div>
  )
}
