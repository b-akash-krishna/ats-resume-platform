export default function ResumePreview({ data = {} }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-8 max-w-2xl mx-auto">
      <div className="mb-6">
        <h1 className="text-3xl font-bold">{data.fullName || "Your Name"}</h1>
        <p className="text-gray-600">
          {data.email || "email@example.com"} | {data.phone || "(123) 456-7890"}
        </p>
      </div>

      {data.summary && (
        <div className="mb-6">
          <h2 className="text-xl font-semibold border-b-2 border-blue-600 pb-2 mb-3">Professional Summary</h2>
          <p className="text-gray-700">{data.summary}</p>
        </div>
      )}

      {data.experience && data.experience.length > 0 && (
        <div className="mb-6">
          <h2 className="text-xl font-semibold border-b-2 border-blue-600 pb-2 mb-3">Experience</h2>
          {data.experience.map((exp, idx) => (
            <div key={idx} className="mb-4">
              <h3 className="font-semibold">{exp.title}</h3>
              <p className="text-gray-600">{exp.company}</p>
            </div>
          ))}
        </div>
      )}

      {data.skills && data.skills.length > 0 && (
        <div>
          <h2 className="text-xl font-semibold border-b-2 border-blue-600 pb-2 mb-3">Skills</h2>
          <div className="flex flex-wrap gap-2">
            {data.skills.map((skill, idx) => (
              <span key={idx} className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">
                {skill}
              </span>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
