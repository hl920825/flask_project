from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, request, redirect, session, url_for
from apps.cms import cms_bp
from apps.forms.auth_forms import RegisterForm, LoginForm
from apps.models.auth_model import Auth, db


@cms_bp.route("/")
def index():
    return render_template("auth/index.html")


@cms_bp.route("/register/", methods=["GET", "POST"], endpoint="reg")
def auth_register():
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        u1 = Auth()
        u1.username = form.username.data
        # 哈希加密
        u1.password = generate_password_hash(form.password.data)
        db.session.add(u1)
        db.session.commit()
        return redirect(url_for("cms.login"))
    return render_template("auth/reg.html", form=form, flags="注册")


@cms_bp.route('/login/', methods=['GET', 'POST'])
def login():
    error = ""
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        # 根据账号获取模型对象
        d1 = db.session.query(Auth).filter_by(username=username).first()
        # 判断密码是否正确
        if check_password_hash(d1.password, password):
            # 设置session
            session["uid"] = username
            return redirect(url_for("cms.index"))
        error = "用户名或者密码错误!"
    return render_template('auth/reg.html', form=form, flags="登陆", error=error)


@cms_bp.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('cms.login'))
