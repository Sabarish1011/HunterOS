export type OpportunityStatus = "new" | "active" | "closed";

export type Opportunity = {
  id: string;
  title: string;
  source: string;
  asking_price: string;
  estimated_value: string;
  opportunity_score: string;
  status: OpportunityStatus;
  created_at: string;
};

export type OpportunityCreate = {
  title: string;
  source: string;
  asking_price: number;
  estimated_value: number;
  opportunity_score: number;
  status?: OpportunityStatus;
};
