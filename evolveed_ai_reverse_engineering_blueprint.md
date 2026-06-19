# EvolveED.AI — Reverse Engineering Blueprint For Flutter Rebuild

# 1. CORE IDEA EXTRACTION

## Main Idea

EvolveED.AI is an AI-powered personalized learning ecosystem designed to solve:
- Information overload
- Lack of learning direction
- Inconsistent learning habits
- Poor-quality resource discovery
- Lack of mentorship
- Accessibility limitations in modern learning systems

The platform acts as:
- An AI mentor
- A personalized learning planner
- A smart YouTube learning curator
- A hackathon & career growth companion
- An accessibility-first educational assistant

---

## Primary User Problems Solved

### Problem 1 — “What should I learn?”
Solution:
Gemini AI generates structured learning paths.

### Problem 2 — “Which resources are actually good?”
Solution:
Gemini + YouTube API fetch curated educational videos.

### Problem 3 — “I lose motivation quickly.”
Solution:
- Streaks
- AI tutor
- Weekly summaries
- Notifications
- Achievements

### Problem 4 — “I need guidance while learning.”
Solution:
Gemini AI tutor.

### Problem 5 — “Learning platforms ignore accessibility.”
Solution:
- Braille support
- Voice support
- Simplified reminders
- Cognitive assistance

---

# 2. PRODUCT POSITIONING

The app should feel like:
- Duolingo + ChatGPT + YouTube Learning + AI Mentor

NOT like:
- A chatbot only
- A course-selling platform
- A random YouTube wrapper

---

# 3. TECH STACK EXTRACTION

## Frontend Stack

- React
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- Lovable AI frontend builder

---

## Backend / Cloud Stack

### Firebase
Used for:
- Authentication
- Firestore
- Storage
- Cloud Messaging

Services:
- Firebase Authentication
- Cloud Firestore
- Firebase Storage
- Firebase Cloud Messaging (FCM)

---

## AI Stack

### Gemini AI
Purpose:
- Learning path generation
- AI tutor
- Summaries
- Hackathon intelligence
- YouTube query generation
- Accessibility transformations

Model:
- Gemini 2.5 Flash

---

## Video Integration

### YouTube Data API
Purpose:
- Curated educational content
- AI-generated learning recommendations

---

## Voice AI

### ElevenLabs
Purpose:
- AI voice narration
- Voice mentor
- Placement guidance
- Accessibility support

---

## Deployment Platforms

- Lovable
- Netlify

---

## Future Flutter Stack Recommendation

### Flutter Frontend
Recommended Packages:
- flutter_riverpod
- go_router
- firebase_core
- firebase_auth
- cloud_firestore
- firebase_storage
- firebase_messaging
- dio
- youtube_player_iframe
- just_audio
- flutter_animate
- lottie

---

# 4. LOVABLE PROMPT EXTRACTION (RECONSTRUCTED)

## Core Product Prompt

"Build an AI-powered learning ecosystem called EvolveED.AI.
The app should help users learn technical and creative skills using Gemini AI, curated YouTube videos, AI tutoring, learning streaks, accessibility features, and hackathon recommendations.
The app should feel modern, minimal, student-friendly, and productivity-oriented."

---

## Firebase Integration Prompt

"Integrate Firebase Authentication, Cloud Firestore, Firebase Storage, and Firebase Cloud Messaging into the app.
Use Firestore only for lightweight metadata.
Store large AI outputs in Firebase Storage.
Authentication must survive refresh and work using Google Sign-In."

---

## Gemini Integration Prompt

"Integrate Gemini AI as the core intelligence layer.
Gemini must generate learning paths, summaries, practice tasks, and personalized guidance.
All AI outputs must be stored in Firebase Storage.
Gemini must fail gracefully and never crash the app."

---

## YouTube Integration Prompt

"Use Gemini to generate optimized YouTube search queries.
Fetch only high-quality educational videos using YouTube Data API.
Limit results to 3–5 videos per concept.
Avoid distractions and random recommendations."

---

## Accessibility Prompt

"Add accessibility support including Braille learning mode and simplified cognitive reminders.
Use Gemini to generate Braille pattern representations and simplified learning assistance."

---

## Stability Prompt

"The entire application must remain refresh-safe and stable.
All async calls must use try/catch.
No feature should crash another feature.
Missing API keys must fail gracefully without breaking the UI."

---

# 5. EXACT FEATURE EXTRACTION

## Authentication System

Features:
- Google Sign-In
- Session persistence
- New user profile setup
- Returning user dashboard routing

---

## AI Learning Path Generator

Inputs:
- Topic
- Current level
- Goal
- Timeframe

Outputs:
- Weekly roadmap
- Daily goals
- Practice tasks
- Mini-projects
- Mastery metrics

---

## AI Tutor

Capabilities:
- Doubt solving
- Motivation
- Simplified explanations
- Career guidance
- Interview preparation

---

## YouTube Learning Feed

Features:
- AI-curated educational videos
- Embedded playback
- Minimal distractions
- Personalized learning suggestions

---

## Notes Summarizer

