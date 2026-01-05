# As classes que representam um personagem serão salvas neste arquivo.

class PersonagemBasico: # Molde de Personagem Básico
    def __init__(self, nome, pv, dano_atk, defesa):
        self.nome = nome
        self.pv_total = pv
        self.pv_atual = pv
        self.dano_atk = dano_atk
        self.defesa = defesa
    
    @property
    def esta_vivo(self):
        return self.pv_atual > 0
    
    def mostrar_status(self): # Mostra os status do personagem.
        print(f"STATUS DE {self.nome.upper()}\n • Pontos de Vida: {self.pv_atual}/{self.pv_total}\n • Dano do Ataque: {self.dano_atk}\n • Defesa: {self.defesa}\n")
    
    def receber_dano(self, dano): # O personagem recebe dano.
        if not self.esta_vivo:
            print(f"{self.nome} já está derrotado.\n")
            return
                
        dano_final = max(0, dano - self.defesa)
        self.pv_atual -= dano_final

        if dano_final == 0:
            print(f"{self.nome} evitou todo o dano!\n")
        else:
            if dano_final > 1:
                print(f"{self.nome} recebeu {dano_final} pontos de dano!", end=" ")
            else:
                print(f"{self.nome} recebeu {dano_final} ponto de dano!", end=" ")
        
        if self.pv_atual <= 0:
            self.pv_atual = 0
            print(f"{self.nome} foi derrotado!\n")
        else:
            if self.pv_atual > 1:
                print(f"{self.nome} agora tem {self.pv_atual} pontos de vida.\n")
            else:
                print(f"{self.nome} agora tem {self.pv_atual} ponto de vida.\n")

    def atacar(self, inimigo): # O personagem ataca o inimigo.
        if not self.esta_vivo:
            print(f"{self.nome} não pode atacar, pois foi derrotado.\n")
            return
        
        if not inimigo.esta_vivo:
            print(f"{inimigo.nome} já está derrotado.\n")
            return

        if self.dano_atk > 1:
            print(f"{self.nome} atacou {inimigo.nome} e causou {self.dano_atk} pontos de dano!")
        else:
            print(f"{self.nome} atacou {inimigo.nome} e causou {self.dano_atk} ponto de dano!")
        inimigo.receber_dano(self.dano_atk)



class Guerreiro(PersonagemBasico): # Molde de Guerreiro
    def atacar(self, inimigo): # Ataque do Guerreiro
        if not self.esta_vivo:
            print(f"{self.nome} não pode atacar, pois foi derrotado.\n")
            return
        
        if not inimigo.esta_vivo:
            print(f"{inimigo.nome} já está derrotado.\n")
            return
        
        dano_guerreiro = self.dano_atk + 5
        if dano_guerreiro > 1:
            print(f"{self.nome} atacou {inimigo.nome} com força extra, causando {dano_guerreiro} pontos de dano!")
        else:
            print(f"{self.nome} atacou {inimigo.nome} com força extra, causando {dano_guerreiro} ponto de dano!")
        inimigo.receber_dano(dano_guerreiro)



class Mago(PersonagemBasico): # Molde de Mago
    def atacar(self, inimigo): # Ataque do Mago
        if not self.esta_vivo:
            print(f"{self.nome} não pode atacar, pois foi derrotado.\n")
            return
        
        if not inimigo.esta_vivo:
            print(f"{inimigo.nome} já está derrotado.\n")
            return
        
        dano_mago = self.dano_atk + 8
        if dano_mago > 1:
            print(f"{self.nome} atacou {inimigo.nome} com uma magia, causando {dano_mago} pontos de dano!")
        else:
            print(f"{self.nome} atacou {inimigo.nome} com uma magia, causando {dano_mago} ponto de dano!")
        inimigo.receber_dano(dano_mago)