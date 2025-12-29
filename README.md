# PRISMA-Py: A Python Package for PRISMA 2020 Flow Charts

This packages creates PRISMA 2020--style flow diagrams using matplotlib.
You provide counts for each step of your screening process, and it generates a two-column diagram with arrows and phase labels.

It supports:

- **New reviews** (standard PRISMA 2020)
- **Updated reviews** (previous + new studies)
- **Optional extensions**:
  - Other search methods (additional lane)
  - Automation-based exclusions
  - Detailed exclusion-reason breakdowns

You can either:
- pass structured counts programmatically, or
- **derive counts automatically from a CoLRev `records.bib` file**.

The design goal is a **small, transparent interface** with sensible defaults and layout that adapts to your data.

<!--
## Features

- PRISMA 2020–compliant layout
- Dynamic box height (based on text length)
- Dynamic column width (based on longest line)
- Automatic alignment across lanes
- Optional updated-review layout
- Optional CLI for CoLRev workflows
- Output to PNG, SVG, PDF, …
-->

## Installation

The only required dependency is `matplotlib`.

```bash
pip install matplotlib
```

Clone or copy the package (e.g., as `py_prisma/`) into your Python path, or install it in editable mode.

## Public API Overview

```python
from py_prisma import (
    PrismaStatus,
    load_status_from_records,
    plot_prisma2020,
)
```

## Quick Start (New Review)

```python
from py_prisma import plot_prisma2020

plot_prisma2020(
    db_registers={
        "identification": {"databases": 120, "registers": 10},
        "removed_before_screening": {"duplicates": 30, "automation": 5},
        "records": {"screened": 95, "excluded": 55},
        "reports": {
            "sought": 40,
            "not_retrieved": 4,
            "assessed": 36,
            "excluded_reasons": {
                "Wrong population": 12,
                "Wrong outcome": 8,
            },
        },
    },
    included={"studies": 10, "reports": 12},
    filename="prisma.png",
)
```

## Working with CoLRev Records

```python
from py_prisma import load_status_from_records, plot_prisma2020

params = load_status_from_records("data/records.bib")

plot_prisma2020(
    **params.__dict__,
    filename="prisma_from_records.png",
)
```

## Command-Line Interface

```bash
prisma-from-records data/records.bib prisma.png
```

## License

Free to use, modify, and integrate into academic or applied workflows.
