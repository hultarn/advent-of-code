import requests
import yaml

class advent_of_code:
    def __init__(self, year: str, day: str):
        self.day = day
        self.base_url = "https://adventofcode.com/" + year + "/day/" + day + "/"
        
        with open('../config.yaml') as f:
            session = yaml.load(f, Loader=yaml.FullLoader)["session"]
            self.cd = {'session': session}
        r = requests.get(self.base_url + "input", cookies=self.cd)
        self.data = r.text[:len(r.text) - 1]
        
    def post(self, answer: str, level: str):
        payload = {
            'level': level,
            'answer': answer
        }
        
        r = requests.post(self.base_url + "answer", cookies=self.cd, data=payload).text
        if "not the right answer" in r: 
            return False, "0"
        elif "You have" in r:
            return False, r.split("You have")[1].split(".")[0].strip()
        else:
            return True