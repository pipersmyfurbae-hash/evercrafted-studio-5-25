"use client";

import { useState } from "react";
import {
  classifyEmotion,
  createBlueprint,
  type EmotionOutput,
  type Blueprint,
} from "../lib/api";

// ---------------------------------------------------------------------------
// Quadrant badge colour map
// ---------------------------------------------------------------------------
const QUADRANT_COLORS: Record<string, string> = {
  "Cozy & Calm": "bg-blue-900/40 text-blue-300 border-blue-700",
  "Bright & Joyful": "bg-yellow-900/40 text-yellow-300 border-yellow-700",
  "Deep & Contemplative": "bg-purple-900/40 text-purple-300 border-purple-700",
  "Bold & Expressive": "bg-red-900/40 text-red-300 border-red-700",
};

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------

function EmotionBar({ label, value }: { label: string; value: number }) {
  const pct = Math.round(value * 100);
  return (
    <div className="flex items-center gap-3">
      <span className="w-24 text-xs text-zinc-400 capitalize shrink-0">{label}</span>
      <div className="flex-1 h-1.5 rounded-full bg-zinc-800">
        <div
          className="h-full rounded-full bg-amber-400"
          style={{ width: `${pct}%` }}
        />
      </div>
      <span className="w-8 text-xs text-zinc-500 text-right">{pct}%</span>
    </div>
  );
}

// ---------------------------------------------------------------------------
// Main page
// ---------------------------------------------------------------------------

