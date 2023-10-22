import pandas
from pandas import DataFrame
from pathlib import Path
from datetime import datetime
from .entities import Fiche, Bonification

repertoire_fiche = Path(__file__).parent / "../etc/db/repertoire_fiche.csv"
repertoire_bonification = (
    Path(__file__).parent / "../etc/db/repertoire_bonification.csv"
)


def csv_reader(file) -> DataFrame:
    dataframe = pandas.read_csv(
        file,
        delimiter=";",
        encoding="utf-8",
        parse_dates=["date_debut", "date_fin"],
    )

    dataframe["date_fin"] = (
        dataframe["date_fin"]
        .astype(object)
        .where(dataframe["date_fin"].notnull(), None)
    )

    return dataframe


class FicheRepository:
    def __init__(self):
        self.db = csv_reader(repertoire_fiche).to_dict("records")

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(FicheRepository, cls).__new__(cls)
        return cls.instance

    def find(self, id: str) -> Fiche | None:
        collection = list(filter(lambda x: x["id"] == id, self.db))
        return self.to_entity(collection[0]) if len(collection) > 0 else None

    def search(self, params: dict = {}) -> list[Fiche]:
        def fn(row) -> bool:
            if params.get("code", None) and params["code"] != row["code"]:
                return False
            if params.get("secteur", None) and params["secteur"] != row["code_secteur"]:
                return False
            if (
                params.get("sousSecteur", None)
                and params["sousSecteur"] != row["code_sous_secteur"]
            ):
                return False
            if params.get("date", None):
                date = datetime.fromisoformat(params["date"])
                start = row["date_debut"]
                end = row["date_fin"]

                if start > date or (end != None and end < date):
                    return False

            if (
                params.get("metropole", None)
                and params["metropole"] != row["metropole"]
            ):
                return False

            return True

        return [self.to_entity(item) for item in list(filter(fn, self.db))]

    def to_entity(self, data: dict) -> Fiche:
        return Fiche(
            id=data["id"],
            code=data["code"],
            nom=data["nom"],
            version=data["version"],
            date_debut=data["date_debut"],
            date_fin=data["date_fin"],
            metropole=bool(data["metropole"]),
            outre_mer=bool(data["outre_mer"]),
            code_secteur=data["code_secteur"],
            secteur=data["secteur"],
            code_sous_secteur=data["code_sous_secteur"],
            sous_secteur=data["sous_secteur"],
        )


class BonificationRepository:
    def __init__(self):
        self.db = csv_reader(repertoire_bonification).to_dict("records")

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(BonificationRepository, cls).__new__(cls)
        return cls.instance

    def find(self, id: str) -> Bonification | None:
        collection = list(filter(lambda x: x["id"] == id, self.db))
        return self.to_entity(collection[0]) if len(collection) > 0 else None

    def search(self, params: dict = {}) -> list[Bonification]:
        def fn(row) -> bool:
            if params.get("code", None) and params["code"] != row["code"]:
                return False
            if params.get("date", None):
                date = datetime.fromisoformat(params["date"])
                start = row["date_debut"]
                end = row["date_fin"]

                if start > date or (end != None and end < date):
                    return False

            return True

        return [self.to_entity(item) for item in list(filter(fn, self.db))]

    def to_entity(self, data: dict) -> Bonification:
        return Bonification(
            id=data["id"],
            code=data["code"],
            nature=data["nature"],
            nom=data["nom"],
            version=data["version"],
            date_debut=data["date_debut"],
            date_fin=data["date_fin"],
        )
