def sort_logs(web_log_list):
    
    web_log_list.sort(key = lambda log: log[1], reverse = True ) #sap xem tem thoi gian truoc
    web_log_list.sort(key = lambda log: log[2])
    return web_log_list

# --- Chạy thử ---
web_logs = [
    ('1.1.1.1', '2023-10-27T10:05:00Z', 200),
    ('2.2.2.2', '2023-10-27T10:01:00Z', 404),
    ('3.3.3.3', '2023-10-27T10:02:00Z', 200),
    ('4.4.4.4', '2023-10-27T10:03:00Z', 500),
]
print("Sắp xếp 2 lần:", sort_logs(web_logs.copy()))