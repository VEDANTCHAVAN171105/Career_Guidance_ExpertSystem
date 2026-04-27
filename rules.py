# rules.py
class CareerExpertSystem:
    def __init__(self):
        self.rules = [
            {
                'name': 'Software Developer',
                'conditions': {
                    'interests': ['coding', 'programming'],
                    'cgpa_min': 7.0,
                    'skills': ['programming', 'problem_solving'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'team']
                },
                'confidence': 0.0,
                'description': 'Design, develop, and maintain software applications',
                'skills_roadmap': [
                    'Learn Python/Java/JavaScript',
                    'Master Data Structures & Algorithms',
                    'Learn Version Control (Git)',
                    'Build projects and contribute to open source',
                    'Learn frameworks (React/Django/Spring)'
                ]
            },
            {
                'name': 'Data Scientist',
                'conditions': {
                    'interests': ['data', 'analytics', 'statistics'],
                    'cgpa_min': 7.5,
                    'skills': ['analytics', 'programming', 'mathematics'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent']
                },
                'confidence': 0.0,
                'description': 'Analyze complex data to help organizations make decisions',
                'skills_roadmap': [
                    'Learn Python and SQL',
                    'Master Statistics and Probability',
                    'Learn Pandas, NumPy, Matplotlib',
                    'Study Machine Learning (Scikit-learn)',
                    'Learn Data Visualization (Tableau/PowerBI)'
                ]
            },
            {
                'name': 'Product Manager',
                'conditions': {
                    'interests': ['management', 'business', 'strategy'],
                    'cgpa_min': 7.0,
                    'skills': ['communication', 'leadership', 'analytics'],
                    'personality': ['extrovert', 'ambivert'],
                    'work_style': ['team']
                },
                'confidence': 0.0,
                'description': 'Lead product development from concept to launch',
                'skills_roadmap': [
                    'Learn Agile/Scrum methodologies',
                    'Develop market research skills',
                    'Learn product analytics tools',
                    'Improve stakeholder management',
                    'Study UX fundamentals'
                ]
            },
            {
                'name': 'UX/UI Designer',
                'conditions': {
                    'interests': ['design', 'art', 'creativity'],
                    'cgpa_min': 6.5,
                    'skills': ['creativity', 'communication', 'design'],
                    'personality': ['ambivert', 'extrovert'],
                    'work_style': ['team', 'independent']
                },
                'confidence': 0.0,
                'description': 'Create intuitive and beautiful user experiences',
                'skills_roadmap': [
                    'Learn Figma/Adobe XD',
                    'Study Color Theory and Typography',
                    'Learn User Research methods',
                    'Master Prototyping',
                    'Learn HTML/CSS basics'
                ]
            },
            {
                'name': 'Cybersecurity Analyst',
                'conditions': {
                    'interests': ['security', 'hacking', 'networks'],
                    'cgpa_min': 7.0,
                    'skills': ['programming', 'analytics', 'problem_solving'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent']
                },
                'confidence': 0.0,
                'description': 'Protect organizations from cyber threats',
                'skills_roadmap': [
                    'Learn Networking fundamentals',
                    'Master Linux and command line',
                    'Learn Python for security',
                    'Study Cryptography',
                    'Get Security+ certification'
                ]
            },
            {
                'name': 'Cloud Architect',
                'conditions': {
                    'interests': ['cloud', 'devops', 'infrastructure'],
                    'cgpa_min': 7.0,
                    'skills': ['programming', 'problem_solving', 'analytics'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'team']
                },
                'confidence': 0.0,
                'description': 'Design and manage cloud infrastructure',
                'skills_roadmap': [
                    'Learn AWS/Azure/GCP basics',
                    'Master Docker and Kubernetes',
                    'Learn Infrastructure as Code (Terraform)',
                    'Study CI/CD pipelines',
                    'Learn Linux system administration'
                ]
            },
            {
                'name': 'Marketing Specialist',
                'conditions': {
                    'interests': ['marketing', 'social_media', 'branding'],
                    'cgpa_min': 6.0,
                    'skills': ['communication', 'creativity', 'analytics'],
                    'personality': ['extrovert', 'ambivert'],
                    'work_style': ['team']
                },
                'confidence': 0.0,
                'description': 'Develop and execute marketing strategies',
                'skills_roadmap': [
                    'Learn Digital Marketing fundamentals',
                    'Master SEO/SEM',
                    'Learn Google Analytics',
                    'Study Social Media Marketing',
                    'Learn Content Creation'
                ]
            },
            {
                'name': 'Business Analyst',
                'conditions': {
                    'interests': ['business', 'analytics', 'strategy'],
                    'cgpa_min': 6.5,
                    'skills': ['analytics', 'communication', 'problem_solving'],
                    'personality': ['ambivert'],
                    'work_style': ['team']
                },
                'confidence': 0.0,
                'description': 'Bridge business needs with technical solutions',
                'skills_roadmap': [
                    'Learn SQL and Excel',
                    'Master Data Visualization',
                    'Learn Business Process Modeling',
                    'Study Requirements Gathering',
                    'Learn Agile methodologies'
                ]
            }
        ]
    
    def calculate_confidence(self, rule, interests, cgpa, skills, personality, work_style):
        confidence = 0.0
        weights = {
            'interests': 0.35,
            'cgpa': 0.20,
            'skills': 0.25,
            'personality': 0.10,
            'work_style': 0.10
        }
        
        # Check interests match
        interest_match = any(i in rule['conditions']['interests'] for i in interests)
        if interest_match:
            confidence += weights['interests']
        
        # Check CGPA
        if cgpa >= rule['conditions']['cgpa_min']:
            cgpa_score = min(1.0, (cgpa - rule['conditions']['cgpa_min']) / 3.0 + 0.5)
            confidence += weights['cgpa'] * cgpa_score
        else:
            confidence += weights['cgpa'] * (cgpa / rule['conditions']['cgpa_min']) * 0.5
        
        # Check skills match
        skill_match_count = sum(1 for s in skills if s in rule['conditions']['skills'])
        skill_score = skill_match_count / len(rule['conditions']['skills']) if rule['conditions']['skills'] else 0
        confidence += weights['skills'] * skill_score
        
        # Check personality match
        if personality.lower() in rule['conditions']['personality']:
            confidence += weights['personality']
        
        # Check work style match
        if work_style.lower() in rule['conditions']['work_style']:
            confidence += weights['work_style']
        
        return round(confidence, 2)
    
    def predict(self, interests, cgpa, skills, personality, work_style):
        results = []
        
        for rule in self.rules:
            confidence = self.calculate_confidence(rule, interests, cgpa, skills, personality, work_style)
            if confidence > 0.3:  # Only include if confidence > 30%
                results.append({
                    'career': rule['name'],
                    'confidence': confidence,
                    'confidence_percent': int(confidence * 100),
                    'description': rule['description'],
                    'skills_roadmap': rule['skills_roadmap']
                })
        
        # Sort by confidence descending and take top 3
        results.sort(key=lambda x: x['confidence'], reverse=True)
        top_results = results[:3]
        
        # Generate explanation for top career
        if top_results:
            explanation = self.generate_explanation(top_results[0]['career'], interests, skills, personality)
        else:
            explanation = "Based on your profile, we recommend exploring general career paths and developing foundational skills."
        
        return {
            'recommendations': top_results,
            'explanation': explanation
        }
    
    def generate_explanation(self, career, interests, skills, personality):
        career_lower = career.lower()
        if 'developer' in career_lower:
            return f"You are suggested {career} because you have strong interest in coding and programming. Your analytical and problem-solving skills align well with software development requirements. This career offers excellent growth opportunities and creative problem-solving."
        elif 'data' in career_lower:
            return f"You are suggested {career} because you enjoy working with data and analytics. Your mathematical and analytical skills make you well-suited for extracting insights from complex datasets. This field combines technical skills with business impact."
        elif 'manager' in career_lower:
            return f"You are suggested {career} because you have strong leadership and communication abilities. Your interest in management and strategy aligns with product leadership roles. This career lets you drive product vision and team success."
        elif 'designer' in career_lower:
            return f"You are suggested {career} because you have a creative mindset and eye for design. Your interest in creating beautiful and functional experiences makes UX/UI design a perfect fit. This role combines art with user psychology."
        elif 'security' in career_lower or 'cyber' in career_lower:
            return f"You are suggested {career} because you have strong analytical skills and interest in security. Your problem-solving abilities are crucial for identifying and mitigating cyber threats. This field offers challenging and impactful work."
        elif 'cloud' in career_lower:
            return f"You are suggested {career} because you have technical aptitude and interest in infrastructure. Your skills in programming and system design align with cloud architecture. This role is critical for modern organizations."
        elif 'marketing' in career_lower:
            return f"You are suggested {career} because you have excellent communication skills and creativity. Your outgoing personality and interest in branding make marketing a natural fit. This career lets you shape brand perception and drive growth."
        elif 'business' in career_lower:
            return f"You are suggested {career} because you have strong analytical and communication skills. Your ability to bridge business and technical concepts is valuable for this role. Business analysis offers diverse opportunities across industries."
        else:
            return f"You are suggested {career} based on your unique combination of interests in {', '.join(interests[:2])}, skills in {', '.join(skills[:2])}, and {personality} personality type."