from random import randint
from flask import Flask, render_template

app = Flask(__name__)

counter = 0

adjektiv = []
banneord = []
with open('adjektiv.txt') as f:
    adjektiv = f.read().splitlines()
with open('banneord.txt') as f:
    banneord = f.read().splitlines()

@app.route('/')
def index():
    global counter
    counter = counter + 1
    rnd_adj = randint(0, len(adjektiv))
    rnd_banne = randint(0, len(banneord))
    navn = f'{adjektiv[rnd_adj].lower()} {banneord[rnd_banne].lower()}'
    print(f'{counter}: {navn}')
    return render_template("index.html", navn=navn)
