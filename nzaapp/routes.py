from flask import render_template,redirect,url_for
from nzaapp import app
from nzaapp.forms import LoginForm, RegisterForm, ContactForm

# Import Models for Routes -- USERNAME, REVIEW, COMMENT
from nzaapp.models import db, Username, Review, Comment

from flask_login import login_user, current_user, logout_user, login_required

@app.route("/home")
def welcome_page():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register_form():
    form= RegisterForm()
    if form.validate_on_submit():
        print("The username is {}".format(form.username.data))
        user=User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()       
        return redirect(url_for("login"))
    else:
        print("Form not valid")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET","POST"])
def login ():
        form = LoginForm()
        user_username= form.username.data
        password= form.password.data
        user = User.query.filter(User.username == user_username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            print(current_user.username)
            return redirect(url_for('hello_world'))
        print(form.username.data, form.password.data)
        return render_template("login.html", form=form)

@app.route("/contact",methods=["GET","POST"])
def contact_form():
    form=ContactForm()
    # Get form data from Contact Us Form -- form.first_name.data
    print(form.first_name.data)
    # Create Comment Instance 
    #contact=Comment()
    # Using db create session to add
    #db.session.add(contact)
    # Using db commit session
    #db.session.commit()
    return render_template("contact.html",form=form)

@app.route("/review")
def review_form():
    form= ReviewForm()
    title=form.title.data
    content=form.content.data
    user_id=current_user.id 
    review= Review(title= title, content = content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return render_template("review.html")