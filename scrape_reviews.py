import csv
data_list =  []
def get_ids_from_hotel_url(url):
  url = url.split('-')
  geo = url[1]
  loc = url[2]
  return (int(geo[1:]), int(loc[1:]))

def read_csv(file):
    with open(file, mode='r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_list.extend(row)

GRAPHQL_URL = 'https://www.tripadvisor.com/data/graphql/batched'


if __name__ == "__main__":
    read_csv("links_oberriexingen.csv")
    for i in data_list:
        link = get_ids_from_hotel_url(i)
        