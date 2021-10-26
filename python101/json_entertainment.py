import json

e1 = {
    "agg_id_1": "time_org",
    "agg_id_4": "geo_dst",
    "agg_id_2": "time_dst",
    "agg_id_3": "geo_org",
    "unit": "teu",
    "agg_value_4": "country",
    "name": "Volume",
    "agg_type_4": "geo",
    "topic": "ocean",
    "agg_type_3": "geo",
    "id": "filename",
    "agg_value_2": "monthly",
    "value": 1,
    "agg_value_3": "country",
    "agg_type_2": "time",
    "timestamp": f"2020-07-30T00:00:00.000Z",
    "agg_type_1": "time",
    "agg_value_1": "monthly"
}

value_serializer = lambda x: json.dumps(x).encode('utf-8')
print(value_serializer )

for record in e1:
    print(record)
    #future = producer.send('test', value=record)
    #result = future.get(timeout=60)

print(json.dumps(e1, indent = 4))
