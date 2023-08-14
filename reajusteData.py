from datetime import datetime, timedelta


def data(data_, interval):
    data = datetime.strptime(data_, '%d/%m/%Y')
    future_date = data+timedelta(days=int(interval))
    day_of_the_week = future_date.weekday()
    if day_of_the_week == 5:
        future_date = future_date+timedelta(days=2)
        pass
    elif day_of_the_week == 6:
        future_date = future_date+timedelta(days=1)
        pass
    corrected_date = future_date
    corrected_date = str(corrected_date.strftime("%d/%m/%Y"))
    return corrected_date
