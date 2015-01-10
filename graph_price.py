import matplotlib.pyplot as plt
import matplotlib
import json
import pdb
from collections import defaultdict
import numpy as np
# import time
from datetime import datetime

def get_prices_dates(filename):
    dates = defaultdict(list)
    
    data  = json.loads(open(filename).read())['results']
    days = dict([ (t['url'], t) for t in data['trip'] if t['to'] != "" ])

    for t in data['times']:
        date_string = days[t['url']]['date']
        date = datetime.strptime(date_string, "%A %B %d, %Y")   
        # date = datetime.fromtimestamp(mktime(strdateuct))

        dates[date].append(float(t['price']))

    for d in dates:
        dates[d] = np.mean(dates[d])

    return dates

    
def graph(prices, dates):
    sorted_dates = sorted(zip(prices, dates), key=lambda x: x[1])
    dates = [x[1] for x in sorted_dates]
    prices = [x[0] for x in sorted_dates]

    for i in range(7):
        plt.plot(dates[i::7], prices[i::7], label=dates[i].strftime("%A"))

    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Average price vs day of the week')
    plt.legend()
    plt.show()
    plt.savefig('by_weekday.jpg')



if __name__ == "__main__":
    prices =  get_prices_dates("prices.json")
    graph(prices.values(), prices.keys())