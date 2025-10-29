#!/usr/bin/env python
"""
Serve the backend docs folder (including openapi.html and openapi.json) via a simple HTTP server.
Usage: python scripts/serve_docs.py [port]
"""
import http.server
import socketserver
import sys
from pathlib import Path

def main() -> int:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    docs_dir = Path("docs").resolve()
    if not docs_dir.exists():
        print("docs/ not found. Run: python scripts/generate_openapi_site.py")
        return 2
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving docs from {docs_dir} at http://localhost:{port}")
        try:
            # Change working directory to docs before serving
            import os
            os.chdir(docs_dir)
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
