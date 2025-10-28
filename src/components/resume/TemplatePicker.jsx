"use client"

export default function TemplatePicker({ onSelect }) {
  const templates = [
    { id: 1, name: "Professional", description: "Clean and professional design" },
    { id: 2, name: "Modern", description: "Contemporary layout with accent colors" },
    { id: 3, name: "Minimal", description: "Simple and elegant design" },
  ]

  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      <h3 className="text-lg font-semibold mb-4">Choose a Template</h3>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {templates.map((template) => (
          <div
            key={template.id}
            onClick={() => onSelect(template.id)}
            className="border-2 border-gray-300 rounded-lg p-4 cursor-pointer hover:border-blue-600 hover:bg-blue-50 transition"
          >
            <div className="bg-gray-200 h-40 rounded mb-3"></div>
            <h4 className="font-semibold">{template.name}</h4>
            <p className="text-sm text-gray-600">{template.description}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
