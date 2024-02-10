Sistema de Reserva de Hotel - API

Um projeto simples, explorando a concepção de uma API em um sistema refinado de reservas de hotel

O projeto contém 4 tabelas no banco de dados:

Hospede -(Representa os hospedes)
Hotel - ()
Quarto -(Representa o quarto do hotel onde haverá a reserva)
Reserva - (Representa a reserva de um quarto ou mais quartos)


Hospede:

id - Chave Primária, não repetível e auto incrementário pelo banco de dados.
nome - nome do hóspede.
email - email do hóspede.
cpf - cpf do hóspede.
telefone: cpf do hóspede.

--------------------------------------------------------------------------

Hospede/
    GET - Retorna todos os hóspede cadastrados.
Hospede/id/<id>
    GET - Reporta um hóspede baseado no ID escolhido.
Hospede/create
    POST - Cria um hóspede pasando os parâmetros escolhidos.
Hospede/delete/<id>
    DELETE - Deleta um hóspede baseado no ID escolhido.
Hospede/update/<id>
    PUT - Atualiza um hóspede baseado no ID escolhido.
    

