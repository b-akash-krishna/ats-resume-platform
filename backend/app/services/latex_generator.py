import logging
from typing import Dict, Any
import json

logger = logging.getLogger(__name__)

def generate_pdf_from_template(resume_data: Dict[str, Any], template_id: int = 1) -> str:
    """
    Generate PDF resume from template using LaTeX
    """
    try:
        from pylatex import Document, Section, Subsection, Command, NoEscape
        
        doc = Document()
        
        # Add header with name and contact info
        doc.append(Command('centering'))
        doc.append(Command('Large', NoEscape(r'\textbf{' + resume_data.get('full_name', 'Your Name') + '}')))
        doc.append(Command('normalsize'))
        
        contact_info = f"{resume_data.get('email', '')} | {resume_data.get('phone', '')}"
        doc.append(NoEscape(contact_info))
        
        # Add professional summary
        if resume_data.get('summary'):
            with doc.create(Section('Professional Summary')):
                doc.append(resume_data['summary'])
        
        # Add skills
        if resume_data.get('skills'):
            with doc.create(Section('Skills')):
                skills = resume_data['skills']
                if isinstance(skills, str):
                    skills = json.loads(skills)
                doc.append(', '.join(skills))
        
        # Add experience
        if resume_data.get('experience'):
            with doc.create(Section('Experience')):
                experience = resume_data['experience']
                if isinstance(experience, str):
                    experience = json.loads(experience)
                for exp in experience:
                    with doc.create(Subsection(exp.get('title', ''))):
                        doc.append(exp.get('company', ''))
        
        # Add education
        if resume_data.get('education'):
            with doc.create(Section('Education')):
                education = resume_data['education']
                if isinstance(education, str):
                    education = json.loads(education)
                for edu in education:
                    with doc.create(Subsection(edu.get('degree', ''))):
                        doc.append(edu.get('school', ''))
        
        logger.info(f"Generated PDF resume with template {template_id}")
        return doc.dumps()
    except Exception as e:
        logger.error(f"Error generating PDF: {e}")
        return ""
