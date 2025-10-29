type WSConfig = {
  path?: string;
  onOpen?: (ev: Event) => void;
  onMessage?: (ev: MessageEvent) => void;
  onClose?: (ev: CloseEvent) => void;
  onError?: (ev: Event) => void;
};

const WS_BASE = (import.meta as any).env?.VITE_WS_BASE_URL || (__WS_BASE_URL__ as string) || '';

/**
 * PUBLIC_INTERFACE
 * connectWS establishes a WebSocket connection to the backend path.
 */
export function connectWS(cfg: WSConfig) {
  const url = `${WS_BASE}${cfg.path || ''}`;
  const ws = new WebSocket(url);
  if (cfg.onOpen) ws.addEventListener('open', cfg.onOpen);
  if (cfg.onMessage) ws.addEventListener('message', cfg.onMessage);
  if (cfg.onClose) ws.addEventListener('close', cfg.onClose);
  if (cfg.onError) ws.addEventListener('error', cfg.onError);
  return ws;
}
