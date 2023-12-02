import requests

from settings.implemented import YOUR_ACCESS_KEY


class SalaryConversion:
    """
    The class converts currencies using the apilayer.
    Methods:
        _check_salary_dict: The method checks the value in the dictionary for existence, if it does not exist,
            it replaces it with 0. If there is no dictionary, it creates a new one with zero values
        salary_value: replaces the Null value with 0, calculates the average salary,
            converts it to RUB if it is not already in rubles
        salary_conversion: sends a request to the URL, receives a response,
            and we get the result from it
    """

    @classmethod
    def _check_salary_dict(cls, salary_dict: dict) -> dict:
        """
        Returns a dictionary converted for operation with some modified values
        Param:
            salary_dict: dict, dictionary with all salary parameters
        Return:
            dict: the converted dictionary
        """
        if salary_dict:
            for i in salary_dict:
                if salary_dict[i] is None:
                    salary_dict[i] = 0
        else:
            salary_dict = {"from": 0, "to": 0, "currency": "RUR"}
        return salary_dict

    @classmethod
    def salary_value(cls, salary_dict: dict) -> int:
        """
        The method returns the final beautiful salary value
        Param:
            salary_dict: dict, dictionary with all salary parameters
        Return:
            int, the final salary value
        """
        salary_dict = cls._check_salary_dict(salary_dict)
        from_value = salary_dict.get('from')
        to_value = salary_dict.get('to')
        currency = salary_dict.get('currency')

        value = (from_value + to_value) // 2
        if currency != 'RUR':
            result = cls._salary_conversion(currency, value)
            return result
        return value

    @staticmethod
    def _salary_conversion(from_value: str, amount: int, to_value='RUB') -> int:
        """
        Converts currencies according to the updated values

        Params:
            from_value: str, the name of the currency to convert from
            to_value: str, the name of the currency to convert to
            amount: int, the amount to be converted to another value

        Return:
            int, converted value
        """
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_value}&from={from_value}&amount={amount}"
        payload = {}
        headers = {"apikey": YOUR_ACCESS_KEY}
        response = requests.request("GET", url, headers=headers, data=payload)
        return round(response.json()['result'])
