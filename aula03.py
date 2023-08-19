class AlunoMedia:

    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        pass
    
    
    def executar_media(self, nome, nota1, nota2):
        mediaTotal = (nota1 + nota2) / 2
        
        if mediaTotal >= 7:
            return print(f'{nome} aprovado!')
        else:
            return print(f'{nome} reprovado!')
        

newAluno = AlunoMedia('Gustavo', 5, 7)

newAluno.executar_media(newAluno.nome, newAluno.nota1, newAluno.nota2)

newAluno2 = AlunoMedia('Aline', 8, 9)
newAluno2.executar_media(newAluno2.nome, newAluno2.nota1, newAluno2.nota2)