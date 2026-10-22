# VeriLayer Method — public review v0.5

**Working title • Research draft • Open call for falsification**

**VeriLayer Method** proposes an *evidence-governed* process for AI-assisted software development. It combines abstraction-aligned verification, **TRIZ-based resolution of significant engineering contradictions**, scope-specific verification obligations and local stop gates.

> This is a falsifiable engineering hypothesis, **not** an established standard, independently validated best practice, or claim of global originality. The authors welcome negative results.

## Start here

- 📖 **[Full methodology in Russian](METHODOLOGY.md)** — public-review edition v0.5, including TRIZ, L0–L5, VO and S01–S12.
- 🧪 **[Evaluation plan](EXPERIMENT_PROTOCOL.md)** — comparison with a strong spec-driven baseline, cost, false stops and false proceeds.
- 🔎 **[How to challenge the method](REVIEW_GUIDE.md)** — what evidence and counterexamples we need.
- 📣 **[Русский анонс](ANNOUNCEMENT_RU.md)** — public invitation to peer review.
- 📝 **[Submit a critique](https://github.com/SoldatovAlexander/verilayer-method/issues/new/choose)** or browse [open issues](https://github.com/SoldatovAlexander/verilayer-method/issues).

## Central testable hypothesis

Compared with ordinary coding agents and mature specification-driven workflows (for example, GitHub Spec Kit / OpenSpec), coupling *design ↔ verifiability ↔ contradiction resolution* with scoped evidence-based gate decisions will reduce serious unsupported actions and errors **without an unacceptable increase in needless stops, rework, elapsed time and cost**.

TRIZ is part of the **defined workflow for significant contradictions**, but its *incremental benefit* remains an independent hypothesis to be tested.

## We invite you to disprove it

Bring a reproducible case where:

1. An unsafe action was wrongly allowed (**False Proceed**).
2. Safe independent work was wrongly blocked (**False Stop**).
3. An existing method or published paper solves the same problem better (**prior art**).
4. TRIZ adds no value over regular architecture trade-off analysis.
5. The proposed benchmark, test oracle or inference is invalid.
6. Cost and delay exceed the actual risk reduction.

One independently checkable claim per issue. Please include task inputs, assumptions, tools/model version where appropriate, actual outcome, expected outcome, and why the discrepancy matters.

## What is and is not published

**Published:** methodology draft, evaluation criteria, review instructions and public challenge templates.

**Not published as evidence:** 22 author-generated scenarios have not yet undergone independent validation or live controlled runs; their evaluator-only answer key is deliberately withheld to avoid leakage. No fabricated benchmark results are claimed.

## Related engineering foundations

NASA systems engineering and V&V; GSN assurance cases; risk-based verification; TDD/BDD; GitHub Spec Kit/OpenSpec; Altshuller's TRIZ. See [methodology references](METHODOLOGY.md). This project does **not** claim invention of those practices.

## Naming and reuse

**VeriLayer is a provisional research name.** Similar marks have been reported in Russian and US trademark sources; a legal clearance assessment has **not** been completed. Publication of this document does not establish brand rights.

No open-source/content license has been selected yet. **Public visibility and a request for criticism are not a grant of reuse rights.** Proposed licensing can be discussed in an issue before adoption.

## Language

Core document and announcement: Russian. Review process: Russian or English. International contributions and reproducible counterexamples are welcome.
