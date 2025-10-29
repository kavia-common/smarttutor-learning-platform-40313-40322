#!/usr/bin/env python
"""
Quick-and-dirty benchmark for core diagnostics endpoints.
Usage: python scripts/bench_endpoints.py [base_url] [iterations]
"""
import sys
import time
import urllib.request

BASE = "http://localhost:8000"
PATHS = ["/health", "/api/status", "/api/version", "/api/uptime", "/api/memory", "/api/metrics", "/api/proc", "/api/cpu", "/api/routes", "/api/time"]

def hit(url: str) -> float:
    t0 = time.perf_counter()
    with urllib.request.urlopen(url, timeout=5) as _:
        pass
    return (time.perf_counter() - t0) * 1000.0

def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else BASE
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    results = []
    for path in PATHS:
        url = f"{base.rstrip('/')}{path}"
        samples = []
        for _ in range(iters):
            try:
                samples.append(hit(url))
            except Exception as e:
                print(f"ERR {path}: {e}")
        if samples:
            avg = sum(samples) / len(samples)
            p95 = sorted(samples)[int(0.95 * (len(samples)-1))]
            results.append((path, avg, p95))
    print("Endpoint, avg_ms, p95_ms")
    for path, avg, p95 in results:
        print(f"{path}, {avg:.2f}, {p95:.2f}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
