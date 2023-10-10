from fastapi import FastAPI
from .providers import FicheItemProvider, FicheCollectionProvider
from .providers import BonificationItemProvider, BonificationCollectionProvider
from .providers import BonusItemProvider, BonusCollectionProvider

app = FastAPI(docs_url=None, redoc_url=None)


@app.get("/fiches")
async def get_fiches(
    code: str | None = None,
    secteur: str | None = None,
    sousSecteur: str | None = None,
    date: str | None = None,
    metropole: bool | None = None,
    outreMer: bool | None = None,
):
    provider = FicheCollectionProvider()
    return provider.provides(
        query={
            "code": code,
            "secteur": secteur,
            "sousSecteur": sousSecteur,
            "date": date,
            "metropole": metropole,
            "outreMer": outreMer,
        }
    )


@app.get("/fiches/{id}")
async def get_fiche_by_id(id: str):
    provider = FicheItemProvider()
    return provider.provides(id=id)


@app.get("/bonifications")
async def get_bonifications(
    code: str | None = None,
    fiche: str | None = None,
    date: str | None = None,
):
    provider = BonificationCollectionProvider()
    return provider.provides(query={"code": code, "fiche": fiche, "date": date})


@app.get("/bonifications/{id}")
async def get_bonification_by_id(id: str):
    provider = BonificationItemProvider()
    return provider.provides(id=id)


@app.get("/bonus")
async def get_bonus(
    code: str | None = None,
    date: str | None = None,
):
    provider = BonusCollectionProvider()
    return provider.provides(query={"code": code, "date": date})


@app.get("/bonus/{id}")
async def get_bonus_by_id(id: str):
    provider = BonusItemProvider()
    return provider.provides(id=id)
