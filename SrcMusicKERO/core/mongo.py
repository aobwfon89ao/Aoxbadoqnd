from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER("𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌").info("جـارِ الاتصـال بقاعـدة البيانـات . . .")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER("𝙿𝚊𝚗𝚍𝚊 𝙼𝚞𝚜𝚒𝚌").info("تم الاتصـال بقاعـدة البيانـات ...✓")
except:
    LOGGER(__name__).error("حدث خطأ اثناء الاتصال بقاعدة البيانات.")
    exit()
