from .repositories import FicheRepository, BonificationRepository, BonusRepository
from .views import Fiche, Bonification, Bonus


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


class BonusCollectionProvider:
    repository = BonusRepository()

    def provides(self, query: dict) -> list[Bonus]:
        return [Bonus.fromentity(item) for item in self.repository.search(params=query)]


class BonusItemProvider:
    repository = BonusRepository()

    def provides(self, id: str) -> Bonus | None:
        entity = self.repository.find(id=id)
        return Bonus.fromentity(entity) if entity != None else None
