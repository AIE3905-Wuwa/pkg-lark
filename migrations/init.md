---
verb: init
verify: init.py
---
First-run setup for the lark domain:

1. **Connector** — lark-cli lives outside this package (external): install and configure per its own repository, then `lark-cli auth login --profile <name>` (web login; tokens stay local, ~/.lark-cli).
2. **Identity page** — wiki/lark/<profile>/profile.md per the lark constitution: one-sentence identity + lark block mapping (profile / app_id / kind) + trust fields. One directory per enterprise; the profile name is always carried.
3. Pointer pages arrive via lark-map on demand (lazy — do not pre-create).
