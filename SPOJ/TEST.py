import os

s = os.read(0, 999999999)
end = s.index(b'\n42\n')
os.write(1, s[:end])
