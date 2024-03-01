from smspva.api import SMSPVActivator

if __name__ == "__main__":
    smspva = SMSPVActivator("<YOU-API-TOKEN>")

    # Balance
    result = smspva.get_balance()
    print(result)

    # Get number
    result = smspva.get_number(country="TZ", service="opt1")
    print(result)

    # Users info
    result = smspva.get_users_info()
    print(result)

    # Get all prices
    result = smspva.get_all_prices()
    print(result)

    # Get service prices
    resut = smspva.get_prices_service("opt219", filter="lower")
    print(result)

    # Get orders
    resut = smspva.get_orders()
    print(result)

    # Get all countries
    resut = smspva.get_all_countries()
    print(result)

    # Get all services
    resut = smspva.get_all_services()
    print(result)

    # Get available numbers
    resut = smspva.get_available_numbers(country="SI")
    print(result)