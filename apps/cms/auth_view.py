from flask import render_template, request
from apps.cms import cms_bp
from apps.forms.auth_forms import RegisterForm, LoginForm
from apps.models.auth_model import Auth, db


@cms_bp.route("/")
def index():
    return render_template("index.html")


@cms_bp.route("/register/", methods=["GET", "POST"], endpoint="reg")
def auth_register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        u1 = Auth()
        u1.username = form.username.data
        u1.password = form.password.data
        db.session.add(u1)
        db.session.commit()
        return "success"
    return render_template("reg.html", form=form, flags="注册")


@cms_bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        return "success"
    return render_template('reg.html', form=form, flags="登陆")
