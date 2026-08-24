export interface Env { KOTTONS_ENV: string; CONTENT_API_VERSION: string; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const headers = { "content-type": "application/json", "cache-control": "no-store" };

    if (url.pathname === "/health") {
      return Response.json({ ok: true, service: "kottons-code-engine", env: env.KOTTONS_ENV, apiVersion: env.CONTENT_API_VERSION }, { headers });
    }

    if (url.pathname === "/api/content") {
      return Response.json({ version: env.CONTENT_API_VERSION, lanes: ["watch", "play", "read", "collect"], status: "ready-for-content-bindings" }, { headers });
    }

    return Response.json({ error: "Not found" }, { status: 404, headers });
  }
};
