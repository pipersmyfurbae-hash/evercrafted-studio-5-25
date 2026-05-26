/**
 * Evercrafted API client — typed fetch wrapper.
 *
 * Reads NEXT_PUBLIC_API_URL from the environment.
 * All calls go through the FastAPI backend; the Anthropic API key never
 * touches this file.
 */

const API_BASE =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...init,
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`API ${res.status}: ${body}`);
  }

  return res.json() as Promise<T>;
}

// ---------------------------------------------------------------------------
// Emotion
// ---------------------------------------------------------------------------

export interface EmotionClassifyInput {
  text: string;
  occasion?: string;
  color_preferences?: string;
}

export interface EmotionOutput {
  primary_tone: string;
  secondary_tones: string[];
  valence: number;
  arousal: number;
  quadrant: string;
  emotion_vector: Record<string, number>;
  palette_direction: string;
  density_bias: string;
  movement_bias: string;
  formula_candidates: string[];
  narrative_summary: string;
}

export function classifyEmotion(input: EmotionClassifyInput): Promise<EmotionOutput> {
  return apiFetch<EmotionOutput>("/api/v1/emotion/classify", {
    method: "POST",
    body: JSON.stringify(input),
  });
}

// ---------------------------------------------------------------------------
// Blueprints
// ---------------------------------------------------------------------------

export interface EmotionInterpretationInput {
  tone: string;
  intensity: number;
  keywords: string[];
  summary: string;
  primary_tone?: string;
  secondary_tones?: string[];
  valence?: number;
  arousal?: number;
  quadrant?: string;
  emotion_vector?: Record<string, number>;
  palette_direction?: string;
  density_bias?: string;
  movement_bias?: string;
  narrative_summary?: string;
}

export interface BlueprintCreateInput {
  schema_version: "EC_CANON_V1";
  name: string;
  status?: "draft" | "saved" | "archived";
  emotion: EmotionInterpretationInput;
}

export interface Blueprint {
  id: string;
  schema_version: "EC_CANON_V1";
  name: string;
  status: "draft" | "saved" | "archived";
  emotion: EmotionInterpretationInput;
  created_at: string;
  updated_at: string;
}

export function createBlueprint(input: BlueprintCreateInput): Promise<Blueprint> {
  return apiFetch<Blueprint>("/api/v1/blueprints", {
    method: "POST",
    body: JSON.stringify(input),
  });
}

export function listBlueprints(): Promise<Blueprint[]> {
  return apiFetch<Blueprint[]>("/api/v1/blueprints");
}
