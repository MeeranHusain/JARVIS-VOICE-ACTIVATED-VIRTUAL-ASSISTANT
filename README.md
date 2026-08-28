# 🤖 Jarvis — AI Voice Assistant

Jarvis is a Python-based **AI Voice Assistant** that listens for the wake word **"Jarvis"** and performs different tasks using voice commands.

It can open websites, play songs, fetch the latest Indian news, and answer general questions using **Ollama Cloud AI**.

---

## ✨ Features

* 🎤 **Voice Recognition** — Uses Google Speech Recognition
* 🗣️ **Text-to-Speech** — Jarvis responds using your system voice
* 🤖 **AI Assistant** — Uses Ollama Cloud with `gpt-oss:20b-cloud`
* 🌐 **Website Launcher** — Open websites using voice commands
* 🎵 **Music Player** — Play songs from your custom music library
* 📰 **News Reader** — Fetches and reads the latest Indian news
* 🔐 **Environment Variables** — API keys are stored securely in `.env`
* ⚡ **Voice Wake Word** — Activates when "Jarvis" is detected
* 🛡️ **Error Handling** — Handles speech, network, and runtime errors

---

## 🛠️ Technologies Used

* **Python**
* **SpeechRecognition**
* **PyAudio**
* **pyttsx3**
* **Requests**
* **python-dotenv**
* **Ollama Python Client**
* **NewsData.io API**
* **Google Speech Recognition**

---

## 📁 Project Structure

```text
Jarvis/
│
├── main.py
├── musicLibrary.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### File Description

| File               | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `main.py`          | Main Jarvis application                                  |
| `musicLibrary.py`  | Stores songs and their links                             |
| `requirements.txt` | Required Python dependencies                             |
| `.env`             | Stores API keys                                          |
| `.gitignore`       | Prevents sensitive/unnecessary files from being uploaded |
| `README.md`        | Project documentation                                    |

---

## ⚙️ Requirements

Before running Jarvis, make sure you have:

* Python **3.10+**
* A working microphone 🎤
* Internet connection 🌐
* Ollama Cloud API key
* NewsData.io API key

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone MeeranHusain/JARVIS-VOICE-ACTIVATED-VIRTUAL-ASSISTANT
```

Move into the project directory:

```bash
cd Jarvis
```

---

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Configuration

Create a `.env` file in the root directory:

```env
NEWSDATA_API_KEY=your_newsdata_api_key
OLLAMA_API_KEY=your_ollama_api_key
```

Replace the values with your actual API keys.

### ⚠️ Important

**Never upload your `.env` file to GitHub.**

Your `.gitignore` should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## ▶️ Run Jarvis

After activating your virtual environment:

```bash
python main.py
```

You should hear:

```text
Initializing Jarvis...
```

Jarvis will then start listening for the wake word.

---

## 🎙️ How to Use

### Wake Jarvis

Say:

```text
Jarvis
```

Jarvis will respond:

```text
Yes, how can I assist you?
```

Then give your command.

---

## 🌐 Open Websites

Say:

```text
Jarvis
```

Then:

```text
Open YouTube
```

Jarvis will open:

```text
https://www.youtube.com
```

You can also provide a domain:

```text
Open google.com
```

---

## 🎵 Play Music

Add your songs inside `musicLibrary.py`.

Example:

```python
music = {
    "believer": "https://www.youtube.com/watch?v=...",
    "shape of you": "https://www.youtube.com/watch?v=..."
}
```

Then say:

```text
Jarvis
```

followed by:

```text
Play believer
```

Jarvis will open the corresponding song link.

---

## 📰 Get Latest News

Say:

```text
Jarvis
```

Then:

```text
Give me the news
```

Jarvis will fetch the latest Indian news from NewsData.io and read the first five headlines aloud.

---

## 🤖 Ask AI Questions

For commands that don't match the built-in commands, Jarvis sends the request to Ollama Cloud.

Example:

```text
Jarvis
```

Then:

```text
What is artificial intelligence?
```

Jarvis will generate an AI response using:

```text
gpt-oss:20b-cloud
```

---

## 🔄 Command Flow

```text
              🎤 User
                 │
                 ▼
        Speech Recognition
                 │
                 ▼
        Detect "Jarvis"
                 │
                 ▼
       ┌───────────────────┐
       │   User Command    │
       └───────────────────┘
                 │
       ┌─────────┼──────────┐
       ▼         ▼          ▼
    Website    Music      News
       │         │          │
       ▼         ▼          ▼
    Browser    Browser   NewsData API

                 │
                 ▼
          Unknown Command
                 │
                 ▼
          Ollama Cloud AI
                 │
                 ▼
          🗣️ Jarvis Speaks
```

---

## 📦 Dependencies

The project uses the following Python packages:

```text
SpeechRecognition==3.17.0
pyttsx3==2.99
requests==2.34.2
python-dotenv==1.2.3
ollama==0.6.2
PyAudio==0.2.14
```

Install everything using:

```bash
pip install -r requirements.txt
```

---

## 🛡️ Security

API keys should **never** be hardcoded directly into Python files.

❌ Don't do this:

```python
api_key = "your-secret-api-key"
```

✅ Use environment variables:

```python
api_key = os.getenv("OLLAMA_API_KEY")
```

and store the actual key in `.env`.

---

## 🐛 Error Handling

Jarvis handles common errors including:

* Speech recognition timeout
* Unrecognized speech
* Google Speech Recognition errors
* News API connection errors
* HTTP request timeouts
* Unknown songs
* General runtime exceptions

---

## 🔮 Future Improvements

Some planned improvements for Jarvis:

* 🔊 Better wake-word detection
* 🧠 Conversation memory
* 🌦️ Weather information
* ⏰ Alarms and reminders
* 📧 Email integration
* 💻 System controls
* 📂 File and application management
* 🔍 Web search
* 🪟 GUI interface
* 🎙️ Fully offline speech recognition
* 🧩 More customizable commands

---

## 🤝 Contributing

Contributions are welcome!

If you want to improve Jarvis:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Make your changes
4. Commit your changes

```bash
git add .
git commit -m "Add new feature"
```

5. Push your branch

```bash
git push origin feature/new-feature
```

6. Open a Pull Request

---

## 📄 License

This project is created for **learning and personal use**.

You are free to modify and improve the project according to your needs.

---

## 👨‍💻 Author

**Meeran Husain**

Built with ❤️ using Python and AI.

---

⭐ If you find this project useful, consider giving the repository a **star**!
