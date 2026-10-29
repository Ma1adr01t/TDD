# Mayor on Delivery Duty · v0.6

An early, dependency-free HTML5 Canvas driving prototype for a delivery driver who accidentally got elected mayor.

## Run it

Keep `index.html` and the `assets/` directory together. Open `index.html` in a modern browser. There is no build step or dependency for playing.

To host on GitHub Pages, upload `index.html`, `README.md`, and the complete `assets/` directory to the repository root, then enable **Settings → Pages → Deploy from a branch** and select the main branch and `/ (root)`.

## Controls

- **W / Up:** Accelerate
- **S / Down:** Brake and reverse
- **A / D or Left / Right:** Rotate/steer the vehicle
- **Space:** Handbrake
- **J:** Open the job board
- **Slow down at a marked stop:** Automatically pick up or deliver when near its entrance (roughly under 72 speed units)

Touchscreen buttons are shown on touch-oriented devices. Controls and physics are provisional.

## Current features

- Seeded street names, locations, hazards, and requests; same seed reproduces the layout.
- Small, connected, irregular street network with seeded street names and occasional loops, T-junctions, and dead ends.
- Wider pavement and a substantially closer camera than v0.1.
- Fewer hazards, quicker acceleration and more forgiving steering. Off-road travel remains possible at a low speed.
- **Actual replaceable PNG assets:** terrain tile atlas and separate building, car, debris, package, and smoke sprite files.
- The game builds the map out of 32×32 terrain tiles selected according to the generated roads. No terrain or buildings are painted from JavaScript shapes.
- A fixed 384×216 game frame, scaled to the screen with hard nearest-neighbor pixels.
- Animated package tosses toward destination buildings and opaque pixel dust during sharp steering at speed.
- Car-following, north-up camera; no minimap.
- Eight-direction arrow pointing straight at the next stop, without routing.
- Potholes and rubbish affect vehicle health and speed.
- A three-minute day, multiple sequential jobs, and a primitive reliability score.

## Deliberately missing

No City Hall decision phase, town growth, building economy, meaningful traffic, AI drivers, sound, save system, or road improvements yet. The current PNG artwork is deliberately provisional. This is still a handling, navigation, and art-pipeline test rather than a full gameplay vertical slice.

## Replacing art

Each PNG under `assets/` is independently replaceable. Keep the file names and canvas sizes unchanged for a direct swap. `terrain.png` is a horizontal atlas of eight 32×32 tiles (256×32), in this order: grass, alternate grass, asphalt, alternate asphalt, sidewalk, gravel, cracked asphalt, marked asphalt. Buildings are separate 64×64 transparent PNGs. Other sprite dimensions are visible in the supplied images.

`build_assets.py` is **optional**. It recreates the current draft artwork using Pillow and is not needed to run the game. Don't run it after replacing sprites with your own work, because it regenerates the temporary art files.

## Suggested next steps

1. Playtest steering, camera scale, shift length, and drop-off readability.
2. Make road generation less grid-like while preserving reachability and consistent street names.
3. Introduce morning decisions that change roads and building health between shifts.
4. Save the town state between days, then implement business closure and opening.
