# buzzwordify

![hustle](https://img.shields.io/badge/hustle-maximum-critical)
![synergy](https://img.shields.io/badge/synergy-100%25-blueviolet)
![grindset](https://img.shields.io/badge/grindset-activated-orange)
![license](https://img.shields.io/badge/license-MIT-informational)

**Turns what you actually did into insufferable LinkedIn hustle-speak. In 2 minutes, you too can become a Thought Leader.**

You didn't fix a typo. You **resolved a critical production-blocking issue.**
You didn't take a nap. You **recharged for peak performance.**
You didn't quit your job. You **began an exciting new chapter.**

`buzzwordify` does the emotional labor of personal branding for you, so you don't have to.

## Before / After

```
$ buzzwordify "fixed a typo"
Humbled to announce: I resolved a critical production-blocking issue. This is only the beginning. 🙏 #winning #grindset #synergy

$ buzzwordify "fixed a bug in the login page"
🚀 Thrilled to share that I just shipped a critical hotfix in the login page. Grateful for this incredible journey. #grindset #winning #disruptive

$ buzzwordify "helped my team clean up some code"
Humbled to announce: I spearheaded my high-performing pod clean up some infrastructure. This is only the beginning. 🙏 #winning #growthmindset #innovation

$ buzzwordify "wrote documentation"
🔥 Just authored comprehensive technical documentation. Manifesting even bigger wins ahead. #synergy #disruptive #hustle

$ buzzwordify "reviewed a pr"
Excited to share that I provided strategic technical leadership on a pull request. Onwards and upwards! 💪 #growthmindset #leadership #winning

$ buzzwordify "built an app over the weekend"
Reflecting on a big milestone: I engineered an ecosystem over the weekend. Grateful, humbled, and hungry for more. #innovation #synergy #grindset

$ buzzwordify "took a nap"
🔥 Just recharged for peak performance. Manifesting even bigger wins ahead. #buildinpublic #leadership #hustle

$ buzzwordify "quit my job to work on a small project"
Big news 📈 — I began an exciting new chapter to drive a scrappy initiative. So proud of what we're building. #innovation #buildinpublic #hustle
```

Note that the grammar is occasionally worse after buzzwordifying. This is accurate to the source material.

## Installation

```bash
git clone https://github.com/<you>/buzzwordify.git
cd buzzwordify
pip install -e .
```

## Usage

```bash
buzzwordify "wrote some tests"
buzzwordify "attended a meeting" --seed 42     # reproducible hype, for consistent personal branding
buzzwordify "used a library" --hashtags 5      # more hashtags, more reach
buzzwordify "fixed a bug" --raw                # buzzwords only, skip the LinkedIn post wrapper
```

Or, without installing:

```bash
python3 -m buzzwordify "cleaned up some code"
```

Also importable, for programmatic hustling:

```python
from buzzwordify import hypeify, linkedinify

hypeify("fixed a bug")
# 'shipped a critical hotfix'

linkedinify("fixed a bug", seed=1)
# "Humbled to announce: I shipped a critical hotfix. This is only the beginning. 🙏 #winning #grindset #synergy"
```

## FAQ

**Is this satire?**
Yes.

**Does it use AI?**
No. It's regular expressions pretending to have a personal brand. This is, coincidentally, also how most LinkedIn thought leadership is produced.

**Can I use this unironically?**
You can, but we cannot be held responsible for the connection requests that follow.

**Will this get me a promotion?**
`rockstar` claimed it would make you a Rockstar C++ Programmer in 2 minutes and had testimonials to prove it. We are prepared to make equally unverifiable claims.

## Testimonials

> "I ran my standup notes through buzzwordify and my manager asked if I was interviewing at OpenAI."
> — A Guy Named Chad, Growth-Minded Synergist

> "I posted the raw output and got 40,000 impressions. I have never felt more empty."
> — Anonymous, Thought Leader (Self-Appointed)

> "10/10, would leverage again."
> — Someone Who Definitely Exists

## License

MIT
