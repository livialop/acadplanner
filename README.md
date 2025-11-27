# AcadPlanner
Sistema para salvar datas de provas, trabalhos e eventos acadêmicos.

# Informações relevantes sobre o repositório

## Como executar a aplicação
* Clone este repositório na sua máquina com o comando 
```cmd
git clone https://github.com/livialop/acadplanner.git
```
* Abra o repositório.
* Navegue até a pasta `src` com o comando `cd src/`.
* Crie o ambiente virtual e ative:
```cmd
python -m venv env
.\env\Scripts\activate
```
> [!NOTE]
> Estou utilizando o Windows 11. Para usuários Linux, troque o comando por: `python3 -m venv env` e `source env/bin/activate`. Para outras versões do Windows que não seja a 11, utilize `py -m venv env`.
* Instale as dependências do projeto com:
```cmd
pip install -r requirements.txt
```
* Inicialize o seu servidor MySQL.
> [!IMPORTANT]
> Cheque as suas configurações no MySQL e, se precisar, troque a configuração no arquivo /src/config/config_database.py
* Localizado no diretório `src`, execute o comando `python app.py`.

## Como navegar pelo repositório
* No diretório `/src` está contido todos os códigos da aplicação. 
    * `/src/config` -> Configuração do banco de dados.
    * `/src/controllers` -> Blueprints da aplicação.
        * `auth` -> Blueprint com rotas de login, registro e logout.
        * `error` -> Blueprint com rotas de error handlers (404, etc). 
        * `main` -> Blueprint com a rota home da aplicação.
        * `events` -> Blueprint com rotas das datas de eventos: editar, adicionar, excluir e visualizar eventos.
> [!IMPORTANT]
> Se precisar mudar alguma coisa referente a porta do banco de dados, user, host e senha, é no arquivo `/src/config/__init__.py` que você deve fazer a alteração. 

* O banco de dados está contido no diretório `/model`
* O diretório `/static` possui subdiretórios referentes ao estilo (`style`) e imagens.
* O diretório `/templates` é onde está localizado os arquivos HTML da aplicação.
* O arquivo `app.py` é o aplicativo onde todos os Blueprints são registrados e assim, a aplicação é executada.