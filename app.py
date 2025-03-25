from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template(template_name_or_list='index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
