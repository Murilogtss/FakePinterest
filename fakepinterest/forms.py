from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario
from fakepinterest import bcrypt


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 18)])
    botao_confirmacao = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário não encontrado.')


class FormCriarConta(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    username = StringField('Usuário', validators=[DataRequired(), Length(5, 20)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 18)])
    confirmacao_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado, faça login para continuar.')
    def validate_username(self, username):
        username = Usuario.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('Nome de usuário em uso, escolha outro nome de usuário.')


class FormFoto(FlaskForm):
    foto = FileField('Selecionar foto', validators=[DataRequired()])
    botao_confirmacao = SubmitField('Enviar')
