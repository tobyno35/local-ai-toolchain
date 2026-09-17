#!/usr/bin/env python3
import sys, os, json, argparse, urllib.request, urllib.error
from pathlib import Path
WEAVE_DIR = Path.home() / ".weave"
PATTERNS_DIR = Path(__file__).resolve().parent / "patterns"
OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
DEFAULT_MODEL = os.environ.get("WEAVE_MODEL", "qwen2.5-coder:7b")
def call_ollama(sp, ui, model):
    pay = json.dumps({"model":model,"messages":[{"role":"system","content":sp},{"role":"user","content":ui}],"stream":True}).encode()
    req = urllib.request.Request(OLLAMA_URL+"/api/chat",data=pay,headers={"Content-Type":"application/json"},method="POST")
    try:
        with urllib.request.urlopen(req) as r:
            for l in r:
                l=l.decode().strip()
                if not l: continue
                try:
                    c=json.loads(l); print(c.get("message",{}).get("content",""),end="",flush=True)
                    if c.get("done"): print()
                except: continue
    except urllib.error.URLError as e: print("[weave] Ollama unreachable",file=sys.stderr); sys.exit(1)
def safe_pattern_path(name):
    root = PATTERNS_DIR.resolve()
    path = (root / (name + ".md")).resolve()

    if not path.is_relative_to(root):
        print("[weave] Permission Denied: Invalid pattern path", file=sys.stderr)
        sys.exit(1)

    return path


def load_pattern(name):
    p = safe_pattern_path(name)
    if not p.exists():
        print("[weave] Not found: " + name, file=sys.stderr)
        sys.exit(1)
    return p.read_text().strip()
def list_patterns():
    ps=sorted(PATTERNS_DIR.glob("*.md"))
    print("  Weave Patterns ("+str(len(ps))+" total)")
    for p in ps:
        lines=p.read_text().splitlines()
        desc=next((l.lstrip("# ").strip() for l in lines[1:] if l.strip()),"")
        print("  "+p.stem.ljust(30)+desc[:50])
def create_pattern(name):
    p = safe_pattern_path(name)
    p.write_text("# " + name + " ")
    print("Created: " + str(p))
def main():
    ap=argparse.ArgumentParser(prog="weave")
    ap.add_argument("-p","--pattern"); ap.add_argument("-m","--model",default=DEFAULT_MODEL)
    ap.add_argument("-t","--text"); ap.add_argument("--list",action="store_true"); ap.add_argument("--new",metavar="NAME")
    args=ap.parse_args()
    PATTERNS_DIR.mkdir(parents=True,exist_ok=True)
    if args.list: list_patterns(); return
    if args.new: create_pattern(args.new); return
    if not args.pattern: ap.print_help(); sys.exit(1)
    ui=args.text if args.text else sys.stdin.read().strip()
    if not ui: print("[weave] No input",file=sys.stderr); sys.exit(1)
    print("-- weave "+args.pattern+" --")
    call_ollama(load_pattern(args.pattern),ui,args.model)
if __name__=="__main__": main()
