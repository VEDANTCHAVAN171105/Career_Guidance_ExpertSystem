# app.py (COMPLETE FIXED VERSION)
from flask import Flask, render_template, request, jsonify, session
from expert_system import CareerExpertSystem
from chatbot import CareerChatbot
import secrets
import traceback

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

expert_system = CareerExpertSystem()
chatbot = CareerChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        print("Received data:", data)
        
        education_level = data.get('education_level', '12th')
        interests = data.get('interests', [])
        skills = data.get('skills', [])
        personality = data.get('personality', '')
        work_style = data.get('work_style', '')
        
        # Validate required fields
        if not interests:
            return jsonify({'error': 'Please select at least one interest'}), 400
        if not skills:
            return jsonify({'error': 'Please select at least one skill'}), 400
        if not personality:
            return jsonify({'error': 'Please select your personality type'}), 400
        if not work_style:
            return jsonify({'error': 'Please select your work style'}), 400
        
        results = expert_system.predict(education_level, interests, skills, personality, work_style)
        print("Results:", results)
        return jsonify(results)
        
    except Exception as e:
        print("Error in analyze:", str(e))
        print(traceback.format_exc())
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'response': "Please enter a message."})
        
        response = chatbot.get_response(message)
        return jsonify({'response': response})
    except Exception as e:
        print("Error in chat:", str(e))
        return jsonify({'response': "I'm having trouble responding right now. Please try again."})

if __name__ == '__main__':
    app.run(debug=True, port=5000)