# expert_system.py
class CareerExpertSystem:
    def __init__(self):
        self.careers = {
            'software_developer': {
                'name': 'Software Developer',
                'icon': '💻',
                'description': 'Design, develop, and maintain software applications that power the digital world.',
                'salary_range': '₹6-25 LPA',
                'demand': 'Very High',
                'work_env': 'Tech companies, startups, IT firms',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['coding', 'programming', 'technology'],
                    'skills': ['programming', 'problem_solving', 'logical_thinking'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Learn basic programming with Scratch/Python',
                        'Participate in coding competitions',
                        'Study mathematics and logic',
                        'Explore computer science fundamentals'
                    ],
                    '12th': [
                        'Master Python/Java programming',
                        'Learn Data Structures & Algorithms',
                        'Build projects (websites, apps)',
                        'Learn Git & GitHub',
                        'Study database concepts',
                        'Prepare for coding interviews'
                    ]
                },
                'weight': 1.0
            },
            'data_scientist': {
                'name': 'Data Scientist',
                'icon': '📊',
                'description': 'Analyze complex data to help organizations make better decisions.',
                'salary_range': '₹8-30 LPA',
                'demand': 'Very High',
                'work_env': 'Tech companies, research labs, finance',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['data', 'analytics', 'statistics', 'mathematics'],
                    'skills': ['analytics', 'mathematics', 'problem_solving', 'programming'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Build strong foundation in mathematics',
                        'Learn statistics basics',
                        'Practice data interpretation',
                        'Learn Excel and data visualization'
                    ],
                    '12th': [
                        'Learn Python programming',
                        'Master Statistics & Probability',
                        'Learn Pandas, NumPy, Matplotlib',
                        'Study Machine Learning basics',
                        'Learn SQL for data querying',
                        'Build data analysis projects'
                    ]
                },
                'weight': 0.95
            },
            'product_manager': {
                'name': 'Product Manager',
                'icon': '🎯',
                'description': 'Lead product strategy, development, and launch from concept to market.',
                'salary_range': '₹12-35 LPA',
                'demand': 'High',
                'work_env': 'Tech companies, product-based firms',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['management', 'business', 'strategy', 'leadership'],
                    'skills': ['communication', 'leadership', 'analytics', 'problem_solving'],
                    'personality': ['extrovert', 'ambivert'],
                    'work_style': ['team', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Develop leadership skills in school projects',
                        'Practice public speaking',
                        'Learn basic business concepts',
                        'Participate in group activities'
                    ],
                    '12th': [
                        'Pursue BBA/BTech degree',
                        'Learn Agile & Scrum methodologies',
                        'Develop market research skills',
                        'Learn product analytics tools',
                        'Build communication & negotiation skills',
                        'Study UX fundamentals'
                    ]
                },
                'weight': 0.9
            },
            'ux_designer': {
                'name': 'UX/UI Designer',
                'icon': '🎨',
                'description': 'Create intuitive, beautiful, and user-friendly digital experiences.',
                'salary_range': '₹5-20 LPA',
                'demand': 'High',
                'work_env': 'Design agencies, tech companies',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['design', 'art', 'creativity', 'user_experience'],
                    'skills': ['creativity', 'design', 'communication', 'problem_solving'],
                    'personality': ['ambivert', 'extrovert'],
                    'work_style': ['team', 'independent']
                },
                'roadmap': {
                    '10th': [
                        'Practice digital art and design',
                        'Learn color theory and typography',
                        'Study user behavior basics',
                        'Create simple website mockups'
                    ],
                    '12th': [
                        'Master Figma/Adobe XD',
                        'Learn User Research methods',
                        'Study Interaction Design',
                        'Build a design portfolio',
                        'Learn HTML/CSS basics',
                        'Understand accessibility principles'
                    ]
                },
                'weight': 0.85
            },
            'cybersecurity_analyst': {
                'name': 'Cybersecurity Analyst',
                'icon': '🔒',
                'description': 'Protect organizations from cyber threats and security breaches.',
                'salary_range': '₹6-22 LPA',
                'demand': 'Very High',
                'work_env': 'Security firms, IT companies, banks',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['security', 'hacking', 'networks', 'technology'],
                    'skills': ['programming', 'problem_solving', 'analytics', 'logical_thinking'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'team']
                },
                'roadmap': {
                    '10th': [
                        'Learn computer networking basics',
                        'Understand cybersecurity fundamentals',
                        'Practice safe computing habits',
                        'Learn Linux basics'
                    ],
                    '12th': [
                        'Master Networking concepts',
                        'Learn Python for security',
                        'Study Cryptography basics',
                        'Get Security+ certification',
                        'Learn ethical hacking',
                        'Practice on CTF platforms'
                    ]
                },
                'weight': 0.88
            },
            'cloud_architect': {
                'name': 'Cloud Architect',
                'icon': '☁️',
                'description': 'Design and manage cloud infrastructure for modern applications.',
                'salary_range': '₹10-32 LPA',
                'demand': 'Very High',
                'work_env': 'Tech companies, cloud providers',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['cloud', 'devops', 'infrastructure', 'technology'],
                    'skills': ['programming', 'problem_solving', 'analytics', 'logical_thinking'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'team']
                },
                'roadmap': {
                    '10th': [
                        'Learn basic server concepts',
                        'Understand how internet works',
                        'Practice Linux commands',
                        'Learn about virtualization'
                    ],
                    '12th': [
                        'Master Linux administration',
                        'Learn AWS/Azure fundamentals',
                        'Study Docker & Kubernetes',
                        'Learn Infrastructure as Code',
                        'Understand CI/CD pipelines',
                        'Get cloud certifications'
                    ]
                },
                'weight': 0.87
            },
            'marketing_specialist': {
                'name': 'Marketing Specialist',
                'icon': '📢',
                'description': 'Develop and execute marketing strategies to grow brands and businesses.',
                'salary_range': '₹4-15 LPA',
                'demand': 'High',
                'work_env': 'Marketing agencies, corporate firms',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['marketing', 'social_media', 'branding', 'business'],
                    'skills': ['communication', 'creativity', 'analytics', 'leadership'],
                    'personality': ['extrovert', 'ambivert'],
                    'work_style': ['team', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Learn digital marketing basics',
                        'Practice content creation',
                        'Study social media trends',
                        'Develop communication skills'
                    ],
                    '12th': [
                        'Master SEO/SEM techniques',
                        'Learn Google Analytics',
                        'Study social media marketing',
                        'Learn email marketing',
                        'Understand brand strategy',
                        'Build a personal brand'
                    ]
                },
                'weight': 0.82
            },
            'business_analyst': {
                'name': 'Business Analyst',
                'icon': '📈',
                'description': 'Bridge business needs with technical solutions to improve processes.',
                'salary_range': '₹6-18 LPA',
                'demand': 'High',
                'work_env': 'Consulting firms, IT companies',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['business', 'analytics', 'strategy', 'management'],
                    'skills': ['analytics', 'communication', 'problem_solving', 'leadership'],
                    'personality': ['ambivert'],
                    'work_style': ['team', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Learn business fundamentals',
                        'Practice data interpretation',
                        'Develop problem-solving skills',
                        'Study basic economics'
                    ],
                    '12th': [
                        'Master SQL and Excel',
                        'Learn data visualization',
                        'Study business process modeling',
                        'Learn requirements gathering',
                        'Understand Agile methodologies',
                        'Get CBAP certification'
                    ]
                },
                'weight': 0.83
            },
            'ai_ml_engineer': {
                'name': 'AI/ML Engineer',
                'icon': '🤖',
                'description': 'Build intelligent systems that learn from data and make predictions.',
                'salary_range': '₹10-40 LPA',
                'demand': 'Very High',
                'work_env': 'Tech companies, research labs',
                'conditions': {
                    'education': ['10th', '12th'],
                    'interests': ['coding', 'data', 'analytics', 'statistics', 'technology'],
                    'skills': ['programming', 'mathematics', 'analytics', 'problem_solving'],
                    'personality': ['introvert', 'ambivert'],
                    'work_style': ['independent', 'hybrid']
                },
                'roadmap': {
                    '10th': [
                        'Learn Python basics',
                        'Study mathematics and statistics',
                        'Explore basic AI concepts',
                        'Practice logical reasoning'
                    ],
                    '12th': [
                        'Master Python programming',
                        'Learn Linear Algebra & Calculus',
                        'Study Machine Learning algorithms',
                        'Learn Deep Learning (TensorFlow/PyTorch)',
                        'Build AI projects',
                        'Participate in Kaggle competitions'
                    ]
                },
                'weight': 0.92
            }
        }
    
    def calculate_match_score(self, career_key, career_data, interests, skills, personality, work_style):
        score = 0
        total_weight = 0
        
        # Interest matching (40% weight)
        interest_match = 0
        user_interests_lower = [i.lower() for i in interests]
        career_interests = career_data['conditions']['interests']
        
        for interest in user_interests_lower:
            if any(ci in interest or interest in ci for ci in career_interests):
                interest_match += 1
        
        interest_score = min(1.0, interest_match / max(1, len(career_interests))) * 40
        score += interest_score
        total_weight += 40
        
        # Skill matching (35% weight)
        skill_match = 0
        user_skills_lower = [s.lower() for s in skills]
        career_skills = career_data['conditions']['skills']
        
        for skill in user_skills_lower:
            if any(cs in skill or skill in cs for cs in career_skills):
                skill_match += 1
        
        skill_score = min(1.0, skill_match / max(1, len(career_skills))) * 35
        score += skill_score
        total_weight += 35
        
        # Personality matching (15% weight)
        if personality.lower() in career_data['conditions']['personality']:
            score += 15
        total_weight += 15
        
        # Work style matching (10% weight)
        if work_style.lower() in career_data['conditions']['work_style']:
            score += 10
        total_weight += 10
        
        # Calculate final percentage
        final_percentage = (score / total_weight) * 100 if total_weight > 0 else 0
        return round(final_percentage, 1)
    
    def predict(self, education_level, interests, skills, personality, work_style):
        results = []
        
        for career_key, career_data in self.careers.items():
            # Check if career is available for education level
            if education_level not in career_data['conditions']['education']:
                continue
            
            match_score = self.calculate_match_score(
                career_key, career_data, interests, skills, personality, work_style
            )
            
            # Get appropriate roadmap based on education level
            roadmap = career_data['roadmap'].get(education_level, career_data['roadmap']['12th'])
            
            results.append({
                'career': career_data['name'],
                'icon': career_data['icon'],
                'confidence': match_score,
                'confidence_percent': int(match_score),
                'description': career_data['description'],
                'salary_range': career_data['salary_range'],
                'demand': career_data['demand'],
                'work_env': career_data['work_env'],
                'skills_roadmap': roadmap
            })
        
        # Sort by confidence and get top 3
        results.sort(key=lambda x: x['confidence'], reverse=True)
        top_results = results[:3]
        
        # Generate explanation for top career
        if top_results:
            explanation = self.generate_explanation(
                top_results[0]['career'], 
                interests, 
                skills, 
                personality,
                education_level
            )
        else:
            explanation = "Based on your profile, we recommend exploring careers in technology and business. Focus on developing foundational skills in communication, problem-solving, and technical areas."
        
        return {
            'recommendations': top_results,
            'explanation': explanation
        }
    
    def generate_explanation(self, career, interests, skills, personality, education_level):
        career_lower = career.lower()
        
        templates = {
            'software': f"🎯 You are strongly recommended to pursue {career} because your interest in {', '.join(interests[:2])} and skills in {', '.join(skills[:2])} align perfectly with this field. As a {personality} person, you'll thrive in the {career} work environment. With your {education_level} background, you have a solid foundation to start this journey.",
            
            'data': f"📊 {career} is an excellent match for you! Your analytical mindset and interest in {', '.join(interests[:2])} are crucial for success in data science. Your {', '.join(skills[:2])} skills will help you excel. Being {personality} is common among successful data professionals.",
            
            'product': f"🚀 {career} suits you well! Your leadership qualities and interest in {', '.join(interests[:2])} make you a natural product leader. Your strong {', '.join(skills[:2])} abilities will help you excel in this role. Your {personality} personality is great for product management.",
            
            'design': f"🎨 {career} is perfect for you! Your creative spirit and interest in {', '.join(interests[:2])} are exactly what design roles need. Your {', '.join(skills[:2])} skills will help you create amazing user experiences. As a {personality}, you'll connect well with users.",
            
            'security': f"🔒 {career} matches your profile excellently! Your analytical mind and interest in {', '.join(interests[:2])} are critical for cybersecurity. Your problem-solving skills and {personality} nature will help you succeed in protecting digital assets.",
            
            'cloud': f"☁️ {career} is a great fit! Your technical aptitude and interest in {', '.join(interests[:2])} align with cloud computing demands. Your {', '.join(skills[:2])} skills will help you master cloud technologies. Being {personality} works well for system architecture.",
            
            'marketing': f"📢 {career} suits you perfectly! Your creative communication skills and interest in {', '.join(interests[:2])} are essential for marketing. Your {personality} personality will help you connect with audiences effectively.",
            
            'business': f"📈 {career} matches your profile well! Your analytical and communication skills combined with interest in {', '.join(interests[:2])} make you ideal for business analysis. Your {personality} nature will help you bridge business and technical teams.",
            
            'ai_ml': f"🤖 {career} is an outstanding match! Your technical interests in {', '.join(interests[:2])} and skills in {', '.join(skills[:2])} are perfect for AI/ML. Your {personality} analytical nature will help you excel in this cutting-edge field."
        }
        
        # Find matching template
        for key, template in templates.items():
            if key in career_lower:
                return template
        
        # Default template
        return f"💼 {career} is recommended for you based on your interests in {', '.join(interests[:2])}, skills in {', '.join(skills[:2])}, and {personality} personality type. Your {education_level} background provides a good starting point for this career path."