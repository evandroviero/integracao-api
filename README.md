# API REST - Guia Rápido

## O que é uma API REST?

API REST (“Representational State Transfer”) é um estilo de arquitetura para a criação de serviços web. Ela define um conjunto de princípios que garantem a comunicação entre sistemas de forma escalável, simples e eficiente.

## Principais Características

- **Baseada em HTTP:** As APIs REST utilizam os métodos HTTP (GET, POST, PUT, DELETE) para operações CRUD (Create, Read, Update, Delete).
- **Stateless (Sem estado):** Cada requisição HTTP deve conter todas as informações necessárias para ser processada, sem depender de requisições anteriores.
- **Uso de URIs:** Cada recurso é identificado por uma URI (Uniform Resource Identifier) única.
- **Suporte a formatos padronizados:** JSON e XML são os formatos mais comuns para troca de dados.
- **Cacheabilidade:** As respostas podem ser armazenadas em cache para melhorar a performance.

## Exemplos de Métodos HTTP em uma API REST

| Método HTTP | Descrição |
|-------------|------------|
| **GET** | Obtém dados de um recurso. |
| **POST** | Cria um novo recurso. |
| **PUT** | Atualiza um recurso existente. |
| **DELETE** | Remove um recurso. |

## Exemplo de Requisição REST

### Requisição GET para obter uma lista de usuários
```http
GET /usuarios HTTP/1.1
Host: api.exemplo.com
```

### Resposta (JSON)
```json
[
    { "id": 1, "nome": "João" },
    { "id": 2, "nome": "Maria" }
]
```

## Benefícios do Uso de API REST

- Facilidade de integração entre diferentes sistemas.
- Baixo acoplamento entre cliente e servidor.
- Melhor escalabilidade e desempenho.
- Ampla adoção na indústria e compatibilidade com diversas tecnologias.

## Conclusão

As APIs REST são um dos principais padrões utilizados para construção de serviços web modernos. Elas possibilitam a interação entre sistemas de maneira simples, eficiente e escalável. Seu uso é essencial para o desenvolvimento de aplicações web e móveis.

---

### Quer aprender mais?
Explore documentações oficiais, como a [RFC 2616 (HTTP 1.1)](https://www.rfc-editor.org/rfc/rfc2616) e frameworks populares como [Flask](https://flask.palletsprojects.com/) e [Django Rest Framework](https://www.django-rest-framework.org/).

