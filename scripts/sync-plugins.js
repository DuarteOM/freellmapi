import fs from 'fs';
import path from 'path';

const base = JSON.parse(fs.readFileSync('plugin-base.json', 'utf8'));

const pluginDirs = [
  '.claude-plugin',
  '.cursor-plugin',
  '.codex-plugin',
  '.devin-plugin',
  '.muse-plugin'
];

pluginDirs.forEach(dir => {
  const filePath = path.join(dir, 'plugin.json');
  if (fs.existsSync(filePath)) {
    const existing = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    // Mescla a base com as partes específicas (hooks, interface, etc)
    const updated = {
      ...base,
      description: existing.description || base.description,
      // Preserva campos específicos se existirem
      skills: existing.skills || "./skills/",
      hooks: existing.hooks || undefined,
      interface: existing.interface || undefined
    };

    fs.writeFileSync(filePath, JSON.stringify(updated, null, 2) + '\n');
    console.log(`Synced: ${filePath}`);
  }
});
