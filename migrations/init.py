import os
import re


def verify(ctx):
    issues = []
    base = os.path.join(ctx.root, "wiki", "lark")
    profiles = [d for d in os.listdir(base) if os.path.isfile(os.path.join(base, d, "profile.md"))] if os.path.isdir(base) else []
    if not profiles:
        issues.append(("error", "no lark profile initialized — create wiki/lark/<profile>/profile.md (lark block mapping)"))
    else:
        p = os.path.join(base, sorted(profiles)[0], "profile.md")
        text = open(p, encoding="utf-8").read()
        if not re.search(r"^type:\s*lark\s*$", text, re.M):
            issues.append(("error", f"{p}: missing `type: lark`"))
        if "app_id" not in text:
            issues.append(("error", f"{p}: missing the lark block mapping (app_id ...)"))
    if not os.path.isdir(os.path.expanduser("~/.lark-cli")):
        issues.append(("warning", "lark-cli not logged in yet — guide the user at first pull"))
    return issues
