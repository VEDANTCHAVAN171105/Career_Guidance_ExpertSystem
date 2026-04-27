// static/script.js (COMPLETE WITH RESET BUTTON)
// Multi-step form handling
let currentStep = 1;
const totalSteps = 4;

function updateProgress() {
    const steps = document.querySelectorAll('.progress-step');
    steps.forEach((step, index) => {
        if (index + 1 <= currentStep) {
            step.classList.add('active');
        } else {
            step.classList.remove('active');
        }
    });
}

function showStep(step) {
    const allSteps = document.querySelectorAll('.form-step');
    allSteps.forEach((stepElement) => {
        stepElement.classList.remove('active');
    });
    const targetStep = document.querySelector(`.form-step[data-step="${step}"]`);
    if (targetStep) {
        targetStep.classList.add('active');
    }
    currentStep = step;
    updateProgress();
}

// Initialize form steps
document.addEventListener('DOMContentLoaded', function() {
    // Show first step
    showStep(1);
    
    // Next button handlers
    const nextButtons = document.querySelectorAll('.next-btn');
    nextButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            // Validate current step
            if (currentStep === 1) {
                const educationSelected = document.querySelector('input[name="education_level"]:checked');
                if (!educationSelected) {
                    alert('Please select your education level');
                    return;
                }
            }
            
            if (currentStep === 2) {
                const interestsSelected = document.querySelectorAll('input[name="interests"]:checked');
                if (interestsSelected.length === 0) {
                    alert('Please select at least one interest');
                    return;
                }
            }
            
            if (currentStep === 3) {
                const skillsSelected = document.querySelectorAll('input[name="skills"]:checked');
                if (skillsSelected.length === 0) {
                    alert('Please select at least one skill');
                    return;
                }
            }
            
            if (currentStep < totalSteps) {
                showStep(currentStep + 1);
            }
        });
    });
    
    // Previous button handlers
    const prevButtons = document.querySelectorAll('.prev-btn');
    prevButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            if (currentStep > 1) {
                showStep(currentStep - 1);
            }
        });
    });
});

// Form submission
const assessmentForm = document.getElementById('assessmentForm');
if (assessmentForm) {
    assessmentForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validate final step
        const personality = document.querySelector('input[name="personality"]:checked');
        const workStyle = document.querySelector('input[name="work_style"]:checked');
        
        if (!personality) {
            alert('Please select your personality type');
            return;
        }
        
        if (!workStyle) {
            alert('Please select your preferred work style');
            return;
        }
        
        // Collect all form data
        const education_level = document.querySelector('input[name="education_level"]:checked').value;
        const interests = Array.from(document.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value);
        const skills = Array.from(document.querySelectorAll('input[name="skills"]:checked')).map(cb => cb.value);
        const personality_value = personality.value;
        const work_style_value = workStyle.value;
        
        console.log("Sending data:", {
            education_level,
            interests,
            skills,
            personality: personality_value,
            work_style: work_style_value
        });
        
        // Show loading overlay
        const loadingOverlay = document.getElementById('loadingOverlay');
        if (loadingOverlay) {
            loadingOverlay.style.display = 'flex';
        }
        
        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    education_level,
                    interests,
                    skills,
                    personality: personality_value,
                    work_style: work_style_value
                })
            });
            
            const data = await response.json();
            console.log("Response data:", data);
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            // Store results in localStorage
            localStorage.setItem('careerResults', JSON.stringify(data));
            
            // Redirect to results page
            window.location.href = '/result';
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred: ' + error.message);
            if (loadingOverlay) {
                loadingOverlay.style.display = 'none';
            }
        }
    });
}

// Load and display results on result page
if (window.location.pathname === '/result') {
    const resultsData = localStorage.getItem('careerResults');
    
    if (!resultsData) {
        window.location.href = '/form';
    } else {
        const data = JSON.parse(resultsData);
        displayResults(data);
    }
}

