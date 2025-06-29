from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    shift = int(shift)
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        text = request.form['text']
        shift = request.form['shift']
        mode = request.form['mode']

        if not shift.isdigit():
            result = "Shift must be a number."
        else:
            result = caesar_cipher(text, shift, mode)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
