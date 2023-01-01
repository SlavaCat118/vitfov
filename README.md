# What is ViTFoV?
Vitfov (Vital Tools for Vital) is a python package for splitting Vital preset files into workable objects. Parameters can then be modified and objects recombined to form a new preset. As a bonus, each object suports full randomization of parameters.
Vitfov splits presets into the following heirarchy:
- Preset
  - Info
  - Settings
    - Advanced
    - Effects
      - Chorus
      - Compressor
      - Delay
      - Distortion
      - Eq
      - Flanger
      - Phaser
      - Reverb
      - Filters
        - Filter 1
        - Filter 2
      - Filter Fx
   - Envelopes [1-6]
   - Lfos [1-8]
   - Custom Warps [1-3]
   - Matirx Ports
   - Matrix Wires
   - Randoms [1-4]
   - Voices [1-3]
   - Sample
   - Random Seeds [1-3]

# Planned
- Documentation

# Notes
As of now, ViTFoV's planned feature set is implemented; However, I will likely be reworking things as writing the documentation will force me to come to terms with my own failures. PyPi release is planned
