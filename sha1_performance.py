# Nama : Siti Adira Ramadhani
# NIM : 18220094
# File analisis performa SHA1
import hashlib
import psutil
import time

def calculate_performance_sha1(message, iterations=1000):
    total_execution_time = 0
    total_cpu_usage = 0
    total_memory_usage = 0

    for i in range(iterations):
        # start
        start_time = time.time()
        start_cpu_usage = psutil.cpu_percent()
        start_memory_usage = psutil.Process().memory_info().rss

        # Hashing
        hash_object = hashlib.sha1(message.encode())
        hex_digest = hash_object.hexdigest()

        # end
        end_time = time.time()
        end_cpu_usage = psutil.cpu_percent()
        end_memory_usage = psutil.Process().memory_info().rss

        # calculate
        execution_time = end_time - start_time
        cpu_usage = max(end_cpu_usage - start_cpu_usage, 0) # set negative value to 0
        memory_usage = end_memory_usage - start_memory_usage

        total_execution_time += execution_time
        total_cpu_usage += cpu_usage
        total_memory_usage += memory_usage


    average_execution_time = (total_execution_time / iterations) * 1000 # convert to milliseconds
    average_cpu_usage = (total_cpu_usage / iterations)
    average_memory_usage = (total_memory_usage / iterations)

    print('SHA-1 hash result:', hex_digest)
    print('Average execution time:', average_execution_time, 'milliseconds')
    print('Average CPU usage:', average_cpu_usage, '%')
    print('Average memory usage:', average_memory_usage, 'bytes')

message = input("Masukkan password : ")
print(f'Panjang password : {len(message)}')
calculate_performance_sha1(message, 1000)