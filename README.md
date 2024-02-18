# Sistema de Reserva de Hotel - API

### Este é um projeto simples que explora a implementação de uma API em um sistema de reservas de hotel.
### O projeto inclui quatro tabelas no banco de dados:
- Hospede - Representa os hóspedes.
- Hotel - Representa os hotéis.
- Quarto - Representa os quartos do hotel onde as reservas serão efetuadas.
- Reserva - Representa a reserva de um ou mais quartos.

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

## Endpoint: Hospede
Hospede/
> GET: Retorna todos os hóspedes cadastrados.

Hospede/id/+id
> GET: Retorna informações de um hóspede com base no ID escolhido.

Hospede/create
> POST: Cria um novo hóspede, passando os parâmetros escolhidos.

Hospede/delete/+id
> DELETE: Deleta um hóspede com base no ID escolhido.

Hospede/update/+id
> PUT: Atualiza as informações de um hóspede com base no ID escolhido.
