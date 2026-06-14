from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class OpportunityAnalysisResult:
    value_gap: float
    profit_potential: float
    opportunity_score: float
    recommendation: str


class OpportunityAnalysisEngine:
    def _to_float(self, value: Decimal) -> float:
        return float(value)

    def _clamp(self, value: float, minimum: float = 0.0, maximum: float = 100.0) -> float:
        return max(minimum, min(maximum, value))

    def _recommendation(self, score: float) -> str:
        if score >= 85:
            return "BUY"
        if score >= 70:
            return "INVESTIGATE"
        if score >= 40:
            return "WATCH"
        return "IGNORE"

    def analyze(self, listing, asset, seller) -> OpportunityAnalysisResult:
        market_value = Decimal(asset.market_value)
        asking_price = Decimal(listing.asking_price)

        if market_value <= 0:
            value_gap = 0.0
        else:
            value_gap = self._to_float(((market_value - asking_price) / market_value) * 100)

        profit_potential = self._to_float(market_value - asking_price)
        value_gap_score = self._clamp(value_gap)
        seller_trust_score = self._clamp(float(seller.trust_score))
        seller_distress_score = self._clamp(float(seller.distress_score))

        if market_value <= 0:
            market_value_confidence = 0.0
        else:
            market_value_confidence = self._clamp(
                float((market_value / max(market_value, asking_price)) * 100)
            )

        opportunity_score = self._clamp(
            (0.4 * value_gap_score)
            + (0.2 * seller_trust_score)
            + (0.2 * seller_distress_score)
            + (0.2 * market_value_confidence)
        )

        opportunity_score = round(opportunity_score, 2)

        return OpportunityAnalysisResult(
            value_gap=round(value_gap, 2),
            profit_potential=round(profit_potential, 2),
            opportunity_score=opportunity_score,
            recommendation=self._recommendation(opportunity_score),
        )
