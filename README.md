# LOLlama

**LOLlama** is an open‑source, end‑to‑end pipeline that downloads a YouTube video, analyzes it with AI, dynamically generates memes based on context (without relying on a static folder), overlays the memes on the video, formats the result for YouTube, TikTok, and Instagram, and uploads them to your social media accounts.

## Features

- **Download Video:** Retrieves the best‑quality version from YouTube using *yt‑dl‑p*.
- **AI Analysis:** (Stub - Placeholder functionality) Analyzes the video using open‑source models (e.g. Whisper, Ollama/LLaMA‑2) to determine highlights and generate context. This feature is currently a prototype and requires further development.
- **Dynamic Meme Generation:** Generates contextually fitting memes using Stable Diffusion—creating images on the fly without a local meme folder.
- **Unique Naming & Thumbnail:** Automatically generates unique names and extracts a thumbnail from the edited video.
- **Multi‑Platform Formatting:** Produces video variants optimized for YouTube (5‑min clip), TikTok, and Instagram.
- **Upload Automation:** (Stub) Currently, the upload functionality is limited to basic authentication and placeholder methods for uploading videos. Users can extend this by integrating APIs or libraries such as YouTube Data API, TikTok API, or Instagram Graph API to enable full upload automation.
- **Parallel Processing:** Uses Python’s concurrency features to run stages concurrently.
- **Dockerized:** Fully containerized using Docker & docker‑compose for easy deployment on macOS (Apple M1).

## Requirements

- Docker & docker‑compose
- A system that supports Docker (e.g., macOS, including Apple M1 Max)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/LOLlama.git
   cd LOLlama

2.	Configure credentials:
    Provide your credentials for YouTube, TikTok, and Instagram either via environment variables or command‑line arguments. For example:
    
    docker build -t lollama .
      ```bash
      export YT_CREDENTIALS="path_to_youtube_credentials.json"
      export TIKTOK_COOKIES="your_tiktok_cookies"
      export IG_USER="your_instagram_username"
      export IG_PASS="your_instagram_password"
      ```
    - **Command-Line Arguments:** Pass the credentials directly when running the container:
      ```bash
      docker run --rm \
        -e YT_CREDENTIALS="path_to_youtube_credentials.json" \
        -e TIKTOK_COOKIES="your_tiktok_cookies" \
        -e IG_USER="your_instagram_username" \
        -e IG_PASS="your_instagram_password" \
        lolllama
      ```
    For more details on securely managing credentials, refer to [Docker Secrets](https://docs.docker.com/engine/swarm/secrets/) or your preferred credential management tool.
3.	Build the Docker image:
    docker build -t lolllama .

4.	(Optional) Run with docker‑compose:
    docker-compose up --build

## YouTube Credentials

You need a YouTube OAuth2 credentials JSON file to upload videos.  
Below is an example of the required format (`youtube_credentials_example.json`):

```json
{
  "installed": {
    "client_id": "YOUR_CLIENT_ID.apps.googleusercontent.com",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": [
      "urn:ietf:wg:oauth:2.0:oob",
      "http://localhost"
    ]
  }
}
```

You can generate this file using the helper script:

```bash
python generate_yt_creds.py --client-id YOUR_CLIENT_ID --client-secret YOUR_CLIENT_SECRET --project-id YOUR_PROJECT_ID --output ~/youtube_credentials.json
```

## Usage

Run the container with required arguments. For example:

docker run --rm \
  -e YT_CREDENTIALS="path_to_youtube_credentials.json" \
  -e TIKTOK_COOKIES="your_tiktok_cookies" \
  -e IG_USER="your_instagram_username" \
  -e IG_PASS="your_instagram_password" \
  lolllama \
  --video-url "https://www.youtube.com/watch?v=EXAMPLE" \
  --title "Warzone LOL Highlights"

Command‑Line Arguments

| Argument          | Description                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------|
| `--video-url`     | (Required) YouTube video URL to process.                                                    |
| `--title`         | (Optional) Base title for the generated video.                                              |
| `--yt-creds`      | Path to YouTube credentials (or set via environment variable `YT_CREDENTIALS`).             |
| `--tiktok-cookies`| TikTok cookies string (or set via environment variable `TIKTOK_COOKIES`).                   |
| `--ig-user`       | Instagram username (or use environment variable `IG_USER`).                                 |
| `--ig-pass`       | Instagram password (or use environment variable `IG_PASS`).                                 |

Modules Overview
	•	downloader: Downloads videos using yt‑dl‑p.
	•	analyzer: (Stub) Determines highlight segments from the video.
	•	dynamic_meme: Dynamically generates memes using Stable Diffusion.
	•	meme_overlay: Overlays the dynamically generated memes on the video.
Disclaimer

This is a prototype. AI analysis and uploading functions are stubbed for you to extend with your preferred models and APIs. Contributions and improvements are welcome!

This project is licensed under the [MIT License](LICENSE). By contributing, you agree that your contributions will be licensed under the same terms. Please ensure compliance with the license and avoid using the project for any unlawful purposes.

Disclaimer

This is a prototype. AI analysis and uploading functions are stubbed for you to extend with your preferred models and APIs. Contributions and improvements are welcome!