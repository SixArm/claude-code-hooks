# Tagger

This Claude Code hook happens on the user prompt submit.

The simple `tagger` python program demonstrates three steps:

1. Search the prompt for typical software engineering words and phrases.
2. When a search succeds, then create a suitable tag to help Claude run.
3. Output the tags, which will be combined with the user prompt.

Demonstration:

```sh
cat tagger-input-example.json | ./tagger.py
```

You should see output such as:

```xml
<tags>
  expert database administrator,
  expert software architecture,
  expert software security,
  expert software backend,
  expert software testing,
  expert software debugging,
  expert software frontend
</tags>
```
