text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
        'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
text = text.split()
new_text = []

for word in text:
    if word[-1] in ',.':
        word = word[:-1] + 'ing' + word[-1]
    else:
        word += 'img'
    new_text.append(word)

new_text = ' '.join(new_text)
print(new_text)
