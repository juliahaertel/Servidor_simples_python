# Servidor Simples em Python

Este projeto consiste em um servidor web simples e um cliente de ping UDP. Você pode escolher entre as duas tarefas quando executar o programa.


**Nota: Este projeto foi desenvolvido como parte da disciplina de Redes de Computadores. Espero que goste. :)**

## Opção 1: Servidor Web Simples

Este é um servidor web simples que pode responder a solicitações HTTP básicas.

### Funcionalidade
- O servidor é vinculado ao endereço `localhost` na porta `80`.
- Aguarda a conexão de um cliente.
- Recebe uma solicitação HTTP.
- Analisa a solicitação para obter o nome do arquivo solicitado.
- Se o arquivo existir, lê seu conteúdo e retorna uma resposta HTTP "200 OK" com o conteúdo.
- Se o arquivo não existir, retorna uma resposta HTTP "404 Not Found".

### Como usar
Para executar o servidor web, siga estas etapas:
1. Execute o script.
2. Digite '1' quando solicitado.
3. Abra um navegador e acesse `http://localhost/index.html` para testar o servidor.

## Opção 2: Cliente Ping UDP

Este é um cliente que envia mensagens de ping UDP para um servidor.

### Funcionalidade
- O cliente envia 10 mensagens de ping UDP para o servidor.
- Registra o tempo de envio de cada mensagem.
- Espera até 1 segundo por uma resposta do servidor.
- Registra o tempo de recebimento de cada resposta.
- Calcula o tempo de ida e volta (RTT) para cada mensagem de ping.
- Exibe as respostas do servidor e os RTTs correspondentes.
- Registra "Request Timed Out" caso o servidor não responda dentro do limite de tempo.

### Como usar
Para executar o cliente de ping UDP, siga estas etapas:
1. Execute o script.
2. Digite '2' quando solicitado.
3. O cliente enviará 10 mensagens de ping UDP e registrará as respostas e os tempos de ida e volta.

