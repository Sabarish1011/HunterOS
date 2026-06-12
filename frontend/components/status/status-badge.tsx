import { Badge } from "@/components/ui/badge";

type StatusBadgeProps = {
  status: string;
};

function statusVariant(
  status: string,
): "success" | "error" | "unknown" | "default" {
  if (status === "ok") return "success";
  if (status === "error" || status === "degraded") return "error";
  if (status === "unknown") return "unknown";
  return "default";
}

export function StatusBadge({ status }: StatusBadgeProps) {
  return (
    <Badge variant={statusVariant(status)} className="uppercase">
      {status}
    </Badge>
  );
}
