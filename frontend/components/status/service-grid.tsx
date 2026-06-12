import { StatusBadge } from "@/components/status/status-badge";

type ServiceGridProps = {
  items: Record<string, string>;
};

export function ServiceGrid({ items }: ServiceGridProps) {
  return (
    <div className="divide-y">
      {Object.entries(items).map(([name, status]) => (
        <div
          key={name}
          className="flex items-center justify-between py-3 first:pt-0 last:pb-0"
        >
          <span className="capitalize text-sm">{name}</span>
          <StatusBadge status={status} />
        </div>
      ))}
    </div>
  );
}
