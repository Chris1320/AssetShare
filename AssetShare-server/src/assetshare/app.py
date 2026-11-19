from fastapi import FastAPI

from assetshare.core import info
from assetshare.routes.misc import router as misc_router

app = FastAPI(
    title=info.NAME,
    version=info.VERSION,
    description=info.DESCRIPTION,
    root_path="/api",
)

app.include_router(misc_router)
