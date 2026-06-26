from http.server import BaseHTTPRequestHandler
import json
import urllib.request
from datetime import datetime

# YOUR MULTI-MILLION DOLLAR AMAZON TAG
AMAZON_TAG = "timevalue0e2-20"

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Get Current Time to determine Match Phase (Simulated for 0-confusion setup)
        hour = datetime.now().hour
        phase = "pre_match" if hour < 12 else "halftime" if hour < 15 else "post_match"

        # 2. Define Context-Aware Amazon Products (High Ticket + High Volume)
        products = {
            "pre_match": {
                "title": "Ultimate FIFA Watch Party Snack & Drink Bundle",
                "search": "party snack box delivery",
                "value_msg": "Match is starting soon! Don't run out of snacks. Get this ultimate bundle delivered in 2 hours."
            },
            "halftime": {
                "title": "Samsung 75-Inch 4K QLED Smart TV",
                "search": "75 inch 4k smart tv",
                "value_msg": "HALFTIME! Is your TV blurry? Upgrade to 4K QLED right now and get it before the 2nd half kicks off!"
            },
            "post_match": {
                "title": "Official FIFA World Cup Replica Jersey",
                "search": "official fifa world cup jersey",
                "value_msg": "What a match! Celebrate the win with the official replica jersey. Limited stock available."
            }
        }

        current_product = products[phase]
        
        # 3. Generate the Exact Amazon Affiliate Link
        # (In production, this calls Amazon PA-API 5.0. For instant setup, we use Amazon Search URL with your tag)
        affiliate_link = f"https://www.amazon.com/s?k={urllib.parse.quote(current_product['search'])}&tag={AMAZON_TAG}"

        # 4. Deliver the "Real Value" JSON to the Fan/Frontend
        response_data = {
            "fan_value": {
                "status": "LIVE MATCH CENTER",
                "phase": phase.replace("_", " ").title(),
                "message": current_product["value_msg"],
                "recommended_product": current_product["title"]
            },
            "monetization": {
                "affiliate_tag": AMAZON_TAG,
                "click_here_to_buy": affiliate_link,
                "potential_commission": "$45.00 - $120.00 per sale"
            }
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=4).encode('utf-8'))
