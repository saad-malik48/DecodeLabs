import http.server, json, random, socketserver, sys, webbrowser

INTENTS={
    'greeting':['hi','hello','hey','good morning'],
    'farewell':['bye','goodbye','exit','quit','see you'],
    'thanks':['thank you','thanks','thx'],
    'help':['help','what can you do','assist'],
    'about':['who are you','what are you','your name'],
}
RESP={
    'greeting':['Hello! How can I help you today?','Hi there! What would you like to talk about?','Hey! I am here to answer your questions.'],
    'farewell':['Goodbye! Take care!','See you later! Have a great day!','Bye! Feel free to chat again soon.'],
    'thanks':['You are welcome!','No problem, happy to help!','Anytime! Let me know if you need anything else.'],
    'help':['I can greet you, tell you about myself, say goodbye, and respond to thanks.','Try saying "hello", "who are you", "thanks", or "bye".','I am a simple rule-based bot. Ask me about my name or say goodbye to exit.'],
    'about':['I am a simple rule-based chatbot created in Python.','My name is RuleBot, and I match your input to predefined intents.','I am a simple browser-friendly bot.'],
}

def sanitize(text): return text.lower().strip()

def get_response(text):
    for intent,phrases in INTENTS.items():
        if text in phrases:
            return intent, random.choice(RESP[intent])
    return None, "I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    print('=== RuleBot ===')
    print("Type 'help' or 'bye' to exit.")
    while True:
        intent,response=get_response(sanitize(input('You: ')))
        print('Bot:',response)
        if intent=='farewell': break

HTML='''<!DOCTYPE html><html><head><meta charset="utf-8"><title>RuleBot</title><style>body{font-family:monospace;background:#fff;color:#000;margin:0;padding:1rem}#chat{max-width:680px;margin:auto}div{margin:.6rem 0}input{width:calc(100%-90px);padding:.6rem}button{padding:.6rem}</style></head><body><div id="chat"><div>Bot: Hello! I am RuleBot. Ask me something like "hello".</div></div><div><input id="msg" placeholder="Type a message..."><button onclick="send()">Send</button></div><script>async function send(){const i=document.getElementById('msg');if(!i.value.trim())return;const t=i.value;document.getElementById('chat').innerHTML+='<div>You: '+t+'</div>';i.value='';const r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})});const j=await r.json();document.getElementById('chat').innerHTML+='<div>Bot: '+j.response+'</div>';window.scrollTo(0,document.body.scrollHeight);}document.getElementById('msg').addEventListener('keydown',e=>{if(e.key==='Enter')send();});</script></body></html>'''

class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/','/index.html']:
            self.send_response(200);self.send_header('Content-Type','text/html');self.end_headers();self.wfile.write(HTML.encode())
        else:
            self.send_response(404);self.end_headers()
    def do_POST(self):
        if self.path=='/chat':
            l=int(self.headers.get('Content-Length',0));b=self.rfile.read(l);d=json.loads(b.decode());_,r=get_response(sanitize(d.get('message','')))
            self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(json.dumps({'response':r}).encode())
        else:
            self.send_response(404);self.end_headers()
    def log_message(self,fmt,*a): return


def run_web():
    url='http://127.0.0.1:8000'
    with socketserver.TCPServer(('127.0.0.1',8000),Handler) as httpd:
        print('=== RuleBot Web App ===');print('Opening',url);webbrowser.open_new_tab(url);httpd.serve_forever()

if __name__=='__main__':
    run_web() if len(sys.argv)>1 and sys.argv[1] in ('--web','web') else run_chatbot()
