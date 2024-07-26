from datetime import datetime

class Agenda:
    def __init__(self):
        self.eventos = []

    def adicionar_evento(self, nome, inicio, fim):
        if(nome == None or nome == ""):
            return "Falha ao adicionar evento."
        
        if(inicio != None or inicio != ""):
            try:
                datetime.strptime(inicio, "%Y-%m-%d %H:%M")
            except ValueError:
                return "Falha ao adicionar evento."
        else:
            return "Falha ao adicionar evento."

        if(fim != None or fim != ""):
            try:
                datetime.strptime(fim, "%Y-%m-%d %H:%M")
            except ValueError:
                return "Falha ao adicionar evento."
        else:
            return "Falha ao adicionar evento."

        inicio_dt = datetime.strptime(inicio, "%Y-%m-%d %H:%M")
        fim_dt = datetime.strptime(fim, "%Y-%m-%d %H:%M")

        for evento in self.eventos:
            if not (fim_dt <= evento["inicio"] or inicio_dt >= evento["fim"]):
                return "Conflito de agendamento detectado."

        self.eventos.append({
            "nome": nome,
            "inicio": inicio_dt,
            "fim": fim_dt
        })
        return "Evento adicionado com sucesso."
    
    def remover_evento(self, nome):
        if(nome == None or nome == ""):
            return "Falha ao remover evento."

        for evento in self.eventos:
            if evento["nome"] == nome:
                self.eventos.remove(evento)
                return "Evento removido com sucesso."
        return "Evento não encontrado."
    
    def mostrar_agenda(self):
        agenda = str()
        for evento in self.eventos:
            agenda += f"{evento['nome']}: {evento['inicio'].strftime('%Y-%m-%d %H:%M')} a {evento['fim'].strftime('%Y-%m-%d %H:%M')}\n"
        return agenda
    
