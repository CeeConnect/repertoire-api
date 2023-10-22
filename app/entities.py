from datetime import datetime


class Fiche:
    def __init__(
        self,
        id: str,
        code: str,
        nom: str,
        version: str,
        date_debut: datetime,
        date_fin: datetime | None,
        metropole: bool,
        outre_mer: bool,
        code_secteur: str,
        secteur: str,
        code_sous_secteur: str,
        sous_secteur: str,
    ):
        self.id = id
        self.code = code
        self.nom = nom
        self.version = version
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.metropole = metropole
        self.outre_mer = outre_mer
        self.code_secteur = code_secteur
        self.secteur = secteur
        self.code_sous_secteur = code_sous_secteur
        self.sous_secteur = sous_secteur


class Bonification:
    def __init__(
        self,
        id: str,
        code: str,
        nature: str,
        nom: str,
        version: str,
        date_debut: datetime,
        date_fin: datetime | None,
    ):
        self.id = id
        self.code = code
        self.nature = nature
        self.nom = nom
        self.version = version
        self.date_debut = date_debut
        self.date_fin = date_fin
