# Slidev Presentation Hub

This project is set up to handle multiple presentations effortlessly.

## 🚀 Getting Started

To start the default presentation (`slides.md`):

```bash
npm run dev
```

## 📂 Multi-Slide Management

You can add any number of markdown files for different presentations. To run a specific one:

```bash
npm run dev -- your-presentation.md
```

### Example

1. Create a file called `my-topic.md`
2. Run `npm run dev -- my-topic.md`

## 🧩 Modular Slides (Shared Content)

If you follow the `src` pattern in your markdown, you can split one presentation into several files:

```markdown
---
# In your main slides.md
---
# Main Slide

---
src: ./sub-section.md
---
```

Slidev handles this automatically for you.

## 📦 Building and Exporting

- **Build to static assets:** `npm run build -- filename.md`
- **Export to PDF:** `npm run export -- filename.md`

## 🎨 Themes

By default, the `default` and `seriph` themes are installed. You can change the theme by updating the frontmatter in your `.md` file:

```markdown
---
theme: seriph
---
```
