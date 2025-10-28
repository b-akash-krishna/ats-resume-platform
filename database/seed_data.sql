-- Insert sample users
INSERT INTO users (email, full_name, hashed_password, is_active) VALUES
('john@example.com', 'John Doe', '$2b$12$abcdefghijklmnopqrstuvwxyz', TRUE),
('jane@example.com', 'Jane Smith', '$2b$12$abcdefghijklmnopqrstuvwxyz', TRUE),
('bob@example.com', 'Bob Johnson', '$2b$12$abcdefghijklmnopqrstuvwxyz', TRUE)
ON CONFLICT (email) DO NOTHING;

-- Insert sample resumes
INSERT INTO resumes (user_id, title, full_name, email, phone, summary, skills, ats_score, template_id) VALUES
(1, 'Senior Software Engineer Resume', 'John Doe', 'john@example.com', '555-0001', 
 'Experienced software engineer with 10+ years in full-stack development', 
 '["Python", "JavaScript", "React", "PostgreSQL", "AWS"]', 85.0, 1),
(2, 'Product Manager Resume', 'Jane Smith', 'jane@example.com', '555-0002',
 'Product manager with expertise in SaaS and mobile applications',
 '["Product Strategy", "Agile", "Analytics", "User Research"]', 78.0, 2),
(3, 'Data Scientist Resume', 'Bob Johnson', 'bob@example.com', '555-0003',
 'Data scientist specializing in machine learning and data analysis',
 '["Python", "Machine Learning", "SQL", "TensorFlow", "Tableau"]', 82.0, 1)
ON CONFLICT DO NOTHING;

-- Insert sample interviews
INSERT INTO interviews (user_id, job_title, job_description, difficulty, status) VALUES
(1, 'Senior Software Engineer', 'We are looking for a senior software engineer with 8+ years of experience in full-stack development...', 'hard', 'completed'),
(2, 'Product Manager', 'Join our team as a Product Manager to lead product strategy and development...', 'medium', 'completed'),
(3, 'Data Scientist', 'We seek a Data Scientist to build ML models and drive data-driven insights...', 'medium', 'in_progress')
ON CONFLICT DO NOTHING;

-- Insert sample interview questions
INSERT INTO interview_questions (interview_id, question_number, question, category) VALUES
(1, 1, 'Tell me about your most challenging project', 'behavioral'),
(1, 2, 'How do you approach system design?', 'technical'),
(1, 3, 'Describe your experience with cloud platforms', 'technical'),
(2, 1, 'How do you prioritize features in product development?', 'behavioral'),
(2, 2, 'Tell me about a product failure and what you learned', 'situational'),
(3, 1, 'Explain your approach to feature engineering', 'technical'),
(3, 2, 'How do you handle imbalanced datasets?', 'technical')
ON CONFLICT DO NOTHING;

-- Insert sample interview responses
INSERT INTO interview_responses (interview_id, question_id, answer, duration, score, feedback) VALUES
(1, 1, 'I led a team to build a real-time analytics platform...', 120, 85.0, 'Great technical depth and clear communication'),
(1, 2, 'I follow a systematic approach starting with requirements...', 180, 88.0, 'Excellent understanding of scalability concerns'),
(2, 1, 'I use a framework combining user impact and effort...', 150, 82.0, 'Good prioritization methodology'),
(3, 1, 'I start by understanding the data and domain...', 140, 80.0, 'Solid approach to feature engineering')
ON CONFLICT DO NOTHING;
