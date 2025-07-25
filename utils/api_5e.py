# utils/api_5e.py
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

API_BASE_URL = "https://api.open5e.com"
MAX_WORKERS = 10

def fetch_all_resources(resource_type: str) -> list[dict]:
    """Fetch all pages of a given resource type from the 5e-bits API."""
    results = []
    url = f"{API_BASE_URL}/{resource_type}/"

    while url:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch {url} — Status code {response.status_code}")

        data = response.json()
        results.extend(data["results"])
        url = data.get("next")

    return results

def fetch_all_resources_mt(resource_type: str) -> list[dict]:
    """Fetch all pages of a given resource type from the Open5e API in parallel."""
    results = []
    url = f"{API_BASE_URL}/{resource_type}/"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url} — Status code {response.status_code}")

    # Fetch first page to determine how many total pages
    data = response.json()
    results = data["results"]
    count = data["count"]
    page_size = len(data["results"])
    total_pages = (count + page_size - 1) // page_size

    print(f"📦 Total {count} {resource_type}, {total_pages} pages")

    # Prepare all remaining URLs
    # urls = [f"{url}?page={i}" for i in range(2, total_pages + 1)]
    urls = [(i, f"{url}?page={i}") for i in range(2, total_pages + 1)]

    def fetch_page(page_info):
        page_num, page_url = page_info
        print(f"⏳ Fetching page {page_num}...")
        r = requests.get(page_url)
        if r.status_code == 200:
            print(f"✅ Page {page_num} fetched ({len(r.json()['results'])} items)")
            return r.json()["results"]
        else:
            print(f"❌ Failed to fetch page {page_num} — Status {r.status_code}")
            return []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(fetch_page, u) for u in urls]
        for future in as_completed(futures):
            results.extend(future.result())

    return results