from Imports import *

dfVt1 = None
dfVt2 = None
dfVt3 = None
dfVt4 = None
dfVt5 = None
dfVt6 = None

dfPi = None
dfCompiled = None

dfUclLcl = None

dfCompiledProcess = None

def ReadProcess1Csv():
    global dfVt1
    
    dfVt1 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT1\log000_1.csv', encoding='latin1')
    # dfVt1 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT1\log000_1.csv', encoding='latin1')
    dfVt1.columns = ["Process 1 DATA No",
        "Process 1 DATE",
        "Process 1 TIME",
        "Process 1 Model Code",
        "Process 1 S/N",
        "Process 1 ID",
        "Process 1 NAME",
        "Process 1 Regular/Contractual",
        "Process 1 Em2p",
        "Process 1 Em2p Lot No",
        "Process 1 Em3p",
        "Process 1 Em3p Lot No",
        "Process 1 Harness",
        "Process 1 Harness Lot No",
        "Process 1 Frame",
        "Process 1 Frame Lot No",
        "Process 1 Bushing",
        "Process 1 Bushing Lot No",
        "Process 1 ST",
        "Process 1 Actual Time",
        "Process 1 NG Cause",
        "Process 1 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt1['Process 1 DateTime'] = pd.to_datetime(dfVt1['Process 1 DATE'] + ' ' + dfVt1['Process 1 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt1 = dfVt1.drop(['Process 1 DATE', 'Process 1 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt1.columns.tolist()
    cols.remove('Process 1 DateTime')
    cols.insert(1, 'Process 1 DateTime')
    dfVt1 = dfVt1[cols]


def ReadProcess2Csv():
    global dfVt2
    
    dfVt2 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT2\log000_2.csv', encoding='latin1')
    # dfVt2 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT2\log000_2.csv', encoding='latin1')
    dfVt2.columns = ["Process 2 DATA No",
        "Process 2 DATE",
        "Process 2 TIME",
        "Process 2 Model Code",
        "Process 2 S/N",
        "Process 2 ID",
        "Process 2 NAME",
        "Process 2 Regular/Contractual",
        "Process 2 M4x40 Screw",
        "Process 2 M4x40 Screw Lot No",
        "Process 2 Rod Blk",
        "Process 2 Rod Blk Lot No",
        "Process 2 Df Blk",
        "Process 2 Df Blk Lot No",
        "Process 2 Df Ring",
        "Process 2 Df Ring Lot No",
        "Process 2 Washer",
        "Process 2 Washer Lot No",
        "Process 2 Lock Nut",
        "Process 2 Lock Nut Lot No",
        "Process 2 ST",
        "Process 2 Actual Time",
        "Process 2 NG Cause",
        "Process 2 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt2['Process 2 DateTime'] = pd.to_datetime(dfVt2['Process 2 DATE'] + ' ' + dfVt2['Process 2 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt2 = dfVt2.drop(['Process 2 DATE', 'Process 2 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt2.columns.tolist()
    cols.remove('Process 2 DateTime')
    cols.insert(1, 'Process 2 DateTime')
    dfVt2 = dfVt2[cols]


def ReadProcess3Csv():
    global dfVt3
    
    dfVt3 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT3\log000_3.csv', encoding='latin1')
    # dfVt3 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT3\log000_3.csv', encoding='latin1')
    dfVt3.columns = ["Process 3 DATA No",
        "Process 3 DATE",
        "Process 3 TIME",
        "Process 3 Model Code",
        "Process 3 S/N",
        "Process 3 ID",
        "Process 3 NAME",
        "Process 3 Regular/Contractual",
        "Process 3 Frame Gasket",
        "Process 3 Frame Gasket Lot No",
        "Process 3 Casing Block",
        "Process 3 Casing Block Lot No",
        "Process 3 Casing Gasket",
        "Process 3 Casing Gasket Lot No",
        "Process 3 M4x16 Screw 1",
        "Process 3 M4x16 Screw 1 Lot No",
        "Process 3 M4x16 Screw 2",
        "Process 3 M4x16 Screw 2 Lot No",
        "Process 3 Ball Cushion",
        "Process 3 Ball Cushion Lot No",
        "Process 3 Frame Cover",
        "Process 3 Frame Cover Lot No",
        "Process 3 Partition Board",
        "Process 3 Partition Board Lot No",
        "Process 3 Built In Tube 1",
        "Process 3 Built In Tube 1 Lot No",
        "Process 3 Built In Tube 2",
        "Process 3 Built In Tube 2 Lot No",
        "Process 3 Head Cover",
        "Process 3 Head Cover Lot No",
        "Process 3 Casing Packing",
        "Process 3 Casing Packing Lot No",
        "Process 3 M4x12 Screw",
        "Process 3 M4x12 Screw Lot No",
        "Process 3 Csb L",
        "Process 3 Csb L Lot No",
        "Process 3 Csb R",
        "Process 3 Csb R Lot No",
        "Process 3 Head Packing",
        "Process 3 Head Packing Lot No",
        "Process 3 ST",
        "Process 3 Actual Time",
        "Process 3 NG Cause",
        "Process 3 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt3['Process 3 DateTime'] = pd.to_datetime(dfVt3['Process 3 DATE'] + ' ' + dfVt3['Process 3 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt3 = dfVt3.drop(['Process 3 DATE', 'Process 3 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt3.columns.tolist()
    cols.remove('Process 3 DateTime')
    cols.insert(1, 'Process 3 DateTime')
    dfVt3 = dfVt3[cols]

def ReadProcess4Csv():
    global dfVt4
    
    dfVt4 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT4\log000_4.csv', encoding='latin1')
    # dfVt4 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT4\log000_4.csv', encoding='latin1')
    dfVt4.columns = ["Process 4 DATA No",
        "Process 4 DATE",
        "Process 4 TIME",
        "Process 4 Model Code",
        "Process 4 S/N",
        "Process 4 ID",
        "Process 4 NAME",
        "Process 4 Regular/Contractual",
        "Process 4 Tank",
        "Process 4 Tank Lot No",
        "Process 4 Upper Housing",
        "Process 4 Upper Housing Lot No",
        "Process 4 Cord Hook",
        "Process 4 Cord Hook Lot No",
        "Process 4 M4x16 Screw",
        "Process 4 M4x16 Screw Lot No",
        "Process 4 Tank Gasket",
        "Process 4 Tank Gasket Lot No",
        "Process 4 Tank Cover",
        "Process 4 Tank Cover Lot No",
        "Process 4 Housing Gasket",
        "Process 4 Housing Gasket Lot No",
        "Process 4 M4x40 Screw",
        "Process 4 M4x40 Screw Lot No",
        "Process 4 PartitionGasket",
        "Process 4 PartitionGasket Lot No",
        "Process 4 M4x12 Screw",
        "Process 4 M4x12 Screw Lot No",
        "Process 4 Muffler",
        "Process 4 Muffler Lot No",
        "Process 4 Muffler Gasket",
        "Process 4 Muffler Gasket Lot No",
        "Process 4 VCR",
        "Process 4 VCR Lot No",
        "Process 4 ST",
        "Process 4 Actual Time",
        "Process 4 NG Cause",
        "Process 4 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt4['Process 4 DateTime'] = pd.to_datetime(dfVt4['Process 4 DATE'] + ' ' + dfVt4['Process 4 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt4 = dfVt4.drop(['Process 4 DATE', 'Process 4 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt4.columns.tolist()
    cols.remove('Process 4 DateTime')
    cols.insert(1, 'Process 4 DateTime')
    dfVt4 = dfVt4[cols]

def ReadProcess5Csv():
    global dfVt5
    
    dfVt5 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT5\log000_5.csv', encoding='latin1')
    # dfVt5 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT5\log000_5.csv', encoding='latin1')
    dfVt5.columns = ["Process 5 DATA No",
        "Process 5 DATE",
        "Process 5 TIME",
        "Process 5 Model Code",
        "Process 5 S/N",
        "Process 5 ID",
        "Process 5 NAME",
        "Process 5 Regular/Contractual",
        "Process 5 Rating Label",
        "Process 5 Rating Label Lot No",
        "Process 5 ST",
        "Process 5 Actual Time",
        "Process 5 NG Cause",
        "Process 5 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt5['Process 5 DateTime'] = pd.to_datetime(dfVt5['Process 5 DATE'] + ' ' + dfVt5['Process 5 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt5 = dfVt5.drop(['Process 5 DATE', 'Process 5 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt5.columns.tolist()
    cols.remove('Process 5 DateTime')
    cols.insert(1, 'Process 5 DateTime')
    dfVt5 = dfVt5[cols]

def ReadProcess6Csv():
    global dfVt6
    
    dfVt6 = pd.read_csv(r'\\192.168.2.10\csv\csv\VT6\log000_6.csv', encoding='latin1')
    # dfVt6 = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\FC1 CSV\VT6\log000_6.csv', encoding='latin1')
    dfVt6.columns = ["Process 6 DATA No",
        "Process 6 DATE",
        "Process 6 TIME",
        "Process 6 Model Code",
        "Process 6 S/N",
        "Process 6 ID",
        "Process 6 NAME",
        "Process 6 Regular/Contractual",
        "Process 6 Vinyl",
        "Process 6 Vinyl Lot No",
        "Process 6 ST",
        "Process 6 Actual Time",
        "Process 6 NG Cause",
        "Process 6 Repaired Action"]
    
    # Merge date and time columns into a single datetime column
    dfVt6['Process 6 DateTime'] = pd.to_datetime(dfVt6['Process 6 DATE'] + ' ' + dfVt6['Process 6 TIME'])
    
    # Optionally drop the original date and time columns if you don't need them anymore
    # dfVt6 = dfVt6.drop(['Process 6 DATE', 'Process 6 TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfVt6.columns.tolist()
    cols.remove('Process 6 DateTime')
    cols.insert(1, 'Process 6 DateTime')
    dfVt6 = dfVt6[cols]

def ReadPiMachineCsv():
    global dfPi

    dfPi = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\CompiledPiMachine\CompiledPIMachine.csv', encoding='latin1')

    dfPi.columns = [
        "DATE",
        "TIME",
        "MODEL CODE",
        "S/N",
        "PASS_NG",
        "VOLTAGE MAX_(V)",
        "WATTAGE MAX (W)",
        "CLOSED PRESSURE_MAX (kPa)",
        "VOLTAGE Middle (V)",
        "WATTAGE Middle (W)",
        "AMPERAGE Middle (A)",
        "CLOSED PRESSURE Middle (kPa)",
        "VOLTAGE MIN (V)",
        "WATTAGE MIN (W)",
        "CLOSED PRESSURE MIN (kPa)"
    ]

    # dfPi = dfPi.drop([
    #     "ÂÂ¶",
    #     "dB(A) 1",
    #     "dB(A) 2",
    #     "dB(A) 3",
    #     "Middle ÂzÂÃ¼ÂÃ",
    #     "Max ÂzÂÃ¼ÂÂÂÃ",
    #     "INSULATION PASS/NG",
    #     "WITHSTAND VOLTAGE PASS/GO",
    #     "mL/min",
    #     "DM01293",
    #     "VOLTAGE MAX PASS/NG",
    #     "WATTAGE MAX PASS/NG",
    #     "CLOSED PRESSURE MAX PASS/NG",
    #     "Middle inhale Air volume",
    #     "MAX inhale Air volume",
    #     "VOLTAGE Middle PASS/NG",
    #     "WATTAGE Middle PASS/NG",
    #     "AMPERAGE Middle PASS/NG",
    #     "CLOSED PRESSURE Middle PASS/NG",
    #     "VOLTAGE MIN PASS_NG",
    #     "WATTAGE MIN PASS/NG",
    #     "CLOSED PRESSURE MIN PASS/NG",
    #     "ÃÂ°Â¸TESTÂÂÂÃPASS/NG",
    #     "INSPECTED Q'TY",
    #     "PASSED Q'TY",
    #     "AMPERAGE MAX (A)",
    #     "PRESSURE MAXÂ@(kPa)",
    #     "PRESSURE Middle (kPa)",
    #     "PRESSURE MIN (kPa)",
    #     "Min LEAK PRESSURE (kPa)",
    #     "Min LEAK TIME (sec)",
    #     "CLOSED VOLTAGE MAX (V)",
    #     "CLOSED AMPERAGE MAX (A)",
    #     "NG Q'TY",
    #     "CLOSED WATTAGE MAX (W)",
    #     "CLOSED VOLTAGE Middle (V)",
    #     "CLOSED AMPERAGE Middle (A)",
    #     "CLOSED WATTAGE Middle (W)",
    #     "AMPERAGE MIN (A)",
    #     "CLOSED VOLTAGE MIN (V)",
    #     "CLOSED AMPERAGE MIN (A)",
    #     "CLOSED WATTAGE MIN (W)",
    #     "DM01800",
    #     "S/N SWAP",
    #     "ÃÃÃÂ²ÃÃÂdÂÂ³ÂÃ¼ÂgÂÂÂÂªÂÃ¨Âl"
    # ], axis=1)

    # Merge date and time columns into a single datetime column
    dfPi['DATETIME'] = pd.to_datetime(dfPi['DATE'] + ' ' + dfPi['TIME'])

    # Optionally drop the original date and time columns if you don't need them anymore
    # dfPi = dfPi.drop(['DATE'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfPi.columns.tolist()
    cols.remove('DATETIME')
    cols.insert(0, 'DATETIME')
    dfPi = dfPi[cols]

def ReadCompiledFC1():
    global dfCompiled

    dfCompiled = pd.read_csv(r'\\192.168.2.19\ai_team\AI Program\Outputs\Debug\FC1DataBase.csv', encoding='latin1')

    for column in dfCompiled:
        print(f"{column.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')} VARCHAR(64),")

def ReadUclLcl():
    global dfUclLcl

    dfUclLcl = pd.read_csv(r"\\192.168.2.19\ai_team\INDIVIDUAL FOLDER\June-San\p2LTG\p2LTG_TransferData\compiledFrameOut.csv", encoding='latin1')

    # Merge date and time columns into a single datetime column
    dfUclLcl['DATETIME'] = pd.to_datetime(dfUclLcl['DATE'] + ' ' + dfUclLcl['TIME'])

    # Optionally drop the original date and time columns if you don't need them anymore
    dfUclLcl = dfUclLcl.drop(['DATE', 'TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfUclLcl.columns.tolist()
    cols.remove('DATETIME')
    cols.insert(0, 'DATETIME')
    dfUclLcl = dfUclLcl[cols]
    # for column in dfUclLcl:
    #     print(f"{column.replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')} VARCHAR(64),")

def ReadCompiledProcess(date):
    global dfCompiledProcess

    dfCompiledProcess = pd.read_csv(fr"\\192.168.2.19\ai_team\AI Program\Outputs\CompiledProcess\CompiledProcess{date}.csv", encoding='latin1')

    # Merge date and time columns into a single datetime column
    dfCompiledProcess['DATETIME'] = pd.to_datetime(dfCompiledProcess['DATE'] + ' ' + dfCompiledProcess['TIME'])

    # Optionally drop the original date and time columns if you don't need them anymore
    dfCompiledProcess = dfCompiledProcess.drop(['DATE', 'TIME'], axis=1)
    
    # Reorder columns to move DateTime to second position
    cols = dfCompiledProcess.columns.tolist()
    cols.remove('DATETIME')
    cols.insert(0, 'DATETIME')
    dfCompiledProcess = dfCompiledProcess[cols]