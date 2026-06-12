import { getApiUrl } from "@/lib/env";

export class ApiError extends Error {
  constructor(
    message: string,
    public status: number,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export async function apiFetch<T>(
  path: string,
  options?: RequestInit & { revalidate?: number },
): Promise<T> {
  const { revalidate, ...fetchOptions } = options ?? {};
  const url = `${getApiUrl()}${path}`;

  const res = await fetch(url, {
    ...fetchOptions,
    ...(revalidate !== undefined ? { next: { revalidate } } : {}),
  });

  if (!res.ok) {
    throw new ApiError(`Request failed: ${res.status}`, res.status);
  }

  return res.json() as Promise<T>;
}
