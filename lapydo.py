from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sys
import pandas as pd

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

def main(option, SPREADSHEET_ID, RANGE, out):
    #Looks for the option to use online resources or search in the offline file system
    if(option=='o'):
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        #PyLint throws an error here, therefore the functionality was temporarily disabled
        sheet = service.spreadsheets()#pylint: disable=no-member
        
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE).execute()
        values = result.get('values', [])
        # Calculates the difference between the columns to find the appropriate size of the table
        i = 0
        r = []
        q = []
        turnAround = ''
        resultTurn = ''
        for elem in RANGE:
            turnAround += elem
            if(elem == '!'):
                resultTurn = turnAround
                for nelem in RANGE[i+1:len(RANGE)]:
                    if(ord(nelem) >= 65 and ord(nelem)<=90):
                        r.append(ord(nelem))
                        q.append(nelem)
                break        
            i = i + 1
        rowSpace = r[1] - r[0] + 1
        

        #Iterates through the pulled data and gives it the found label        
        reList = []
        bot = True
        if not values:
            print('No data found.')
        else:
            print('Widerstand, Spannung, Strom:')
            for row in values:
                if(bot):
                    newList = row[0:rowSpace]
                    bot = False
                    continue
                print(row[0:rowSpace])
                reList.append(row[0:rowSpace])
        df = pd.DataFrame(reList, columns=newList).to_latex()
        with open(out + '.tex', 'w') as file:
            file.write(df)
    elif option == 'f':
        if RANGE == 'NORANGE':
            df = pd.read_excel(ID)
            with open(out + '.tex', 'w') as file:
                file.write(df.to_latex())
        else:
            #As there is no Range needed for offline functionality yet, the Range has to be filled in by NORANGE
            print("Invalid Option: RANGE")

    else:
        #Handles the use of Invalid Command Options as there are no other options besides o - online and f - file
        print('Invalid Command Structure, try o or f')



if __name__ == '__main__':
    option = str(sys.argv[1])
    ID = str(sys.argv[2])
    RANGE = str(sys.argv[3])
    out = str(sys.argv[4])
    main(option, ID, RANGE, out)