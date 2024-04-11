import pandas as pd
import redis

def read_excel_and_store_in_redis(filename):
    # Read Excel data
    df = pd.read_excel(filename)
    # Sort data by sts column
    df = df.sort_values(by='sts')

    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Store data in Redis cache
    for index, row in df.iterrows():
        device_id = row['device_fk_id']
        latest_data = {
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'time_stamp': str(row['time_stamp']),
            'speed': row['speed']
        }
        r.hmset(device_id, latest_data)


if __name__ == '__main__':
    read_excel_and_store_in_redis('raw_data (4) (6).csv')
