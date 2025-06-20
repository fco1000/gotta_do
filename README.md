# Gotta\_Do App

> "You gotta do what you gotta do."

**Gotta\_Do** is a brutal, no-nonsense productivity and accountability app built for people who are tired of their own excuses. It combines tasks, journaling, reminders, and an intelligent tone-shifting AI that adjusts based on your behavior. It's your personal drill sergeant in your pocket — sarcastic, sometimes cruel, but always effective.

---

## 📌 Table of Contents

* [App Description](#app-description)
* [Features](#features)
* [Screenshots](#screenshots)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Backend Setup](#backend-setup)
* [Frontend Setup](#frontend-setup)
* [Deployment](#deployment)
* [AI Philosophy & Modes](#ai-philosophy--modes)
* [License & Disclaimer](#license--disclaimer)

---

## 💡 App Description

**Gotta\_Do** was created by someone tired of dreaming and doing the bare minimum. It’s an app built for the creator — and people like them — who want to take back control of their habits, goals, and time.

This app doesn’t baby the user. In fact, it gets more sarcastic and indifferent the longer you stay away. And when you return, it treats you like the unproductive ghost you’ve been. Welcome back.

---

## 🚀 Features

### ✅ Core MVP (Phase 1)

* **Authentication** – Firebase Auth (Email/Password)
* **Tasks** – Create, edit, delete, mark as done
* **Journal** – Daily entries with mood tags (happy, fine, groggy, crappy)
* **Basic UI** – FlutterFlow implementation, PWA optional

### ⚙️ Pre-AI Infrastructure (Phase 2-3)

* **Reminder system** – Time-based tasks with notification scheduling
* **User Settings** – Controls for AI tone, profanity level, journal analysis
* **Interaction Tracking** – Logs behavior (app open, task done, etc.)
* **Goal Tracker** – Create goals with multi-step milestones
* **Tagging System** – Categorize tasks/journal for context-aware AI

### 🧠 AI Engine (Future Phase)

* **Dynamic Tone Adjustment** – Friendly, sarcastic, cruel, indifferent based on user behavior
* **Mood-Driven Responses** – AI adjusts based on journal moods
* **Journal Reflection** – AI comments on your entries if you opt in
* **Profanity Toggle** – Choose your level of verbal abuse
* **Escalating Notification Logic** – Longer gaps = harsher, colder reminders

---

## 📷 Screenshots

> Add your UI screenshots here

```
![Home Screen](path-to-image)
![Task List](path-to-image)
![Journal Entry](path-to-image)
![Reminder Settings](path-to-image)
```

---

## 🧱 Tech Stack

* **Frontend:** FlutterFlow (temporary), Flutter (future plan)
* **Backend:** Django + Django REST Framework
* **Database:** SQLite (Dev), PostgreSQL (Prod)
* **Auth:** Firebase Authentication
* **Cloud Functions:** Firebase (Notifications)
* **Deployment:** Render (Backend), Firebase Hosting (optional)

---

## 🗂 Project Structure

### Backend (Django)

```
gotta_do_backend/
├── api/
│   ├── models.py         # Task, Journal, Reminder, Settings, etc.
│   ├── views.py          # API endpoints
│   ├── serializers.py    # JSON serializers
│   └── urls.py
├── core/
│   ├── settings.py
│   └── urls.py
├── manage.py
```

### Frontend (FlutterFlow)

```
flutterflow_project/
├── lib/
│   ├── main.dart
│   ├── pages/
│   ├── components/
│   └── theme/
```

---

## 🛠 Backend Setup

1. Clone the repo:

```bash
git clone https://github.com/your-username/gotta_do_backend.git
cd gotta_do_backend
```

2. Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables for Firebase secret keys

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Run server:

```bash
python manage.py runserver
```

---

## 🎨 Frontend Setup (FlutterFlow)

> Designed in FlutterFlow for rapid prototyping. Will be migrated to full Flutter when MVP solidifies.

1. Open FlutterFlow
2. Import or open the project
3. Ensure Firebase is connected (Authentication enabled)
4. Bind Firestore to UI models
5. Set test mode or build PWA to test

---

## 🚢 Deployment

### Backend (Render)

* Connect GitHub repo to Render
* Auto-deploy on push to main
* Add build and post-deploy script:

```bash
python manage.py migrate
```

* Add environment variables:

  * `DJANGO_SECRET_KEY`
  * `FIREBASE_ADMIN_KEY`

### Frontend (Future Flutter Export)

* Export code from FlutterFlow
* Build and deploy with Android Studio / Xcode
* Host web version (optional) with Firebase Hosting

---

## 🧠 AI Philosophy & Modes

| Mode        | Trigger        | Example Behavior                          |
| ----------- | -------------- | ----------------------------------------- |
| Neutral     | Normal use     | Balanced reminders                        |
| Sarcastic   | 1 day missed   | "Wow. A full day without doing sh\*t."    |
| Cruel       | 3+ days missed | "Honestly? You're allergic to progress."  |
| Indifferent | 7+ days missed | "We gave up on you. But here's your app." |

**Profanity levels:**

* Mild: Clean and sharp
* Medium: Passive-aggressive roast
* Full: Drill-sergeant swearing

All behavior is opt-in and modifiable in settings.

---

## ⚠️ License & Disclaimer

This project is not intended to provide mental health care. Users are advised to use it with self-awareness and consent.

By installing and using this app, you agree that:

* You understand the tone and content may be blunt, sarcastic, or harsh
* You have full control over tone settings and journal reflection options
* You won’t complain like a Karen if it hurts your feelings – the app warned you 🫡

**License:** MIT

---

## 📢 Final Note

This app was built to change the developer’s life. If it ends up changing others’ too — great. If not? At least one person will have done what they gotta do.

> "You gotta do what you gotta do."

---

**Add your screenshots and credits below here:**

```
![Add more screenshots](path)
```
