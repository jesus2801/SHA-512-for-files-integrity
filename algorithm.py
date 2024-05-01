import hashlib

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!


def SHA512(file_path: str):
  sha512 = hashlib.sha512()

  with open(file_path, 'rb') as f:
    while True:
      data = f.read(BUF_SIZE)
      if not data:
        break
      sha512.update(data)

  return sha512.digest()
