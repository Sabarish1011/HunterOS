export type HealthResponse = {
  status: string;
  service: string;
  environment: string;
};

export type ReadinessResponse = {
  status: string;
  checks: Record<string, string>;
};
