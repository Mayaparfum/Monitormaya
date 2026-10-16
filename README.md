# Monitor Maya Cloud — prototipo inicial

Incluye seis tiendas confiables y cinco perfumes en `config/watchlist.json`.

## Estado
- GitHub Actions ejecuta `monitor.py` aproximadamente cada hora (los horarios no están garantizados).
- Sin `MELI_ACCESS_TOKEN`, muestra un diagnóstico y **no consulta precios**.
- Con token válido, prueba la API oficial con la publicación `MLM3446626491`; su producto y vendedor aún no están identificados.
- El descubrimiento de productos por tienda, la verificación de vendedor, el historial persistente y las alertas Telegram **todavía no están implementados**.

## Subir a GitHub
Extrae el ZIP y sube el contenido de la carpeta al repositorio. Asegúrate de conservar `.github/workflows/monitor.yml`.

## Seguridad
Nunca incluyas tokens en archivos públicos. Configura secretos en GitHub → Settings → Secrets and variables → Actions.

## Prueba
GitHub → Actions → Monitor Maya hourly → Run workflow. Revisa los registros del trabajo.
