"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template

@bp.route("/dashboard") # cria uma rota para navegador
def dashboard(): # função que gerencia rota deve ser única
    """ Painel de Vendas"""
    #  if 'user' not in session:  # garante autenticação
    #       return redirect(url_for("auth.login"))
    import locale 
    #Define a localização para portugues brasileiro 
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    vendas: list = [
        {"mes":"Janeiro", "total": 13519.19 }, 
        {"mes":"Fevereiro", "total": 15985.50},
        {"mes":"Março", "total": 11899.45},
        {"mes":"Abril", "total": 8647.90},
        {"mes":"Maio", "total": 12988.59},
        {"mes":"Junho", "total": 7546.58},
        {"mes":"Julho", "total": 9887.78},
        {"mes":"Agosto", "total": 11875.68},
        {"mes":"Setembro", "total": 12843.77},
        {"mes":"Outubro", "total": 13847.54},
        {"mes":"Novembro", "total": 10980.63},
        {"mes":"Dezembro", "total": 15983.75},
    ]#fim da lista de vendas
    
    return render_template("dashboard/index.html", title="Painel de Vendas", vendas=vendas, locale=locale) # Renderiza um template
