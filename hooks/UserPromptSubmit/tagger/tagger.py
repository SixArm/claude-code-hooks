#!/usr/bin/env python

# Add tags to a user's prompt, ideally to make the prompt smarter.
# 
# The tags in this example code are for typical software engineering needs.
# You can customize these for your own goals and needs.
# 
# - Package: claude-code-hooks-user-prompt-submit-tagger
# - Version: 1.0.0
# - Created: 2026-02-22T19:08:48Z
# - Updated: 2026-02-22T19:08:48Z
# - License: MIT or Apache-2.0 or GPL-2.0 or GPL-3.0 or contact us for more
# - Contact: Joel Parker Henderson <joel@joelparkerhenderson.com>

import json, re, sys
tags = set()

regex_tag_dict = {
    r"\b(adrs?|architectures?|architecture[- ]decision[- ]records?|domain[- ]driven[- ]designs?)\b": "expert software architecture",
    r"\b(availability|dependability|maintainability|reliability|scalability)\b": "expert system quality attributes",
    r"\b(auths?|authentications?|authorizations?|jwt|login|logoff|owasp|signin|signout|vulnerability|xss)\b": "expert software security",
    r"\b(css|design systems?|frontend|front-end|stylesheets?|ui|user interfaces?|ux)\b": "expert software frontend",
    r"\b(apis?|balancers?|containers?|networks?|servers?|hosts?|hostnames?|rpcs?)\b": "expert software backend",
    r"\b(databases?|database columns?|database index|database indexes|database migrations?|database rows?|database schemas?|database tables?|db|mysql|postgres|postgresql|sql|sqlserver)\b": "expert database administrator",
    r"\b(bdd|behavior[- ]driven[- ]development|sdd|spec[- ]driven[- ]development|tdd|test[- ]driven[- ]development|behavior[- ]tests?|benchmark[- ]tests?|functional[- ]tests?|integration[- ]tests?|mutation[- ]tests?|unit tests?|code coverages?|code metrics?|dora metrics?)\b": "expert software testing",
    r"\b(breakpoints?|broken|bugs?|debugs?|debugger?|debugging|fix|fixes|fails?|failings?|failures?|errs?|errors?)\b": "expert software debugging",
}

prompt = json.load(sys.stdin)["prompt"].lower()
for regex, tag in regex_tag_dict.items():
    if re.search(regex, prompt):
        tags.add(tag)

print("<tags>\n", ',\n  '.join(tags), "\n</tags>")
