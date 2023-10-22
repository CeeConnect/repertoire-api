from typing import Self
from .entities import Fiche as FicheEntity
from .entities import Bonification as BonificationEntity


class Secteur:
    def __init__(self, code: str, nom: str):
        self.code = code
        self.nom = nom


class SousSecteur:
    def __init__(self, code: str, nom: str):
        self.code = code
        self.nom = nom


class Fiche:
    def __init__(
        self,
        id: str,
        code: str,
        nom: str,
        version: str,
        dateDebut: str,
        dateFin: str | None,
        metropole: bool,
        outreMer: bool,
        secteur: Secteur,
        sousSecteur: SousSecteur,
    ):
        self.id = id
        self.code = code
        self.nom = nom
        self.version = version
        self.dateDebut = dateDebut
        self.dateFin = dateFin
        self.metropole = metropole
        self.outreMer = outreMer
        self.secteur = secteur
        self.sousSecteur = sousSecteur

    @staticmethod
    def fromentity(entity: FicheEntity) -> Self:
        return Fiche(
            id=entity.id,
            code=entity.code,
            nom=entity.nom,
            version=entity.version,
            dateDebut=entity.date_debut.strftime("%Y-%m-%d"),
            dateFin=entity.date_fin.strftime("%Y-%m-%d")
            if entity.date_fin != None
            else None,
            metropole=entity.metropole,
            outreMer=entity.outre_mer,
            secteur=Secteur(code=entity.code_secteur, nom=entity.secteur),
            sousSecteur=Secteur(code=entity.code_sous_secteur, nom=entity.sous_secteur),
        )


class Bonification:
    def __init__(
        self,
        id: str,
        code: str,
        nature: str,
        nom: str,
        version: str,
        dateDebut: str,
        dateFin: str | None,
    ):
        self.id = id
        self.code = code
        self.nature = nature
        self.nom = nom
        self.version = version
        self.dateDebut = dateDebut
        self.dateFin = dateFin

    @staticmethod
    def fromentity(entity: BonificationEntity) -> Self:
        return Bonification(
            id=entity.id,
            code=entity.code,
            nature=entity.nature,
            nom=entity.nom,
            version=entity.version,
            dateDebut=entity.date_debut.strftime("%Y-%m-%d"),
            dateFin=entity.date_fin.strftime("%Y-%m-%d")
            if entity.date_fin != None
            else None,
        )
