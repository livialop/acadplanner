# AcadPlanner

Sistema de planejamento acadêmico que funciona como um calendário para guardar provas, seminários, projetos e outros eventos acadêmicos. O sistema conta com um recurso de níveis de relevância para ajudar na organização e priorização das tarefas.

---

## 📁 Navegação do Repositório

`/docs`               → Documentação e anotações do projeto  
`/src`                → Código principal da aplicação  
`/src/controllers`  → Rotas (views/controllers Flask)  
`/src/static`       → Arquivos estáticos (CSS, imagens)  
`/src/templates`    → Páginas HTML (Jinja2)  
`/src/utils`        → Funções auxiliares usadas repetidamente no código  
`/src/config`       → Configuração da aplicação, database e inserção de dados das tabelas domínio  
`/src/models`       → Scripts em SQLAlchemy do banco de dados  


---

## 🌐 Rotas da Aplicação

| Rota | Descrição |
|------|-----------|
| `/` | Página inicial |
| `/user` | Perfil do usuário |
| `/user/edit` | Editar perfil |
| `/events` | Listar eventos |
| `/events/add` | Adicionar novo evento |
| `/events/edit` | Editar evento |
| `/events/delete` | Deletar evento |
| `/register` | Página de registro |
| `/login` | Página de login |
| `/logout` | Fazer logout |
| `/404` | Página não encontrada |
| `/401` | Não autorizado |
| `/500` | Erro interno do servidor |

---

## 📦 Requisitos

- **Python** 3.10+


## 🚀 Como Rodar o Projeto

<details>
<summary>Windows</summary>

### No Windows

**1.** Crie o ambiente virtual:
```cmd
python -m venv env
```

**2.** Ative o ambiente virtual:
```cmd
.\env\Scripts\activate
```

**3.** Instale as dependências:
```cmd
pip install -r requirements.txt
```

**4.** Configure o banco de dados (se necessário, altere as credenciais em `src/config/config_database.py`)

**5.** Execute a aplicação:
```cmd
python app.py
```
</details>

<details>
<summary>Linux</summary>

### No Linux

**1.** Crie o ambiente virtual:
```bash
python3 -m venv env
```

**2.** Ative o ambiente virtual:
```bash
source env/bin/activate
```

**3.** Instale as dependências:
```bash
pip install -r requirements.txt
```

**4.** Configure o banco de dados (se necessário, altere as credenciais em `src/config/config_database.py`)

**5.** Execute a aplicação:
```bash
python app.py
```
</details>

### ⚙️ Configuração do Banco de Dados

> [!IMPORTANT]
> Se você precisar alterar a **porta, usuário, host ou senha** do MySQL (caso for usar), edite o arquivo `src/config/config_database.py` com as suas credenciais.
* O diretório `/static` possui subdiretórios referentes ao estilo (`style`) e imagens.
* O diretório `/templates` é onde está localizado os arquivos HTML da aplicação.
* O arquivo `app.py` é o aplicativo onde todos os Blueprints são registrados e assim, a aplicação é executada.