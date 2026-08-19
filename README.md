# 🔗 API REST - Agenda de Contatos

API REST desenvolvida em Python com Flask e SQLAlchemy, sem interface HTML — toda comunicação é feita via JSON. Cada usuário possui login próprio e gerencia sua lista de contatos de forma independente.

## Funcionalidades
- 🔐 Cadastro e login de usuários (senha protegida com hash)
- 👤 Autenticação via sessão
- ✅ CRUD completo de contatos (criar, listar, buscar, editar, remover), vinculados ao usuário autenticado

## Endpoints

| Método | Rota                  | Descrição                          |
|--------|-----------------------|-------------------------------------|
| POST   | `/cadastro`           | Cria um novo usuário               |
| POST   | `/login`              | Autentica o usuário                |
| GET    | `/contatos`           | Lista os contatos do usuário       |
| POST   | `/contatos`           | Adiciona um novo contato           |
| GET    | `/contatos/<id>`      | Busca um contato específico        |
| PUT    | `/contatos/<id>`      | Edita um contato existente         |
| DELETE | `/contatos/<id>`      | Remove um contato                  |

## Como executar
1. Clone o repositório
2. Crie um ambiente virtual e instale as dependências
3. Crie um arquivo `.env` com a variável `SECRET_KEY`
4. Execute o arquivo `app.py`

```bash
pip install -r requirements.txt
python app.py
```

## Testando a API
Recomendado usar o [Postman](https://www.postman.com/) para testar os endpoints, já que não há interface visual.

## Tecnologias
- Python 3
- Flask
- SQLAlchemy (ORM)
- SQLite
- Werkzeug (hash de senha)

## Autor
João Pauletti