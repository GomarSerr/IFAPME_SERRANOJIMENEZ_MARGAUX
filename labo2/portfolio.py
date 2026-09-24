from flask import Flask, render_template
portfolio=Flask(__name__)

@portfolio.route ("/")
def accueil():
    return render_template("index.html")

@portfolio.route ("/competences")
def competences():
    return render_template("competences.html")

@portfolio.route ("/experiences")
def experiences():
    return render_template("experiences.html")

@portfolio.route ("/apropos")
def apropos():
    return render_template("apropos.html")


portfolio.run(debug=True)