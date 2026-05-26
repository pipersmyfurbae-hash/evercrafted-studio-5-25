import type { EmotionInterpretation } from "./emotion";

export enum BlueprintStatus {
  DRAFT = "draft",
  SAVED = "saved",
  ARCHIVED = "archived",
}

export interface Blueprint {
  id: string;
  schema_version: "EC_CANON_V1";
  name: string;
  status: BlueprintStatus;
  emotion: EmotionInterpretation;
  created_at: string; // ISO 8601
  updated_at: string; // ISO 8601
}
