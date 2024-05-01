import hashlib # hashlib for hash algorithms

BUF_SIZE = 65536  # this determinate data will be read in 64kb chunks

"""
this functions receives a file path and then return
the SHA-512 of the file's content
"""
def SHA512(file_path: str):
  sha512 = hashlib.sha512() # instance of the algorithm

  with open(file_path, 'rb') as f: # reads the file in binary mode
    while True:
      data = f.read(BUF_SIZE) # reads the next chunk of data
      if not data: # if there is no more data, then break the while
        break
      sha512.update(data) # updates SHA-512 with more data to be hashed

  return sha512.digest() # returns the hash in bytes
