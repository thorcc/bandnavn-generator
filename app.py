from random import randint
from flask import Flask, render_template

app = Flask(__name__)

adjektiv = []
banneord = []
with open('adjektiv.txt') as f:
    adjektiv = f.read().splitlines()
with open('banneord.txt') as f:
    banneord = f.read().splitlines()

tilfeldig_adj = randint(0, len(adjektiv))
tilfeldig_banne = randint(0, len(banneord))
print(tilfeldig_adj, tilfeldig_banne)
print(adjektiv[tilfeldig_adj] + " " + banneord[tilfeldig_banne])


@app.route('/')
def hello_world():
    rnd_adj = randint(0, len(adjektiv))
    rnd_banne = randint(0, len(banneord))
    navn = f'{adjektiv[rnd_adj]} {banneord[rnd_banne]}'
    
    return render_template("index.html", navn=navn)
