// src/setupProxy.ts (atau setupProxy.js untuk JavaScript)
import { createProxyMiddleware } from 'http-proxy-middleware';

export default function(app: any) {
  app.use(
    '/upload_dataset',  // Ganti dengan path yang sesuai dengan endpoint Anda
    createProxyMiddleware({
      target: 'http://localhost:5000',
      changeOrigin: true,
    })
  );
}