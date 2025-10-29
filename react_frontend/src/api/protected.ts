import { authHeaders } from './auth';

// PUBLIC_INTERFACE
export async function getMyProfile(apiBase: string) {
  const url = `${apiBase}/profile/`;
  const res = await fetch(url, { method: 'GET', headers: authHeaders() });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`GET ${url} failed: ${res.status} ${text}`);
  }
  return res.json() as Promise<{ id: number; email: string; name: string; role: string }>;
}
