INSERT INTO spells
    (
     name,
     level,
     casting_time,
     range_area,
     component_visual,
     component_semantic,
     component_material,
     component_materials,
     duration,
     concentration,
     ritual,
     school,
     save_type,
     description,
     image_url,
     source_id
    )
VALUES
('Banishing Smite', '5th', '1 bonus action', 'self', 'True', 'False', 'False', '', 'concentration 1 minute', 'False', 'False', 'abjuration', 'none', 'The next time you hit a creature with a weapon attack before this spell ends, your weapon crackles with force, and the attack deals an extra 5d10 force damage to the target.
Additionally, if this attack reduces the target to 50 hit points or fewer, you banish it. If the target is native to a different plane of existence than the one you’re on, the target disappears, returning to its home plane. If the target is native to the plane you’re on, the creature vanishes into a harmless demiplane. While there, the target is incapacitated. It remains there until the spell ends, at which point the target reappears in the space it left or in the nearest unoccupied space if that space is occupied.', '', '5')
