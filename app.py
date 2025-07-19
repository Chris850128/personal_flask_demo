from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='首頁')

@app.route('/about')
def about():
    return render_template('about.html', title='關於我們')

@app.route('/api/data')
def api_data():
    data = {
        "status": "success",
        "message": "這是 JSON 資料",
        "items": [1, 2, 3, 4]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
