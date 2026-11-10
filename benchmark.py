import json
import time
import urllib.request
import statistics
import math

URL = "http://127.0.0.1:8000/predict"

student = {
    "school": "GP",
    "sex": "F",
    "age": 18,
    "address": "U",
    "famsize": "GT3",
    "Pstatus": "T",
    "Medu": 4,
    "Fedu": 4,
    "Mjob": "at_home",
    "Fjob": "teacher",
    "reason": "course",
    "guardian": "mother",
    "traveltime": 1,
    "studytime": 2,
    "failures": 0,
    "schoolsup": "no",
    "famsup": "yes",
    "paid": "no",
    "activities": "yes",
    "nursery": "yes",
    "higher": "yes",
    "internet": "yes",
    "romantic": "no",
    "famrel": 4,
    "freetime": 3,
    "goout": 3,
    "Dalc": 1,
    "Walc": 2,
    "health": 5,
    "absences": 2,
    "G1": 12,
    "G2": 13
}

times = []

for i in range(100):
    request_data = json.dumps(student).encode("utf-8")

    req = urllib.request.Request(
        URL,
        data=request_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    start = time.perf_counter()

    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))

    elapsed = (time.perf_counter() - start) * 1000
    times.append(elapsed)

mean_latency = statistics.mean(times)
sorted_times = sorted(times)
p95_latency = sorted_times[math.ceil(0.95 * len(times)) - 1]

print("Количество запросов:", len(times))
print("Последний прогноз:", result)
print(f"Средняя задержка (mean): {mean_latency:.2f} мс")
print(f"95-й перцентиль (p95): {p95_latency:.2f} мс")
print(f"Минимальная задержка: {min(times):.2f} мс")
print(f"Максимальная задержка: {max(times):.2f} мс")