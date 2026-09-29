# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar livros usando FastAPI. Você vai praticar endpoints HTTP, validação de dados com modelos Pydantic e respostas apropriadas para operações CRUD.

## 📝 Tarefas

### 🛠️ Criar um Endpoint para a Coleção de Livros

#### Descrição
Execute o código inicial e consulte a documentação interativa em `/docs`. Em seguida, implemente `GET /books` para retornar a coleção de livros fornecida no starter code.

#### Requisitos
O programa concluído deve:

- Instalar as dependências com `pip install fastapi uvicorn`
- Iniciar com `python -m uvicorn starter-code:app --reload`
- Retornar a coleção de livros em `GET /books`
- Usar os modelos Pydantic fornecidos para representar cada livro


### 🛠️ Adicionar Endpoint de Criação com Validação

#### Descrição
Adicione `POST /books` para receber os dados de um livro novo. Use um modelo Pydantic de entrada sem o campo `id`; a API deve atribuir um identificador e armazenar o livro.

#### Requisitos
O programa concluído deve:

- Validar `title`, `author` e `year` com um modelo Pydantic
- Atribuir um `id` único e incluir o novo livro na coleção
- Retornar o livro criado com status HTTP `201 Created`
- Retornar erros de validação para dados ausentes ou inválidos

Exemplo de corpo da requisição:

```json
{
  "title": "A Wizard of Earthsea",
  "author": "Ursula K. Le Guin",
  "year": 1968
}
```


### 🛠️ Implementar Operações CRUD para Livros

#### Descrição
Complete a API adicionando consulta de um livro por identificador, atualização de um livro existente e remoção. Use códigos HTTP que indiquem claramente o resultado de cada operação.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books/{book_id}` e retornar `404 Not Found` quando o livro não existir
- Implementar `PUT /books/{book_id}` para atualizar os dados de um livro existente
- Implementar `DELETE /books/{book_id}` e retornar `204 No Content` após a remoção
- Verificar os endpoints na documentação interativa em `/docs`, incluindo casos de sucesso e de livro inexistente