function displayResults(data) {
    const container = document.getElementById('resultsContent');
    if (!container) return;
    
    let html = `
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="font-size: 2rem; background: linear-gradient(135deg, #fff, #6c63ff); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🎯 Your Career Recommendations
            </h1>
            <p style="color: rgba(255,255,255,0.8);">Based on your unique profile analysis</p>
        </div>
    `;
    
    // Check if recommendations exist
    if (!data.recommendations || data.recommendations.length === 0) {
        html += `
            <div class="result-card" style="text-align: center;">
                <p>No recommendations found. Please try the assessment again.</p>
                <a href="/form" class="cta-btn" style="margin-top: 1rem;">Take Assessment Again</a>
            </div>
        `;
        container.innerHTML = html;
        return;
    }
    
    // Display each recommendation
    data.recommendations.forEach((rec, index) => {
        const medal = index === 0 ? '🥇' : index === 1 ? '🥈' : '🥉';
        
        html += `
            <div class="result-card">
                <div class="result-header">
                    <div class="career-title">
                        <span class="career-icon">${rec.icon || '💼'}</span>
                        ${medal} ${rec.career}
                    </div>
                    <div class="confidence-badge">
                        ${rec.confidence_percent || 0}% Match
                    </div>
                </div>
                
                <div class="progress-bar-container">
                    <div class="progress-bar-fill" style="width: ${rec.confidence_percent || 0}%"></div>
                </div>
                
                <p style="margin: 1rem 0; line-height: 1.6;">${rec.description || 'No description available'}</p>
                
                <div class="career-details">
                    <div class="detail-item">
                        <i class="fas fa-rupee-sign"></i>
                        <span><strong>Salary Range:</strong> ${rec.salary_range || 'Competitive'}</span>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-chart-line"></i>
                        <span><strong>Job Demand:</strong> ${rec.demand || 'High'}</span>
                    </div>
                    <div class="detail-item">
                        <i class="fas fa-building"></i>
                        <span><strong>Work Environment:</strong> ${rec.work_env || 'Various industries'}</span>
                    </div>
                </div>
                
                <div class="skills-roadmap">
                    <h4><i class="fas fa-road"></i> Your Learning Roadmap</h4>
                    <ul class="roadmap-list">
                        ${rec.skills_roadmap ? rec.skills_roadmap.map(skill => `<li>${skill}</li>`).join('') : '<li>Roadmap not available</li>'}
                    </ul>
                </div>
            </div>
        `;
    });
    
    // Add explanation
    if (data.explanation) {
        html += `
            <div class="result-card explanation-card">
                <h3><i class="fas fa-lightbulb"></i> Why These Recommendations?</h3>
                <p style="line-height: 1.8; margin-top: 1rem;">${data.explanation}</p>
            </div>
        `;
    }
    
    html += `
        <div class="result-card" style="text-align: center;">
            <h3><i class="fas fa-comments"></i> Need More Guidance?</h3>
            <p style="margin: 1rem 0;">Our AI chatbot can answer specific questions about these careers!</p>
            <a href="/" class="cta-btn" style="margin-top: 0.5rem; display: inline-block;">
                Back to Home
            </a>
        </div>
    `;
    
    container.innerHTML = html;
    
    // Animate result cards
    const resultCards = document.querySelectorAll('.result-card');
    resultCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'all 0.6s ease';
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 200);
    });
}

