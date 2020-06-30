from flask import Flask, render_template
from itertools import islice
from googletrans import Translator


app = Flask(__name__)


def translator(text):
    translator = Translator()
    trans = translator.translate(text)
    return trans.text


def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))


@app.route('/', defaults={'filename': 'file1.txt'})
@app.route('/<string:filename>')
def file_data(filename):
    try:
        filename, start_line, end_line = filename.split("_")
    except Exception as e:
        filename = filename.split("_")[0]
        start_line, end_line = None, None
    with open(filename, 'r', encoding="utf8", errors='ignore') as f:
        a = []
        if start_line and end_line is not None:
            for line in islice(f, int(start_line), int(end_line)):
                print(line)
                data = a.append(line)
            data = listToString(a)
            return render_template('content.html', text=data)
        else:
            try:
                data = f.read()
                data = translator(data)
            except Exception as e:
                data = f.read()
            return render_template('content.html', text=data)


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=False)
