LOGIC SKELETON

1. Input Loop
- Run a continuous `while True` loop.
- Every cycle: prompt user → sanitize → match intent → print response.

2. Sanitization
- Apply `.lower().strip()` to every input before matching.

3. Knowledge Base
- Use a dictionary with 5+ intents. Each key is an intent name, value is a list of trigger phrases.
- Required intents:
  - greeting  → ["hi", "hello", "hey", "good morning"]
  - farewell  → ["bye", "goodbye", "exit", "quit", "see you"]
  - thanks    → ["thank you", "thanks", "thx"]
  - help      → ["help", "what can you do", "assist"]
  - about     → ["who are you", "what are you", "your name"]

4. Fallback
- If no intent matches → reply: "I didn't understand that. Type 'help' to see what I can do."

5. Exit Strategy
- Detect farewell intent → print a goodbye message → `break` the loop cleanly.
