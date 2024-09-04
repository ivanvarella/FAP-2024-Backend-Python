import tkinter as tk
from tkcalendar import Calendar
from tkinter import messagebox

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Scheduler App")
        self.root.geometry("600x600")
        
        self.selected_date = None
        self.schedule = {}
        
        # Create Calendar
        self.cal = Calendar(root, selectmode='day', year=2024, month=9, day=3)
        self.cal.pack(pady=20)
        
        # Create Button to select date
        self.select_date_btn = tk.Button(root, text="Select Date", command=self.select_date)
        self.select_date_btn.pack(pady=10)
        
        # Create frame for schedule grid
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=20)
        
        self.create_schedule_grid()

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

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()
