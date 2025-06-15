# README

A scaffold for frontend projects using **React** and **Vite**. This setup is based on the latest Vite initialization, with some personal preferences. It aims to provide a solid starting point for modern web development in my opinion.

---

## Features

### Testing

- Uses [Vitest](https://vitest.dev/) for unit testing.
- Integrates with [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) for component testing.

### Styling

- [Tailwind CSS](https://tailwindcss.com/) for utility-first styling.

### Component Library

- [shadcn/ui](https://ui.shadcn.com/) as component library.

---

## Other
public/manifest -> Read more about how to populate it here https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest

---

## Moving forward

### Component folder structure

I've purposely kept the simple flat folder structure, however something that's good to keep in mind is if the app grows then start grouping related files together to avoid having to look around in the repo for the correct files.

```text
src/
└── components/
    └── Header/
        ├── __tests__/
        │   └── Header.test.tsx
         ├──something-other-related-that-is-only-used-here
        │   └── -related.tsx
        ├── Header.tsx
        └── index.ts
```


