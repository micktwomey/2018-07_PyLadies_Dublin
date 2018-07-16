from datetime import datetime

d1 = datetime.utcnow()
print(f"d1 is {d1!r}")

s = d1.isoformat()
print(f"d1's isoformat is {s!r}")

d2 = datetime.fromisoformat(s)
print(f"parsed into d2: {d2!r}")

print(f"d1 == d2? {d1 == d2}")

datetime.fromisoformat(d1.isoformat(sep=" ")) == d1
