import tkinter
import tkMessageBox
import src.accounting.employeeDB
import src.accounting.receiptsDB
import src.accounting.timecardsDB


class TopGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        #Create a frame
        self.button_frame = tkinter.Frame(self.main_window)


        #Create the button widgets
        self.new_employee_button = tkinter.Button(self.button_frame, text='Employee Info')
        self.view_timecards_button = tkinter.Button(self.button_frame, text='Timecards')
        self.view_pay_rate_button = tkinter.Button(self.button_frame, text='View salary info')
        self.view_sales_data_button = tkinter.Button(self.button_frame, text='View sales info')
        self.change_pay_meth_button = tkinter.Button(self.button_frame, text='Edit Payment Method')
        self.process_payroll_button = tkinter.Button(self.button_frame, text='Process payroll',
                                                     command=self.process_payroll_button)
        self.import_employees_button = tkinter.Button(self.button_frame, text='Import Employees',
                                                     command=self.import_employees_button)
        self.import_timesheets_button = tkinter.Button(self.button_frame, text='Import TimeSheets',
                                                     command=self.import_timesheets_button)
        self.import_receipts_button = tkinter.Button(self.button_frame, text='Import Receipts',
                                                     command=self.import_receipts_button)


        # Pack the labels
        self.button_frame.pack()
        self.new_employee_button.pack()
        self.view_timecards_button.pack()
        self.view_pay_rate_button.pack()
        self.view_sales_data_button.pack()
        self.change_pay_meth_button.pack()
        self.process_payroll_button.pack()
        self.import_employees_button.pack()
        self.import_timesheets_button.pack()
        self.import_receipts_button.pack()

        tkinter.mainloop()

    def import_employees_button(self):
        src.accounting.employeeDB.import_employees()

    def import_timesheets_button(self):
        src.accounting.timecardsDB.import_timecards()

    def import_receipts_button(self):
        src.accounting.receiptsDB.import_receipts()

    def process_payroll_button(self):
        ()



topgui = TopGUI()