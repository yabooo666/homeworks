import re
import time
from django.db.models import F
from .models import Category


class CategoryVisitAndPerformanceMiddleware:
    """
    Middleware:
    1. ითვლის კონკრეტულ კატეგორიაზე მომხმარებლების წვდომის (ნახვების) რაოდენობას და ანახლებს ბაზაში.
    2. ზომავს თითოეული request/response-ის შესრულების დროს (ხანგრძლივობას).
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.category_pattern = re.compile(r"^/category/(?P<category_id>\d+)/?$")

    def __call__(self, request):
        # 1. request-ის დასაწყისის დროის დაფიქსირება
        start_time = time.time()

        # 2. კატეგორიის ნახვის დაფიქსირება
        match = self.category_pattern.match(request.path)
        if match:
            category_id = match.group("category_id")
            try:
                # განახლება ატომურად (F expression)
                Category.objects.filter(id=category_id).update(visit_count=F("visit_count") + 1)
            except Exception:
                pass

        # 3. response-ის მიღება
        response = self.get_response(request)

        # 4. ხანგრძლივობის გამოთვლა
        duration_ms = (time.time() - start_time) * 1000
        response["X-Response-Time-Ms"] = f"{duration_ms:.2f}"

        return response
