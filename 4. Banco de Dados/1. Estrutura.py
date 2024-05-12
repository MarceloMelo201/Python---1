#Criação da tabela

'''
CREATE TABLE CLIENTES #TABELA COM O NOME 'CLIENTES'
(
    ID INT PRIMARY KEY AUTO_INCREMENT #CRIA UM ID NOVO AUTOMATICAMENTE
    NOME VARCHAR(60) NOT NULL #NOT NULL DIZ QUE O DADO DEVE SER INICIALIZADO
    CPF VARCHAR(11) NOT NULL
    EMAIL VARCHAR(100) NOT NULL

)

'''

#Inserção de Dados

'''

#Botão insert

INSERT INTO `clientes`(`ID`, `NOME`, `CPF`, `EMAIL`) VALUES 
('[value-1]','[value-2]','[value-3]','[value-4]')



'''

#Edição e Exclusão de dados

'''
#Edição de Dados

UPDATE CLIENTES SET VALOR = 'mudança' 
where id = 1

valor = nome, cpf, email, id...

#Exclusão de Dados

DELETE FROM CLIENTES WHERE VALOR = 1

valor = id, nome, cpf, email...

'''

