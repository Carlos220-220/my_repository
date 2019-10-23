from rest_framework.routers import SimpleRouter
from Food.views import Foods_View

router = SimpleRouter()
router.register(r'API/Food',Foods_View)