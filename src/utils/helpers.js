export const formatDate = (date) => {
  return new Date(date).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  })
}

export const calculateATSScore = (resume, jobDescription) => {
  // TODO: Implement ATS scoring logic
  return Math.floor(Math.random() * 100)
}

export const parseResume = (file) => {
  // TODO: Implement resume parsing logic
  return {}
}
