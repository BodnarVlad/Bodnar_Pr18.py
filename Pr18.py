1
import threading
import time
import random

def countdown():
    for i in range(10, 0, -1):
        print(f"Зворотний відлік: {i}")
        time.sleep(1)

if __name__ == "__main__":
    countdown_thread = threading.Thread(target=countdown)
    countdown_thread.start()
    countdown_thread.join()

2
import threading
import time
import random

def simulate_download(file_id):
    duration = random.randint(3, 5)
    print(f" Завантаження файлу {file_id}...")
    time.sleep(duration)
    print(f" Файл {file_id} завантажено за {duration} с.")

if __name__ == "__main__":
    download_threads = []
    for i in range(3):
        t = threading.Thread(target=simulate_download, args=(i+1,))
        download_threads.append(t)
        t.start()

    for t in download_threads:
        t.join()

3
import threading
import time
import random

numbers = [random.randint(1, 100) for _ in range(1000)]
sums = [0, 0, 0, 0]

def sum_part(index, part):
    part_sum = sum(part)
    sums[index] = part_sum
    print(f" Потік {index + 1} обробив частину з сумою {part_sum}")

if __name__ == "__main__":
    size = len(numbers) // 4
    parts = [numbers[i*size:(i+1)*size] for i in range(4)]
    sum_threads = []

    for i in range(4):
        t = threading.Thread(target=sum_part, args=(i, parts[i]))
        sum_threads.append(t)
        t.start()

    for t in sum_threads:
        t.join()

    total = sum(sums)
    print(f"\n Загальна сума: {total}")