export default function MemoryWeaverPage() {
  // Form state
  const [text, setText] = useState("");
  const [occasion, setOccasion] = useState("");
  const [colorPrefs, setColorPrefs] = useState("");

  // Workflow state
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [emotion, setEmotion] = useState<EmotionOutput | null>(null);

  // Blueprint save state
  const [blueprintName, setBlueprintName] = useState("");
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState<Blueprint | null>(null);

  // ---- Step 1: interpret emotion ----
  async function handleInterpret() {
    if (!text.trim()) return;
    setLoading(true);
    setError(null);
    setEmotion(null);
    setSaved(null);
    try {
      const result = await classifyEmotion({
        text: text.trim(),
        occasion: occasion.trim() || undefined,
        color_preferences: colorPrefs.trim() || undefined,
      });
      setEmotion(result);
      setBlueprintName(result.primary_tone);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "Interpretation failed.");
    } finally {
      setLoading(false);
    }
  }

  // ---- Step 2: save blueprint ----
  async function handleSave() {
    if (!emotion || !blueprintName.trim()) return;
    setSaving(true);
    setError(null);
    try {
      const blueprint = await createBlueprint({
        schema_version: "EC_CANON_V1",
        name: blueprintName.trim(),
        status: "draft",
        emotion: {
          tone: "calm", // default tone; later engines will refine
          intensity: Math.abs(emotion.valence),
          keywords: emotion.secondary_tones,
          summary: emotion.narrative_summary,
          primary_tone: emotion.primary_tone,
          secondary_tones: emotion.secondary_tones,
          valence: emotion.valence,
          arousal: emotion.arousal,
          quadrant: emotion.quadrant,
          emotion_vector: emotion.emotion_vector,
          palette_direction: emotion.palette_direction,
          density_bias: emotion.density_bias,
          movement_bias: emotion.movement_bias,
          narrative_summary: emotion.narrative_summary,
        },
      });
      setSaved(blueprint);
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : "Save failed.");
    } finally {
      setSaving(false);
    }
  }

  const quadrantClass =
    emotion ? (QUADRANT_COLORS[emotion.quadrant] ?? "bg-zinc-800 text-zinc-300 border-zinc-700") : "";

  return (
    <div className="max-w-2xl mx-auto px-6 py-10 space-y-10">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold text-zinc-100 tracking-tight">
          Memory Weaver
        </h1>
        <p className="mt-1 text-sm text-zinc-400">
          Describe a memory, feeling, or mood. The Emotion Engine will interpret it into a
          structured design brief.
        </p>
      </div>

      {/* ── Section 1: Input ── */}
      <section className="space-y-4">
        <div>
          <label className="block text-xs font-medium text-zinc-400 mb-1.5 uppercase tracking-wider">
            Memory or mood *
          </label>
          <textarea
            className="w-full rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 text-sm px-4 py-3 focus:outline-none focus:ring-1 focus:ring-amber-400 resize-none placeholder:text-zinc-600"
            rows={4}
            placeholder="My grandmother's rose garden in summer — warm afternoons, dusty light, the smell of old wood and petals..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-medium text-zinc-400 mb-1.5 uppercase tracking-wider">
              Occasion (optional)
            </label>
            <input
              type="text"
              className="w-full rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 text-sm px-4 py-2.5 focus:outline-none focus:ring-1 focus:ring-amber-400 placeholder:text-zinc-600"
              placeholder="Anniversary, memorial, home décor…"
              value={occasion}
              onChange={(e) => setOccasion(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-xs font-medium text-zinc-400 mb-1.5 uppercase tracking-wider">
              Colour preferences (optional)
            </label>
            <input
              type="text"
              className="w-full rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 text-sm px-4 py-2.5 focus:outline-none focus:ring-1 focus:ring-amber-400 placeholder:text-zinc-600"
              placeholder="Warm ivory, dusty rose…"
              value={colorPrefs}
              onChange={(e) => setColorPrefs(e.target.value)}
            />
          </div>
        </div>

        <button
          onClick={handleInterpret}
          disabled={!text.trim() || loading}
          className="w-full py-3 rounded-lg bg-amber-400 text-zinc-950 text-sm font-semibold hover:bg-amber-300 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          {loading ? "Interpreting…" : "Interpret Emotion →"}
        </button>

        {error && (
          <p className="text-sm text-red-400 bg-red-900/20 border border-red-800 rounded-lg px-4 py-3">
            {error}
          </p>
        )}
      </section>

      {/* ── Section 2: Emotion Results ── */}
      {emotion && (
        <section className="space-y-5 border border-zinc-800 rounded-xl bg-zinc-900/50 p-6">
          {/* Primary tone + quadrant */}
          <div className="flex items-start justify-between gap-4">
            <div>
              <p className="text-xs text-zinc-500 uppercase tracking-wider mb-1">
                Primary tone
              </p>
              <h2 className="text-xl font-semibold text-zinc-100 capitalize">
                {emotion.primary_tone}
              </h2>
              <p className="text-sm text-zinc-400 mt-0.5 italic">
                {emotion.secondary_tones.join(" · ")}
              </p>
            </div>
            <span
              className={`shrink-0 text-xs font-medium px-3 py-1.5 rounded-full border ${quadrantClass}`}
            >
              {emotion.quadrant}
            </span>
          </div>

          {/* Narrative */}
          <p className="text-sm text-zinc-300 leading-relaxed">
            {emotion.narrative_summary}
          </p>

          {/* Emotion vector */}
          <div>
            <p className="text-xs text-zinc-500 uppercase tracking-wider mb-3">
              Emotion vector
            </p>
            <div className="space-y-2">
              {Object.entries(emotion.emotion_vector)
                .sort(([, a], [, b]) => b - a)
                .map(([key, val]) => (
                  <EmotionBar key={key} label={key} value={val} />
                ))}
            </div>
          </div>

          {/* Design direction */}
          <div className="grid grid-cols-3 gap-3 text-sm">
            <div className="bg-zinc-800/60 rounded-lg p-3">
              <p className="text-xs text-zinc-500 mb-1">Palette</p>
              <p className="text-zinc-200">{emotion.palette_direction}</p>
            </div>
            <div className="bg-zinc-800/60 rounded-lg p-3">
              <p className="text-xs text-zinc-500 mb-1">Density</p>
              <p className="text-zinc-200">{emotion.density_bias}</p>
            </div>
            <div className="bg-zinc-800/60 rounded-lg p-3">
              <p className="text-xs text-zinc-500 mb-1">Movement</p>
              <p className="text-zinc-200">{emotion.movement_bias}</p>
            </div>
          </div>

          {/* Formula candidates */}
          <div>
            <p className="text-xs text-zinc-500 uppercase tracking-wider mb-2">
              Formula candidates
            </p>
            <div className="flex flex-wrap gap-2">
              {emotion.formula_candidates.map((f) => (
                <span
                  key={f}
                  className="text-xs px-3 py-1 rounded-full bg-zinc-800 border border-zinc-700 text-zinc-300 font-mono"
                >
                  {f}
                </span>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* ── Section 3: Save Blueprint ── */}
      {emotion && !saved && (
        <section className="space-y-4 border border-zinc-800 rounded-xl bg-zinc-900/30 p-6">
          <div>
            <h3 className="text-sm font-semibold text-zinc-200 mb-1">
              Save as Blueprint
            </h3>
            <p className="text-xs text-zinc-500">
              This will create a draft EC_CANON_V1 blueprint with the emotion data above.
            </p>
          </div>
          <div>
            <label className="block text-xs font-medium text-zinc-400 mb-1.5 uppercase tracking-wider">
              Blueprint name
            </label>
            <input
              type="text"
              className="w-full rounded-lg bg-zinc-900 border border-zinc-700 text-zinc-100 text-sm px-4 py-2.5 focus:outline-none focus:ring-1 focus:ring-amber-400"
              value={blueprintName}
              onChange={(e) => setBlueprintName(e.target.value)}
            />
          </div>
          <button
            onClick={handleSave}
            disabled={!blueprintName.trim() || saving}
            className="w-full py-3 rounded-lg bg-zinc-800 border border-zinc-700 text-zinc-200 text-sm font-medium hover:bg-zinc-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
          >
            {saving ? "Saving…" : "Save Blueprint"}
          </button>
        </section>
      )}

      {/* Success state */}
      {saved && (
        <section className="border border-emerald-800/50 rounded-xl bg-emerald-900/10 p-6 space-y-2">
          <div className="flex items-center gap-2 text-emerald-400">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fillRule="evenodd"
                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                clipRule="evenodd"
              />
            </svg>
            <span className="font-semibold text-sm">Blueprint saved</span>
          </div>
          <p className="text-sm text-zinc-400">
            <span className="text-zinc-300 font-medium">{saved.name}</span>
          </p>
          <p className="text-xs text-zinc-600 font-mono">{saved.id}</p>
          <button
            onClick={() => {
              setText("");
              setOccasion("");
              setColorPrefs("");
              setEmotion(null);
              setSaved(null);
              setBlueprintName("");
            }}
            className="text-xs text-amber-400 hover:text-amber-300 mt-2"
          >
            ← Start a new design
          </button>
        </section>
      )}
    </div>
  );
}
