# chatbot.py
import random
import re

class CareerChatbot:
    def __init__(self):
        self.context = {}
        self.intents = {
            'greeting': {
                'patterns': [
                    r'hi|hello|hey|greetings|good morning|good afternoon|good evening|namaste|hola',
                    r'^hey there$|^hello there$'
                ],
                'responses': [
                    "👋 Hello! I'm your Career Guide Assistant. How can I help you explore careers today?",
                    "🌟 Hi there! Ready to discover your dream career? I'm here to help!",
                    "🎯 Hello! I can help you with career guidance, skill development, and job market insights. What would you like to know?",
                    "💫 Greetings! Ask me about any career, skill requirements, or take our assessment for personalized recommendations!"
                ]
            },
            'career_info': {
                'patterns': [
                    r'tell me about (.*)',
                    r'what is (.*)',
                    r'explain (.*)',
                    r'information about (.*)',
                    r'about (.*) career'
                ],
                'responses': {}
            },
            'best_career': {
                'patterns': [
                    r'which career is best for me',
                    r'best career for me',
                    r'what career should i choose',
                    r'recommend career for me',
                    r'suggest career'
                ],
                'responses': [
                    "🎯 To find the best career for you, please click the 'Start Assessment' button on our home page. Our expert system will analyze your interests, skills, personality, and provide personalized recommendations with confidence scores!",
                    "📊 Great question! Take our comprehensive career assessment to get data-driven recommendations. Click 'Assessment' in the navigation menu to begin your journey!",
                    "💡 I'd love to help! The best career depends on your unique profile. Please fill out our assessment form - it considers 10+ career paths and provides detailed roadmaps!"
                ]
            },
            'skills_for_career': {
                'patterns': [
                    r'what skills (?:are needed|required|should i learn) for (.*)',
                    r'skills required for (.*)',
                    r'how to become (.*)',
                    r'path to become (.*)'
                ],
                'responses': {}
            },
            'salary_info': {
                'patterns': [
                    r'salary of (.*)',
                    r'how much does (.*) earn',
                    r'(.*) salary',
                    r'pay for (.*)'
                ],
                'responses': {}
            },
            'demand_info': {
                'patterns': [
                    r'is (.*) in demand',
                    r'demand for (.*)',
                    r'job market for (.*)',
                    r'future of (.*)'
                ],
                'responses': {}
            },
            'thank_you': {
                'patterns': [
                    r'thank you|thanks|appreciate it|helpful|great help'
                ],
                'responses': [
                    "🌟 You're very welcome! I'm glad I could help. Feel free to ask more questions about your career journey!",
                    "💪 Happy to help! Remember, your career success starts with the right guidance. Take our assessment for personalized recommendations!",
                    "🎉 My pleasure! Best of luck on your career path. Come back anytime you need guidance!"
                ]
            },
            'help': {
                'patterns': [
                    r'help|what can you do|capabilities|features|how to use'
                ],
                'responses': [
                    "🤖 I can help you with:\n\n📌 Career information (ask 'Tell me about Data Scientist')\n📌 Skill requirements ('What skills for AI Engineer?')\n📌 Salary insights ('Salary of Product Manager')\n📌 Job demand ('Is Cloud Architect in demand?')\n📌 Career assessment guidance\n\nTry asking me anything about careers!",
                    "💡 My capabilities include:\n\n• Detailed career descriptions\n• Skill roadmaps for any career\n• Salary ranges and job demand\n• Industry insights\n• Education path guidance\n\nWhat would you like to explore?"
                ]
            },
            'education_path': {
                'patterns': [
                    r'education required for (.*)',
                    r'degree for (.*)',
                    r'how to study (.*)',
                    r'qualification for (.*)'
                ],
                'responses': {}
            },
            'greeting_response': {
                'patterns': [
                    r'how are you|how do you do|what\'s up'
                ],
                'responses': [
                    "🌟 I'm doing great! Ready to help you explore exciting career opportunities. How can I assist you today?",
                    "💫 I'm functioning perfectly! Your career guide assistant is here to help. What career questions do you have?"
                ]
            },
            'assessment_help': {
                'patterns': [
                    r'how to take assessment|assessment process|how does expert system work'
                ],
                'responses': [
                    "📝 Our expert system works like this:\n\n1. You answer questions about interests, skills, personality, and work style\n2. Our AI matches your profile against 10+ career paths\n3. We calculate match percentages for each career\n4. You get top 3 recommendations with detailed roadmaps\n\nClick 'Assessment' in the menu to start!",
                    "🎯 The assessment process:\n\n• Select your education level (10th/12th)\n• Choose your interests and skills\n• Pick personality type and work style\n• Get instant personalized recommendations with confidence scores!\n\nReady to begin? Click the Assessment button!"
                ]
            },
            'farewell': {
                'patterns': [
                    r'bye|goodbye|see you later|exit|quit'
                ],
                'responses': [
                    "👋 Goodbye! Best wishes for your career journey. Come back anytime for guidance!",
                    "🌟 Farewell! Remember, the best time to plan your career is now. Take care!",
                    "💫 See you later! Feel free to return whenever you need career advice."
                ]
            }
        }
        
        # Career-specific responses database
        self.career_database = {
            'software developer': {
                'description': 'Software developers design, code, and maintain applications that power our digital world.',
                'skills': 'Python, Java, JavaScript, Data Structures, Algorithms, Git, Databases',
                'salary': '₹6-25 LPA (entry to senior level)',
                'demand': 'Very High - 22% growth expected',
                'education': "Bachelor's in CS/IT or related field",
                'roadmap': 'Learn programming → Master DSA → Build projects → Learn frameworks → Apply for internships'
            },
            'data scientist': {
                'description': 'Data scientists analyze complex data to help organizations make better decisions.',
                'skills': 'Python, SQL, Statistics, Machine Learning, Data Visualization',
                'salary': '₹8-30 LPA',
                'demand': 'Very High - 35% growth expected',
                'education': "Bachelor's/Master's in Statistics/Maths/CS",
                'roadmap': 'Learn Python → Master Statistics → Learn ML → Build projects → Kaggle competitions'
            },
            'product manager': {
                'description': 'Product managers lead product strategy, development, and launch.',
                'skills': 'Communication, Leadership, Analytics, Agile, Market Research',
                'salary': '₹12-35 LPA',
                'demand': 'High - 15% growth expected',
                'education': "MBA or Bachelor's with experience",
                'roadmap': 'Learn business → Develop tech knowledge → Build leadership → Get certified (PMP/Agile)'
            },
            'ux designer': {
                'description': 'UX/UI designers create intuitive and beautiful user experiences.',
                'skills': 'Figma, Adobe XD, User Research, Prototyping, Visual Design',
                'salary': '₹5-20 LPA',
                'demand': 'High - 18% growth expected',
                'education': "Bachelor's in Design or related",
                'roadmap': 'Learn design tools → Study UX principles → Build portfolio → Internships'
            },
            'cybersecurity analyst': {
                'description': 'Cybersecurity analysts protect organizations from cyber threats.',
                'skills': 'Networking, Linux, Python, Security tools, Cryptography',
                'salary': '₹6-22 LPA',
                'demand': 'Very High - 31% growth expected',
                'education': "Bachelor's in CS/Cybersecurity",
                'roadmap': 'Learn networking → Master Linux → Learn security tools → Get certified (Security+)'
            },
            'cloud architect': {
                'description': 'Cloud architects design and manage cloud infrastructure.',
                'skills': 'AWS/Azure, Docker, Kubernetes, Linux, DevOps',
                'salary': '₹10-32 LPA',
                'demand': 'Very High - 25% growth expected',
                'education': "Bachelor's in CS/IT",
                'roadmap': 'Learn Linux → Master cloud platforms → Learn containers → Get cloud certifications'
            },
            'marketing specialist': {
                'description': 'Marketing specialists develop and execute marketing strategies.',
                'skills': 'SEO/SEM, Social Media, Analytics, Content Creation, Branding',
                'salary': '₹4-15 LPA',
                'demand': 'High - 10% growth expected',
                'education': "Bachelor's in Marketing/Business",
                'roadmap': 'Learn digital marketing → Master SEO → Learn analytics → Build portfolio'
            },
            'business analyst': {
                'description': 'Business analysts bridge business needs with technical solutions.',
                'skills': 'SQL, Excel, Data Analysis, Requirements Gathering, Agile',
                'salary': '₹6-18 LPA',
                'demand': 'High - 14% growth expected',
                'education': "Bachelor's in Business/CS",
                'roadmap': 'Learn SQL/Excel → Study business processes → Learn Agile → Get CBAP certified'
            },
            'ai engineer': {
                'description': 'AI engineers build intelligent systems using machine learning.',
                'skills': 'Python, TensorFlow, PyTorch, ML Algorithms, Deep Learning',
                'salary': '₹10-40 LPA',
                'demand': 'Very High - 40% growth expected',
                'education': "Master's in AI/ML or related",
                'roadmap': 'Master Python → Learn ML algorithms → Study Deep Learning → Build AI projects'
            }
        }
    
    def extract_career(self, text):
        """Extract career name from user message"""
        text = text.lower()
        for career in self.career_database.keys():
            if career in text:
                return career
        return None
    
    def get_response(self, message):
        message = message.lower().strip()
        
        # Check for career-specific queries
        career = self.extract_career(message)
        
        if 'skills' in message and career:
            career_data = self.career_database.get(career, {})
            skills = career_data.get('skills', 'Various technical and soft skills')
            return f"📚 To become a {career.title()}, you should learn:\n\n{skills}\n\nStart with the basics and build your way up!"
        
        elif 'salary' in message and career:
            career_data = self.career_database.get(career, {})
            salary = career_data.get('salary', 'Competitive industry standards')
            return f"💰 The salary for {career.title()} typically ranges from {salary}. This varies based on experience, location, and company."
        
        elif 'demand' in message and career:
            career_data = self.career_database.get(career, {})
            demand = career_data.get('demand', 'High demand in the market')
            return f"📈 {career.title()} has {demand} job demand. The technology sector is continuously growing, creating many opportunities."
        
        elif 'education' in message and career:
            career_data = self.career_database.get(career, {})
            education = career_data.get('education', "Bachelor's degree in relevant field")
            return f"🎓 Recommended education for {career.title()}:\n{education}\n\nSome roles may accept alternative paths with strong portfolios."
        
        elif career:
            career_data = self.career_database.get(career, {})
            desc = career_data.get('description', f'{career.title()} is an exciting career path with great opportunities.')
            return f"💼 About {career.title()}:\n\n{desc}\n\n💡 Key skills needed: {career_data.get('skills', 'Various skills')}\n💰 Salary range: {career_data.get('salary', 'Competitive')}\n📈 Job demand: {career_data.get('demand', 'High')}\n\nWould you like to know more about skills, salary, or education requirements?"
        
        # Check intents
        for intent_name, intent_data in self.intents.items():
            for pattern in intent_data['patterns']:
                if re.search(pattern, message, re.IGNORECASE):
                    responses = intent_data['responses']
                    if isinstance(responses, list):
                        return random.choice(responses)
                    elif callable(responses):
                        return responses(message)
        
        # Default response
        default_responses = [
            "🤔 I'm not sure about that. Try asking me:\n\n• 'Tell me about Data Scientist'\n• 'What skills for Software Developer?'\n• 'Salary of Product Manager'\n• 'Is AI Engineer in demand?'\n\nOr take our career assessment for personalized recommendations!",
            
            "💭 I can help with career-related questions! Try:\n\n• Information about specific careers\n• Skill requirements for any role\n• Salary insights\n• Job market trends\n\nWhat would you like to explore?",
            
            "🎯 Let me help you better! Ask me about:\n\n• Specific careers (e.g., 'Tell me about Cloud Architect')\n• Skills needed for any job\n• Salary ranges\n• Education paths\n\nWhat interests you?"
        ]
        
        return random.choice(default_responses)