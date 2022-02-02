from chalice import Chalice
import requests

app = Chalice(app_name='whotofollow_api')
s = requests.Session()


@app.route('/')
def index():
    return {'hello': 'world'}


def sort_by_stars(query: str) -> dict:
    url = f"https://api.github.com/search/repositories?q={query}&sort=star&order=desc"
    r = s.get(url)
    return r.json()


@app.route("/{technology}/projects")
def get_by_amount_of_projects():
    ...


@app.route("/{technology}/stars")
def get_by_amount_of_stars(technology: str) -> dict:
    repos = sort_by_stars(technology)
    top_five = repos['items'][:5]
    readable_top_five = {}

    for repo in top_five:
        readable_top_five[repo['owner']['login']] = repo['owner']['url']

    return readable_top_five


@app.route("/{technology}")
def get_based_on_projects_and_stars():
    ...


@app.route("/{technology}/projects/{total_profiles}")
def get_n_profiles_by_amount_of_projects():
    ...


@app.route("/{technology}/stars/{total_profiles}")
def get_n_profiles_by_amount_of_stars():
    ...


@app.route("/{technology}/{total_profiles}")
def get_n_profiles_based_on_projects_and_stars():
    ...
