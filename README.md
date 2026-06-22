# 🤖 Jarvis - AI Voice Assistant
 
A Python-based personal voice assistant inspired by Iron Man's J.A.R.V.I.S. It listens for a wake word, understands your voice commands, and performs tasks like opening websites, playing music, and reading the latest news.
 
---
 
## ⚠️ Known Limitation
 
> The `speak()` (text-to-speech) function is not fully utilized throughout the project because the **NewsAPI free tier key got exhausted** during development and testing. Some voice responses that were planned could not be tested or implemented fully as a result. This will be improved in future versions.
 
---
 
## ✨ Features
 
- 🎙️ **Wake word detection** — Activates only when you say **"Jarvis"**
- 🌐 **Open websites** — Google, YouTube, LinkedIn, Facebook, GitHub
- 🎵 **Play music** — Plays songs from a custom music library
- 📰 **Latest news** — Reads top headlines from India via NewsAPI
- 🔊 **Text-to-speech** — Responds back to you with voice using `pyttsx3`
---
 
## 🛠️ Tech Stack
 
| Library | Purpose |
|---|---|
| `speech_recognition` | Captures and transcribes voice input |
| `pyttsx3` | Converts text to speech (offline) |
| `webbrowser` | Opens URLs in the default browser |
| `requests` | Fetches news from NewsAPI |
| `musicLibrary` | Custom module storing song name → URL mappings |
 
---
 
## 📦 Installation
 
**1. Clone the repository**
```bash
git clone https://github.com/your-username/jarvis-assistant.git
cd jarvis-assistant
```
 
**2. Install dependencies**
```bash
pip install speechrecognition pyttsx3 requests pyaudio
```
 
> **Note for Windows users:** If `pyaudio` fails to install, download the correct `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.
 
**3. Set up your NewsAPI key**
 
Get a free API key from [newsapi.org](https://newsapi.org) and set it as an environment variable:
 
```bash
# Windows
set NEWS_API_KEY=your_api_key_here
 
# Mac/Linux
export NEWS_API_KEY=your_api_key_here
```
 
**4. Set up your music library**
 
Edit `musicLibrary.py` and add your songs:
```python
music = {
    "believer": "https://www.youtube.com/watch?v=...",
    "rockstar": "https://www.youtube.com/watch?v=...",
}
```
 
---
 
## 🚀 Usage
 
```bash
python main.py
```
 
Once running:
1. Wait for Jarvis to say **"Initializing Jarvis, your personal assistant"**
2. Say **"Jarvis"** to wake it up
3. Give a command when it responds
---
 
## 🗣️ Example Commands
 
| You say | Jarvis does |
|---|---|
| `"Jarvis"` | Wakes up and listens |
| `"Open YouTube"` | Opens YouTube in browser |
| `"Open GitHub"` | Opens GitHub in browser |
| `"Play believer"` | Plays that song from your music library |
| `"What's the news"` | Reads top Indian headlines aloud |
 
---
 
## 📁 Project Structure
 
```
jarvis-assistant/
│
├── main.py            # Main assistant logic
├── musicLibrary.py    # Song name → URL dictionary
└── README.md
```
 
---
 
## 🐛 Known Bugs Fixed During Development
 
- Play command was matching exact word `"play"` instead of checking if it was contained in the command
- `pyttsx3` engine was being re-initialized inside the loop causing freeze
- API key was hardcoded (now uses environment variable)
- No error handling for missing songs in the music library
- `phrase_time_limit` was too short to capture the wake word reliably
---
 
## 🔮 Future Improvements
 
- [ ] Add OpenAI/Gemini API for smarter responses
- [ ] Add weather updates
- [ ] Add reminder/alarm functionality
- [ ] Improve wake word detection accuracy
- [ ] Fix and expand `speak()` usage once API limits are resolved
---
 
## 🙏 Acknowledgements
 
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) by Anthony Zhang
- [NewsAPI](https://newsapi.org/) for news data
- Inspired by Iron Man's J.A.R.V.I.S.
---
