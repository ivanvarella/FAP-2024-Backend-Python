# Sistema de Agendamento em Python com Tkinter – V1.0
# José Alfredo F. Costa - Agosto 2024
# Materiais para FAP Softex UFRN 2024

import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime, timedelta

class SistemaAgendamento:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Agendamento")
        
        self.criar_calendario()
        self.criar_grade_horarios()
        
    def criar_calendario(self):
        self.cal_frame = ttk.Frame(self.root)
        self.cal_frame.pack(pady=10)
        
        self.ano_atual = datetime.now().year
        self.mes_atual = datetime.now().month
        
        self.cal_label = ttk.Label(self.cal_frame, text=f"{calendar.month_name[self.mes_atual]} {self.ano_atual}")
        self.cal_label.grid(row=0, column=1, pady=5)
        
        ttk.Button(self.cal_frame, text="<", command=self.mes_anterior).grid(row=0, column=0)
        ttk.Button(self.cal_frame, text=">", command=self.proximo_mes).grid(row=0, column=2)
        
        self.cal = ttk.Treeview(self.cal_frame, columns=("seg", "ter", "qua", "qui", "sex", "sab", "dom"), show="headings", height=6)
        for i, dia in enumerate(["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]):
            self.cal.heading(f"{dia.lower()}", text=dia)
            self.cal.column(f"{dia.lower()}", width=40, anchor="center")
        
        self.cal.grid(row=1, column=0, columnspan=3)
        self.preencher_calendario()
        
    def preencher_calendario(self):
        self.cal.delete(*self.cal.get_children())
        
        cal = calendar.monthcalendar(self.ano_atual, self.mes_atual)
        for semana in cal:
            dados_semana = []
            for dia in semana:
                if dia == 0:
                    dados_semana.append("")
                else:
                    dados_semana.append(str(dia))
            self.cal.insert("", "end", values=dados_semana)
        
    def mes_anterior(self):
        self.mes_atual -= 1
        if self.mes_atual < 1:
            self.mes_atual = 12
            self.ano_atual -= 1
        self.atualizar_calendario()
        
    def proximo_mes(self):
        self.mes_atual += 1
        if self.mes_atual > 12:
            self.mes_atual = 1
            self.ano_atual += 1
        self.atualizar_calendario()
        
    def atualizar_calendario(self):
        self.cal_label.config(text=f"{calendar.month_name[self.mes_atual]} {self.ano_atual}")
        self.preencher_calendario()
        
    def criar_grade_horarios(self):
        self.grade_frame = ttk.Frame(self.root)
        self.grade_frame.pack(pady=10)
        
        horarios = ["08:00", "09:00", "10:00", "11:00", "15:00", "16:00", "17:00", "18:00"]
        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        
        ttk.Label(self.grade_frame, text="Horários").grid(row=0, column=0)
        for i, dia in enumerate(dias):
            ttk.Label(self.grade_frame, text=dia).grid(row=0, column=i+1)
        
        for i, horario in enumerate(horarios):
            ttk.Label(self.grade_frame, text=horario).grid(row=i+1, column=0)
            for j in range(5):
                btn = tk.Button(self.grade_frame, width=10, height=2, bg="white")
                btn.grid(row=i+1, column=j+1)
                btn.bind("<Button-1>", lambda e, h=horario, d=dias[j]: self.agendar(h, d))
        
    def agendar(self, horario, dia):
        print(f"Agendado para {dia} às {horario}")
        # Aqui você pode adicionar a lógica para marcar o horário como ocupado
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaAgendamento(root)
    root.mainloop()