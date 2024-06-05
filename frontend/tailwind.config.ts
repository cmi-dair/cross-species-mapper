import { join } from "path";
import type { Config } from "tailwindcss";
import { cmiLight } from "@cmi-dair/skeleton-themes";
import { skeleton } from "@skeletonlabs/tw-plugin";

export default {
  darkMode: "class",
  content: [
    "./src/**/*.{html,js,svelte,ts}",
    join(
      require.resolve("@skeletonlabs/skeleton"),
      "../**/*.{html,js,svelte,ts}",
    ),
  ],
  theme: {
    themes: { preset: ["cmi-light"] },
  },
  plugins: [
    require("@tailwindcss/typography"),
    skeleton({
      themes: {
        custom: [cmiLight],
      },
    }),
  ],
} as Config;
