from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

from root.users.custom_form_validators import safe_string, unique_or_current_user_field


class RegistrationForm(FlaskForm):
    """Register a new user with email, username, and password"""
    email = StringField(
        "Email",
        description="your@email.com...",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    username = StringField(
        "Username",
        description="Username...",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Username is already taken."),
            safe_string(),
            Length(min=3, max=20),
        ],
    )
    company_name = StringField(
        "Company name",
        description="Company name...",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Company name is already taken."),
            safe_string(),
            Length(min=6, max=25),
        ],
    )
    password = PasswordField(
        "Password",
        description="Password",
        validators=[DataRequired(), Length(min=8, max=30)],
    )
    pass_confirm = PasswordField(
        "Confirm password",
        description="Password confirm",
        validators=[
            DataRequired(),
            EqualTo("pass_confirm", message="Passwords Must Match!"),
        ],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    """Allow users to log in with username or email compared against a pw"""

    username_or_email = StringField(
        "Username or email",
        description="Username or email",
        validators=[DataRequired()],
    )
    password = PasswordField(
        "Password", description="Password", validators=[DataRequired()]
    )
    submit = SubmitField("Log In")


class SettingsForm(FlaskForm):
    """Allow users to update their name, username, email, and password"""

    company_name = StringField(
        "Company name",
        description="New company name",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Company name is already taken."),
            safe_string(),
            Length(min=6, max=25),
        ],
    )
    username = StringField(
        "Username",
        description="New username",
        validators=[
            DataRequired(),
            unique_or_current_user_field("Username already exists."),
            safe_string(),
            Length(min=3, max=20),
        ],
    )
    email = StringField(
        "Email",
        description="your@email.com",
        validators=[
            DataRequired(),
            Email(),
            unique_or_current_user_field("Email is already registered."),
        ],
    )
    new_pass = PasswordField(
        "New Password",
        description="New password",
        validators=[Optional(), Length(min=8, max=30)],
    )
    pass_confirm = PasswordField(
        "Confirm password",
        description="Confirm password",
        validators=[Optional(), EqualTo("new_pass", message="Passwords Must Match!")],
    )
    submit = SubmitField("Update")