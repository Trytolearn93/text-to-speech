import os
from google.cloud import texttospeech
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

# 🔐 Ange sökvägen till din servicekonto-nyckel
SERVICE_ACCOUNT_FILE = type: "service_account",
  project_id: "infinite-cache-443518-j5",
  private_key_id: "ec5f9758112b240fc3448a2b3e57535a43ec64bb",
  private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCsF3cr2q8XP6lR\nqqGjcJ7LDEkL0DFEhEM5wI6iz2v0HcqPe/5j0X69Wv2OPfkveGDKRcoPK3k6nPIo\n4tGPEKiyU7dudCfwgBoo5uc/uxCRYY/TLBJZa5aE+hnWs3Np2YhGg4bLWmvNDnqh\n4/KAlfZhS/cutgg0fOIFdYCLnZmJbbODdPdSVqnUWZ5QX+mT1EVeSN06ZMnTph9B\n+hvFGKkDDVQ5fbdvT8riWrFi2yYI6wAUYYj5m9MGa3m+Md40kbW3M/tokaYABIMY\n1DPPoG9eErCkE7/deDeWz4y5OZq8/dRZQaDTz7emy6Ep5xRbgYL+FUYTjUo0TWSI\nPKhif6afAgMBAAECgf8l45BZXUDSaTHG98pwMaFQKnuNkqYAb9iLx03OuVCuQA9w\nQgsGHaVsxYSCKd0QOXC46Y1kslwtFxsin4fhDw+4M3CMg+8v7QRhFEbtBvzNYn8C\nLfetuF9rc0gOiOhUlEqD9hRDDo4h3WtRIiSfQjafknc2ulGfyGq1JhJtB+jF+77s\nq0tTGhr4YtvPUo6ORtR0ir7azmAbEIi7CmPggxwixigX9Il0wwCGEELPjAUgZvMh\nx/OKqINhZMHpLlqCIpXpXzWzTw5pKpwnvP3jE8nReWX7DiNhrRIgqbrmKN8BO1Tz\nZfU/Akbsx1uFvpcnl0jfLxrqRl6hcjXODn9DYYECgYEA1NeplKV9rfYT5PEgm5CJ\ns7tGzLLqhiImLMKyuYkVSuzAAsz1ycnclQYwQcYOQ7MRtPcRoWh3pgvyKaosXqc9\nCt3JbIbIZtFs690bQ1q+rxT1r8NoKvUJZbCEmrRuSGaESFPSETHo6sau8/08m5a8\nZHObhmPi8Y9cNYlScw4kve8CgYEAzvx9l44lEdZCX0tuXJrBzD92ARoHq7t5vOyQ\nvq+oLOYbRGY+C5JWtCaafChofdTB0wLezb1xjWwIYHNEtdB6pAfaurvrzARKSI8y\n52xPZ/xcBQFLP4SHMO7vGf6wSb7ijASY2lTWzFmqQhpyoUc/0h3RY5JGXnDtXVbj\n4bWHUlECgYEAn996frAsDh535REGCDPyazGxxZJivOwrtpVsgBarCsN4muHvgWoC\nKWIjn1QwZMO9+itXb+EzdmMkvA0aFOMT4/SiFsXLBAgtA6Hql5YzAvoAbcyekx3J\nuDt172q2J+XxWQ61DLtrk+Y3hgfinZAE5IM+AB1JW17uyTvj1Y57JLsCgYEAwh9b\nSoAtlAT2Splb783UY9JAwde/yfgRvHXBapUjjLhiakvZdNDSMDLkP/1Fwn1/Kn9O\npnY9wPzI/mwczMexvZUANpF4G+cKI/LpMtIJxuSPCMKl5/RLNkFgTWjnvMIhhl/p\nWxqmORD+9PAJAejomg8NCe1twbT3aMrM/ipZt4ECgYEAoRlEhteYiI4MbfNbnweM\ntDsEwm9zleYkkNVMzZjW2674JH8pbovYuQ6G0FTPBwp3h3fk9AkengzMDqsqYa6Y\n3XdTFyYf2AWNWRjjJtWNh+wW+KzUM76D7gRI97kkzf4Fubb2GBkwEG8CqQvDuIyK\nAUfGflsHNJea3TaR7JuQFNU=\n-----END PRIVATE KEY-----\n",
  client_email: "spara-med-ai@infinite-cache-443518-j5.iam.gserviceaccount.com",
  client_id: "112376880404922838874",
  auth_uri: "https://accounts.google.com/o/oauth2/auth",
  token_uri: "https://oauth2.googleapis.com/token",
  auth_provider_x509_cert_url: "https://www.googleapis.com/oauth2/v1/certs",
  client_x509_cert_url: "https://www.googleapis.com/robot/v1/metadata/x509/spara-med-ai%40infinite-cache-443518-j5.iam.gserviceaccount.com",
  universe_domain: "googleapis.com"

