
import time
import requests


PRIMARY_MODEL = "primary-model"
FALLBACK_MODEL = "fallback-model"

MAX_RETRIES = 3


class ResilientAPI:
    def __init__(self):
        self.session = requests.Session()

    def call_model(self, model, prompt):
        """
        Demo API behavior:
        The primary model returns HTTP 429 twice,
        then succeeds. The fallback model succeeds immediately.
        """
        if not hasattr(self, "attempts"):
            self.attempts = {}

        self.attempts[model] = self.attempts.get(model, 0) + 1

        attempt = self.attempts[model]

        print(f"Calling {model}, attempt {attempt}...")

        # Simulate rate limiting for the primary model
        if model == PRIMARY_MODEL and attempt <= 2:
            response = requests.Response()
            response.status_code = 429
            response._content = b'{"error": "Rate limit exceeded"}'
            return response

        # Simulate a successful API response
        response = requests.Response()
        response.status_code = 200
        response._content = (
            f'{{"model": "{model}", '
            f'"result": "Processed: {prompt}"}}'
        ).encode("utf-8")

        return response

    def request_with_retry(self, model, prompt):
        for attempt in range(MAX_RETRIES):
            response = self.call_model(model, prompt)

            if response.status_code == 200:
                return response.json()

            if response.status_code == 429:
                wait_time = 2 ** attempt
                print(
                    f"Rate limited. Waiting {wait_time} seconds..."
                )
                time.sleep(wait_time)
                continue

            response.raise_for_status()

        return None

    def generate(self, prompt):
        # Try the primary model first
        result = self.request_with_retry(PRIMARY_MODEL, prompt)

        if result is not None:
            return result

        # Switch to fallback after retries are exhausted
        print("\nPrimary model failed. Switching to fallback...")

        result = self.request_with_retry(FALLBACK_MODEL, prompt)

        if result is not None:
            return result

        raise RuntimeError("Both models failed.")


if __name__ == "__main__":
    api = ResilientAPI()

    try:
        result = api.generate(
            "Explain Python in one sentence."
        )

        print("\nFinal result:")
        print(result)

    except (requests.RequestException, RuntimeError) as error:
        print(f"API request failed: {error}")
