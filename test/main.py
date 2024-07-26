from agenda import Agenda

def main():
    agenda = Agenda()

    while True:
        acao = input("Digite a ação (adicionar, remover, mostrar, sair): ").strip().lower()

        if acao == "adicionar":
            nome = input("Digite o nome do evento: ")
            h_inicio = input("Digite a hora de início (YYYY-MM-DD HH:MM): ")
            h_fim = input("Digite a hora de término (YYYY-MM-DD HH:MM): ")

            print(f"{agenda.adicionar_evento(nome, h_inicio, h_fim)}\n")
        elif acao == "remover":
            nome = input("Digite o nome do evento para remover: ")

            print(f"{agenda.remover_evento(nome)}\n")
        elif acao == "mostrar":
            lista_eventos = str()
            lista_eventos += agenda.mostrar_agenda()

            if(lista_eventos == ""):
                print("Nenhum evento agendado.\n")
            else:
                print(f"{lista_eventos}")
        elif acao == "sair":
            break
        else:
            print("Ação inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    