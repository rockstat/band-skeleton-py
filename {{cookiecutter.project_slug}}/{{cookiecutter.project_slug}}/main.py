# Band service skeleton
# (c) Dmitry Rodin 2018
# ---------------------
import asyncio
from itertools import count
from prodict import Prodict as pdict
from band import expose, cleanup, worker, settings, logger, response


state=pdict()


@expose.handler()
async def main(**params):
    pass


@worker()
async def service_worker():
    for num in count():
        try:
            if num == 0:
                pass
        except asyncio.CancelledError:
            break
        except Exception:
            logger.exception('exc')
        await asyncio.sleep(30)
