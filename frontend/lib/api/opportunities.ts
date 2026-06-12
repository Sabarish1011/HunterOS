import { apiFetch } from "@/lib/api/client";
import type { Opportunity, OpportunityCreate } from "@/types/opportunity";

export async function fetchOpportunities(): Promise<Opportunity[]> {
  return apiFetch<Opportunity[]>("/api/v1/opportunities", { revalidate: 0 });
}

export async function createOpportunity(
  data: OpportunityCreate,
): Promise<Opportunity> {
  return apiFetch<Opportunity>("/api/v1/opportunities", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
}
