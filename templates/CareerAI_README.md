# 🤖 CareerAI — Agentic AI Career Mentor & Placement Ecosystem

![Next.js](https://img.shields.io/badge/Next.js_14-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google_Gemini_AI-8E75B2?style=for-the-badge&logo=google&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

CareerAI is an intelligent, multi-agent AI mentorship ecosystem developed to guide engineering candidates toward placement readiness. Built during a competitive hackathon, the platform deploys **seven specialized autonomous agents** orchestrating resume analysis, mock interview simulations, adaptive learning curves, and actionable career guidance.

---

## 🌟 The 7 Autonomous AI Agents

1. 📄 **Resume Intelligence Agent**: Evaluates ATS compliance, extracts skills, flags structural gaps, and scores placement readiness.
2. 🗺️ **Adaptive Roadmap Agent**: Dynamically constructs customized learning paths based on candidate target roles and current deficiencies.
3. 🎙️ **Mock Interview Agent**: Conducts adaptive technical and behavioral interview sessions powered by Gemini prompt chains.
4. 📋 **Task & Milestone Planner**: Breaks down multi-month preparation into daily achievable technical objectives.
5. 💼 **Job Match Engine**: Analyzes job descriptions against candidate profiles to suggest high-probability opportunities.
6. 🎮 **Gamification & Habit Tracker**: Rewards consistent problem-solving streaks and project progress with milestones.
7. 🚨 **Proactive Alert Engine**: Sends reminders and alerts for upcoming deadlines, applications, and revision cycles.

---

## 🛠️ Technology Stack

- **Frontend / Framework**: Next.js (App Router), React, TypeScript, Tailwind CSS
- **AI / LLM Engine**: Google Gemini API via custom prompt engineering and structured JSON outputs
- **Database & Auth**: Supabase (PostgreSQL, row-level security, realtime subscriptions)
- **Deployment**: Vercel

---

## 🚀 Getting Started

### Prerequisites
- **Node.js 18+**
- **npm** or **pnpm**
- **Google Gemini API Key**
- **Supabase Account**

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/mohammadasim07/career-coach.git
   cd career-coach
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables in `.env.local`:
   ```env
   NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

4. Launch local development server:
   ```bash
   npm run dev
   ```
   Open `http://localhost:3000` in your browser.

---

## 🏆 Accolades
- Built and showcased during **GeekVerse Hackathon (Winner)** & **HACK AI Season 2 (Top 10 Finalist)**.

---

## 👨‍💻 Author
- **Mohammad Asim** — [GitHub](https://github.com/mohammadasim07) | [LinkedIn](https://www.linkedin.com/in/mohammadasim07)
