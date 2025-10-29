const API_BASE = (import.meta as any).env?.VITE_API_BASE_URL || (__API_BASE_URL__ as string) || '';

type LoginResponse = { user: { id: number; email: string; name: string; role: string }; token: string };
type RegisterResponse = LoginResponse;

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const url = `${API_BASE}${path}`;
  const res = await fetch(url, { headers: { 'Content-Type': 'application/json', ...(init?.headers || {}) }, ...init });
  if (!res.ok) {
    const text = await res.text().catch(() => '');
    throw new Error(`${init?.method || 'GET'} ${url} failed: ${res.status} ${text}`);
  }
  return res.json() as Promise<T>;
}

// PUBLIC_INTERFACE
export async function apiHealth() {
  return request<{ status: string }>('/../health');
}

// PUBLIC_INTERFACE
export async function apiStatus() {
  return request<Record<string, number>>('/status');
}

// PUBLIC_INTERFACE
export async function apiCourses(limit?: number, offset?: number) {
  const qs = new URLSearchParams();
  if (limit !== undefined) qs.set('limit', String(limit));
  if (offset !== undefined) qs.set('offset', String(offset));
  const q = qs.toString();
  return request<Array<{ id: number; title: string; description?: string }>>(`/courses/${q ? `?${q}` : ''}`);
}

// PUBLIC_INTERFACE
export async function apiCourseDetail(courseId: number) {
  return request<{ id: number; title: string; description?: string; lessons: Array<{ id: number; title: string; video_url?: string }> }>(
    `/course/${courseId}`
  );
}

// PUBLIC_INTERFACE
export async function apiLessons(courseId?: number) {
  const qs = new URLSearchParams();
  if (courseId !== undefined) qs.set('course_id', String(courseId));
  const q = qs.toString();
  return request<Array<{ id: number; course_id: number; title: string; content?: string; video_url?: string }>>(`/lessons/${q ? `?${q}` : ''}`);
}

// PUBLIC_INTERFACE
export async function apiRegister(name: string, email: string, password: string): Promise<RegisterResponse> {
  return request<RegisterResponse>('/auth/register', { method: 'POST', body: JSON.stringify({ name, email, password }) });
}

// PUBLIC_INTERFACE
export async function apiLogin(email: string, password: string): Promise<LoginResponse> {
  return request<LoginResponse>('/auth/login', { method: 'POST', body: JSON.stringify({ email, password }) });
}

// PUBLIC_INTERFACE
export async function apiProfile(token: string) {
  return request<{ id: number; email: string; name: string; role: string }>('/profile/', {
    headers: { Authorization: `Bearer ${token}` }
  });
}
