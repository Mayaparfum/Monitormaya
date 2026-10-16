"""Initial API connectivity diagnostic; no scraping or fabricated prices."""
import json
import os
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

config = json.loads(Path('config/watchlist.json').read_text(encoding='utf-8'))
token = os.getenv('MELI_ACCESS_TOKEN')
print(f"Monitor Maya {datetime.now(timezone.utc).isoformat()}: {len(config['products'])} products, {len(config['stores'])} stores")
if not token:
    print('MELI_ACCESS_TOKEN not configured. No live prices checked.')
else:
    for listing in config['listings']:
        item_id = listing['item_id']
        req = urllib.request.Request(
            f'https://api.mercadolibre.com/items/{item_id}',
            headers={'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'User-Agent': 'MonitorMaya/0.1'},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as response:
                data = json.load(response)
            print(json.dumps({k: data.get(k) for k in ('id', 'title', 'price', 'currency_id', 'seller_id', 'status')}, ensure_ascii=False))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            print(f'{item_id}: API unavailable ({exc}); no price recorded')
