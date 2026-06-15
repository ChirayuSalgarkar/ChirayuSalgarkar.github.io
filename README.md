# ChirayuSalgarkar.github.io

Personal academic website of **Chirayu M. Salgarkar** — Biomedical Engineering &
Mathematics. Live at <https://ChirayuSalgarkar.github.io>.

Built with [Jekyll](https://jekyllrb.com/) on the
[academicpages](https://github.com/academicpages/academicpages.github.io)
template (a fork of the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)
theme, © Michael Rose, MIT License).

## Repository layout

| Path | What it holds |
|------|---------------|
| `_config.yml` | Site-wide settings (title, author, nav, plugins). Restart the server after editing. |
| `_pages/` | Standalone pages (about, resume, portfolio, talks, notes, etc.). |
| `_portfolio/` | Portfolio project entries. |
| `_posts/` | Blog posts. |
| `_notes/` | Study / paper notes. |
| `_publications/`, `_talks/`, `_teaching/` | Academic collections (add Markdown entries here). |
| `_data/` | Navigation, UI text, author metadata. |
| `_layouts/`, `_includes/`, `_sass/` | Theme source (templates, partials, styles). |
| `assets/` | Compiled CSS/JS, fonts. |
| `images/` | Site images. |
| `files/` | Downloadable files (PDFs, LaTeX sources, code). Served at `/files/...`. |
| `markdown_generator/` | Optional scripts to generate publication/talk Markdown from TSV. |

## Editing content

Most updates are just adding or editing Markdown files:

- **New blog post** → add `_posts/YYYY-MM-DD-title.md` with front matter.
- **New portfolio item** → add `_portfolio/your-project.md`.
- **New note** → add `_notes/your-note.md`.
- **Site settings / navigation** → edit `_config.yml` and `_data/navigation.yml`.

## Run locally

Requires Ruby + Bundler.

```sh
bundle install            # first time only
bundle exec jekyll serve  # serves at http://localhost:4000
```

The site auto-rebuilds on file changes. (Delete `Gemfile.lock` and re-run
`bundle install` if you hit dependency errors.)

## Deploy

Pushing to the `master`/`main` branch publishes automatically via GitHub Pages.

## Notes on this repo

- Build artifacts (LaTeX `.aux`/`.log`/etc., Python `.venv`/`__pycache__`,
  Manim render caches) are intentionally **not** committed — see `.gitignore`.
  Regenerate them locally as needed.
