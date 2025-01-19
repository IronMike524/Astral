from flask import Flask, render_template, request, redirect, url_for
import webbrowser

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('search_query')
    if query:
        webbrowser.open(query)
        return "URL opened successfully!"
    else:
        return "Please enter a valid URL or search term."

if __name__ == '__main__':
    app.run(debug=True)
