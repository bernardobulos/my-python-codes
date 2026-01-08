from personagens import *
from time import sleep

hero = Guerreiro("Hero", 120, 18, 6)
merlin = Mago("Merlin", 70, 25, 2)
slime = PersonagemBasico("Slime", 40, 7, 3)

while True: # Escolha de Personagem
    print("\nPara selecionar um personagem, digite somente seu número correspondente.")
    print("\nPERSONAGENS DISPONÍVEIS:\n[1] Hero\n[2] Merlin")
    escolha = input("Escolha seu personagem: ").strip()[0]
    if escolha == "1":
        jogador = hero
        print(f"Você escolheu \033[33m{jogador.nome}\033[m!\n")
        sleep(1)
        break
    elif escolha == "2":
        jogador = merlin
        print(f"Você escolheu \033[33m{jogador.nome}\033[m!\n")
        sleep(1)
        break
    else:
        print("\033[31mOpção inválida, tente novamente.\033[m")
        sleep(1)
        continue

jogador.mostrar_status()
sleep(1)
slime.mostrar_status()
sleep(1)

rodada = 1
turno_jogador = 1
turno_slime = 1
while True: # Batalha Automática
    print(f"=== [{rodada}º RODADA] ===")
    print(f"[{turno_jogador}º TURNO DE {jogador.nome.upper()}]")
    jogador.atacar(slime)
    if not slime.esta_vivo:
        print("O combate terminou!")
        break
    turno_jogador += 1

    print(f"[{turno_slime}º TURNO DE {slime.nome.upper()}]")
    slime.atacar(jogador)
    if not jogador.esta_vivo:
        print("O combate terminou!")
        break
    turno_slime += 1

    rodada += 1
