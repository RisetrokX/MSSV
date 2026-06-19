from mcstatus import JavaServer

def check_server(address):
    try:
        # Connect to the server
        server = JavaServer.lookup(address)
        status = server.status()
        
        print(f"--- Server Status: {address} ---")
        print(f"Players: {status.players.online}/{status.players.max}")
        print(f"Latency: {status.latency:.2f} ms")
        print(f"Version: {status.version.name}")
        
        # Display list of players if available
        if status.players.sample:
            print("Players online:")
            for player in status.players.sample:
                print(f"- {player.name}")
        else:
            print("No public player list available.")
            
    except Exception as e:
        print(f"Failed to connect to the server: {e}")

if __name__ == "__main__":
    ip = input("Enter server IP address (e.g., mc.hypixel.net): ")
    check_server(ip)
