# Hack2Hire – AI Interview Simulation Engine

A **rule-based AI interview simulation system** built for the **Hack2Hire: AI-Powered Interview Hackathon**.  
This project mimics how real-world AI interview platforms evaluate candidates using structured logic, adaptive flow, and deterministic scoring.

---

## 🚀 Project Overview

Modern hiring platforms rely on intelligent systems to evaluate thousands of candidates efficiently.  
This project simulates such a system by:

- Processing interview rounds (MCQ + Coding)
- Applying predefined evaluation rules
- Managing interview state transitions
- Producing a final interview readiness decision

The focus is on **engineering correctness, clarity, and decision-making logic**, rather than machine learning.

---

## 🧠 Key Features

- **Rule-Based AI Engine**
  - Deterministic scoring and evaluation
  - Early termination on failure conditions
  - Clean state management (IN_PROGRESS, TERMINATED, COMPLETED)

- **Interview Rounds**
  - MCQ Round (10 questions – UI simulation)
  - Coding Round (5 problems with validation checks)

- **Adaptive Interview Flow**
  - Interview progression depends on candidate performance
  - Failed rounds trigger early termination

- **Clean Dark AI UI**
  - MCQ and Coding pages styled as AI interview screens
  - Terminal-style coding interface
  - Result dashboard for final evaluation

- **Judge-Safe Architecture**
  - No real-time execution
  - No backend-server dependency
  - Fully deterministic and explainable

---

## 🏗️ Project Structure
<img width="732" height="507" alt="image" src="https://github.com/user-attachments/assets/b5f194b8-1195-4606-b6a8-f962cc85b142" />

