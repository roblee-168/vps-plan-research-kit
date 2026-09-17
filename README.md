# VPS Plan Research Kit

A small, reusable kit for comparing VPS billing terms without treating credits as prices.

## Included

- `official-sources.csv`: 14 official provider source URLs exported from the PerkMingle source configuration on 2026-09-17. A source URL is a research starting point, not a claim that a current promotion exists.
- `CHECKLIST.md`: a purchasing and evidence checklist.
- `cost.py`: an offline calculator for an initial fixed term followed by a renewal term. No network access, tracking, affiliate links, or price database.

The accompanying public directory is [PerkMingle](https://perkmingle.com/).

## Usage

Python 3, standard library only:

```sh
python cost.py --initial-total 24 --initial-months 12 --renewal-monthly 4 --months 24
```

This is a synthetic calculation example, not a provider quote. Output: 72.00 total, 3.00 effective monthly. Formula: initial total + max(0, requested months - initial months) * renewal monthly. The full initial commitment is charged even when the requested horizon is shorter. Use one currency for all inputs. Enter an actual renewal rate; do not reuse a promotional rate if renewal is unknown. Taxes, setup fees, exchange rates, refunds and optional extras are excluded.

Run verification with `python -m unittest -v`.

## Data limitations and maintenance

These URLs are a dated snapshot, not a live verification service. Check the official page before use. HTTP failures and robots restrictions are not permission to bypass access controls. No performance rankings or renewal prices are inferred. Report broken sources with the official replacement URL and the date checked.

## Provenance

Source: `roblee-168/vps-deals-promo-radar`, `.ilang/site.ilang`, local snapshot dated 2026-09-17. Only official public source URLs are exported; account identifiers, affiliate parameters and private data are excluded. Vendor sites retain their own terms. The original checklist and utility are provided under the MIT license.
