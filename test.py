def save_img():
    with open('imgs/a.png', 'rb') as l:
        content = l.read()
    # content = image.read()
    with open('imgs/b.png', 'wb') as f:
        f.write(content)

save_img()