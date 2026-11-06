"""Shipping rate calculations."""

_SURCHARGES = {"standard": 0.0, "express": 7.0}


def shipping_quote(weight_kg: float, zone: str, service: str = "standard") -> float:
    """Quote shipping in dollars.

    Args:
        weight_kg: Parcel weight; must be positive.
        zone: Delivery zone — ``"local"`` or ``"regional"``.
        service: ``"standard"`` (default) or ``"express"`` ($7 surcharge).

    Returns:
        Total quote in USD, rounded to cents.

    Raises:
        ValueError: If weight is non-positive, zone is unknown, or service is unknown.
    """
    if weight_kg <= 0:
        raise ValueError("weight must be positive")
    if zone not in {"local", "regional"}:
        raise ValueError("unknown zone")
    if service not in _SURCHARGES:
        raise ValueError(f"unknown service: {service!r}")
    base = 5.0 if zone == "local" else 8.0
    return round(base + 1.5 * weight_kg + _SURCHARGES[service], 2)
