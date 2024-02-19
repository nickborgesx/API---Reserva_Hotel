# Sistema de Reserva de Hotel - API

### Este é um projeto simples que explora a implementação de uma API em um sistema de reservas de hotel.
### O projeto inclui quatro tabelas no banco de dados:
- Hospede - Representa os hóspedes.
- Hotel - Representa os hotéis.
- Quarto - Representa os quartos do hotel onde as reservas serão efetuadas.
- Reserva - Representa a reserva de um ou mais quartos.
  
![Ilustração do SQL](https://drawsql.app/teams/nicolas-20/diagrams/sistema-hotel)

# Tabelas:

## Tabela: Hospede

- id: Chave primária, não repetível e autoincrementada pelo banco de dados.
- nome: Nome do hóspede.
- email: Email do hóspede.
- cpf: CPF do hóspede.
- telefone: Telefone do hóspede.

## Tabela: Hotel

- id: Chave primária, não repetível e autoincrementada pelo banco de dados.
- nome: Nome do hotel.
- rua: Rua do hotel
- bairro: Bairro do hotel.
- cidade: Cidade onde o hotel está localizado.

## Tabela: Quarto

- id: Chave primária, não repetível e autoincrementada pelo banco de dados.
- numero: Número do quarto
- capacidade: Capacidade de alocação de pessoas no quarto.
- disponível: Verificar se o quarto está disponível.
- hotel_id: ID do quarto que está relacionado ao Hotel.

## Tabela: Reserva

- id: Chave primária, não repetível e autoincrementada pelo banco de dados.
- entrada: Data da entrada do hospede.
- saida: Data da saida do hospede.
- valor: Valor da reserva em relação ao quarto.
- quarto_id: ID do quarto onde a reserva foi marcada.
- hospede_id: ID do hoespede que fez a reserva.
# Endpoints da API

#Endpoints:

## Endpoint: Hospede
hospede/
> GET: Retorna todos os hóspedes cadastrados.

hospede/id/+id
> GET: Retorna informações de um hóspede com base no ID escolhido.

hospede/create
> POST: Cria um novo hóspede passando os parâmetros escolhidos.

hospede/delete/+id
> DELETE: Deleta um hóspede com base no ID escolhido.

hospede/update/+id
> PUT: Atualiza as informações de um hóspede com base no ID escolhido.


## Endpoint: Hotel
hotel/
> GET: Retorna todos os hoteis cadastrados.

hotel/id/+id
> GET: Retorna informações de um hotel com base no ID escolhido.

hotel/create
> POST: Cria um novo hotel passando os parâmetros escolhidos.

hotel/delete/+id
> DELETE: Deleta um hotel com base no ID escolhido.

hospede/update/+id
> PUT: Atualiza as informações de um hotel com base no ID escolhido.


## Endpoint: Quarto
quarto/
> GET: Retorna todos os quartos cadastrados em todos os hoteis.

quarto/+hotel_id/+id
> GET: Retorna informações de um quarto com base nos ID's escolhidos.

quarto/create
> POST: Cria um novo quarto passando os parâmetros escolhidos.

quarto/delete/+hotel_id/+id
> DELETE: Deleta um quarto com base nos ID's escolhidos.

quarto/update/+hotel_id/+id
> PUT: Atualiza as informações de um quarto com base nos ID's escolhidos.

quarto/disponiveis/"true or false"
> GET: Verifica todos os quartos que estão disponíveis ou não.

## Endpoint: Reserva
reserva/
> GET: Retorna todas as reservas dos hoteis.

reserva/+hotel_id
> GET: Retorna todas as reservas de um hotel determinado.

reserva/+id
> GET: Retorna uma reserva de com o id determinado independente do hotel escolhido.

reserva/create
> POST: Cria uma nova reserva passando os parâmetros escolhidos.

reserva/update/+hotel_id/+id
> PUT: Atualiza as informações de uma reserva com base nos ID's escolhidos.

reserva/delete/+hotel_id/+id
> DELETE: Deleta uma reeserva com base nos ID's escolhidos.

