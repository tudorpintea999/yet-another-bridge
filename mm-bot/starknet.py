import requests
import constants
import json

class SetOrderEvent:
    def __init__(self, recipient_address, amount):
        self.recipient_address = recipient_address
        self.amount = amount
    
    def __str__(self):
        return f"recipent: {self.recipient_address}, amount: {self.amount}"

def get_starknet_events() -> int:
    body = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "starknet_getEvents",
        "params": [
            {
            "address": constants.SN_CONTRACT_ADDR,
            "chunk_size": 1000
            }
        ]
    }
    return requests.post(constants.SN_RPC_URL, json = body)

def get_latest_order(): 
    request_result = get_starknet_events().json()
    events = request_result['result']['events']

    # orders = []
    SET_ORDER_KEY_EVENT='0x2c75a60b5bdad73ebbf539cc807fccd09875c3cbf3f44041f852cdb96d8acd3'
    for i in reversed(range(len(events))):
        # Obtain first event that match with SET_ORDER_KEY_EVENT
        # We assume that we have a single SetOrder event
        if (len(events[i]['keys']) > 0 and events[i]['keys'][0] == SET_ORDER_KEY_EVENT):
            # orders.append(SetOrderEvent(event['data'][0], event['data'][1]))
            order = SetOrderEvent(events[i]['data'][0], events[i]['data'][1])
            break

    if (order):
        return order
    else:
        return None

print(get_latest_order())
# main
# wait x secs
# call check_new_events
# track latest order_id that was processed