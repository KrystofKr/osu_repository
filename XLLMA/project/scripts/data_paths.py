"""Shared data locations and profile schema; resolving a path has no side effects."""
from pathlib import Path

DATA = Path(__file__).resolve().parents[2] / "data"
PROFILE_COLUMNS = ['Identifikace transakce', 'Profil', 'Jmeno', 'Typ profilu', 'Kategorie', 'Synteticka', 'Skupina transakci']
ROUTES = {
    "data_all.csv": "transactions",
    "data_synthetic.csv": "transactions",
    "data_combined.csv": "transactions",
    "original_profiles.csv": "profiles",
    "reference_scenarios.csv": "profiles",
    "synthetic_profiles.csv": "profiles",
    "category_dictionary.csv": "dictionaries",
    "category_mapping.csv": "dictionaries",
    "main_category_dictionary.csv": "dictionaries",
    "original_classification_audit.csv": "diagnostics",
    "merchant_verification.csv": "diagnostics"
}


def data_path(name):
    """Return a known artifact path without creating files or directories."""
    try:
        folder = ROUTES[name]
    except KeyError as exc:
        raise ValueError(f"Unknown data artifact: {name}") from exc
    return DATA / folder / name


def require_synthetic_reference(rows):
    """Reject accidental replacement of the reference by an ordinary bank export."""
    if not rows or any(not row.get('Identifikace transakce', '').startswith('REF-') for row in rows):
        raise ValueError('data_all.csv musí být syntetická reference s identifikátory REF-; skutečný bankovní výpis sem nepatří.')