# 📄 Spreadsheet-ID från den angivna Google Sheets-URL:en
SPREADSHEET_ID = '1S8GLCpGrPq3pVTxinMtCk3zs2EjIymnt25VvedvRNJ8'

# 📁 Google Drive-mappens ID (uppdaterat)
DRIVE_FOLDER_ID = '1DZ_-adeG2ER0CloKne9B6rNHlCJC7h26'

# ✅ Autentisering för Google Sheets och Google Drive
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# 📊 Google Sheets API-klient
sheets_service = build('sheets', 'v4', credentials=credentials)

# 📁 Google Drive API-klient
drive_service = build('drive', 'v3', credentials=credentials)

# 🗣️ Google Cloud Text-to-Speech-klient
tts_client = texttospeech.TextToSpeechClient(credentials=credentials)

def synthesize_text_to_speech(text, output_filename):
    """Genererar ljudfil från text med Google TTS API och sparar den som en MP3-fil."""
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="sv-SE", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = tts_client.synthesize_speech(input=input_text, voice=voice, audio_config=audio_config)

    # Spara ljudfilen som MP3
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
    print(f"Ljudfil genererad: {output_filename}")

def upload_to_google_drive(file_path, file_name, folder_id):
    """Laddar upp en fil till Google Drive och returnerar delningslänken."""
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, mimetype='audio/mpeg')

    # Ladda upp filen
    uploaded_file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    file_id = uploaded_file.get('id')

    # Sätt filens behörighet till "public"
    drive_service.permissions().create(
        fileId=file_id,
        body={'role': 'reader', 'type': 'anyone'}
    ).execute()

    # Skapa delningslänk
    file_link = f"https://drive.google.com/uc?id={file_id}"
    print(f"Fil uppladdad till Google Drive: {file_link}")
    return file_link

def update_sheet_with_audio_links(row, audio_url):
    """Uppdaterar Google Sheets med länken till ljudfilen i kolumn C."""
    range_ = f'youtubeshorts!C{row}'
    values = [[audio_url]]
    body = {'values': values}

    sheets_service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_, valueInputOption='RAW', body=body
    ).execute()
    print(f"Uppdaterade Google Sheet med länk för rad {row}: {audio_url}")

def process_spreadsheet():
    """Läser text från Google Sheets, genererar ljudfiler, laddar upp till Google Drive och uppdaterar Google Sheets."""
    try:
        # Hämta text från kolumn B i youtubeshorts
        range_ = 'youtubeshorts!B2:B'
        result = sheets_service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
        values = result.get('values', [])

        for i, row in enumerate(values, start=2):  # Starta från rad 2
            if row:  # Kontrollera att raden inte är tom
                text = row[0]  # Text från kolumn B
                output_filename = f"audio_{i}.mp3"  # Namn på ljudfilen

                # Generera ljudfil
                synthesize_text_to_speech(text, output_filename)

                # Ladda upp ljudfilen till Google Drive
                audio_url = upload_to_google_drive(output_filename, output_filename, DRIVE_FOLDER_ID)

                # Uppdatera Google Sheets med länken i kolumn C
                update_sheet_with_audio_links(i, audio_url)

    except HttpError as err:
        print(f"Ett fel inträffade: {err}")

if __name__ == '__main__':
    process_spreadsheet()
