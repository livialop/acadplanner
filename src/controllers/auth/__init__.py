from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import User, engine
from sqlalchemy.orm import sessionmaker

auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # O operador | funciona como um OU -> no bd, ele pega o que encontrar primeiro: OU o email OU o user do usuario
        Session = sessionmaker(bind=engine)
        with Session() as session:
            existing_user = session.query(User).filter((User.username == username) | (User.email == email)).first()
            if existing_user:
                flash('Usuário ou login já cadastrado.', category='error')
                return redirect(url_for('auth.register'))

            else: # Se o user não for cadastrado
                new_user = User(
                    name=name,
                    username=username,
                    email=email,
                    password=generate_password_hash(password)
                )
                session.add(new_user)
                session.commit()
                flash('Cadastro realizado com sucesso! Faça login.', category='success')
                return redirect(url_for('auth.login'))
        
    elif request.method == 'GET':
        return render_template('register.html')
    

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email_or_username')
        password = request.form.get('password')

        # O operador | funciona como um OU -> no bd, ele pega o que encontrar primeiro: OU o email OU o user do usuario
        Session = sessionmaker(bind=engine)
        with Session() as session:
            user = session.query(User).filter((User.email == email_or_username) | (User.username == email_or_username)).first()
            
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Login realizado com sucesso!', category='success')
                return redirect(url_for('events.dashboard')) # ISSO PODE MUDAR POSTERIORMENTE. VERIFICAR O NOME DA ROTA.

            else:
                flash('Credenciais inválidas. Tente novamente.', category='error')
                return redirect(url_for('auth.login'))
        
    elif request.method == 'GET':
        return render_template('login.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta.', category='success')
    return redirect(url_for('main.home'))