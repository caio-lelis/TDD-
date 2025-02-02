from datetime import datetime
from agenda import Agenda


class TestAgenda():

    def test_adicionar_evento(self):
        agenda = Agenda()
        nome_evento = "Final dos 100m"
        inicio = "2024-07-24 10:00"
        fim = "2024-07-24 11:00"
        resultado = agenda.adicionar_evento(nome_evento, inicio, fim)
        assert(resultado == "Evento adicionado com sucesso.")


    def test_adicionar_evento_com_conflito(self):
        agenda = Agenda()
        nome_evento1 = "Final dos 100m"
        inicio1 = "2024-07-24 10:00"
        fim1 = "2024-07-24 11:00"
        resultado1 = agenda.adicionar_evento(nome_evento1, inicio1, fim1)
        assert(resultado1 == "Evento adicionado com sucesso.")

        nome_evento2 = "Final dos 200m"
        inicio2 = "2024-07-24 10:30"
        fim2 = "2024-07-24 11:30"
        resultado2 = agenda.adicionar_evento(nome_evento2, inicio2, fim2)
        assert(resultado2 == "Conflito de agendamento detectado.")

    def test_remover_evento(self):
        agenda = Agenda()
        nome_evento = "Final dos 100m"
        inicio = "2024-07-24 10:00"
        fim = "2024-07-24 11:00"
        resultado = agenda.adicionar_evento(nome_evento, inicio, fim)
        assert(resultado == "Evento adicionado com sucesso.")

        resultado = agenda.remover_evento(nome_evento)
        assert(resultado == "Evento removido com sucesso.")

    def test_mostrar_agenda(self):
        agenda = Agenda()
        nome_evento = "Final dos 100m"
        inicio = "2024-07-24 10:00"
        fim = "2024-07-24 11:00"
        resultado = agenda.adicionar_evento(nome_evento, inicio, fim)
        assert(resultado == "Evento adicionado com sucesso.")

        lista_eventos = str()
        eventos = agenda.eventos

        for evento in eventos:
            lista_eventos += f"{evento['nome']}: {evento['inicio'].strftime('%Y-%m-%d %H:%M')} a {evento['fim'].strftime('%Y-%m-%d %H:%M')}\n"

        assert(lista_eventos == agenda.mostrar_agenda())

    def test_entradas_invalidas(self):
        agenda = Agenda()
        nome_evento = ""
        inicio = "24-07-2024 10:00"
        fim = "24-07-2024 11:00"
        resultado = agenda.adicionar_evento(nome_evento, inicio, fim)
        assert(resultado == "Falha ao adicionar evento.")

        nome_evento2 = "Teste"
        inicio2 = "2024-07-24 10:00"
        fim2 = "2024-07-24 11:00"
        resultado2 = agenda.adicionar_evento(nome_evento2, inicio2, fim2)
        assert(resultado2 == "Evento adicionado com sucesso.")

        resultado3 = agenda.remover_evento("")
        assert(resultado3 == "Falha ao remover evento.")



        