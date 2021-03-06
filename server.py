from flask import Flask, request
import random
import json
import random

app = Flask(__name__)

f = open("words.txt", "r")
words = f.readlines()
f.close()

SAMPLING_RATE = 16

def bitlist(num):
  return [int(digit) for digit in bin(num)[2:]]

@app.route("/words")
def hello():
  w1 = random.randrange(len(words))
  w2 = random.randrange(len(words))
  w3 = random.randrange(len(words))
  s = words[w1].strip() + " " + words[w2].strip() + " " + words[w3].strip()
  return json.dumps({'words': s})

@app.route("/audio", methods=["POST"])
def audio():
  audio = request.form['audio'][1:].split(' ')
  audio = audio[:-1]
  cleaned_audio = []
  for astr in audio:
    if astr != '00000000':
      cleaned_audio.append(int(astr, 16))
  rs = []

  sampling_rate = len(cleaned_audio) / (16 + 1)
  bit_counter = 0
  index = sampling_rate

  random_bitstring = ''

  while index < len(cleaned_audio) and len(random_bitstring) < 16:
    b = bitlist(cleaned_audio[index])
    x = b[0]
    for i in range(len(b) - 1):
      x ^= b[i+1]

    bit_counter ^= x

    if (index % sampling_rate) == 0:
      random_bitstring += str(bit_counter)
    index += 1

  if len(random_bitstring) == 0:
    return '0'

  return str(int(random_bitstring, 2))

'''
  for i in range(16):
    ind1 = random.randrange(len(cleaned_audio) - 1)
    random.seed(cleaned_audio[ind1])
    pseudo1 = random.getrandbits(16)
    ind2 = random.randrange(len(cleaned_audio) -1)
    r1 = cleaned_audio[ind2] ^ pseudo1
    cleaned_audio = cleaned_audio[:ind2] + cleaned_audio[ind2+1:]
    for i in range(len(cleaned_audio) / 16):
      r1 ^= random.choice(cleaned_audio)

    rs.append(r1)

  return str(random.choice(rs) ^ random.getrandbits(16)) 
  '''


if __name__ == "__main__":
  app.run()