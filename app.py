from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template(template_name_or_list='index.html')

@app.route("/events")
def events():
    return render_template(template_name_or_list='events.html')

@app.route("/how-to-join")
def how_to_join():
    return render_template(template_name_or_list='how-to-join.html')

@app.route("/maps")
def maps():
    return render_template(template_name_or_list='maps.html')

@app.route("/news")
def news():
    return render_template(template_name_or_list='news.html')

@app.route("/resources")
def resources():
    return render_template(template_name_or_list='resources.html')

@app.route("/about")
def about():
    return render_template(template_name_or_list='about.html')

@app.route("/contact")
def contact():
    return render_template(template_name_or_list='contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
