
class Horario:
    def __init__(self, hora, minuto, segundo):
        self.hora = int(hora)
        self.minuto = int(minuto)
        self.segundo = int(segundo)

    def incrementar_segundos(self, segundos):
        self.segundo += segundos

        while self.segundo >= 60:
            self.segundo -= 60
            self.minuto += 1

        while self.minuto >= 60:
            self.minuto -= 60
            self.hora += 1

        while self.hora >= 24:
            self.hora -= 24

    def diferenca_em_segundos(self, outro_horario):
        total_self = self.hora * 3600 + self.minuto * 60 + self.segundo
        total_outro = outro_horario.hora * 3600 + outro_horario.minuto * 60 + outro_horario.segundo
        return abs(total_self - total_outro)

    def mostrar(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"
    
h1 = Horario(10, 15, 30)
h2 = Horario(12, 45, 15)

print("Horário 1:", h1.mostrar())
print("Horário 2:", h2.mostrar())

# Incrementar segundos
h1.incrementar_segundos(125)
print("Horário 1 após incremento:", h1.mostrar())

# Diferença entre horários
print("Diferença em segundos:", h1.diferenca_em_segundos(h2))
