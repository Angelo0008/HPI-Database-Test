from Imports import *
import VariableManager
import CsvReader
import Sql

def RunProcess1ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT1\log000_1.csv')

    while True:
        VariableManager.process1Loading.config(text=VariableManager.spinnerChars[VariableManager.process1LoadingIndex])

        if VariableManager.process1LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process1LoadingIndex += 1
        else:
            VariableManager.process1LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT1\log000_1.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process1Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess1Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess1Table(CsvReader.dfVt1)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process1Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")
        time.sleep(1)

def RunProcess2ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT2\log000_2.csv')

    while True:
        VariableManager.process2Loading.config(text=VariableManager.spinnerChars[VariableManager.process2LoadingIndex])

        if VariableManager.process2LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process2LoadingIndex += 1
        else:
            VariableManager.process2LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT2\log000_2.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process2Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess2Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess2Table(CsvReader.dfVt2)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process2Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)

def RunProcess3ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT3\log000_3.csv')

    while True:
        VariableManager.process3Loading.config(text=VariableManager.spinnerChars[VariableManager.process3LoadingIndex])

        if VariableManager.process3LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process3LoadingIndex += 1
        else:
            VariableManager.process3LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT3\log000_3.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process3Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess3Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess3Table(CsvReader.dfVt3)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process3Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)

def RunProcess4ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT4\log000_4.csv')

    while True:
        VariableManager.process4Loading.config(text=VariableManager.spinnerChars[VariableManager.process4LoadingIndex])

        if VariableManager.process4LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process4LoadingIndex += 1
        else:
            VariableManager.process4LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT4\log000_4.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process4Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess4Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess4Table(CsvReader.dfVt4)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process4Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)

def RunProcess5ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT5\log000_5.csv')

    while True:
        VariableManager.process5Loading.config(text=VariableManager.spinnerChars[VariableManager.process5LoadingIndex])

        if VariableManager.process5LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process5LoadingIndex += 1
        else:
            VariableManager.process5LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT5\log000_5.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process5Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess5Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess5Table(CsvReader.dfVt5)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process5Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)
        
def RunProcess6ToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT6\log000_6.csv')

    while True:
        VariableManager.process6Loading.config(text=VariableManager.spinnerChars[VariableManager.process6LoadingIndex])

        if VariableManager.process6LoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.process6LoadingIndex += 1
        else:
            VariableManager.process6LoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.10\csv\csv\VT6\log000_6.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.process6Loading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            while True:
                try:
                    CsvReader.ReadProcess6Csv()
                    break
                except:
                    pass

            Sql.InsertDataToProcess6Table(CsvReader.dfVt6)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.process6Loading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)

def RunInspectionMachineToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.19\ai_team\AI Program\Outputs\CompiledPiMachine\CompiledPIMachine.csv')

    while True:
        try:
            VariableManager.inspectionMachineLoading.config(text=VariableManager.spinnerChars[VariableManager.inspectionMachineLoadingIndex])

            if VariableManager.inspectionMachineLoadingIndex < len(VariableManager.spinnerChars) - 1:
                VariableManager.inspectionMachineLoadingIndex += 1
            else:
                VariableManager.inspectionMachineLoadingIndex = 0

            currentFile = os.path.getmtime(r'\\192.168.2.19\ai_team\AI Program\Outputs\CompiledPiMachine\CompiledPIMachine.csv')
                
            #If Changes Detected In File
            if currentFile != origFile:
                VariableManager.inspectionMachineLoading.config(text="TRANSFERRING TO SQL")
                print("Changes Detected")
                
                while True:
                    try:
                        CsvReader.ReadPiMachineCsv()
                        break
                    except:
                        pass
                    
                Sql.InsertDataToFC1InspectionMachineTable(CsvReader.dfPi)

                #Setting The Original File Onto Current File
                origFile = currentFile
                VariableManager.inspectionMachineLoading.config(text="TRANSFERRING DONE")

            print("Waiting For Changes In PiCompiled")

            time.sleep(1)
        except:
            print("Failed Trying Again")

def RunUclLclToSql():
    #Checking Changes In CSV File Every Seconds

    #Reading Original File
    origFile = os.path.getmtime(r'\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\compiledFrameOut.csv')

    while True:
        VariableManager.uclLclLoading.config(text=VariableManager.spinnerChars[VariableManager.uclLclLoadingIndex])

        if VariableManager.uclLclLoadingIndex < len(VariableManager.spinnerChars) - 1:
            VariableManager.uclLclLoadingIndex += 1
        else:
            VariableManager.uclLclLoadingIndex = 0

        #Checking Changes In PiCompiled Using Forced Reading Of Csv
        while True:
            try:
                currentFile = os.path.getmtime(r'\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\compiledFrameOut.csv')
                break
            except:
                print("Failed Reading Of PiCompiled Trying Again In 1 Seconds")

        #If Changes Detected In File
        if currentFile != origFile:
            VariableManager.uclLclLoading.config(text="TRANSFERRING TO SQL")
            print("Changes Detected")
            
            CsvReader.ReadUclLcl()
            Sql.InsertDataToFC1UclLclTable(CsvReader.dfUclLcl)

            #Setting The Original File Onto Current File
            origFile = currentFile
            VariableManager.uclLclLoading.config(text="TRANSFERRING DONE")

        print("Waiting For Changes In PiCompiled")

        time.sleep(1)

def ChangeDate():
    while True:
        selectedDate = VariableManager.calendarPicker.get_date()
        selectedDate = selectedDate.strftime("%Y-%m-%d")

        print(selectedDate)

        time.sleep(2)