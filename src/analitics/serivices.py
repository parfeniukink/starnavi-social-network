from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.query import QuerySet

from blog.models import Like


def get_quantity_of_likes_by_date(date_from: str, date_to: str) -> QuerySet:
    """Returns QuerySet(<Like(created_at, quantity_of_likes)>)
       date by date with agregated quantity of likes
       if user's entered data correctly
       request pattern: ?date_from=2020-02-20&date_to=2020-02-30
    """

    try:
        date_from = datetime.strptime(date_from, "%Y-%m-%d").date()
        date_to = datetime.strptime(date_to, "%Y-%m-%d").date()

        likes_by_date = Like.objects.filter(
            created_at__range=[date_from, date_to]
        ).values('created_at').annotate(quantity_of_likes=Count("id"))

        return likes_by_date

    except TypeError:
        return {
            'Type error': "Plese enter ?date_from=2020-02-20&date_to=2020-02-30 in URL"
        }
    except ValueError as e:
        return {
            'Value error': "Use ?date_from=2020-02-20&date_to=2020-02-30 in URL"
        }


def get_user_activity() -> QuerySet:
    """Returns QuerySet(<User(last_login, last_visit)>) object of users"""

    users = get_user_model().objects.values(
        'id',
        'last_login',
        'last_visit'
    )

    return users
