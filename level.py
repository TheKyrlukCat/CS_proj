import random
import engine

def load_masses():
    masses = []
    for i in range(5):
        masses.append(engine.Planet(random.randint(0, 720), random.randint(-720, 0), random.randint(1, 10), random.randint(1, 100)))
    return masses