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

export interface EmotionInterpretation {
  tone: EmotionTone;
  intensity: number; // 0.0 – 1.0
  keywords: string[];
  summary: string;
}
