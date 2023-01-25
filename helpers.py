import os
from Jogos import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.length(min=1, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.length(min=1, max=40)])
    plataforma = StringField('Plataforma', [validators.DataRequired(), validators.length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.length(min=1, max=8)])
    senha = StringField('Senha', [validators.DataRequired(), validators.length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_img(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo


    return 'capa_padrao.jpg'


def deleta_arq(id):
    arquivo = recupera_img(id)
    if arquivo != 'capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH']), arquivo)