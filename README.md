# Sistema de Reserva de Hotel - API

### Este é um projeto simples que explora a implementação de uma API em um sistema refinado de reservas de hotel.
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
