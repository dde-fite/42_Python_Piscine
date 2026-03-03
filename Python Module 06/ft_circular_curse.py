from alchemy.grimoire import validate_ingredients, record_spell

print('\n=== Circular Curse Breaking ===\n'

      '\nTesting ingredient validation:\n'
      f'validate_ingredients("fire air"): {validate_ingredients("fire air")}\n'
      'validate_ingredients("dragon scales"): '
      f'{validate_ingredients("dragon scales")}\n'

      '\nTesting spell recording with validation:\n'
      'record_spell("Fireball", "fire air"): '
      f'{record_spell("Fireball", "fire air")}\n'
      'record_spell("Dark Magic", "shadow"): '
      f'{record_spell("Dark Magic", "shadow")}\n'

      '\nTesting late import technique:\n'
      f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}\n'

      '\nCircular dependency curse avoided using late imports!\n'
      'All spells processed safely!')
