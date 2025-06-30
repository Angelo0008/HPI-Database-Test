#%%
from Imports import *
import CsvReader
import Sql

Sql.SqlConnection()
# Sql.CreateFC1InspectionMachineTable()

CsvReader.ReadPiMachineCsv()
Sql.InsertDataToFC1InspectionMachineTable(CsvReader.dfPi)

# CsvReader.ReadUclLcl()
# Sql.CreateFC1UclLclTable()
# Sql.InsertDataToFC1UclLclTable(CsvReader.dfUclLcl)

# CsvReader.ReadCompiledProcess('2024-11-04')


# %%

# %%
