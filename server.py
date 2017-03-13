from flask import Flask
import random
import json

app = Flask(__name__)

f = open("words.txt", "r")
words = f.readlines()
f.close()

@app.route("/words")
def hello():
  w1 = random.randrange(len(words))
  w2 = random.randrange(len(words))
  w3 = random.randrange(len(words))
  s = words[w1].strip() + " " + words[w2].strip() + " " + words[w3].strip()
  return json.dumps({'words': s})


if __name__ == "__main__":
  app.run()