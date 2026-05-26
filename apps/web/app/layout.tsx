import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Evercrafted Studio",
  description: "Emotion-aware procedural floral design operating system",
};

const NAV_ITEMS = [
  { label: "Memory Weaver", href: "/", active: true },
  { label: "Design Studio", href: "#", active: false },
  { label: "Design Library", href: "#", active: false },
  { label: "Inventory", href: "#", active: false },
  { label: "Build Sheets", href: "#", active: false },
];

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex bg-zinc-950 text-zinc-100">
        {/* Sidebar */}
        <aside className="w-56 shrink-0 flex flex-col border-r border-zinc-800 bg-zinc-900 min-h-screen">
          {/* Wordmark */}
          <div className="px-5 py-6 border-b border-zinc-800">
            <span className="text-sm font-semibold tracking-widest uppercase text-amber-400">
              Evercrafted
            </span>
            <span className="block text-xs text-zinc-500 tracking-wider mt-0.5">
              Studio
            </span>
          </div>

          {/* Navigation */}
          <nav className="flex-1 px-3 py-4 space-y-1">
            {NAV_ITEMS.map((item) =>
              item.active ? (
                <a
                  key={item.label}
                  href={item.href}
                  className="flex items-center gap-2 px-3 py-2 rounded-md text-sm font-medium bg-amber-400/10 text-amber-300"
                >
                  {item.label}
                </a>
              ) : (
                <span
                  key={item.label}
                  className="flex items-center gap-2 px-3 py-2 rounded-md text-sm text-zinc-600 cursor-not-allowed select-none"
                  title="Coming soon"
                >
                  {item.label}
                </span>
              )
            )}
          </nav>

          {/* Footer */}
          <div className="px-5 py-4 border-t border-zinc-800">
            <span className="text-xs text-zinc-600">Sprint 2–3 MVP</span>
          </div>
        </aside>

        {/* Main content */}
        <main className="flex-1 overflow-auto">{children}</main>
      </body>
    </html>
  );
}
