from django.utils.html import escape, strip_tags

class InputSanitizingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Sanitize GET and POST data
        if request.method == 'POST':
            request.POST = self.sanitize_data(request.POST)
        if request.method == 'GET':
            request.GET = self.sanitize_data(request.GET)

        response = self.get_response(request)
        return response

    def sanitize_data(self, data):
        sanitized_data = data.copy()
        for key, value in sanitized_data.items():
            if isinstance(value, str):
                sanitized_data[key] = self.clean_input(value)
        return sanitized_data

    def clean_input(self, value):
        # You can use Django's built-in methods or external libraries for more strict sanitization
        cleaned_value = strip_tags(value)  # Remove HTML tags
        cleaned_value = escape(cleaned_value)  # Escape any special HTML characters
        return cleaned_value
