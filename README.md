# trading-webserver-python

**Description**: Setup a web server with the following functionalities

Place an order on an exchange for a given market (which is marked as executed after 60 seconds of delay)
Cancel a given order 
Fetch balance
- both across exchanges and a specific exchange
- both across tokens and a specific token
Withdraw specific token balance (eg: ETH) to any one of the whitelisted address set

Also, simulate random failures for each of these endpoints with proper feedback to the API consumer.

Note: Use dummy datasets (either in-memory/sqlite) to power the responses

**Test Suite**:
1. Fetch balance for INR
	=> show the starting INR balance

2. Place order worth 50% of the INR balance
	=> return the order reference

3. Fetch balance for INR
	=> show the balance deduction corresponding to the order in-place

4. Cancel the placed order
	=> return the order reference along with status

5. Fetch balance for INR
	=> show the starting INR balance (cancelling the deduction)

6. Place order worth 110% of the INR balance
	=> throw very legible error about insufficient balance

7. Fetch balance for INR
	=> show the starting INR balance (no deductions)

8. Place order worth 100% of the INR balance
	=> return the order reference

9. Fetch balance for INR
	=> show the balance deduction corresponding to the order in-place


**Installation Setup After Cloning**:
1. Create venv using 'python -m venv venv'
2. Activate it using 'source venv/bin/activate'
3. Install requirements using 'pip install -r req.txt'
4. Now run the server using 'python manage.py runserver'


**Endpoint Results**:

1. Order Curl:

	curl --location 'https://8000-gitpodio-empty-18m1e98ma7u.ws-us115.gitpod.io/api/v0/order/' \
	--header 'Content-Type: application/json' \
	--data '{
	    "exchange": "a",
	    "asset_name": "BITCOIN",
	    "type_of_order": "BUY",
	    "order_quantity": 0.5
	}'

	Response: 
	
	{
	    "Message": "Order Placed Successfully, Reference_ID = 635867"
	}


2. Balance Curl:

	curl --location 'https://8000-gitpodio-empty-18m1e98ma7u.ws-us115.gitpod.io/api/v0/balance/' \
	--header 'Content-Type: application/json' \
	--data '{
	"exchange": ["a"],
	"asset_name" : ["BITCOIN"]
	}'

	Response: 
	
	{
	    "Balance(s)": {
	        "a": {
	            "BITCOIN": 60.0
	        }
	    }
	}


3. Cancel Curl:

	curl --location 'https://8000-gitpodio-empty-18m1e98ma7u.ws-us115.gitpod.io/api/v0/cancel/' \
	--header 'Content-Type: application/json' \
	--data '{
	    "exchange": "a",
	    "asset_name": "BITCOIN",
	    "order_id": 761230
	}'
	
	Response:
	
	{
	    "Message": "Order Cancelled Successfully"
	}


4. Withdraw Curl:

	curl --location 'https://8000-gitpodio-empty-18m1e98ma7u.ws-us115.gitpod.io/api/v0/withdraw/' \
	--header 'Content-Type: application/json' \
	--data '{
	    "exchange": "a",
	    "amount": 48,
	    "asset_name": "BITCOIN",
	    "address": "A"
	}'
	
	Response:
	
	{
	    "Message": "Withdraw Successfully Done"
	}


**TODO**:
1. Configure DB
2. Add Loggers
