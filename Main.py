#%%
from Imports import *
import mysql.connector as mariadb

import CsvReader
import Sql
import GuiManager

Sql.SqlConnection()

GuiManager.showGui()