#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:8000}"

echo "Users:"
curl -s "${BASE}/api/users" | jq . || curl -s "${BASE}/api/users"
echo

echo "Courses:"
curl -s "${BASE}/api/courses" | jq . || curl -s "${BASE}/api/courses"
echo

echo "Lessons:"
curl -s "${BASE}/api/lessons" | jq . || curl -s "${BASE}/api/lessons"
echo

echo "Enrollments:"
curl -s "${BASE}/api/enrollments" | jq . || curl -s "${BASE}/api/enrollments"
echo

echo "Payments:"
curl -s "${BASE}/api/payments" | jq . || curl -s "${BASE}/api/payments"
echo

echo "Recommendations Cache:"
curl -s "${BASE}/api/recommendations/cache" | jq . || curl -s "${BASE}/api/recommendations/cache"
echo
