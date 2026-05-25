Decodelabs Week 1 --Rule-Based AI Chatbot--

**Project 1** | AI Intern @ [DecodeLabs](https://github.com/DecodeLabs)

A lightweight, rule-based AI chatbot built in pure Python — no external libraries, no ML models. RuleBot matches user input against predefined intents using dictionary-based logic and responds with randomized replies. Runs both as a **terminal app** and as a **local web app** in your browser.

 **About the Project**

This is my **first project** as an **AI Intern at DecodeLabs**. The goal was to understand the foundational concepts behind conversational AI — intent detection, input sanitization, response variation, and fallback handling — before moving into more advanced NLP and ML-based approaches.


**Features**

**Intent Matching** — Dictionary-based knowledge base with 5 intents
**Input Sanitization** — Handles case differences and extra whitespace
**Response Variation** — Randomly picks from multiple replies per intent
**Continuous Loop** — Keeps chatting until you say goodbye
**Clean Exit** — Farewell intent breaks the loop gracefully
**Dual Mode** — Run in terminal OR launch as a browser web app
**Zero Dependencies** — Only Python standard library (`random`, `http.server`, `json`)

---

## Intents & Triggers

| Intent | Example Triggers |
|-----------|----------------------------------|
| `greeting` | hi, hello, hey, good morning |
| `farewell` | bye, goodbye, exit, quit, see you |
| `thanks` | thank you, thanks, thx |
| `help` | help, what can you do, assist |
| `about` | who are you, what are you, your name |

---

## Project Structure

```
chatbot.py
│
├── INTENTS        → Dictionary of intent → trigger phrases
├── RESP           → Dictionary of intent → response list
│
├── sanitize()     → Lowercases and strips whitespace from input
├── get_response() → Matches input to intent, returns a response
├── run_chatbot()  → Terminal mode: continuous while loop
├── run_web()      → Web mode: starts local HTTP server on port 8000
│
└── HTML           → Inline single-page browser UI (no files needed)
```

---

## Getting Started

### Prerequisites
- Python 3.x (no pip installs required)

### Run in Terminal
```bash
python chatbot.py
```

### Run as Web App
```bash
python chatbot.py --web
```
Then open your browser at: `http://127.0.0.1:8000`

---

## 💬 Terminal Demo

```
=== RuleBot ===
Type 'help' or 'bye' to exit.

You: hello
Bot: Hi there! What would you like to talk about?

You: who are you
Bot: My name is RuleBot, and I match your input to predefined intents.

You: thanks
Bot: No problem, happy to help!

You: bye
Bot: Goodbye! Take care!
```

---

## Logic Skeleton

```
Input Loop    →  Continuous while True cycle
Sanitization  →  .lower().strip() on every input
Knowledge Base →  Dictionary with 5+ intents
Matching      →  if text in phrases → return response
Fallback      →  Default reply for unrecognized input
Exit Strategy →  farewell intent → break loop
```

---

## What I Learned

- How rule-based chatbots work at a fundamental level
- Using Python dictionaries as a simple knowledge base
- Input sanitization before pattern matching
- Serving a web app with Python's built-in `http.server`
- Structuring clean, modular Python code

---

## Future Improvements

- [ ] Add more intents (weather, jokes, time)
- [ ] Support partial phrase matching (not just exact substring)
- [ ] Add a conversation history display in the web UI
- [ ] Integrate basic NLP (NLTK / spaCy) for fuzzy matching
- [ ] Deploy web version to a public URL

---

## Author

**AI Intern : M Saad**

---

## 📄 License

This project is part of an internship training program at **DecodeLabs**. Feel free to fork and build on it.
