# Author: ssshipilo
# Website: https://savweb.studio/
# IMPORTANT: This code is provided for testing purposes only.
# The author is not responsible for any consequences of its use and your funds

import requests
import http.client
import re
import json

class SMSPVActivator():

    def __init__(self, apikey):
        self.apikey = apikey
        self.api_domain = "api.smspva.com"

    # Activation API v2
    def get_number(self, country, service, headers={}):
        """
        ## Obtaining a phone number

        params (type):
            country (str): - ICO standart country (example: US)
            service (str): service ico code (example: opt132) | service list # https://docs.smspva.com/#tag/activation_v2_lists/Services-list
        """

        return self.__requests__(f"/activation/number/{country}/{service}", headers)
    
    def receive_sms(self, orderId, partnerkey=None):
        """
        ## Receiving a message
        """

        headers = {}
        if partnerkey:
            headers = { 'partnerkey': partnerkey }

        return self.__requests__(f"/activation/sms/{orderId}", headers)

    def get_balance(self):
        """
        ## Get balance
        """

        return self.__requests__("/activation/balance")['balance']
    
    def get_users_info(self):
        """
        ## Get user's info
        """

        return self.__requests__("/activation/userinfo")
    
    def get_available_numbers(self, country="RU"):
        """
        ## Get available numbers count for each country and mobile operator
        """

        return self.__requests__(f"/activation/countnumbers/{country}")
    
    def get_all_prices(self):
        """
        ## Get prices for all services
        """

        return self.__requests__(f"/activation/servicesprices")
    
    def get_service_price(self, country="RU", service="opt0"):
        """
        ## Get service price specific country
        """

        return self.__requests__(f"/activation/serviceprice/{country}/{service}")
    
    def get_prices_service(self, service, filter=None):
        """
        ## Get all prices for this service

        params (type):
            -   service (string) - Service (details: https://docs.smspva.com/#tag/activation_v2_lists/Services-list)
            -   filter (string) - height - if it's expensive-cheaper first, lower - first cheaper, then more expensive
        """
        
        result = self.get_all_prices()
        result_array = []

        for item in result:
            if item['service'] == service:
                result_array.append(item)

        if filter == "height":
            result_array.sort(key=lambda x: x['price'], reverse=True)
        elif filter == "lower":
            result_array.sort(key=lambda x: x['price'])

        return result_array

    def get_orders(self):
        """
        ## Get current orders
        """

        return self.__requests__(f"/activation/orders")['orders']

    def get_message_again(self, orderId=123456):
        """
        ## Delete current SMS to receive new one

        params (type):
            -   orderId (integer) - Order ID
        """

        return self.__requests__(f"/activation/clearsms/{orderId}", method="PUT")
    
    def cancel_order(self, orderId=123456):
        """
        ## Cancel order

        params (type):
            -   orderId (integer) - Order ID
        """

        return self.__requests__(f"/activation/cancelorder/{orderId}", method="PUT")
    
    def set_number_nonworking(self, orderId=123456):
        """
        ## Set number as nonworking

        params (type):
            -   orderId (integer) - Order ID
        """

        return self.__requests__(f"/activation/blocknumber/{orderId}", method="PUT")

    def сheck_number_receive_sms(self, number=98765432, service="opt0"):
        """
        ## Check if number is still able to receive SMS for certain service

        Check if number is still able to receive SMS for certain service. Only if you used to receive SMS on this number for this service previously.

        params (type):
            -   number (integer) - example: 98765432 | Phone number without country phone code.
            -   service (integer) - example: opt0 | Service code. To see all service codes please refer to servicesprices method.
        """

        return self.__requests__(f"/activation/numberstatus/{number}/{service}")
    
    def get_all_countries(self):
        """
        ## Full list of supported countries
        """

        return self.__sheme_markdown_parser__("country")
    
    def get_all_services(self):
        """
        ## Full list of supported services
        """

        return self.__sheme_markdown_parser__("services")
    
    def __requests__(self, endpoint, headers_array={}, method="GET"):
        try:
            conn = http.client.HTTPSConnection(self.api_domain)
            headers = { 'apikey': self.apikey }
            for key, value in dict(headers_array).items():
                headers[key] = value

            conn.request(method, endpoint, headers=headers)
            res = conn.getresponse()
            data = res.read()
            return json.loads(data.decode("utf-8"))['data']
        except:
            return False

    def __sheme_markdown_parser__(self, type):
        response = requests.get('https://docs.smspva.com/json/schema.php?lang=en', headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
        if response.status_code == 200:
            responses = response.text.split("---------- |  ---------- |  ---------- |  ----------")
            for idx, item in enumerate(responses):
                # Countries
                if type == "country":
                    if idx == 1:
                        table_row = item.split("	|	")
                        data_text =  " ".join(table_row)
                        pattern = re.compile(r'(\d+)\s!.*?images/flags/64/(.*?)\)\s+(.*?)\s+([A-Z]+)')
                        matches = pattern.findall(data_text)
                        result = []
                        for match in matches:
                            result.append({
                                'index': match[0],
                                'image': f'https://smspva.com/templates/New_theme/images/flags/64/{match[1]}',
                                'country': match[2].strip(),
                                'code': match[3].strip()
                            })

                        json_result = json.dumps(result, ensure_ascii=False, indent=2)
                        return json.loads(json_result)

                # Services
                if type == "services":
                    if idx == 2:                     
                        table_row = item.split("	|	")
                        data_text =  " ".join(table_row)
                        print(data_text)
                        result = []
                        for line in data_text.split('\n'):
                            parts = line.split(' ', 3)
                            if len(parts) == 4:
                                index = parts[0].strip()

                                image_filename = parts[1].split("/")
                                image_filename = image_filename[len(image_filename)-1]

                                parse = parts[3].split(" ")
                                if "activation_v2_fast_start" in parse[3].strip():
                                    continue

                                result.append({
                                    'index': index,
                                    'image': f'https://smspva.com/templates/New_Design/images/ico/{image_filename}',
                                    'service': parse[3].strip(),
                                    'code': parse[4].strip()
                                })

                        json_result = json.dumps(result, ensure_ascii=False, indent=2)
                        return json.loads(json_result)
                
            return []
        return []
