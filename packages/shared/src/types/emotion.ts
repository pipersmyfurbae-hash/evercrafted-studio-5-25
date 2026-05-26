/**
 * Emotion Engine types — EC_CANON_V1 emotion schema.
 *
 * Spec reference: 06_EMOTION_ENGINE_SPEC.md
 */

export enum EmotionTone {
  JOY = "joy",
  GRIEF = "grief",
  LOVE = "love",
  NOSTALGIA = "nostalgia",
  CALM = "calm",
  CELEBRATION = "celebration",
  MELANCHOLY = "melancholy",
  REVERENCE = "reverence",
}

export type EmotionQuadrant =
  | "Cozy & Calm"
  | "Bright & Joyful"
  | "Deep & Contemplative"
  | "Bold & Expressive";

/** Sprint 1 compatible; optional fields are populated by the Emotion Engine. */
export interface EmotionInterpretation {
  tone: EmotionTone;
  intensity: number; // 0.0 – 1.0
  keywords: string[];
  summary: string;
  // Sprint 3 extended fields
  primary_tone?: string;
  secondary_tones?: string[];
  valence?: number; // -1.0 to 1.0
  arousal?: number; // -1.0 to 1.0
  quadrant?: EmotionQuadrant;
  emotion_vector?: Record<string, number>;
  palette_direction?: string;
  density_bias?: string;
  movement_bias?: string;
  narrative_summary?: string;
}

/** Input to POST /api/v1/emotion/classify */
export interface EmotionClassifyInput {
  text: string;
  occasion?: string;
  color_preferences?: string;
}

/** Full structured output from the Emotion Engine. */
export interface EmotionOutput {
  primary_tone: string;
  secondary_tones: string[];
  valence: number;
  arousal: number;
  quadrant: EmotionQuadrant;
  emotion_vector: Record<string, number>;
  palette_direction: string;
  density_bias: string;
  movement_bias: string;
  formula_candidates: string[];
  narrative_summary: string;
}
