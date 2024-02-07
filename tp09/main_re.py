from glob import glob
import re

def main():
    logs = glob('tp09/*.log')
    for log in logs:
        with open(log) as f:
            for line in f:
                line = line.strip()
                # result = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                # result = re.findall(r'^(.+?)\s', line)
                result = re.findall(r'\"\s(\d{3})\s', line)
                print(result)
if __name__=='__main__':
    main()
