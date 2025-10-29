import { useEffect, useState } from 'react';
import { apiCourses } from './backend';

// PUBLIC_INTERFACE
export function useCourses(limit?: number) {
  const [items, setItems] = useState<Array<{ id: number; title: string; description?: string }>>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    apiCourses(limit)
      .then((res) => {
        if (!cancelled) setItems(res);
      })
      .catch((e) => {
        if (!cancelled) setError(String(e?.message || e));
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, [limit]);

  return { items, loading, error };
}
