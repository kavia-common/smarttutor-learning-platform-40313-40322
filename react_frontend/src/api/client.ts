const API_BASE = (import.meta as any).env?.VITE_API_BASE_URL || (__API_BASE_URL__ as string) || '';

/**
 * PUBLIC_INTERFACE
 * doGet performs a GET request against the backend REST API.
 */
export async function doGet<T = unknown>(path: string, init?: RequestInit): Promise<T> {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, { ...init, method: 'GET', headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) } });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`GET ${url} failed: ${res.status} ${text}`);
  }
  return res.json() as Promise<T>;
}

/**
 * PUBLIC_INTERFACE
 * doPost performs a POST request against the backend REST API.
 */
export async function doPost<T = unknown, B = unknown>(path: string, body?: B, init?: RequestInit): Promise<T> {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, {
    ...init,
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) },
    body: body !== undefined ? JSON.stringify(body) : undefined
  });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`POST ${url} failed: ${res.status} ${text}`);
  }
  return res.json() as Promise<T>;
}
