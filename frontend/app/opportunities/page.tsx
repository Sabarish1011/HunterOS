import Link from "next/link";

import { CreateOpportunityForm } from "@/components/opportunities/create-form";
import { Badge } from "@/components/ui/badge";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { fetchOpportunities } from "@/lib/api/opportunities";
import type { Opportunity, OpportunityStatus } from "@/types/opportunity";

function statusVariant(
  status: OpportunityStatus,
): "default" | "success" | "secondary" | "unknown" {
  if (status === "active") return "success";
  if (status === "closed") return "secondary";
  return "default";
}

function formatCurrency(value: string) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
  }).format(Number(value));
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("en-US", {
    dateStyle: "medium",
    timeStyle: "short",
  }).format(new Date(value));
}

export default async function OpportunitiesPage() {
  let opportunities: Opportunity[] = [];
  let fetchError: string | null = null;

  try {
    opportunities = await fetchOpportunities();
  } catch {
    fetchError = "Unable to load opportunities. Is the backend running?";
  }

  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-5xl space-y-8">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold tracking-tight">Opportunities</h1>
            <p className="text-muted-foreground">
              Track price arbitrage opportunities
            </p>
          </div>
          <Link
            href="/"
            className="text-sm text-muted-foreground hover:text-primary"
          >
            &larr; Dashboard
          </Link>
        </div>

        <Card>
          <CardHeader>
            <CardTitle>Add Opportunity</CardTitle>
            <CardDescription>
              Create a new opportunity to track
            </CardDescription>
          </CardHeader>
          <CardContent>
            <CreateOpportunityForm />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>All Opportunities</CardTitle>
            <CardDescription>
              {opportunities.length} record{opportunities.length !== 1 && "s"}
            </CardDescription>
          </CardHeader>
          <CardContent>
            {fetchError ? (
              <p className="text-sm text-destructive">{fetchError}</p>
            ) : opportunities.length === 0 ? (
              <p className="text-sm text-muted-foreground">
                No opportunities yet. Add one above.
              </p>
            ) : (
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>Title</TableHead>
                    <TableHead>Source</TableHead>
                    <TableHead>Asking</TableHead>
                    <TableHead>Est. Value</TableHead>
                    <TableHead>Score</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead>Created</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {opportunities.map((opp) => (
                    <TableRow key={opp.id}>
                      <TableCell className="font-medium">{opp.title}</TableCell>
                      <TableCell>{opp.source}</TableCell>
                      <TableCell>{formatCurrency(opp.asking_price)}</TableCell>
                      <TableCell>{formatCurrency(opp.estimated_value)}</TableCell>
                      <TableCell>{opp.opportunity_score}</TableCell>
                      <TableCell>
                        <Badge variant={statusVariant(opp.status)} className="uppercase">
                          {opp.status}
                        </Badge>
                      </TableCell>
                      <TableCell className="text-muted-foreground">
                        {formatDate(opp.created_at)}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            )}
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
