from datetime import datetime

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
print(f"filename_{date}")
