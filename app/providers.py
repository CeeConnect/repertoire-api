from .repositories import FicheRepository, BonificationRepository
from .views import Fiche, Bonification


class FicheCollectionProvider:
    repository = FicheRepository()

    def provides(self, query: dict) -> list[Fiche]:
        return [Fiche.fromentity(item) for item in self.repository.search(params=query)]


class FicheItemProvider:
    repository = FicheRepository()

    def provides(self, id: str) -> Fiche | None:
        entity = self.repository.find(id=id)
        return Fiche.fromentity(entity) if entity != None else None


class BonificationCollectionProvider:
    repository = BonificationRepository()

    def provides(self, query: dict) -> list[Bonification]:
        return [
            Bonification.fromentity(item)
            for item in self.repository.search(params=query)
        ]


class BonificationItemProvider:
    repository = BonificationRepository()

    def provides(self, id: str) -> Bonification | None:
        entity = self.repository.find(id=id)
        return Bonification.fromentity(entity) if entity != None else None
