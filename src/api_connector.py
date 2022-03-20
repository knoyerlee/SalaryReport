import requests
import os

class ApiConnectionTools:

    def __init__(self):
        self.url = "https://api.adzuna.com/v1/api/"
        self.app_id = os.environ["ADZUNA_APP_ID"]
        self.app_key = os.environ["ADZUNA_APP_KEY"]   

    # Connection Functions
    def generate_category_results(self, country="us"):
        """This function takes the country you want to search for job categories in. By Default the country is the us."""

        adzuna_categories_conn = requests.get(f"{self.url}jobs/{country}/categories?app_id={self.app_id}&app_key={self.app_key}&&content-type=application/json")

        adzuna_categories_json = adzuna_categories_conn.json()

        final_sorted_categories = self._sort_category_results(adzuna_categories_json)

        return final_sorted_categories

    def generate_salary_results(self, category, country="us", timeframe="12"):
        """This function will return the salary data for an approved category. You can specify the country or timeframe you want.
        If you do not it will be the us over the past 12 months."""

        adzuna_get = requests.get(f"{self.url}jobs/{country}/history/?app_id={self.app_id}&app_key={self.app_key}&category={category}&months={timeframe}")

        adzuna_response = adzuna_get.json()

        final_adzuna_response = self._sort_salary_results(adzuna_response)

        return final_adzuna_response

# Helper Functions
    def _sort_category_results(self, results):
        """This is a helper function  that looks at category results from an Api call and trims them down putting them into a list."""

        category_list = []

        for x in results["results"]:
            category_list.append(x["tag"])

        return category_list

    def _sort_salary_results(self, results):
        """This is a helper function to take in month/salary results from an Api call sort them and return them in a chronological list based on month."""

        sorted_results = sorted(results["month"].items())

        return sorted_results