## Muitos tutoriais de API ensinam apenas o mínimo absoluto. Mas uma API pronta para produção é muito mais complicada do que a maioria dos tutoriais ensina.

### Acabamos de publicar um curso massivo de 19 horas no canal freeCodeCamp.org do YouTube que irá ensiná-lo a construir uma API completa usando Python e a biblioteca FastAPI

### Sanjeev Thiyagarajan desenvolveu este curso. Sanjeev é um ótimo professor e realmente sabe como decompor as coisas para iniciantes.

### A API construída neste curso é para um ambiente social aplicativo de tipo de mídia onde os usuários podem criar / ler / excluir / atualizar postagens, bem como postagens de outros usuários. Inclui registro e autenticação do usuário.

### Primeiro, você aprenderá os fundamentos do design de API, incluindo rotas, serialização / desserialização, validação de esquema e modelos. Você também aprenderá como configurar e usar bancos de dados SQL.

### Em seguida, você aprenderá como integrar a API com o banco de dados usando consultas SQL brutas e com o SqlAlchemy ORM. Postgres é usado como banco de dados, mas tudo o que você aprender será aplicável a quase qualquer outro banco de dados SQL.

### A seguir, você aprenderá como configurar o teste do aplicativo usando a biblioteca pytest. Você configurará um banco de dados de teste e executará um bom número de testes de integração.

### Depois de criar a API, você aprenderá como implantar a API usando dois métodos diferentes. O primeiro é implantar em uma máquina Ubuntu e o segundo é implantar no Heroku. Você ainda aprenderá como encaixar o aplicativo.

### Finalmente, você aprenderá como construir um pipeline de CI / CD usando ações do GitHub.

### Aqui está uma lista completa dos tópicos abordados neste curso abrangente:

## Seção 1: introdução
    ° Projeto de Curso
    ° Introdução ao curso
    ° Visão geral do projeto do curso

## Seção 2: configuração e instalação
    ° Instalação Mac Python
    ° Instalação e configuração do Mac VS Code
    ° Instalação do Windows Python
    ° Instalação e configuração do Windows VS Code
    ° Noções básicas do ambiente virtual Python
    ° Ambiente virtual em windows
    ° Ambiente virtual no Mac

## Seção 3: FastAPI
    ° Instale dependências com pip
    ° Iniciando API Fast
    ° Operações de caminho
    ° Ordem de operação do caminho (sim, importa)
    ° Introdução ao Carteiro
    ° Solicitações HTTP Post
    ° Validação de esquema com Pydantic
    ° Operações CRUD
    ° Armazenamento de postagens em Array
    ° Criando postagens
    ° Coleções do carteiro e pedidos de salvamento
    ° Recuperar uma postagem
    ° A ordem do caminho é importante
    ° Alteração dos códigos de status de resposta
    ° Exclusão de postagens
    ° Atualizando Postagens
    ° Documentação Automática
    ° Pacotes Python

## Seção 4: Bancos de dados:
    ° Introdução ao banco de dados
    ° Instalação do Postgres Windows
    ° Postgres Mac Install
    ° Esquema e tabelas do banco de dados
    ° Gerenciando Postgres com PgAdmin GUI
    ° Sua primeira consulta SQL
    ° Filtre os resultados com a palavra-chave "onde"
    ° Operadores SQL
    ° IN palavra-chave
    ° Correspondência de padrões com a palavra-chave LIKE
    ° Resultados de pedidos
    ° LIMIT E OFFSET
    ° Inserindo Dados
    ° Exclusão de dados
    ° Atualizando Dados

## Seção 5: Python + SQL bruto:
    ° Configurar banco de dados de aplicativos
    ° Conectando-se ao banco de dados com Python
    ° Recuperando Postagens
    ° Criando postagem
    ° Obtenha uma postagem
    ° Apague a postagem
    ° Postagem de atualização

## Seção 6: ORMs:
    ° Introdução ORM
    ° Configuração SQLALCHEMY
    ° Adicionando coluna CreatedAt
    ° Obter todas as postagens
    ° Criar Postagens
    ° Obter postagem por ID
    ° Apague a postagem
    ° Postagem de atualização

## Seção 7: Modelos Pydantic:
    ° Modelos Pydantic vs ORM
    ° Mergulho Profundo de Modelos Pydantic
    ° Modelo de Resposta

## Seção 8: Autenticação e usuários:
    ° Criando Tabela de Usuários
    ° Operação do caminho de registro do usuário
    ° Hashing de senhas de usuário
    ° Lógica de hash do refrator
    ° Obter usuário por ID
    ° Roteadores FastAPI
    ° Prefixo do roteador
    ° Tags de roteador
    ° Noções básicas de token JWT
    ° Processo de Login
    ° Criação de um token
    ° OAuth2 PasswordRequestForm
    ° Verifique se o usuário está conectado
    ° Corrigindo Bugs
    ° Protegendo Rotas
    ° Token expirado de teste
    ° Buscando usuário em rotas protegidas
    ° Recursos avançados do Postman

## Seção 9: Relacionamentos:
    ° Noções básicas de relacionamento SQL
    ° Postgres Foreign Keys
    ° SQLAlchemy Foreign Keys
    ° Atualizar o Post Schema para incluir o usuário
    ° Atribuindo ID de proprietário ao criar uma nova postagem
    ° Exclua e atualize apenas suas próprias postagens
    ° Recuperando apenas as postagens do usuário conectado
    ° Relacionamentos Sqlalchemy
    ° Parâmetros de consulta
    ° Limpe nosso arquivo main.py
    ° Variáveis de Ambiente

## Seção 10: Sistema de votar / curtir:
    ° Teoria do Voto / Gosto
    ° Mesa de Votos
    ° Votos Sqlalchemy
    ° Rota de votos
    ° SQL Joins
    ° Junta-se ao SqlAlchemy
    ° Obtenha uma postagem com associações