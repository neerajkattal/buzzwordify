"""buzzwordify — turn what you actually did into insufferable LinkedIn hustle-speak."""

import argparse
import random
import re

__version__ = "0.1.0"

# Multi-word phrases are matched first, before any single-word substitution
# gets a chance to mangle them.
PHRASES = [
    (r"\bfixed a typo\b", "resolved a critical production-blocking issue"),
    (r"\bfixed a bug\b", "shipped a critical hotfix"),
    (r"\bwrote (some )?tests\b", "hardened test coverage across the stack"),
    (r"\bwrote documentation\b", "authored comprehensive technical documentation"),
    (r"\bcleaned up (the |some )?code\b", "refactored legacy technical debt"),
    (r"\brenamed a variable\b", "improved code readability at scale"),
    (r"\bdeleted (some )?unused code\b", "optimized the codebase footprint"),
    (r"\bupdated a dependency\b", "modernized our technology stack"),
    (r"\breviewed a (pr|pull request)\b", "provided strategic technical leadership on a pull request"),
    (r"\battended a meeting\b", "aligned cross-functionally with key stakeholders"),
    (r"\btook a nap\b", "recharged for peak performance"),
    (r"\bdrank (some )?coffee\b", "fueled up for maximum output"),
    (r"\bquit my job\b", "began an exciting new chapter"),
    (r"\btalked to\b", "aligned cross-functionally with"),
    (r"\bworked on\b", "drove"),
    (r"\bwork on\b", "drive"),
]

WORDS = {
    "fixed": "resolved", "fix": "resolve",
    "wrote": "architected", "write": "architect",
    "made": "engineered", "make": "engineer",
    "built": "engineered", "build": "engineer",
    "helped": "spearheaded", "help": "spearhead",
    "used": "leveraged", "use": "leverage",
    "meeting": "sync", "meetings": "syncs",
    "idea": "paradigm shift", "ideas": "paradigm shifts",
    "team": "high-performing pod", "teams": "high-performing pods",
    "improved": "10x'd", "improve": "10x",
    "started": "pioneered", "start": "pioneer",
    "finished": "delivered end-to-end", "finish": "deliver end-to-end",
    "small": "scrappy",
    "typo": "critical production issue", "typos": "critical production issues",
    "bug": "blocker", "bugs": "blockers",
    "website": "platform", "app": "ecosystem", "apps": "ecosystems",
    "code": "infrastructure",
    "project": "initiative", "projects": "initiatives",
    "task": "mission-critical deliverable", "tasks": "mission-critical deliverables",
    "problem": "challenge", "problems": "challenges",
    "changed": "transformed", "change": "transform",
    "added": "shipped", "add": "ship",
    "removed": "deprecated", "remove": "deprecate",
    "updated": "modernized", "update": "modernize",
    "learned": "upskilled in", "learn": "upskill in",
}

TEMPLATES = [
    "\U0001F680 Thrilled to share that I just {text}. Grateful for this incredible journey. {tags}",
    "Humbled to announce: I {text}. This is only the beginning. \U0001F64F {tags}",
    "Big news \U0001F4C8 — I {text}. So proud of what we're building. {tags}",
    "Excited to share that I {text}. Onwards and upwards! \U0001F4AA {tags}",
    "\U0001F525 Just {text}. Manifesting even bigger wins ahead. {tags}",
    "Reflecting on a big milestone: I {text}. Grateful, humbled, and hungry for more. {tags}",
]

HASHTAGS = [
    "#hustle", "#grindset", "#innovation", "#thoughtleadership", "#synergy",
    "#disruptive", "#buildinpublic", "#leadership", "#growthmindset", "#winning",
]


# Every template already puts "I" (or an equivalent) in front of {text}, so
# strip a leading "I" / "I've" / "I'm" / "I was" etc. from the input first to
# avoid producing "I I fixed a bug".
_LEADING_I_RE = re.compile(r"^i(?:'m|'ve|'d|'ll)?\s+(?:was\s+|had\s+)?", re.IGNORECASE)


def _strip_leading_i(text):
    return _LEADING_I_RE.sub("", text.strip(), count=1)


def _apply(pairs, text):
    for pattern, repl in pairs:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text


def hypeify(text):
    """Buzzword-substitute a sentence, no LinkedIn wrapper."""
    text = _apply(PHRASES, text)
    word_pairs = [(r"\b" + re.escape(w) + r"\b", r) for w, r in WORDS.items()]
    text = _apply(word_pairs, text)
    return text


def linkedinify(text, n_hashtags=3, seed=None):
    """Buzzword-substitute a sentence and wrap it in a LinkedIn hustle post."""
    rng = random.Random(seed)
    hyped = hypeify(_strip_leading_i(text))
    template = rng.choice(TEMPLATES)
    n = max(0, min(n_hashtags, len(HASHTAGS)))
    tags = " ".join(rng.sample(HASHTAGS, k=n))
    return template.format(text=hyped, tags=tags).strip()


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="buzzwordify",
        description="Turn what you actually did into insufferable LinkedIn hustle-speak.",
    )
    parser.add_argument("text", nargs="+", help="what you actually did, in plain English")
    parser.add_argument("--seed", type=int, default=None, help="reproducible hype, for consistent personal branding")
    parser.add_argument("--hashtags", type=int, default=3, help="number of hashtags to append (default: 3)")
    parser.add_argument("--raw", action="store_true", help="skip the LinkedIn template, just buzzword the sentence")
    parser.add_argument("--version", action="version", version=f"buzzwordify {__version__}")
    args = parser.parse_args(argv)

    sentence = " ".join(args.text)
    if args.raw:
        print(hypeify(sentence))
    else:
        print(linkedinify(sentence, n_hashtags=args.hashtags, seed=args.seed))


if __name__ == "__main__":
    main()
