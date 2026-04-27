from flask import Flask, render_template, request, redirect
from pdf_utils import extract_text, highlight
from db import init_db, save_pdf, search_pdf, view_pdf, delete_pdf

app = Flask(__name__)

init_db()


@app.route('/')
def home():
    keyword = request.args.get("q", "")

    rows = search_pdf(keyword)

    return render_template("index.html", rows=rows, keyword=keyword)


@app.route('/upload', methods=["POST"])
def upload():
    file = request.files["pdf"]

    if file.filename == "":
        return "No file is chosen"
    if not file.filename.lower().endswith(".pdf"):
        return "PDF Only"

    # extract text from each page of PDF
    text = extract_text(file)

    # SQLite save 
    save_pdf(file.filename, text)

    return redirect("/")


@app.route("/view/<int:id>")
def view(id):

    row = view_pdf(id)
    keyword = request.args.get("q", "")

    return render_template("view.html", row=row, content=highlight(row[1], keyword))


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):

    delete_pdf(id)

    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)