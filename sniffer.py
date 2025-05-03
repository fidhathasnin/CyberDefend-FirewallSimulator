from scapy.all import sniff, IP
import time

class PacketSniffer:
    def __init__(self, rules_ref, logs_ref):
        self.rules = rules_ref  # Reference to Flask's rules list
        self.logs = logs_ref    # Reference to Flask's logs list
        self.running = True

    def packet_callback(self, packet):
        if packet.haslayer(IP):
            src_ip = packet[IP].src
            matched_rule = next(
                (rule for rule in self.rules if rule['ip'] == src_ip),
                None
            )
            
            if matched_rule:
                log_msg = f"🚫 BLOCKED packet from {src_ip} ({matched_rule['action']})"
                self.logs.append(log_msg)
                print(log_msg)
                if matched_rule['action'] == 'BLOCK':
                    return  # Drop packet
            
            log_msg = f"✅ Allowed packet from {src_ip} - {packet.summary()}"
            self.logs.append(log_msg)
            print(log_msg)

    def start(self):
        print("🔥 Starting packet sniffer...")
        while self.running:
            try:
                sniff(
                    prn=self.packet_callback,
                    filter="ip",
                    store=0,
                    timeout=5  # Check for shutdown every 5 seconds
                )
            except Exception as e:
                print(f"Sniffer error: {e}")
                time.sleep(1)

    def stop(self):
        self.running = False