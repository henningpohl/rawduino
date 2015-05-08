import os
import hashlib

h = hashlib.sha256()

with open('rawduino.zip', 'rb') as f:
    for line in f:
        h.update(line)

print "SHA-256:%s" % h.hexdigest()
print "Size:", os.path.getsize('rawduino.zip')
