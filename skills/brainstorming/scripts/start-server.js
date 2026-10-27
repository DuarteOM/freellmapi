import { spawn } from 'child_process';
import path from 'path';
import fs from 'fs';
import os from 'os';

// Script para gerir o servidor brainstorm de forma agnóstica ao SO
const args = process.argv.slice(2);
const SCRIPT_DIR = process.cwd();

// Simulação simplificada dos argumentos originais do start-server.sh
// Em um sistema real, expandiríamos para suportar todas as flags (--project-dir, --host, etc.)
// A prioridade aqui é garantir que o Node.js gere o processo, o que é nativo no Windows.

const env = {
  ...process.env,
  BRAINSTORM_DIR: path.join(os.tmpdir(), `brainstorm-${Date.now()}`),
  BRAINSTORM_HOST: '127.0.0.1'
};

const serverProcess = spawn('node', ['server.cjs', ...args], {
  cwd: SCRIPT_DIR,
  env,
  detached: true,
  stdio: ['ignore', 'pipe', 'pipe']
});

serverProcess.stdout.on('data', (data) => {
  console.log(data.toString());
});

serverProcess.stderr.on('data', (data) => {
  console.error(data.toString());
});

console.log(`Server started with PID: ${serverProcess.pid}`);
serverProcess.unref();
