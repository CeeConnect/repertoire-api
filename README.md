# API Répertoire

## Installation

```
git clone https://github.com/CeeConnect/repertoire-api.git repertoire
cd repertoire
git submodule update --remote
pipenv install
cd app
pipenv run uvicorn main:app --reload
```

## Test

```
pipenv run install --dev
pipenv run pytest
```

## Releases

### @next

- [] Endpoint dédié au téléchargement des fiches d'opérations standardisées au format PDF
