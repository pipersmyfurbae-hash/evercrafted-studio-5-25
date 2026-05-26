// 73_TYPESCRIPT_SHARED_TYPES.ts
// Shared production types for Evercrafted Studio MVP

export type UUID = string;

export type EmotionQuadrant =
  | "Cozy & Calm"
  | "Festive & Bright"
  | "Dramatic Tension"
  | "Vintage Melancholy";

export type MaterialRole =
  | "base"
  | "greenery"
  | "filler"
  | "secondary_floral"
  | "focal_floral"
  | "accent";

export type PlacementLayer =
  | "base"
  | "greenery_base"
  | "greenery_extension"
  | "filler"
  | "secondary_floral"
  | "focal_floral"
  | "berries"
  | "accent"
  | "decorative_overlay";

export interface EmotionVector {
  calm?: number;
  nostalgia?: number;
  joy?: number;
  hope?: number;
  drama?: number;
  romance?: number;
  serenity?: number;
  festive?: number;
  [key: string]: number | undefined;
}

export interface Emotion {
  primary_tone: string;
  secondary_tones?: string[];
  valence: number;
  arousal: number;
  quadrant: EmotionQuadrant | string;
  emotion_vector: EmotionVector;
  narrative_summary?: string;
  palette_direction?: string;
  density_bias?: string;
  movement_bias?: string;
}

export interface BaseSpec {
  form_factor: "circular" | "oval" | "teardrop" | "wreath-ring";
  diameter_in: 18 | 20 | 24 | number;
  base_type: "grapevine" | "foam" | "wire" | "twig" | string;
  base_visibility_percent?: number;
}

export interface Formula {
  formula_id: string;
  formula_name: string;
  arc_start_deg?: number;
  arc_end_deg?: number;
  negative_space_deg?: number;
  primary_cluster_zone?: string;
  secondary_cluster_zone?: string;
  flow_direction?: "clockwise" | "counterclockwise" | "radial" | string;
}

export interface WreathDNA {
  cluster_count: number;
  cluster_weight_distribution?: number;
  cluster_spread_deg?: number;
  density_profile: number;
  greenery_direction?: "inward" | "outward" | "balanced" | string;
  silhouette_bias?: "organic" | "structured" | "mixed" | string;
  greenery_ratio?: number;
  focal_ratio?: number;
  silence_arc?: number;
  focal_depth?: number;
  style_signature?: string;
  color_bias?: string;
}

export interface Placement {
  placement_id: string;
  material_id?: string;
  role: MaterialRole | string;
  layer: PlacementLayer | string;
  theta_deg: number;
  clock_position?: string;
  radius_norm: number;
  radius_in?: number;
  rotation_deg?: number;
  scale?: number;
  stem_direction?: string;
  z_index: number;
  cluster_id?: string;
  metadata?: Record<string, unknown>;
}

export interface InventoryItem {
  id?: UUID;
  material_id?: string;
  name: string;
  type: "flower" | "greenery" | "accent" | "base" | "filler" | string;
  role: MaterialRole | string;
  color?: string;
  quantity: number;
  unit_cost?: number;
  tags?: string[];
  metadata?: Record<string, unknown>;
}

export interface VisualizationSpec {
  renderer: "placement_visualization_engine" | string;
  canvas_size?: number;
  show_grid?: boolean;
  show_zones?: boolean;
  render_layers?: string[];
}

export interface BuildStep {
  step: number;
  title: string;
  instructions: string;
  placement_ids?: string[];
  material_ids?: string[];
}

export interface BuildSheet {
  id?: UUID;
  blueprint_id?: string;
  difficulty: "low" | "medium" | "high" | string;
  estimated_minutes: number;
  materials: InventoryItem[];
  steps: BuildStep[];
  quality_checklist: string[];
}

export interface BlueprintScores {
  overall_score?: number;
  composition_balance?: number;
  movement_score?: number;
  emotional_coherence?: number;
  manufacturability?: number;
  originality?: number;
  warnings?: string[];
}

export interface BlueprintMetadata {
  source_prompt?: string;
  seed?: string;
  created_by?: string;
  created_at?: string;
  updated_at?: string;
  tags?: string[];
  [key: string]: unknown;
}

export interface Blueprint {
  blueprint_id: string;
  version: string;
  name: string;
  base: BaseSpec;
  emotion: Emotion;
  formula: Formula;
  dna: WreathDNA;
  zones?: unknown[];
  anchors?: unknown[];
  placements: Placement[];
  materials?: InventoryItem[];
  visualization?: VisualizationSpec;
  manufacturing?: Partial<BuildSheet>;
  commerce?: Record<string, unknown>;
  scores?: BlueprintScores;
  metadata?: BlueprintMetadata;
}

export interface BlueprintSummary {
  id: UUID;
  blueprint_id: string;
  name: string;
  formula_id?: string;
  emotion_quadrant?: string;
  created_at: string;
  updated_at?: string;
}

export interface ApiError {
  code: string;
  message: string;
  details?: unknown;
}
