📦 Projeto de Integração MQTT + RabbitMQ + MongoDB

Este projeto demonstra a integração entre MQTT, RabbitMQ e MongoDB, simulando um fluxo de mensagens entre publicadores e consumidores. A aplicação está configurada para rodar localmente e requer alguns serviços instalados.

✅ Pré-requisitos

Antes de rodar o projeto, certifique-se de ter os seguintes serviços instalados na sua máquina:
Mosquitto
RabbitMQ   
MongoDB

Instale também as dependências Python com o comando:
pip install -r requirements.txt

🚀 Como Executar
Abra quatro terminais e siga a ordem abaixo:

No primeiro terminal inicie o consumidor MQTT
Este processo escuta as mensagens publicadas. Comando: python3 consumer_mqtt.py

No Segundo execute o publisher MQTT
Publica uma mensagem no tópico definido. Comando: python3 publisher_mqtt.py

Verifique a mensagem no RabbitMQ Acesse o painel do RabbitMQ pelo navegador: http://localhost:15672/#/queues

Caso não consiga acessar o painel mesmo com o RabbitMQ instalado, habilite o plugin de gerenciamento com o comando: sudo rabbitmq-plugins enable rabbitmq_management

No terceiro terminal execute o consumidor AMQP
Este processo consome a mensagem da fila do RabbitMQ e a salva no MongoDB. Comando: python3 consumer_amqp.py

🗃️ Verificando os dados no MongoDB

No quarto terminal execute o comando para acessar o shell do mongoDB: mongosh

Dentro do shell do MongoDB, digite os seguintes comandos:
show databases        // Para verfiar os bancos disponíveis
use banco             // Acessa o banco que criamos chamado "banco"
show collections      // Lista as coleções
db.mensagens.find()   // Exibe as mensagens salvas!

