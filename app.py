from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def countdown():
    today = datetime.today()
    days_until_saturday = (5 - today.weekday()) % 7  # 5 - це субота
    if days_until_saturday == 0:
        days_until_saturday = 7
    return f"До наступної суботи залишилось {days_until_saturday} днів."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)