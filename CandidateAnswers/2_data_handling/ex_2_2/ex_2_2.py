from readrides_dictionary import read_rides_as_dictionary
from collections import Counter
from collections import defaultdict
from datetime import datetime

# route,date,daytype,rides
rows = read_rides_as_dictionary('Data/ctabus.csv')
    
def get_best_route():
    bus_counter = Counter()
    for row in rows:
        if (datetime.strptime(row['date'], '%m/%d/%Y') >= datetime(2001, 1, 1)) and (datetime.strptime(row['date'], "%m/%d/%Y") <= datetime(2011, 12, 31)):
            bus_counter[row['route']] += row['rides']
    top_5 = bus_counter.most_common(5)
    print(top_5)
    return top_5

def get_route_date(route, date):
    routes = bus_index()
    print(routes[route][date])
    return routes[route][date]

def bus_index():
    bus_dict = defaultdict(defaultdict)
    for row in rows:
        bus_dict[row['route']][row['date']] = row['rides']
    return bus_dict    

def bus_route_count():
    route_set = {row['route'] for row in rows} 
    print(len(route_set))

def total_number_of_rides():
    routes = Counter()
    for row in rows:
        routes[row['route']] += row['rides']
    print(routes)

if __name__ == '__main__':
    total_number_of_rides()
