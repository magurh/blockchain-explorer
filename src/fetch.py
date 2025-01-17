import requests

from src.config import config
from src.utils import save_block


def fetch_block(block_number):
    """
    Fetches a specific block by its number from the Flare Network.
    :param block_number: The block number to fetch (integer).
    :return: The block data as a dictionary.
    """
    # JSON-RPC request payload
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(block_number), True],  # Convert block number to hex
        "id": 1,
    }

    try:
        # Send the POST request to the RPC URL
        response = requests.post(config.RPC_URL, json=payload)
        response.raise_for_status()

        # Parse the JSON response
        block_data = response.json().get("result")
        if block_data:
            return block_data
        else:
            print(
                "Error: No block data returned. Check block number or network status."
            )
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching block: {e}")
        return None


# Example usage
if __name__ == "__main__":
    block_number = 100  # Replace with the desired block number
    block = fetch_block(block_number)

    if block:
        filename = f"block_{block_number}.json"  # Example filename
        save_block(block, filename)