Capabilities:
- Notes upload
- PDF summarization
- Key point extraction
- Quiz generation
- Flashcard generation

---

## Hackathon Discovery

Capabilities:
- AI-generated hackathon recommendations
- Skill-based matching
- Career-growth opportunities

---

## Learning Analytics

Tracks:
- Daily streaks
- Longest streak
- Active learning days
- User consistency

---

## Achievements & Gamification

Features:
- Badges
- Milestones
- XP-style progression
- Motivation loops

---

## Accessibility Features

### Braille Mode
- Braille pattern generation
- Accessibility-friendly UI

### Cognitive Support
- Reminder notifications
- Simplified guidance
- Repetition-based prompts

---

## Voice AI

Capabilities:
- Voice guidance
- Placement guidance
- Learning narration
- AI mentor voice support

---

# 6. DASHBOARD STYLE EXTRACTION

## Design Language

Theme:
- Modern AI-native UI
- Minimal but futuristic
- Productivity-focused

Primary Colors:
- Black
- Deep blue
- Red accents

Modes:
- Dark mode
- Light mode
- System mode

---

## Dashboard Sections

### Top Header
Contains:
- Welcome message
- User profile
- Streak overview

---

### Main Dashboard Cards

Cards:
- Continue Learning
- AI Learning Path
- Recommended Videos
- AI Tutor
- Hackathons
- Achievements
- Notes Summarizer

---

## UI Style

Elements:
- Rounded cards
- Soft shadows
- Gradient highlights
- Responsive layout
- Smooth animations
- Minimal clutter
- Large readable typography

---

# 7. RECOMMENDED FLUTTER SCREEN STRUCTURE

## Screens

- SplashScreen
- LoginScreen
- ProfileSetupScreen
- DashboardScreen
- LearningPathScreen
- VideoFeedScreen
- AITutorScreen
- NotesSummarizerScreen
- HackathonScreen
- AchievementsScreen
- AccessibilitySettingsScreen
- NotificationsScreen

---

# 8. FIREBASE DATA ARCHITECTURE

## Firestore Collections

### users
Stores:
- uid
- name
- email
- phone
- preferences
- streaks

---

### learning_metadata
Stores:
- userId
- topic
- storageFileUrl
- createdAt

---

### youtube_metadata
Stores:
- userId
- topic
- videoId
- title
- thumbnail

---

### notifications
Stores:
- preferences
- reminder timings

---

# 9. STORAGE ARCHITECTURE

## Firebase Storage Folders

### learning-paths/
Stores AI-generated JSON roadmaps.

### summaries/
Stores AI-generated summaries.

### audio/
Stores ElevenLabs voice outputs.

### uploads/
Stores user-uploaded notes and PDFs.

---

# 10. DATA STRUCTURES & ALGORITHMS ANALYSIS

## Data Structures Used

### Arrays / Lists
Used for:
- Video recommendations
- Learning modules
- Weekly tasks
- Quiz questions
- Hackathon listings

---

### Maps / JSON Objects
Used for:
- Gemini structured outputs
- Firebase documents
- User profiles
- Metadata storage

---

### Queues / Streams
Used for:
- Async notifications
- AI response streaming
- Real-time updates

---

### Sets
Potentially used for:
- Unique recommendations
- Deduplication of YouTube videos

---

## Algorithms / System Logic

### Recommendation Logic
Used for:
- Matching skills → videos
- Matching skills → hackathons
- Matching interests → learning paths

Approach:
- AI-assisted ranking
- Query optimization
- Context filtering

---

### Search Optimization
Gemini generates optimized YouTube search queries.

---

### Caching Strategy
Used for:
- Avoiding repeated API calls
- Faster dashboard loading

---

### Streak Tracking Logic
Tracks:
- Consecutive active days
- User consistency
- Daily engagement

---

### Reminder Scheduling Logic
Used for:
- FCM notifications
- Learning reminders
- Revision reminders

---

# 11. MCP + ANTIGRAVITY + CODEX AUTOMATION PLAN

## Suggested System Flow

### Step 1 — Flutter Frontend
Build using:
- Flutter
- Riverpod
- Firebase

---

### Step 2 — MCP Server
Use MCP server for:
- Prompt orchestration
- AI request routing
- Agent coordination

---

### Step 3 — Codex / Agent Usage
Use Codex for:
- UI generation
- Flutter widgets
- Firebase integration
- API layer generation
- Routing structure

---

### Step 4 — Gemini Layer
Gemini handles:
- Learning intelligence
- Recommendations
- Summaries
- Accessibility generation

---

### Step 5 — Antigravity Integration
Use Antigravity for:
- Automation flows
- Multi-agent execution
- System orchestration
- Backend workflow automation

---

# 12. FINAL PRODUCT VISION

The rebuilt Flutter version should feel like:
- A modern AI-native learning operating system
- A personal mentor
- A productivity companion
- A socially impactful accessibility-first platform

The experience should combine:
- AI intelligence
- Simplicity
- Inclusivity
- Career growth
- Motivation
- Long-term learning consistency
