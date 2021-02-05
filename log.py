from datetime import datetime
weblog = False
try:
  import extension
  weblog = True
except:
  pass
file = open("chat_history.log","a")
def log(message,command="none",level="INFO"):
  global file
  now = datetime.now()
  print("[" + now.strftime("%H:%M:%S") + "] [" + level + "] " + message)
  if weblog:
    weblogdata(message)
def logf(message,command="none",level="INFO"):
  global file
  now = datetime.now()
  file.write("[" + now.strftime("%H:%M:%S") + "] [" + level + "] " + message + "\n")
  file.close()
  file = open("chat_history.log","a")
  if weblog:
    weblogdata(message)
def weblogdata(datatolog):
  extension.record(datatolog)
