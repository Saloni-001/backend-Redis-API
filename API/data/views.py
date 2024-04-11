from datetime import datetime

from django.http import JsonResponse
import redis

def latest_info(request, device_id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    data = r.hgetall(device_id)
    return JsonResponse(data)

def device_location(request, device_id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    data = r.hgetall(device_id)
    start_location = (float(data[b'latitude']), float(data[b'longitude']))
    end_location = start_location
    return JsonResponse({'start_location': start_location, 'end_location': end_location})

def location_history(request, device_id):
    # Retrieve start time and end time from request parameters
    start_time = request.GET.get('start_time')
    end_time = request.GET.get('end_time')

    # Convert start_time and end_time to datetime objects (assuming they are in ISO format)
    start_time = datetime.fromisoformat(start_time)
    end_time = datetime.fromisoformat(end_time)

    # Connect to Redis (assuming the connection is already established)
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Initialize a list to store location history
    location_history = []

    # Iterate over keys in Redis matching the device ID
    for key in r.scan_iter(f'{device_id}*'):
        # Get the timestamp and convert it to datetime object
        timestamp = datetime.fromisoformat(r.hget(key, 'time_stamp').decode())

        # Check if the timestamp is within the specified time range
        if start_time <= timestamp <= end_time:
            # Get latitude and longitude from Redis and convert to float
            latitude = float(r.hget(key, 'latitude').decode())
            longitude = float(r.hget(key, 'longitude').decode())

            # Append location data to the location history list
            location_history.append({'latitude': latitude, 'longitude': longitude, 'timestamp': timestamp.isoformat()})

    # Return location history as JsonResponse
    return JsonResponse(location_history, safe=False)
