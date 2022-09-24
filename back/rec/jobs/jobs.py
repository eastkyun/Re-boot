from datetime import datetime
import psycopg2
from rec.utils.cron import Cron


timeZone = datetime.now()


def schedule_api():
    # TODO: insert data to DB
    print("schedule_api : successful")
    with psycopg2.connect(database='reboot', user='reboot', password='reboot') as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM rec_apartments")
        apartments = cur.fetchall()
        crawling_list = Cron.crawling_rec_tuple(apartments)
        # crawling_list = [{'apart': 4, 'date': '2022-09-24', 'name': '이노시티애시앙', 'price': 40000, 'per_price': 1198},
        #                  {'apart': 5, 'date': '2022-09-24', 'name': '빛가람코오롱하늘채', 'price': 25900, 'per_price': 861},
        #                  {'apart': 6, 'date': '2022-09-24', 'name': '나주역자이리버파크', 'price': 37770, 'per_price': 1128},
        #                  {'apart': 8, 'date': '2022-09-24', 'name': '빛가람중흥S-클래스센트럴1차', 'price': 32000, 'per_price': 1115},
        #                  {'apart': 9, 'date': '2022-09-24', 'name': '빛가람중흥S-클래스센트럴2차', 'price': 34000, 'per_price': 1182}]
        for alist in crawling_list:
            cur.execute("""
            INSERT INTO rec_priceinfo (apart_id, date, price, per_price)
            VALUES (%s, %s, %s, %s)
            """, (alist['apart'], alist['date'], alist['price'], alist['per_price']))
            con.commit()
