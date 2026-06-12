import { apiFetch } from "@/lib/api/client";
import type { HealthResponse, ReadinessResponse } from "@/types/api";

export async function fetchHealth(): Promise<HealthResponse | null> {
  try {
    return await apiFetch<HealthResponse>("/api/v1/health", { revalidate: 10 });
  } catch {
    return null;
  }
}

export async function fetchReadiness(): Promise<ReadinessResponse | null> {
  try {
    return await apiFetch<ReadinessResponse>("/api/v1/health/ready", {
      revalidate: 10,
    });
  } catch {
    return null;
  }
}
