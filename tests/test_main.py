import collections.abc
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_fiches():
    response = client.get("/fiches")
    assert response.status_code == 200
    assert isinstance(response.json(), collections.abc.Sequence)

def test_get_fiche_by_id():
    response = client.get("/fiches/BAR-TH-172v55-1")
    assert response.status_code == 200
    assert response.json() == {
        "id": "BAR-TH-172v55-1",
        "code": "BAR-TH-172",
        "version": "A55-1",
        "nom": "Pompe à chaleur de type eau/eau ou sol/eau",
        "dateDebut": "2024-01-01",
        "dateFin": "2028-06-30",
        "metropole": True,
        "outreMer": True,
        "secteur": { "code": "BAR", "nom": "Bâtiment Résidentiel"},
        "sousSecteur": {"code": "TH", "nom": "Thermique"}
    }

def test_get_bonifications():
    response = client.get("/bonifications")
    assert response.status_code == 200
    assert isinstance(response.json(), collections.abc.Sequence)

def test_get_bonification_by_id():
    response = client.get("/bonifications/BAR-TH-171.CDP-1v52-1")
    assert response.status_code == 200
    assert response.json() == {
        "id": "BAR-TH-171.CDP-1v52-1",
        "code": "CDP-1",
        "nature": "CDP",
        "version": "A52-1",
        "fiche": "BAR-TH-171",
        "nom": "Coup de pouce Chauffage",
        "dateDebut": "2023-10-07",
        "dateFin": None
    }

def test_get_bonus():
    response = client.get("/bonus")
    assert response.status_code == 200
    assert isinstance(response.json(), collections.abc.Sequence)

def test_get_bonus_by_id():
    response = client.get("/bonus/ZNIv35-1")
    assert response.status_code == 200
    assert response.json() == {
        "id": "ZNIv35-1",
        "code": "ZNI",
        "version": "A35-1",
        "nom": "Zones non interconnectées au réseau métropolitain continental de transport d'électricité",
        "dateDebut": "2021-04-17",
        "dateFin": None
    }
