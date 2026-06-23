#!/usr/bin/env python3
"""Smoke test for the outreach engine. Run: python3 outreach/smoke_test.py

Dependency-free (stdlib + asserts). Exercises the 'example' client end-to-end
and sanity-checks that the real 'sig-lodges' client still builds.
"""
import sys

import build_merge as bm


def check(label, cond):
    print(f"{'ok  ' if cond else 'FAIL'} {label}")
    if not cond:
        check.failed += 1
check.failed = 0


def test_example():
    cfg = bm.load_config("example")
    rows, warnings = bm.build_rows(cfg)
    by_id = {r["id"]: r for r in rows}

    check("example: 4 rows", len(rows) == 4)
    check("example: no warnings", warnings == [])

    versions = sorted(r["email_version"] for r in rows)
    check("example: versions A/B/C/VERIFY", versions == ["A", "B", "C", "VERIFY"])

    # id 2: past_due, $240, ClassPass, balance >= personal_touch_at(200)
    r2 = by_id[2]
    check("example: past_due -> B", r2["email_version"] == "B")
    check("example: balance_due formatted", r2["balance_due"] == "$240")
    check("example: ClassPass note present", "ClassPass" in r2["channel_note"])
    check("example: personal-touch note appended", "call before emailing" in r2["channel_note"])

    # id 3: credit_due, -$50
    r3 = by_id[3]
    check("example: credit_due -> C", r3["email_version"] == "C")
    check("example: credit formatted", r3["credit"] == "$50")
    check("example: credit row balance_due is $0", r3["balance_due"] == "$0")

    # id 1: active_paid, vip flag, lookup enrichment
    r1 = by_id[1]
    check("example: active_paid -> A", r1["email_version"] == "A")
    check("example: vip flag -> yes", r1["vip"] == "yes")
    check("example: lookup studio_name", r1["studio_name"] == "Downtown Studio")
    check("example: global merged in", r1["sender_name"] == "Alex")

    # summary totals (validate-only, no file write)
    s = bm.run("example", check=True)
    check("example: owed total 240", s["owed"] == 240)
    check("example: credits total 50", s["credits"] == 50)
    check("example: all columns produced", not any("not produced" in w for w in s["warnings"]))


def test_sig_builds():
    s = bm.run("sig-lodges", check=True)
    check("sig-lodges: 29 rows", s["rows"] == 29)
    check("sig-lodges: owed total 37,837", s["owed"] == 37837)
    check("sig-lodges: no config warnings", not any("not produced" in w for w in s["warnings"]))


if __name__ == "__main__":
    test_example()
    test_sig_builds()
    if check.failed:
        print(f"\n{check.failed} check(s) failed")
        sys.exit(1)
    print("\nAll checks passed ✔")
