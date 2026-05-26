export enum PlacementRole {
  FOCAL = "focal",
  SECONDARY = "secondary",
  FILLER = "filler",
  ACCENT = "accent",
  GREENERY = "greenery",
}

export interface PlacementEntry {
  id: string;
  blueprint_id: string;
  role: PlacementRole;
  angle: number;   // degrees, 0–360
  radius: number;  // normalized 0.0–1.0
  layer: number;   // integer, 1 = base layer
  z_index: number; // integer, render order
}
