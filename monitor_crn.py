import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import json
from program import Program

def st(crn):
    Monitor(crn)

class Monitor:
    def __init__(self, crn):
        self.crn = crn.split("/")[0]
        self.lessonID = crn.split("/")[1]
        self.main()

    def main(self):
        with requests.Session() as s:
            lastKontenjan = 0
            while True:
                main_content = s.get('https://obs.itu.edu.tr/public/DersProgram')
                soup = BeautifulSoup(main_content.text, 'html.parser')
                r_token = soup.find("input", {"name": "__RequestVerificationToken"})
                cont = s.get(f'https://obs.itu.edu.tr/public/DersProgram/DersProgramSearch?ProgramSeviyeTipiAnahtari=LS&dersBransKoduId={self.lessonID}&__RequestVerificationToken={r_token.get("value")}')
                js = json.loads(cont.text)
                element = sorted(js['dersProgramList'], key=lambda p: p['crn'] == self.crn, reverse=True)[0]
                print(f"[{datetime.now().strftime("%H:%M:%S")}] [{element['crn']}] Current Kontenjan: ", element['kontenjan'])
                if lastKontenjan == 0:
                    lastKontenjan = element['kontenjan']
                else:
                    if element['kontenjan'] > lastKontenjan:
                        Program(element['crn'])
                        break
                calc = 0
                while True:
                    d = datetime.now().strftime("%d/%m/%Y")
                    m = datetime.now().strftime("%M")
                    mm = str(((int(m) // 5) + 1) * 5 if ((int(m) // 5) + 1) * 5 != 60 else 0)
                    mm = mm if len(mm) == 2 else f"0{mm}"
                    sa = str(datetime.now().strftime("%H") if ((int(m) // 5) + 1) * 5 != 60 else int(datetime.now().strftime("%H"))+1)
                    sa = sa if len(sa) == 2 else f"0{sa}"
                    lat = datetime.strptime(f"{d} {sa}:{mm}:03", "%d/%m/%Y %H:%M:%S")
                    calc = (lat - datetime.now()).total_seconds()
                    if calc > 10:
                        break
                    time.sleep(2)
                time.sleep(calc)