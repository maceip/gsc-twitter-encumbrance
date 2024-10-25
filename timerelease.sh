#!/bin/bash

# 

# Define your target release time in a human-readable format
TIMEOUT_TIMESTAMP="2024-10-25 1:15pm pdt"

# Convert human-readable time to Unix timestamp
timeout_unix=$(date -d "$TIMEOUT_TIMESTAMP" +"%s")

# Public Ethereum JSON-RPC endpoint
ETH_NODE_URL="https://rpc.ankr.com/eth"

# Continuously check every minute until the target time is reached
while true; do
    # Fetch the latest block's timestamp
    timestamp_hex=$(curl -s -X POST -H "Content-Type: application/json" --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}' $ETH_NODE_URL | jq -r '.result.timestamp')

    # Remove "0x" prefix and convert to decimal
    current_timestamp=$((16#${timestamp_hex#0x}))

    # Check if current Ethereum timestamp has reached the timeout
    if (( current_timestamp >= timeout_unix )); then
        echo "Time release triggered!"
	echo $PRIVATE_KEY
        break
    else
        echo "Not yet. Waiting until $TIMEOUT_TIMESTAMP (Current Ethereum time: $(date -d @$current_timestamp))"
    fi

    # Wait for 1 minute before checking again
    sleep 60
done
