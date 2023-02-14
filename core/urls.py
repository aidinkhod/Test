from core.controller import PagesController, PostsController
from core.router import Router

router = Router()
router.get("/", PagesController, "home")
router.get("/add", PagesController, "add")
router.get("/posts", PostsController, "posts")
router.post('/', PagesController, "home")
