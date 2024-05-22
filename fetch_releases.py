import requests
import json
import os

def fetch_releases(repository):
    url = f'https://api.github.com/repos/{repository}/releases'
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功
        releases = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching releases: {e}")
        return []

    filtered_releases = [
        {
            'name': release['name'],
            'tag_name': release['tag_name'],
            'prerelease': release['prerelease'],
            'assets': [
                {
                    'name': asset['name'],
                    'browser_download_url': asset['browser_download_url']
                } for asset in release['assets']
            ]
        } for release in releases
    ]

    return filtered_releases

def save_releases_to_file(releases, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(releases, f, indent=2)
        print(f"Releases saved to {filename} successfully.")
    except IOError as e:
        print(f"Error saving releases to file: {e}")

def main():
    repository = '2dust/v2rayN'
    releases = fetch_releases(repository)
    if releases:
        save_releases_to_file(releases, 'v2rayN_releases.json')

if __name__ == "__main__":
    main()
