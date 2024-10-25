import os
import random
import time

def generate_payload(protocol, sin_length, max_length):
    if protocol == "udp":
        # Generate random bytes for the payload
        payload = os.urandom(sin_length) + os.urandom(random.randint(1, max_length - sin_length))
        # Format payload as hex string
        formatted_payload = ''.join(f'\\x{byte:02X}' for byte in payload)
        return formatted_payload
    return None

def print_with_delay(text, delay=0.0001):  # Extremely fast output
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the payload

def main():
    print("Enter 'start' to begin payload generation or 'end' to exit.")
    command = input("Command: ").strip().lower()
    
    if command == "start":
        protocol = input("Enter the protocol ('udp', 'icmp', or 'top'): ").strip().lower()
        
        try:
            sin_length = int(input("Enter the sinus length of the UDP payload (default 8): ") or 8)
            max_length = int(input("Enter the maximum length of the UDP payload (default 1024): ") or 1024)
            num_payloads = int(input("Enter the number of payloads to generate: "))
            
            if num_payloads <= 0:
                print("Number of payloads must be greater than 0.")
                return
            
            with open("om.txt", "w") as file:  # Open file to save payloads
                for _ in range(num_payloads):
                    payload = generate_payload(protocol, sin_length, max_length)
                    if payload is not None:
                        print_with_delay(f"Generated payload: {payload}", delay=0.0001)  # Fast output
                        file.write(f"{payload}\n")  # Save each payload to the file
                    else:
                        print("Unsupported protocol entered.")
                        return
            print("All payloads saved to 'om.txt'.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values for lengths and number of payloads.")
    
    elif command == "end":
        print("Exiting.")
    else:
        print("Invalid command. Please enter 'start' or 'end'.")

if __name__ == "__main__":
    main()