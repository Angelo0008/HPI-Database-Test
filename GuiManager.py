from Imports import *
import VariableManager
import ExecutableManager

def StopProgram():
    VariableManager.root.destroy()

def showGui():
    #Fixing Blur
    windll.shcore.SetProcessDpiAwareness(1)

    VariableManager.root = tk.Tk()
    VariableManager.root.title('FC1 Compiler')
    # VariableManager.root.iconbitmap('Icons/HiblowLogo.ico')
    VariableManager.root.geometry('600x650+50+50')
    VariableManager.root.resizable(True, True)

    #Tab Notebook
    tabControl = ttk.Notebook(VariableManager.root)

    VariableManager.tab1 = tk.Frame(tabControl)
    VariableManager.tab2 = tk.Frame(tabControl)

    tabControl.add(VariableManager.tab1, text ='Csv To Sql')
    tabControl.add(VariableManager.tab2, text ='CompiledProcess To Sql')
    tabControl.pack(expand = 1, fill ="both")

    # configure the grid
    VariableManager.tab1.columnconfigure(0, weight=1)
    VariableManager.tab1.columnconfigure(1, weight=1)

    VariableManager.tab2.columnconfigure(0, weight=1)
    VariableManager.tab2.columnconfigure(1, weight=1)
    VariableManager.tab2.columnconfigure(2, weight=1)
    VariableManager.tab2.columnconfigure(3, weight=1)







    #TAB 1__________________________________________________________________________

    # place a label on the VariableManager.root window
    message = tk.Label(VariableManager.tab1, text="Csv To Sql", font=("Arial", 12, "bold"))
    message.grid(column=0, row=0, columnspan=2)

    #Process1________________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process1", font=("Arial", 12, "bold"))
    message.grid(column=0, row=1, sticky="w")

    #Loading Spinner
    VariableManager.process1Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process1Loading.grid(column=1, row=1, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Process2______________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process2", font=("Arial", 12, "bold"))
    message.grid(column=0, row=2, sticky="w")

    #Loading Spinner
    VariableManager.process2Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process2Loading.grid(column=1, row=2, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Process3____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process3", font=("Arial", 12, "bold"))
    message.grid(column=0, row=3, sticky="w")

    #Loading Spinner
    VariableManager.process3Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process3Loading.grid(column=1, row=3, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Process4____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process4", font=("Arial", 12, "bold"))
    message.grid(column=0, row=4, sticky="w")

    #Loading Spinner
    VariableManager.process4Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process4Loading.grid(column=1, row=4, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Process5____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process5", font=("Arial", 12, "bold"))
    message.grid(column=0, row=5, sticky="w")

    #Loading Spinner
    VariableManager.process5Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process5Loading.grid(column=1, row=5, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Process6____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Process6", font=("Arial", 12, "bold"))
    message.grid(column=0, row=6, sticky="w")

    #Loading Spinner
    VariableManager.process6Loading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.process6Loading.grid(column=1, row=6, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #Inspection Machine____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Inspection Machine", font=("Arial", 12, "bold"))
    message.grid(column=0, row=7, sticky="w")

    #Loading Spinner
    VariableManager.inspectionMachineLoading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.inspectionMachineLoading.grid(column=1, row=7, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________

    #UclLcl____________________________________________________________________________
    message = tk.Label(VariableManager.tab1, text="Ucl Lcl", font=("Arial", 12, "bold"))
    message.grid(column=0, row=8, sticky="w")

    #Loading Spinner
    VariableManager.uclLclLoading = tk.Label(VariableManager.tab1, font=("Arial", 14))
    VariableManager.uclLclLoading.grid(column=1, row=8, padx=10, pady=10, sticky="w")
    #____________________________________________________________________________________





    #TAB 2_________________________________________________________________________________

    # place a label on the VariableManager.root window
    message = tk.Label(VariableManager.tab2, text="CompiledProcess To Sql", font=("Arial", 12, "bold"))
    message.grid(column=0, row=0, columnspan=4)

    message = tk.Label(VariableManager.tab2, text="Select Date:", font=("Arial", 12, "bold"))
    message.grid(column=0, row=1, sticky="w")
 
    #Calender Picker
    VariableManager.calendarPicker = DateEntry(VariableManager.tab2, width=16, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy/mm/dd')
    VariableManager.calendarPicker.grid(column=1, row=1, pady=20, sticky="w")

    compileButton = tk.Button(VariableManager.tab2, text='COMPILE', font=("Arial", 10), command = "StartProgram", width=8, height=0)
    compileButton.grid(column=0, row=3, ipadx=5, ipady=5, pady=20, sticky="w")
    compileButton.config(bg="lightgreen", fg="black")

    #________________________________________________________________________________
    



    #Starting Thread
    threading.Thread(target=ExecutableManager.RunProcess1ToSql).start()
    threading.Thread(target=ExecutableManager.RunProcess2ToSql).start()
    threading.Thread(target=ExecutableManager.RunProcess3ToSql).start()
    threading.Thread(target=ExecutableManager.RunProcess4ToSql).start()
    threading.Thread(target=ExecutableManager.RunProcess5ToSql).start()
    threading.Thread(target=ExecutableManager.RunProcess6ToSql).start()
    threading.Thread(target=ExecutableManager.RunInspectionMachineToSql).start()

    # threading.Thread(target=ExecutableManager.RunUclLclToSql).start()

    # threading.Thread(target=ExecutableManager.ChangeDate).start()
    

    VariableManager.root.protocol("WM_DELETE_WINDOW", StopProgram)
    VariableManager.root.mainloop()