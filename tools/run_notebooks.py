"""
Run the tutorial notebooks and report pass / fail and the run time of each.

Each notebook is executed in its own folder (so relative paths such as
``../data`` work) with a fresh ``python3`` kernel. Code cells tagged
``skip-execution`` (logins, downloads and anything else that needs a user
account or network access) are not run; their stored outputs are kept.

Usage::

    python tools/run_notebooks.py                      # every notebook
    python tools/run_notebooks.py 04_image_classification
    python tools/run_notebooks.py 05_regression/02_feature_selection.ipynb --save

``--save`` writes the executed notebook (with its new outputs) back to its
file; without it the notebooks are only checked.
"""

import argparse
import glob
import os
import sys
import time
from typing import List, Tuple

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_TAG = "skip-execution"


def find_notebooks(targets: List[str]) -> List[str]:
    """Notebook paths for the given folders / files (Default = all sections)."""
    if not targets:
        targets = sorted(d for d in os.listdir(ROOT)
                         if d[:2].isdigit() and os.path.isdir(os.path.join(ROOT, d)))
    paths: List[str] = []
    for target in targets:
        full = target if os.path.isabs(target) else os.path.join(ROOT, target)
        if os.path.isdir(full):
            paths.extend(sorted(glob.glob(os.path.join(full, "*.ipynb"))))
        elif full.endswith(".ipynb") and os.path.exists(full):
            paths.append(full)
        else:
            raise SystemExit(f"Not a notebook or folder: {target}")
    return paths


def run_notebook(path: str, timeout: int, save: bool) -> Tuple[bool, float, str]:
    """Execute one notebook; return ``(passed, seconds, message)``."""
    nb = nbformat.read(path, as_version=4)
    skipped = []
    for idx, cell in enumerate(nb.cells):
        if cell.cell_type == "code" and SKIP_TAG in cell.get("metadata", {}).get("tags", []):
            skipped.append(idx)
    # Run a copy without the skipped cells, then put their stored outputs back.
    run_nb = nbformat.from_dict(nb)
    run_nb.cells = [c for i, c in enumerate(nb.cells) if i not in skipped]
    client = NotebookClient(
        run_nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": os.path.dirname(path)}},
    )
    start = time.perf_counter()
    try:
        client.execute()
        passed, msg = True, f"{len(skipped)} cell(s) skipped" if skipped else ""
    except CellExecutionError as err:
        passed = False
        lines = [ln for ln in str(err).splitlines() if ln.strip()]
        msg = " | ".join(lines[-3:])[:400]
    except Exception as err:  # pylint: disable=broad-except
        passed, msg = False, f"{type(err).__name__}: {err}"[:400]
    secs = time.perf_counter() - start
    if save and passed:
        run_iter = iter(run_nb.cells)
        nb.cells = [nb.cells[i] if i in skipped else next(run_iter)
                    for i in range(len(nb.cells))]
        nbformat.write(nb, path)
    return passed, secs, msg


def main() -> int:
    """Command line interface."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("targets", nargs="*", help="Section folders or notebooks")
    parser.add_argument("--save", action="store_true",
                        help="Write the executed notebooks back with their outputs")
    parser.add_argument("--timeout", type=int, default=1800,
                        help="Per-cell timeout in seconds (Default = 1800)")
    args = parser.parse_args()
    results = []
    for path in find_notebooks(args.targets):
        rel = os.path.relpath(path, ROOT)
        print(f"running {rel} ...", flush=True)
        passed, secs, msg = run_notebook(path, args.timeout, args.save)
        results.append((rel, passed, secs, msg))
        print(f"  {'PASS' if passed else 'FAIL'} {secs:7.1f} s {msg}", flush=True)
    print("\n| Notebook | Result | Time (s) | Notes |\n| --- | --- | --- | --- |")
    for rel, passed, secs, msg in results:
        print(f"| {rel} | {'pass' if passed else 'FAIL'} | {secs:.0f} | {msg} |")
    return 0 if all(r[1] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
