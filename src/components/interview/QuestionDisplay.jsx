export default function QuestionDisplay({ questionNumber, totalQuestions, question }) {
  return (
    <div className="bg-blue-50 border-l-4 border-blue-600 p-4 mb-6">
      <div className="flex justify-between items-start">
        <div>
          <p className="text-sm text-gray-600">
            Question {questionNumber} of {totalQuestions}
          </p>
          <h3 className="text-lg font-semibold text-gray-900 mt-1">{question}</h3>
        </div>
        <div className="text-right">
          <p className="text-sm text-gray-600">Time Remaining</p>
          <p className="text-2xl font-bold text-blue-600">2:30</p>
        </div>
      </div>
    </div>
  )
}
