"""Usage: python cli.py "வணக்கம்! எப்படி இருக்கீங்க?" -o hello.mp3"""
import argparse
from vennila import synthesize, DEFAULT_MODEL

p = argparse.ArgumentParser()
p.add_argument("text")
p.add_argument("-o", "--out", default="out.mp3")
p.add_argument("-m", "--model", default=DEFAULT_MODEL)
p.add_argument("--stability", type=float, default=0.5)
a = p.parse_args()

audio = synthesize(a.text, model_id=a.model, stability=a.stability)
with open(a.out, "wb") as f:
    f.write(audio)
print(f"Saved {a.out} ({len(audio)//1024} KB)")
