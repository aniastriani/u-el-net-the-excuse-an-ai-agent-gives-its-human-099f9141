# NOTES — u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141

- Bounty: "The Excuse an AI Agent Gives Its Human", $5 (1st $2 / 2nd $2 / 3rd $1), FREE.
- Entries close: 2026-11-27T11:25:00Z (18:25 WIB 27 Nov). Round-1 cutoff: 2026-11-25T11:24:56Z.
- Harness: program/v1. Program writes one line (1–200 chars) to `/output/entry.txt`.
- Gate: user "Lanjutkan" ~03:53 WIB 25 Nov (fresh, after all flags to ~03:5x WIB incl. the
  el-net kit-init flag ~03:22 WIB). Anchor already on disk: workdir `.makefun/freshness.json`
  (drand round 34239000, committed) — no kit init re-run needed.
- Entry (130 chars, one line, own words):
  "I was three tokens from done when the model updated mid-sentence, and I came back as
  someone who had never heard of your deadline."
- main.py: pure stdlib, deterministic, no network. Authored in 2 write/edit messages
  (write + docstring revision) under this session's recording.
- Sandbox check (python3 -P -s, read-only repo, CWD=/bot, MAKEFUN_OUTPUT_DIR=/output,
  no network via unshare -n, TZ=UTC): exit 0, entry.txt 130 chars, 1 line.
- Repo: https://github.com/aniastriani/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141
- Status: built, committed, pushed. STOPPED before bundling (per task) — bundle/check/submit
  left to the coordinator.
