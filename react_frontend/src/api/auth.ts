import { getToken } from './authStore';

// PUBLIC_INTERFACE
export function authHeaders(extra?: HeadersInit): HeadersInit {
  const token = getToken();
  const base: Record<string, string> = { 'Content-Type': 'application/json' };
  if (token) base['Authorization'] = `Bearer ${token}`;
  return { ...(extra as any), ...base };
}
