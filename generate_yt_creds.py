import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser(description="Generate YouTube OAuth2 credentials JSON file.")
    parser.add_argument("--client-id", required=True, help="Google API client_id")
    parser.add_argument("--client-secret", required=True, help="Google API client_secret")
    parser.add_argument("--project-id", required=True, help="Google Cloud project_id")
    parser.add_argument("--output", default=os.path.expanduser("~/youtube_credentials.json"), help="Output JSON file path")
    args = parser.parse_args()

    creds = {
        "installed": {
            "client_id": args.client_id,
            "project_id": args.project_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": args.client_secret,
            "redirect_uris": [
                "urn:ietf:wg:oauth:2.0:oob",
                "http://localhost"
            ]
        }
    }

    with open(args.output, "w") as f:
        json.dump(creds, f, indent=2)
    print(f"Credentials JSON written to {args.output}")

if __name__ == "__main__":
    main()
