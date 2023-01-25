from rest_framework import routers
from .views import AttendeesViewset
router = routers.DefaultRouter()

router.register('gdg', AttendeesViewset, 'attendees')

urlpatterns = router.urls
print(urlpatterns)
