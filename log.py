from datetime import datetime
file = open("chat_history.log","a")
def log(message,level="INFO"):
  global file
  now = datetime.now()
  print("[" + now.strftime("%H:%M:%S") + "] [" + level + "] " + message)
def logf(message,level="INFO"):
  global file
  now = datetime.now()
  file.write("[" + now.strftime("%H:%M:%S") + "] [" + level + "] " + message + "\n")
  file.close()
  file = open("chat_history.log","a")
