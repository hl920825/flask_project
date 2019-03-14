from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    username = StringField(
        label="用户名: ",
        validators=[
            validators.DataRequired(message="请输入用户名"),
            validators.Length(min=3, message="不能少于3字符"),
        ],
        render_kw={"class": "form-control", "placeholder": "请输入用户名", "abc": "1122"}
    )
    password = PasswordField(
        label="密 码: ",
        validators=[
            validators.DataRequired(message="请输入密码"),
            validators.Length(min=4, message="不能少于4字符"),
        ],
        render_kw={"class": "form-control", "placeholder": "请输入密码"}
    )


class RegisterForm(LoginForm):
    password1 = PasswordField(
        label="确认密码：",
        validators=[
            validators.DataRequired(message="请输入密码"),
            validators.EqualTo("password", message="两次密码必须一样"),
        ],
        render_kw={'class': 'form-control', 'placeholder': '请确认密码'}
    )
