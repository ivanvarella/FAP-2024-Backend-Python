# Sistema de Agendamento em Python com Tkinter – V3.0
# José Alfredo F. Costa - Agosto 2024
# Materiais para FAP Softex UFRN 2024

import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox
import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scheduler App")
        self.root.geometry("800x600")
        
        self.selected_date = None
        self.schedule = {}
        self.load_schedule()
        
        # Create Calendar
        self.cal = Calendar(root, selectmode='day', year=2024, month=9, day=3)
        self.cal.pack(pady=20)
        
        # Create Buttons
        self.select_date_btn = tk.Button(root, text="Select Date", command=self.select_date)
        self.select_date_btn.pack(pady=10)
        
        self.save_btn = tk.Button(root, text="Save Schedule", command=self.save_schedule)
        self.save_btn.pack(pady=10)
        
        self.export_csv_btn = tk.Button(root, text="Export to CSV", command=self.export_to_csv)
        self.export_csv_btn.pack(pady=10)
        
        self.export_pdf_btn = tk.Button(root, text="Export to PDF", command=self.export_to_pdf)
        self.export_pdf_btn.pack(pady=10)
        
        # Create frame for schedule grid
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=20)
        
        self.create_schedule_grid()
        self.create_notification_system()

    def create_schedule_grid(self):
        # Clear previous grid
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        hours = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
        
        # Create labels for days
        for i, day in enumerate(days):
            tk.Label(self.grid_frame, text=day).grid(row=0, column=i+1)
        
        # Create labels for hours and buttons for schedule slots
        for i, hour in enumerate(hours):
            tk.Label(self.grid_frame, text=hour).grid(row=i+1, column=0)
            for j in range(5):
                btn = tk.Button(self.grid_frame, text="Disponível", width=10, bg="white",
                                command=lambda r=i, c=j: self.toggle_state(r, c))
                btn.grid(row=i+1, column=j+1)
        
        self.update_schedule_grid()
    
    def select_date(self):
        self.selected_date = self.cal.get_date()
        self.schedule.setdefault(self.selected_date, [["Disponível"]*5 for _ in range(9)])
        self.update_schedule_grid()

    def update_schedule_grid(self):
        if self.selected_date:
            schedule_for_date = self.schedule[self.selected_date]
            for i, row in enumerate(schedule_for_date):
                for j, state in enumerate(row):
                    btn = self.grid_frame.grid_slaves(row=i+1, column=j+1)[0]
                    btn.config(text=state, bg=self.get_color_for_state(state))
    
    def toggle_state(self, row, col):
        if not self.selected_date:
            messagebox.showwarning("No Date Selected", "Please select a date first.")
            return
        
        states = ["Disponível", "Ocupado", "Outro"]
        current_state = self.schedule[self.selected_date][row][col]
        next_state = states[(states.index(current_state) + 1) % len(states)]
        self.schedule[self.selected_date][row][col] = next_state
        self.update_schedule_grid()
    
    def get_color_for_state(self, state):
        colors = {"Disponível": "white", "Ocupado": "orange", "Outro": "gray"}
        return colors.get(state, "white")

    def save_schedule(self):
        with open('schedule.json', 'w') as json_file:
            json.dump(self.schedule, json_file)
        messagebox.showinfo("Save Schedule", "Schedule saved successfully.")
    
    def load_schedule(self):
        if os.path.exists('schedule.json'):
            with open('schedule.json', 'r') as json_file:
                self.schedule = json.load(json_file)
    
    def export_to_csv(self):
        if not self.selected_date:
            messagebox.showwarning("No Date Selected", "Please select a date first.")
            return
        
        filename = f"schedule_{self.selected_date.replace('/', '-')}.csv"
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Hora", "Segunda", "Terça", "Quarta", "Quinta", "Sexta"])
            hours = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
            schedule_for_date = self.schedule[self.selected_date]
            for i, row in enumerate(schedule_for_date):
                writer.writerow([hours[i]] + row)
        
        messagebox.showinfo("Export to CSV", f"Schedule exported to {filename}.")

    def export_to_pdf(self):
        if not self.selected_date:
            messagebox.showwarning("No Date Selected", "Please select a date first.")
            return
        
        filename = f"schedule_{self.selected_date.replace('/', '-')}.pdf"
        pdf = canvas.Canvas(filename, pagesize=letter)
        pdf.setTitle(f"Schedule for {self.selected_date}")
        pdf.drawString(100, 750, f"Schedule for {self.selected_date}")
        
        x = 100
        y = 700
        pdf.drawString(x, y, "Hora")
        days = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        for i, day in enumerate(days):
            pdf.drawString(x + (i+1)*60, y, day)
        
        hours = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
        schedule_for_date = self.schedule[self.selected_date]
        for i, row in enumerate(schedule_for_date):
            y -= 20
            pdf.drawString(x, y, hours[i])
            for j, state in enumerate(row):
                pdf.drawString(x + (j+1)*60, y, state)
        
        pdf.save()
        messagebox.showinfo("Export to PDF", f"Schedule exported to {filename}.")

    def create_notification_system(self):
        self.check_for_notifications()

    def check_for_notifications(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        for date, schedule in self.schedule.items():
            if date == now.split(" ")[0]:
                hour = now.split(" ")[1]
                hours = ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
                if hour in hours:
                    index = hours.index(hour)
                    for j, state in enumerate(schedule[index]):
                        if state == "Ocupado":
                            messagebox.showinfo("Notification", f"Reminder: You have a scheduled event at {hour} on {date}.")
        self.root.after(60000, self.check_for_notifications)  # Check every minute

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()