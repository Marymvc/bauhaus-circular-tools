### Quick orientation for AI contributors

This repository implements a small Python library, `bauhaus_circular`, for circular-design analysis in architecture.
Give priority to the following facts when you modify or add code.

1. Project layout and entry points
   - Source uses the `src/` layout. Main package: `src/bauhaus_circular/`.
   - Public API entrypoint: `from bauhaus_circular import quick_analysis` (see `src/bauhaus_circular/__init__.py`).
   - Important modules:
     - `material_analyzer.py` — in-memory material DB and circularity logic.
     - `carbon_calculator.py` — carbon footprint calculations (expects a MaterialAnalyzer instance).
     - `design_optimizer.py` — orchestrates analyses and returns the full report dict.
     - `climate_analyzer.py` — optional Ladybug integration; falls back to simplified estimates when Ladybug is missing.

2. How to run and test (developer workflows)
   - Install in editable/dev mode: `pip install -e ".[dev]"` (pyproject.toml defines dev extras).
   - Unit & integration tests: `pytest tests/` (pyproject.toml sets `pythonpath = ["src"]` for pytest).
   - Examples are in `examples/` (e.g., `examples/basic_usage.py`) and show typical `quick_analysis(...)` calls.
   - Formatting & static checks: `black src/`, `flake8`, and `mypy` are configured in `pyproject.toml`.

3. Patterns and conventions you must follow
   - Data-first API: functions return plain dicts (no custom models). Common top-level keys returned by `DesignOptimizer.optimize_design` include: `current_design`, `material_analysis`, `carbon_analysis`, `climate_analysis`, `cost_analysis`, `recommendations`, `optimized_alternative`, `summary`.
   - Small, explicit modules: responsibilities are separated (analyzer, calculator, optimizer). Pass analyzer/calculator instances explicitly (avoid global state).
   - Material database is an in-memory dict in `MaterialAnalyzer.circular_materials`. Use that structure when adding materials (fields: `category`, `carbon_kg_co2_m3`, `reuse_potential`, `recyclability`, `lifespan_years`, `cost_usd_m3`, `local_availability`, `bauhaus_compliant`, `natural_finish`, `description`).
   - Optional integrations: `climate_analyzer` will try to import `ladybug`. Avoid hard dependency on Ladybug; detect availability via `LADYBUG_AVAILABLE` and fall back to simplified estimates.

4. Known inconsistencies to watch for (important for agents)
   - Tests currently reference keys that don't exactly match implementation. Examples discovered:
     - `carbon_calculator.calculate_carbon_footprint` returns `total_carbon_kg_co2` but tests expect `total_carbon`.
     - Some tests expect `carbon_reduction_kg_co2` in `optimized_alternative['improvements']` whereas code provides `carbon_reduction_percent` or `carbon_reduction` under different names.
   - When changing keys or shapes, update both the implementation and tests. Prefer normalizing on the names used in source code unless you explicitly update test expectations.

5. External/environment notes
   - Optional runtime integrations:
     - Rhino/Grasshopper: examples show adding Python site-packages to `sys.path` for Grasshopper scripts.
     - Ladybug Tools: only required for detailed climate analysis; included in `pyproject.toml` dependencies as `ladybug-core`/`ladybug-geometry`.
   - Python versions: the project targets Python >=3.8 (see `pyproject.toml`).

6. Helpful examples (from the repo)
   - Quick analysis: `from bauhaus_circular import quick_analysis`
     - Input: `materials: List[str]`, `quantities: List[float]`, `climate: str`
     - Output: dict; inspect `result['current_design']` and `result['recommendations']` (see `examples/basic_usage.py`).

7. When you add features
   - Keep functions pure where possible: analyzers should not access I/O or global state.
   - Add unit tests under `tests/` that exercise the public API (`quick_analysis`) and internal helpers.
   - If you change return shapes, update `examples/` and `tests/` to reflect the canonical API.

If anything here is unclear or you want this file expanded with more examples (e.g., expected dict schemas, unit test templates, or mapping of test failures → fixes), tell me which sections to expand and I'll iterate. 
