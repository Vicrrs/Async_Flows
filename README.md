# Async_Flows
O poder de Flask, Celery e RabbitMQ neste projeto prático, destinado a ensinar a implementação eficiente de tarefas assíncronas e sistemas de mensagens em aplicações Python


``` markdown
email_notifications/
│
├── app/
│   ├── __init__.py
│   ├── views.py
│   └── tasks.py
│
├── venv/
│
├── requirements.txt
│
└── run.py

```

Explicação do Código

app/init.py: Configura o Flask e o Celery. Define o Celery para usar o RabbitMQ como broker de mensagens (amqp://localhost//) e rpc:// como backend para resultados de tarefas.
    
app/views.py: Define uma rota onde os usuários podem solicitar o envio de um e-mail. A tarefa é delegada ao Celery, que a executa de forma assíncrona.
    
app/tasks.py: Contém a definição da tarefa do Celery, que neste caso é uma função simples para simular o envio de um e-mail.
    
run.py: Inicia o aplicativo Flask.

Como o Celery e o RabbitMQ são utilizados


Celery: Usa o RabbitMQ como broker para enfileirar tarefas que são executadas de forma assíncrona. Isso permite que a aplicação Flask continue respondendo a outras requisições de usuário enquanto as tarefas mais pesadas ou demoradas são processadas em segundo plano.
    
RabbitMQ: Atua como o intermediário para mensagens entre a instância do Flask e os workers do Celery. Ele gerencia a entrega de tarefas pendentes aos workers disponíveis.

Execução do Projeto

Inicie o RabbitMQ (se necessário).
    
Ative o ambiente virtual e instale as dependências.
    
Execute o Celery worker: celery -A app.celery worker --loglevel=info
    
Inicie o servidor Flask: python run.py
    
Envie requisições POST para http://localhost:5000/send_email com um campo email.
