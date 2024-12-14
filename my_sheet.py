import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials


id = '1S8GLCpGrPq3pVTxinMtCk3zs2EjIymnt25VvedvRNJ8'
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file"]

creds = ServiceAccountCredentials.from_json_keyfile_name('./google-account-key.json', scope)
client = gspread.authorize(creds)

sheet = client.open_by_key(id).worksheet("Youtubeshorts")

column = sheet.col_values(1)  # Hämta alla värden från kolumn 1 (A)

# Skriv ut den hämtade kolumnen
print(column)
