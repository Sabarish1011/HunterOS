"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { getPublicApiUrl } from "@/lib/env";
import type { OpportunityCreate } from "@/types/opportunity";

export function CreateOpportunityForm() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setLoading(true);

    const form = new FormData(e.currentTarget);
    const data: OpportunityCreate = {
      title: form.get("title") as string,
      source: form.get("source") as string,
      asking_price: Number(form.get("asking_price")),
      estimated_value: Number(form.get("estimated_value")),
      opportunity_score: Number(form.get("opportunity_score")),
      status: "new",
    };

    try {
      const res = await fetch(`${getPublicApiUrl()}/api/v1/opportunities`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (!res.ok) {
        const body = await res.json().catch(() => null);
        throw new Error(body?.detail ?? `Request failed (${res.status})`);
      }

      e.currentTarget.reset();
      router.refresh();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to create opportunity");
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-2">
          <Label htmlFor="title">Title</Label>
          <Input id="title" name="title" required placeholder="Vintage Rolex Submariner" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="source">Source</Label>
          <Input id="source" name="source" required placeholder="eBay" />
        </div>
        <div className="space-y-2">
          <Label htmlFor="asking_price">Asking Price</Label>
          <Input
            id="asking_price"
            name="asking_price"
            type="number"
            step="0.01"
            min="0"
            required
            placeholder="4500"
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="estimated_value">Estimated Value</Label>
          <Input
            id="estimated_value"
            name="estimated_value"
            type="number"
            step="0.01"
            min="0"
            required
            placeholder="6200"
          />
        </div>
        <div className="space-y-2">
          <Label htmlFor="opportunity_score">Opportunity Score</Label>
          <Input
            id="opportunity_score"
            name="opportunity_score"
            type="number"
            step="0.01"
            min="0"
            max="100"
            required
            placeholder="78.5"
          />
        </div>
      </div>

      {error && <p className="text-sm text-destructive">{error}</p>}

      <Button type="submit" disabled={loading}>
        {loading ? "Creating..." : "Add Opportunity"}
      </Button>
    </form>
  );
}