// Chatbot functionality with Reset Button
document.addEventListener('DOMContentLoaded', () => {
    const chatToggle = document.getElementById('chatToggle');
    const chatContainer = document.getElementById('chatContainer');
    const chatClose = document.getElementById('chatClose');
    const chatSendBtn = document.getElementById('chatSendBtn');
    const chatInput = document.getElementById('chatInput');
    const chatMessages = document.getElementById('chatMessages');
    const resetChatBtn = document.getElementById('resetChatBtn');
    
    if (chatToggle && chatContainer) {
        chatToggle.addEventListener('click', () => {
            chatContainer.classList.toggle('active');
        });
    }
    
    if (chatClose) {
        chatClose.addEventListener('click', () => {
            chatContainer.classList.remove('active');
        });
    }
    
    // Reset Chatbot Function
    function resetChatbot() {
        if (chatMessages) {
            // Clear all messages
            chatMessages.innerHTML = '';
            
            // Add default welcome message
            const welcomeMessage = document.createElement('div');
            welcomeMessage.className = 'message bot';
            welcomeMessage.innerHTML = `
                <div class="message-avatar">
                    <i class="fas fa-robot"></i>
                </div>
                <div class="message-content">
                    <p>✨ Chat history has been reset! ✨</p>
                    <p>👋 Hello! I'm your AI Career Assistant. I can help you with:</p>
                    <ul>
                        <li>📌 Detailed career information</li>
                        <li>💡 Skill requirements for any job</li>
                        <li>💰 Salary insights and job demand</li>
                        <li>🎓 Education paths and roadmaps</li>
                    </ul>
                    <p>Try asking: "Tell me about Data Scientist" or "What skills for AI Engineer?"</p>
                </div>
            `;
            chatMessages.appendChild(welcomeMessage);
            
            // Optional: Add a small animation effect
            welcomeMessage.style.opacity = '0';
            welcomeMessage.style.transform = 'translateY(10px)';
            setTimeout(() => {
                welcomeMessage.style.opacity = '1';
                welcomeMessage.style.transform = 'translateY(0)';
                welcomeMessage.style.transition = 'all 0.3s ease';
            }, 100);
        }
    }
    
    // Add reset button event listener
    if (resetChatBtn) {
        resetChatBtn.addEventListener('click', resetChatbot);
    }
    
    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;
        
        // Add user message
        addMessage(message, 'user');
        chatInput.value = '';
        
        // Show typing indicator
        const typingId = showTypingIndicator();
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            removeTypingIndicator(typingId);
            addMessage(data.response, 'bot');
        } catch (error) {
            console.error('Chat error:', error);
            removeTypingIndicator(typingId);
            addMessage("I'm having trouble connecting. Please try again.", 'bot');
        }
    }
    
    function addMessage(text, sender) {
        if (!chatMessages) return;
        
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}`;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = sender === 'user' ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        content.innerHTML = text.replace(/\n/g, '<br>');
        
        messageDiv.appendChild(avatar);
        messageDiv.appendChild(content);
        
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
    
    function showTypingIndicator() {
        if (!chatMessages) return null;
        
        const typingId = 'typing-' + Date.now();
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message bot';
        typingDiv.id = typingId;
        
        const avatar = document.createElement('div');
        avatar.className = 'message-avatar';
        avatar.innerHTML = '<i class="fas fa-robot"></i>';
        
        const content = document.createElement('div');
        content.className = 'message-content';
        content.innerHTML = '<em>Typing...</em>';
        
        typingDiv.appendChild(avatar);
        typingDiv.appendChild(content);
        
        chatMessages.appendChild(typingDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        
        return typingId;
    }
    
    function removeTypingIndicator(id) {
        if (!id) return;
        const element = document.getElementById(id);
        if (element) element.remove();
    }
    
    if (chatSendBtn) {
        chatSendBtn.addEventListener('click', sendMessage);
    }
    
    if (chatInput) {
        chatInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendMessage();
        });
    }
});

// Smooth page transitions
document.querySelectorAll('a').forEach(link => {
    if (link.href && link.href.includes(window.location.origin) && !link.href.includes('#') && link.target !== '_blank') {
        link.addEventListener('click', (e) => {
            if (!e.ctrlKey && !e.metaKey) {
                e.preventDefault();
                document.body.style.opacity = '0';
                setTimeout(() => {
                    window.location.href = link.href;
                }, 300);
            }
        });
    }
});

// Fade in page
document.body.style.opacity = '0';
document.body.style.transition = 'opacity 0.3s ease';
window.addEventListener('load', () => {
    document.body.style.opacity = '1';
});