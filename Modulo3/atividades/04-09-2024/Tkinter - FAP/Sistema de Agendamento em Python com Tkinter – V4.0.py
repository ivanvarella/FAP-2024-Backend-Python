import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox, simpledialog
import json
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime, timedelta
import bcrypt
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scheduler App")
        self.root.geometry("800x600")
        
        self.selected_date = None
        self.schedule = {}
        self.user_data = {}
        self.current_user = None
        self.load_user_data()
        
        # Authentication
        self.auth_window()

    def auth_window(self):
        self.auth_frame = tk.Frame(self.root)
        self.auth_frame.pack(pady=20)
        
        tk.Label(self.auth_frame, text="Username:").pack()
        self.username_entry = tk.Entry(self.auth_frame)
        self.username_entry.pack()
        
        tk.Label(self.auth_frame, text="Password:").pack()
        self.password_entry = tk.Entry(self.auth_frame, show="*")
        self.password_entry.pack()
        
        tk.Button(self.auth_frame, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.auth_frame, text="Register", command=self.register).pack(pady=10)
    
    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get().encode('utf-8')
        
        if username in self.user_data:
            messagebox.showerror("Error", "Username already exists.")
            return
        
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        self.user_data[username] = {'password': hashed.decode('utf-8'), 'schedule': {}}
        self.save_user_data()
        messagebox.showinfo("Success", "User registered successfully.")
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get().encode('utf-8')
        
        if username not in self.user_data or not bcrypt.checkpw(password, self.user_data[username]['password'].encode('utf-8')):
            messagebox.showerror("Error", "Invalid username or password.")
            return
        
        self.current_user = username
        self.schedule = self.user_data[username]['schedule']
        self.auth_frame.destroy()
        self.load_schedule()
        self.create_main_interface()
    
    def create_main_interface(self):
        # Create Calendar
        self.cal = Calendar(self.root, selectmode='day', year=2024, month=9, day=3)
        self.cal.pack(pady=20)
        
        # Create Buttons
        self.select_date_btn = tk.Button(self.root, text="Select Date", command=self.select_date)
        self.select_date_btn.pack(pady=10)
        
        self.save_btn = tk.Button(self.root, text="Save Schedule", command=self.save_schedule)
        self.save_btn.pack(pady=10)
        
        self.export_csv_btn = tk.Button(self.root, text="Export to CSV", command=self.export_to_csv)
        self.export_csv_btn.pack(pady=10)
        
        self.export_pdf_btn = tk.Button(self.root, text="Export to PDF", command=self.export_to_pdf)
        self.export_pdf_btn.pack(pady=10)
        
        self.search_btn = tk.Button(self.root, text="Search", command=self.search_appointments)
        self.search_btn.pack(pady=10)
        
        self.sync_google_btn = tk.Button(self.root, text="Sync with Google Calendar", command=self.sync_with_google_calendar)
        self.sync_google_btn.pack(pady=10)
        
        # Create frame for schedule grid
        self.grid_frame = tk.Frame(self.root)
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
        self.user_data[self.current_user]['schedule'] = self.schedule
        self.save_user_data()
        messagebox.showinfo("Save Schedule", "Schedule saved successfully.")
    
    def load_schedule(self):
        if self.current_user:
            self.schedule = self.user_data[self.current_user]['schedule']

    def save_user_data(self):
        with open('user_data.json', 'w') as json_file:
            json.dump(self.user_data, json_file)
    
    def load_user_data(self):
        if os.path.exists('user_data.json'):
            with open('user_data.json', 'r') as json_file:
                self.user_data = json.load(json_file)
    
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
    
    def search_appointments(self):
        search_type = simpledialog.askstring("Search", "Search by (client/type):").lower()
        search_query = simpledialog.askstring("Search", f"Enter {search_type}:").lower()
        
        results = []
        for date, schedule in self.schedule.items():
            for i, row in enumerate(schedule):
                for state in row:
                    if search_query in state.lower():
                        results.append((date, state))
        
        if results:
            result_str = "\n".join([f"{date}: {state}" for date, state in results])
            messagebox.showinfo("Search Results", result_str)
        else:
            messagebox.showinfo("Search Results", "No matching appointments found.")

    def sync_with_google_calendar(self):
        # Setup Google Calendar API
        scopes = ['https://www.googleapis.com/auth/calendar']
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes=scopes)
        creds = flow.run_local_server(port=0)
        
        service = build('calendar', 'v3', credentials=creds)
        
        for date, schedule in self.schedule.items():
            for i, row in enumerate(schedule):
                for j, state in enumerate(row):
                    if state == "Ocupado":
                        event = {
                            'summary': 'Scheduled Event',
                            'start': {
                                'dateTime': f'{date}T08:00:00-07:00',
                                'timeZone': 'America/Los_Angeles',
                            },
                            'end': {
                                'dateTime': f'{date}T09:00:00-07:00',
                                'timeZone': 'America/Los_Angeles',
                            },
                        }
                        event = service.events().insert(calendarId='primary', body=event).execute()
        
        messagebox.showinfo("Sync with Google Calendar", "Events synced with Google Calendar.")
    
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
