# ZeroMQ — Exemplos Distribuídos

Três padrões de comunicação com ZeroMQ, refatorados para execução em **máquinas separadas**.  
Cada componente é agora um processo autônomo que recebe o endereço do parceiro via argumento de linha de comando.

---

## Dependência

```bash
pip install pyzmq
```

---

## 1. Cliente-Servidor (Requisição/Resposta)

Padrão REQ/REP: o cliente envia uma mensagem, o servidor responde acrescentando `*` ao final.

### Máquina A — Servidor

```bash
python server.py [porta]
# Exemplo:
python server.py 12345
```

### Máquina B — Cliente

```bash
python client.py [ip_do_servidor] [porta]
# Exemplo:
python client.py 192.168.1.10 12345
```

**Fluxo:** o servidor fica aguardando; inicie-o antes do cliente.  
O cliente envia `"Hello world"`, recebe `"Hello world*"` e depois envia `STOP` para encerrar o servidor.

---

## 2. Publicador-Assinante (Pub/Sub)

Padrão PUB/SUB: o publicador transmite o horário atual a cada 5 segundos; qualquer número de assinantes pode se conectar.

### Máquina A — Publicador

```bash
python publisher.py [porta]
# Exemplo:
python publisher.py 12345
```

### Máquinas B, C, … — Assinante(s)

```bash
python subscriber.py [ip_do_publicador] [porta] [quantidade_de_mensagens]
# Exemplo:
python subscriber.py 192.168.1.10 12345 5
```

**Fluxo:** inicie o publicador primeiro; depois inicie um ou mais assinantes em máquinas distintas.  
Cada assinante recebe mensagens independentemente dos demais.

---

## 3. Produtor-Consumidor (Pipeline / Push-Pull)

Padrão PUSH/PULL: o produtor distribui cargas de trabalho entre os workers disponíveis usando balanceamento de carga round-robin automático do ZeroMQ.

### Máquina A — Produtor

```bash
python producer.py [porta] [numero_de_workers]
# Exemplo:
python producer.py 12345 4
```

O parâmetro `numero_de_workers` ajusta o ritmo de produção para não sobrecarregar os consumidores.

### Máquinas B, C, D, … — Workers (uma instância por máquina, ou várias)

```bash
python worker.py [id_do_worker] [ip_do_produtor] [porta]
# Exemplos (em máquinas diferentes):
python worker.py 1 192.168.1.10 12345
python worker.py 2 192.168.1.10 12345
python worker.py 3 192.168.1.10 12345
```

**Fluxo:** inicie o produtor primeiro; depois inicie qualquer número de workers em máquinas separadas.  
O ZeroMQ distribui cada tarefa ao próximo worker disponível (round-robin). Adicionar ou remover workers não requer nenhuma alteração no produtor.

---

## Resumo das diferenças em relação ao código original

| Aspecto | Original | Distribuído |
|---|---|---|
| Execução | Um único processo com `multiprocessing` | Processos independentes em máquinas distintas |
| Endereço de conexão | `localhost` fixo no código | Passado como argumento (`sys.argv`) |
| Binding | `127.0.0.1` (loopback) | `*` (todas as interfaces de rede) |
| Workers | Número fixo (`NWORKERS`) instanciado no `main` | Qualquer número, iniciados manualmente |
