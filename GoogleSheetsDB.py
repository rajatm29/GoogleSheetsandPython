import grspread
from oauth2client.service_account import ServiceAccountCredentials
 

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)


workable_sheet = client.open('').sheet1
list_of_maps = workable_sheet.get_all_records()
