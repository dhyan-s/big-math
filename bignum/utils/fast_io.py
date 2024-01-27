import mmap

def fast_read(file, fix_improper_newlines=True):
    with open(file, "rb") as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        content = mm.read()
        mm.close()
        content = content.decode("utf-8")
        if fix_improper_newlines:
            content = content.replace("\r", "")
        return content
    
def fast_write(file, text):
    with open(file, "wb") as f:
        text = text.encode()
        f.write(text)
        
def fast_append(file, text):
    with open(file, "ab") as f:
        f.write(text.encode())