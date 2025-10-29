#!/usr/bin/env bash
set -euo pipefail
BASE="${1:-http://localhost:8000}"

echo "Sessions (all):"
curl -s "${BASE}/api/whiteboard/sessions" | jq . || curl -s "${BASE}/api/whiteboard/sessions"

if [[ $# -ge 2 ]]; then
  COURSE_ID="$2"
  echo
  echo "Sessions for course_id=${COURSE_ID}:"
  curl -s "${BASE}/api/whiteboard/sessions?course_id=${COURSE_ID}" | jq . || curl -s "${BASE}/api/whiteboard/sessions?course_id=${COURSE_ID}"
fi

if [[ $# -ge 3 ]]; then
  SESSION_ID="$3"
  echo
  echo "Events for session_id=${SESSION_ID}:"
  curl -s "${BASE}/api/whiteboard/sessions/${SESSION_ID}/events" | jq . || curl -s "${BASE}/api/whiteboard/sessions/${SESSION_ID}/events"
fi
