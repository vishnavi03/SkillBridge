# SkillBridge 🌉

SkillBridge is a full-stack Django-based skill sharing and mentorship platform where students can teach skills, request mentorship, share learning resources, and collaborate with peers through a modern web application.

🔗 Live Demo: https://skillbridge-ojs0.onrender.com  
💻 GitHub Repository: https://github.com/vishnavi03/SkillBridge

---

# ✨ Features

## 👤 Authentication & Profiles
- User signup, login, and logout
- Profile management system
- Public user profiles
- Profile pictures and bio support

## 🧠 Skills Marketplace
- Add, edit, and delete skills
- Categorize skills by topic
- Search skills using keywords
- Responsive skill cards with polished UI

## 📚 Learning Resources
Each skill supports:
- Public demo resources
- Locked premium resources

Supported resource types:
- PDFs
- External learning links
- Multiple resources per skill

Premium resources become accessible only after request approval.

## 📩 Mentorship Request System
- Send requests to skill owners
- Accept or reject requests
- Duplicate request prevention
- Request status tracking:
  - Pending
  - Accepted
  - Rejected

## ⭐ Reviews & Ratings
- Leave reviews for mentors
- Public review visibility
- Rating system for credibility

## 📊 Personalized Dashboard
Users can manage:
- Posted skills
- Requests received
- Reviews
- Learning activity

## 🎨 Modern UI/UX
- Bootstrap 5 responsive design
- Collapsible sidebar navigation
- Modern homepage hero section
- Improved dashboard layout
- Status badges and polished cards

## 🛡️ Admin Controls
- Skill moderation
- Delete inappropriate skills
- Admin panel management

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, Bootstrap 5 |
| Database | SQLite |
| Deployment | Render + Gunicorn |
| Version Control | Git & GitHub |
| File Handling | Django Media Files |

---

# 🏗️ Project Architecture

skillbridge/
├── accounts/       # Authentication & profiles
├── skills/         # Skills, resources, search
├── requests/       # Request workflow system
├── reviews/        # Reviews and ratings
├── templates/      # HTML templates
├── static/         # CSS, JS, images
├── media/          # Uploaded files
├── build.sh        # Render build configuration
├── requirements.txt
└── manage.py

---

# 🚀 Local Installation

## 1️⃣ Clone Repository

git clone https://github.com/vishnavi03/SkillBridge.git
cd SkillBridge

## 2️⃣ Create Virtual Environment

### Windows
python -m venv env
env\Scripts\activate

### Mac/Linux
python3 -m venv env
source env/bin/activate

## 3️⃣ Install Dependencies

pip install -r requirements.txt

## 4️⃣ Apply Migrations

python manage.py migrate

## 5️⃣ Run Development Server

python manage.py runserver

Open:
http://127.0.0.1:8000

---

# 🌍 Deployment

SkillBridge is deployed on Render using:
- Gunicorn (WSGI server)
- Render Web Service
- GitHub integration
- Static/media file configuration

---

# 📸 Screenshots

Add project screenshots here later.

Suggested screenshots:
- Homepage
- Dashboard
- Skills page
- Skill detail page
- Public profile page

---

# 📚 What I Learned

Through this project, I gained practical experience in:

- Django multi-app architecture
- Authentication and authorization
- CRUD operations
- Database relationships
- Media and file uploads
- Access control systems
- Dynamic template rendering
- UI/UX improvements
- Git & GitHub workflow
- Deployment and production debugging
- Real-world problem solving

---

# 👩‍💻 Developer

Vishnavi  
B.Tech Information Technology — 2nd Year

---

# ❤️ Final Note

SkillBridge started as a simple Django learning project and gradually evolved into a complete deployed full-stack web application with real-world architecture, access control, resource management, and deployment experience.
