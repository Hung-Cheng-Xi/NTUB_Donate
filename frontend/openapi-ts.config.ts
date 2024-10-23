import { defineConfig } from '@hey-api/openapi-ts';

export default defineConfig({
  client: '@hey-api/client-axios',
  input: 'http://127.0.0.1:8000/openapi.json',
  output: {
    format: 'prettier',
    lint: 'eslint',
    path: './app/shared/openapi',
  },
  plugins: ['@tanstack/react-query'],
  types: {
    enums: 'javascript',
  },
});
