import Link from "next/link";

import { ServiceGrid } from "@/components/status/service-grid";
import { StatusBadge } from "@/components/status/status-badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { fetchHealth, fetchReadiness } from "@/lib/api/health";
import { getPublicApiUrl } from "@/lib/env";

export default async function HomePage() {
  const [health, readiness] = await Promise.all([
    fetchHealth(),
    fetchReadiness(),
  ]);

  const publicApiUrl = getPublicApiUrl();

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-8">
      <div className="w-full max-w-lg space-y-6">
        <div className="space-y-2 text-center">
          <h1 className="text-4xl font-bold tracking-tight">HunterOS</h1>
          <p className="text-muted-foreground">
            Price arbitrage monitoring platform
          </p>
        </div>

        <Card>
          <CardHeader>
            <CardTitle className="text-sm font-medium uppercase tracking-wider text-muted-foreground">
              API Status
            </CardTitle>
            <CardDescription>Backend service health</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="divide-y">
              <div className="flex items-center justify-between py-3">
                <span className="text-sm">Backend</span>
                <StatusBadge status={health?.status ?? "unknown"} />
              </div>
              {health && (
                <>
                  <div className="flex items-center justify-between py-3">
                    <span className="text-sm">Service</span>
                    <span className="text-sm text-muted-foreground">
                      {health.service}
                    </span>
                  </div>
                  <div className="flex items-center justify-between py-3">
                    <span className="text-sm">Environment</span>
                    <span className="text-sm text-muted-foreground">
                      {health.environment}
                    </span>
                  </div>
                </>
              )}
            </div>
          </CardContent>
        </Card>

        {readiness && (
          <Card>
            <CardHeader>
              <CardTitle className="text-sm font-medium uppercase tracking-wider text-muted-foreground">
                Infrastructure
              </CardTitle>
              <CardDescription>Data service connectivity</CardDescription>
            </CardHeader>
            <CardContent>
              <ServiceGrid items={readiness.checks} />
            </CardContent>
          </Card>
        )}

        <div className="space-y-2 text-center text-sm text-muted-foreground">
          <p>
            <Link href="/opportunities" className="text-primary hover:underline">
              View Opportunities &rarr;
            </Link>
          </p>
          <p>
            API docs at{" "}
            <a
              href={`${publicApiUrl}/docs`}
              target="_blank"
              rel="noopener noreferrer"
              className="text-primary hover:underline"
            >
              {publicApiUrl}/docs
            </a>
          </p>
        </div>
      </div>
    </main>
  );
}
