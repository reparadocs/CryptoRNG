from flask import Flask
import random

app = Flask(__name__)

f = open("words.txt", "r")
words = f.readlines()
f.close()

@app.route("/words")
def hello():
  w1 = random.randrange(len(words))
  w2 = random.randrange(len(words))
  w3 = random.randrange(len(words))
  s = words[w1] + " " + words[w2] + " " + words[w3]
  return s


if __name__ == "__main__":
  app.run()