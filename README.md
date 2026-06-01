# 🤖 JARVIS AI - OpenAI Powered Desktop Assistant

**Industry:** Artificial Intelligence & Automation  
**Technology:** Python, OpenAI API, Speech Recognition, Text-to-Speech

## Project Overview

JARVIS AI is an intelligent desktop assistant built using Python and OpenAI APIs that can understand voice commands, engage in human-like conversations, and perform various desktop automation tasks.

The assistant listens to user commands through speech recognition, processes them using AI, and responds naturally through text-to-speech technology. It acts as a personal productivity companion capable of answering questions, opening applications, performing searches, and assisting with daily tasks.

## The Problem

Traditional desktop interactions often require multiple manual steps to perform simple tasks. Users frequently need to:

* Navigate through applications manually.
* Search information across multiple platforms.
* Switch between tools for different tasks.
* Spend time on repetitive actions.

This creates inefficiencies and reduces productivity.

## Solution: JARVIS AI Assistant

JARVIS AI simplifies human-computer interaction through voice and AI-powered conversations.

The workflow is simple:

1. **Listen:** Captures user voice commands.
2. **Understand:** Processes the command using OpenAI.
3. **Execute:** Performs requested actions or generates responses.
4. **Respond:** Speaks back naturally using text-to-speech.

## Key Features

### Voice Recognition
Converts user speech into text commands.

### AI-Powered Conversations
Uses OpenAI models to generate intelligent responses.

### Text-to-Speech
Provides natural voice responses.

### Web Search Support
Searches and retrieves information quickly.

### Desktop Automation
Can open applications and perform system tasks.

### Date & Time Assistance
Provides real-time date and time information.

### Fast Response System
Processes commands efficiently for smooth interactions.

## Project Structure

```bash
JARVIS-AI/
│
├── __pycache__/
│
├── .venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   └── pyvenv.cfg
│
├── config.py
├── main.py
├── openaitest.py
├── requirements.txt
│
└── README.md
```

## Tech Stack

### Programming Language
* Python

### AI Integration
* OpenAI API

### Libraries
* SpeechRecognition
* PyAudio
* pyttsx3
* python-dotenv
* requests

## Prerequisites

Before running the project, make sure you have:

* Python 3.10+
* OpenAI API Key
* Microphone Access
* Internet Connection

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/JARVIS-AI.git
```

### 2. Navigate to Project

```bash
cd JARVIS-AI
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application

```bash
python main.py
```

The assistant will start listening for commands.

## Example Commands

```text
Hello Jarvis
What's the time?
Open Chrome
Search Python tutorials
Tell me a joke
Who is Elon Musk?
Generate Python code
Explain React.js
```

## Future Enhancements

* Face Recognition
* GUI Dashboard
* WhatsApp Automation
* Email Assistant
* Multi-Language Support
* Local AI Model Integration
* Smart Home Automation
* Personal Scheduling Assistant

## Author

**Shruti Mistry**
