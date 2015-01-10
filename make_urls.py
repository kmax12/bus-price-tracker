import datetime

def make_urls(start_date, num_days=50):
    base = "http://us.megabus.com/JourneyResults.aspx?originCode=94&destinationCode=123&outboundDepartureDate=%s&inboundDepartureDate=&passengerCount=1"

    urls = []
    d = start_date
    while len(urls) <= num_days:
        # print 
        url = base % d.strftime("%m%2f%d%2f%Y")
        d += datetime.timedelta(days=1)
        urls.append(url)

    return urls

if __name__ == "__main__":
    today = datetime.date.today()
    urls = make_urls(today)

    for u in urls:
        print u