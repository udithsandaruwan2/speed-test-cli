import speedtest
import colorama

def get_server(st):
    # Get the best server
    best = st.get_best_server()
    
    # Extract server details
    host =  best['sponsor']
    host = (colorama.Fore.GREEN + f'{host}')
    country  = best['country']
    country = (colorama.Fore.GREEN + f'{country}')
    city = best['name']
    city = (colorama.Fore.GREEN + f"{city}")

    # Print ISP information
    print(f'ISP: {host}, {city}, {country}')


def main():
    # Initialize colorama for colored text
    colorama.init(autoreset=True)

    while True:
        print('Finding the best server...')
        
        # Initialize Speedtest
        st = speedtest.Speedtest(secure=True)

        # Fetch and display server information
        get_server(st)

        # Perform speed test and display results
        download_speed = st.download() / (1024 * 1024)
        upload_speed = st.upload() / (1024 * 1024)

        print(colorama.Fore.GREEN + f"\nDownload Speed: {download_speed:.2f} Mbps ({download_speed / 8:.2f} MBps)")
        print(colorama.Fore.GREEN + f"Upload Speed: {upload_speed:.2f} Mbps ({upload_speed / 8:.2f} MBps)\n")

        print("")
        print("THANK YOU FOR USING US -- UDITHSANDARUWAN.COM || UDITHSANDARUWAN.XYZ")
        print("")

        break

if __name__ == "__main__":
    main()