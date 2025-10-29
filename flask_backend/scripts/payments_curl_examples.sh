#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:8000}"
PID="${2:-1}"

echo "Payments list:"
curl -s "${BASE}/api/payments" | jq . || curl -s "${BASE}/api/payments"
echo

echo "Receipt for payment_id=${PID}:"
curl -s "${BASE}/api/payments/${PID}" | jq . || curl -s "${BASE}/api/payments/${PID}"
echo
