from cgitb import handler
import requests
from mangum import Mangum

from fastapi import FastAPI

app = FastAPI(title="WhoToFollow")
s = requests.Session()


def sort_by_stars(query: str) -> dict:
    url = f"https://api.github.com/search/repositories?q={query}&sort=star&order=desc"
    r = s.get(url)
    return r.json()


@app.get("/{technology}/projects")
def get_by_amount_of_projects():
    ...


@app.get("/{technology}/stars")
def get_by_amount_of_stars(technology: str) -> dict:
    repos = sort_by_stars(technology)
    top_five = repos['items'][:5]
    readable_top_five = {}

    for repo in top_five:
        readable_top_five[repo['owner']['login']] = repo['owner']['url']

    return readable_top_five


@app.get("/{technology}")
def get_based_on_projects_and_stars():
    ...


@app.get("/{technology}/projects/{total_profiles}")
def get_n_profiles_by_amount_of_projects():
    ...


@app.get("/{technology}/stars/{total_profiles}")
def get_n_profiles_by_amount_of_stars():
    ...


@app.get("/{technology}/{total_profiles}")
def get_n_profiles_based_on_projects_and_stars():
    ...

handler = Mangum(app=app)
